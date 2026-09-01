#!/usr/bin/env python3
"""Export each artboard as an EDITABLE vector SVG.

Going via the printed PDF gives perfect geometry but useless text: Chromium
embeds the variable font as dozens of Type3 fonts, so every run comes out as
font-family="Type3 (255 0 R)", which resolves nowhere. This reads the rendered
DOM instead, where the real font, weight, size and colour are known, and emits
one <text> per line plus rects for fills and borders. Text stays live and
editable, and font-family is plain Inter, which Figma ships by default.

Run:  python3 deck-design/export_svg.py
"""
import json, pathlib, subprocess, tempfile

DECK = pathlib.Path(__file__).resolve().parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

# Walks the rendered page and serialises it as SVG. Text is chopped at every
# break opportunity, so no span ever straddles two lines: a span that does
# reports a union rect, which would drag the line's x back to the paragraph
# edge and put the run on top of the bold run before it.
JS = r"""
(() => {
  const hex = c => {
    const m = c.match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/);
    if (!m) return null;
    if (m[4] !== undefined && parseFloat(m[4]) === 0) return null;
    return '#' + [1,2,3].map(i => (+m[i]).toString(16).padStart(2,'0')).join('').toUpperCase();
  };
  const esc = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  const root = document.querySelector('.slide').getBoundingClientRect();
  const R = r => ({x: r.left - root.left, y: r.top - root.top, w: r.width, h: r.height});
  const out = [];
  const ctx = document.createElement('canvas').getContext('2d');
  const ascentOf = st => {
    ctx.font = `${st.fontStyle} ${st.fontWeight} ${st.fontSize} ${st.fontFamily}`;
    const m = ctx.measureText('Hxy');
    return m.fontBoundingBoxAscent || parseFloat(st.fontSize) * 0.8;
  };

  // 1. fills and borders, in document order so stacking is preserved
  document.querySelectorAll('.slide, .slide *').forEach(el => {
    if (el.closest('svg')) return;
    const st = getComputedStyle(el);
    if (st.display === 'none' || st.visibility === 'hidden') return;
    const b = R(el.getBoundingClientRect());
    if (b.w <= 0 || b.h <= 0) return;
    const bg = hex(st.backgroundColor);
    if (bg) out.push(`<rect x="${b.x.toFixed(1)}" y="${b.y.toFixed(1)}" width="${b.w.toFixed(1)}" height="${b.h.toFixed(1)}" fill="${bg}"/>`);
    [['Top',0,0,b.w,0],['Bottom',0,b.h,b.w,b.h],['Left',0,0,0,b.h],['Right',b.w,0,b.w,b.h]].forEach(([side,x1,y1,x2,y2]) => {
      const w = parseFloat(st['border'+side+'Width']);
      const c = hex(st['border'+side+'Color']);
      if (!w || !c || st['border'+side+'Style'] === 'none') return;
      const off = w / 2;
      const vert = side === 'Left' || side === 'Right';
      const ox = vert ? (side === 'Left' ? off : -off) : 0;
      const oy = vert ? 0 : (side === 'Top' ? off : -off);
      out.push(`<line x1="${(b.x+x1+ox).toFixed(1)}" y1="${(b.y+y1+oy).toFixed(1)}" x2="${(b.x+x2+ox).toFixed(1)}" y2="${(b.y+y2+oy).toFixed(1)}" stroke="${c}" stroke-width="${w}"/>`);
    });
  });

  // 2. inline SVG passed through untouched, positioned and scaled to its box
  document.querySelectorAll('.slide svg').forEach(sv => {
    const b = R(sv.getBoundingClientRect());
    const vb = (sv.getAttribute('viewBox') || `0 0 ${b.w} ${b.h}`).split(/[\s,]+/).map(Number);
    const s = (b.w / vb[2]).toFixed(4);
    const keep = ['fill','stroke','stroke-width','stroke-linecap','stroke-linejoin','color','font-family'];
    const inherit = keep.filter(a => sv.hasAttribute(a))
                        .map(a => `${a}="${sv.getAttribute(a)}"`).join(' ');
    out.push(`<g transform="translate(${b.x.toFixed(1)} ${b.y.toFixed(1)}) scale(${s})" ${inherit}>${sv.innerHTML}</g>`);
  });

  // 3. text, one element per rendered line
  const walker = document.createTreeWalker(document.querySelector('.slide'), NodeFilter.SHOW_TEXT);
  const nodes = [];
  while (walker.nextNode()) {
    const n = walker.currentNode;
    if (!n.textContent.trim() || n.parentElement.closest('svg')) continue;
    nodes.push(n);
  }
  nodes.forEach(n => {
    const parent = n.parentElement;
    const st = getComputedStyle(parent);
    // words become spans; a word is chopped after any hyphen or slash, since
    // that is where the browser is allowed to break it
    const frag = document.createDocumentFragment();
    const spans = [];
    n.textContent.split(/(\s+)/).filter(w => w.length).forEach(word => {
      if (!word.trim()) { frag.appendChild(document.createTextNode(word)); return; }
      word.split(/(?<=[-\/‐])/).forEach((chunk, i) => {
        if (!chunk.length) return;
        const s = document.createElement('span');
        s.textContent = chunk;
        frag.appendChild(s);
        spans.push({el: s, gap: i === 0});   // gap: this chunk follows a space
      });
    });
    parent.replaceChild(frag, n);

    const lines = [];
    const place = (rect, text, gap) => {
      const line = lines.find(l => Math.abs(l.top - rect.top) < 2);
      if (line) { line.parts.push({text, gap}); line.left = Math.min(line.left, rect.left); }
      else lines.push({top: rect.top, left: rect.left, parts: [{text, gap}]});
    };
    spans.forEach(sp => {
      const rects = sp.el.getClientRects();
      if (!rects.length) return;
      if (rects.length === 1) { if (rects[0].width) place(rects[0], sp.el.textContent, sp.gap); return; }
      // still straddling a break: measure it a character at a time
      const chars = [...sp.el.textContent];
      sp.el.textContent = '';
      const cells = chars.map(ch => {
        const e = document.createElement('span'); e.textContent = ch;
        sp.el.appendChild(e); return e;
      });
      let run = null;
      cells.forEach((e, i) => {
        const r = e.getBoundingClientRect();
        if (run && Math.abs(run.top - r.top) < 2) { run.text += chars[i]; return; }
        if (run) place(run, run.text, run.gap);
        run = {top: r.top, left: r.left, text: chars[i], gap: i === 0 && sp.gap};
      });
      if (run) place(run, run.text, run.gap);
    });

    const asc = ascentOf(st);
    const ls = parseFloat(st.letterSpacing);
    lines.forEach(l => {
      const b = R({left: l.left, top: l.top, width: 0, height: 0});
      let text = l.parts.map((p, i) => (i && p.gap ? ' ' : '') + p.text).join('');
      if (st.textTransform === 'uppercase') text = text.toUpperCase();
      const attrs = [
        `x="${b.x.toFixed(1)}"`, `y="${(b.y + asc).toFixed(1)}"`,
        `font-family="Inter, 'Helvetica Neue', Arial, sans-serif"`,
        `font-size="${parseFloat(st.fontSize).toFixed(1)}"`,
        `font-weight="${st.fontWeight}"`,
        `fill="${hex(st.color) || '#000000'}"`,
      ];
      if (ls && !isNaN(ls)) attrs.push(`letter-spacing="${ls.toFixed(2)}"`);
      out.push(`<text ${attrs.join(' ')} xml:space="preserve">${esc(text)}</text>`);
    });
  });
  return JSON.stringify({w: root.width, h: root.height, body: out.join('\n  ')});
})()
"""


def export(name: str, out_dir: pathlib.Path) -> pathlib.Path:
    src = DECK / f"{name}.dc.html"
    probe = f"""<script>window.addEventListener('load', () => {{
        try {{ document.title = {JS} }} catch (e) {{ document.title = 'ERR ' + e.message }} }});</script></head>"""
    tmp = pathlib.Path(tempfile.mkdtemp()) / "probe.html"
    tmp.write_text(src.read_text().replace("</head>", probe), encoding="utf-8")
    dom = subprocess.run(
        [CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars", "--window-size=1920,1400",
         "--virtual-time-budget=6000", "--dump-dom", f"file://{tmp}"],
        capture_output=True, text=True, check=True).stdout
    raw = dom.split("<title>", 1)[1].split("</title>", 1)[0]
    if raw.startswith("ERR "):
        raise RuntimeError(f"{name}: {raw}")
    import html as _html
    d = json.loads(_html.unescape(raw))
    svg = (f'<?xml version="1.0" encoding="UTF-8"?>\n'
           f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {d["w"]:.0f} {d["h"]:.0f}" '
           f'width="{d["w"]:.0f}" height="{d["h"]:.0f}" '
           f"font-family=\"Inter, 'Helvetica Neue', Arial, sans-serif\">"
           f'\n  <title>{name}</title>\n  {d["body"]}\n</svg>\n')
    target = out_dir / f"{name}.svg"
    target.write_text(svg, encoding="utf-8")
    return target


if __name__ == "__main__":
    order = [a["file"].replace(".dc.html", "")
             for a in json.loads((DECK / "canvas.json").read_text())["artboards"]]
    out_dir = DECK / "slides-svg-editable"
    out_dir.mkdir(exist_ok=True)
    for i, name in enumerate(order, 1):
        f = export(name, out_dir)
        f.rename(out_dir / f"{i:02d}-{name}.svg")
        p = out_dir / f"{i:02d}-{name}.svg"
        print(f"{p.name:28s} {p.stat().st_size/1024:6.0f} KB")
    print(f"wrote {len(order)} editable SVGs -> {out_dir}")
