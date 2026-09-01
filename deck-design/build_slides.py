#!/usr/bin/env python3
"""Build the Lio founders-associate deck.

Design follows the Prior Labs founder-associate deck supplied as reference:
sage cover, white content slides, bold black headlines over a full-width rule,
subtitle under the rule, brand lockup top right, small-caps column labels,
grey numerals, left-bar priority rows, grey callout panels, black closing slide.
Inter only, embedded per artboard. No em dashes, no en dashes, plain hyphens.

Run:  python3 deck-design/build_slides.py  then  python3 deck-design/export_pdf.py
"""
import base64, json, pathlib

OUT = pathlib.Path(__file__).resolve().parent
FONT_B64 = base64.b64encode((OUT / "fonts" / "Inter-Variable-latin.woff2").read_bytes()).decode()

INK, BODY, MUTED, FAINT = "#000000", "#3C3C3C", "#767676", "#9A9A9A"
SAGE, GREY, HAIR = "#DBDBCD", "#EFEFED", "#E2E2E2"
LOGO = "#2B2E30"

CSS = f"""
    @font-face {{ font-family:'Inter'; font-style:normal; font-weight:100 900; font-display:block;
      src:url(data:font/woff2;base64,{FONT_B64}) format('woff2'); }}
    * {{ box-sizing:border-box; }}
    @page {{ size:1920px 1080px; margin:0; }}
    html, body {{ width:1920px; height:1080px; }}
    body {{ margin:0; font-family:'Inter','Helvetica Neue',Arial,sans-serif; color:{BODY}; background:#FFFFFF;
      -webkit-font-smoothing:antialiased; -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
    a {{ color:inherit; }}
    .slide {{ width:1920px; height:1080px; position:relative; overflow:hidden; background:#FFFFFF; padding:56px 64px 0; }}

    h1 {{ font-size:54px; font-weight:700; letter-spacing:-0.025em; line-height:1.08; margin:0; color:{INK};
      max-width:1500px; }}
    .titlerule {{ border-top:1.5px solid {INK}; margin-top:34px; }}
    .sub {{ font-size:21px; font-weight:400; line-height:1.4; color:{MUTED}; margin-top:20px; max-width:1500px; }}

    .lock {{ text-align:right; flex-shrink:0; padding-top:4px; }}
    .lockmark {{ display:flex; align-items:center; gap:9px; justify-content:flex-end; }}
    .lockname {{ font-size:25px; font-weight:600; letter-spacing:-0.015em; color:{LOGO}; }}
    .locksub {{ font-size:11px; font-weight:500; letter-spacing:0.09em; text-transform:uppercase; color:{MUTED};
      margin-top:5px; }}

    .col {{ font-size:12.5px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:{INK};
      padding-bottom:8px; border-bottom:1.5px solid {INK}; }}
    .lbl {{ font-size:11.5px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:{INK}; }}
    .lblm {{ font-size:11.5px; font-weight:600; letter-spacing:0.1em; text-transform:uppercase; color:{MUTED}; }}

    .hair {{ border-bottom:1px solid {HAIR}; }}
    .name {{ font-size:20px; font-weight:700; color:{INK}; letter-spacing:-0.01em; }}
    .meta {{ font-size:14.5px; font-weight:400; color:{MUTED}; }}
    .b {{ font-size:16px; line-height:1.5; color:{MUTED}; }}
    .b b, .b strong {{ color:{INK}; font-weight:600; }}
    .bd {{ font-size:16px; line-height:1.5; color:{BODY}; }}
    .bd b, .bd strong {{ color:{INK}; font-weight:600; }}
    .s {{ font-size:14px; line-height:1.45; color:{MUTED}; }}

    .numg {{ font-size:20px; font-weight:700; color:#BDBDBD; width:34px; flex-shrink:0; }}
    .chip {{ display:inline-block; font-size:11px; font-weight:700; letter-spacing:0.08em; text-transform:uppercase;
      padding:5px 10px; background:{SAGE}; color:{INK}; white-space:nowrap; }}
    .chip-grey {{ background:{GREY}; color:#4A4A4A; }}
    .chip-dark {{ background:{INK}; color:#FFFFFF; }}
    .tag {{ display:inline-block; font-size:14px; font-weight:400; padding:6px 12px; background:{GREY};
      color:{BODY}; margin:0 7px 7px 0; }}

    .callout {{ background:{GREY}; padding:20px 26px; }}
    .stat {{ font-size:52px; font-weight:700; letter-spacing:-0.03em; line-height:1; color:{INK}; }}

    .foot {{ position:absolute; left:64px; right:64px; bottom:30px; display:flex; justify-content:space-between;
      align-items:flex-end; gap:48px; }}
    .src {{ font-size:11.5px; font-weight:400; color:{FAINT}; line-height:1.5; max-width:1300px; }}
    .pg {{ font-size:11px; font-weight:500; letter-spacing:0.08em; text-transform:uppercase; color:{FAINT};
      text-align:right; white-space:nowrap; line-height:1.6; }}
"""

MARK = ('<svg width="{s}" height="{s}" viewBox="0 0 48 48" fill="none" stroke="{c}" stroke-width="3.3" '
        'stroke-linecap="round" aria-hidden="true">'
        '<path d="M 24.00 44.00 A 20 20 0 1 1 42.13 15.55"></path>'
        '<path d="M 24.00 43.50 A 13.5 13.5 0 1 1 34.34 21.32"></path>'
        '<path d="M 24.00 43.20 A 8 8 0 1 1 28.59 28.65"></path></svg>')

STAR = ('<svg width="{s}" height="{s}" viewBox="0 0 48 48" stroke="{c}" stroke-width="{w}" stroke-linecap="round" '
        'fill="none" style="{st}" aria-hidden="true"><path d="M 30 24 L 44 24 M 28.24 28.24 L 38.14 38.14 '
        'M 24 30 L 24 44 M 19.76 28.24 L 9.86 38.14 M 18 24 L 4 24 M 19.76 19.76 L 9.86 9.86 M 24 18 L 24 4 '
        'M 28.24 19.76 L 38.14 9.86"></path></svg>')

def lockup(sub="Founders Associate application", size=27, colour=LOGO):
    return (f'<div class="lock"><div class="lockmark">{MARK.format(s=size, c=colour)}'
            f'<span class="lockname">Lio</span></div><div class="locksub">{sub}</div></div>')

def head(title, sub=None, right=None, lock_sub="Founders Associate application"):
    rt = right if right is not None else lockup(lock_sub)
    sb = f'<div class="sub">{sub}</div>' if sub else ""
    return (f'<div style="display:flex; justify-content:space-between; align-items:flex-start; gap:48px;">'
            f'<h1>{title}</h1>{rt}</div><div class="titlerule"></div>{sb}')

def foot(src, page):
    return (f'<div class="foot"><div class="src">{src}</div>'
            f'<div class="pg">khan.abirhilal@gmail.com<br>{page} / 11</div></div>')

def page_html(body, bg=None):
    style = f' style="background:{bg};"' if bg else ""
    return (f'<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
            f'  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n  <style>{CSS}  </style>\n'
            f'</helmet>\n<div class="slide"{style}>\n{body}\n</div>\n</x-dc>\n</body>\n</html>\n')

# ── the machine, drawn ────────────────────────────────────────────────────────
def machine_svg():
    """The operating loop the deck argues for, including the feedback edge."""
    boxes = [
        (0,    "Calendar",    "17 P1 events, dated"),
        (370,  "Target list", "219 named buyers"),
        (740,  "The room",    "brief, live demo, dinner"),
        (1110, "Follow-up",   "inside the same week"),
        (1480, "Pipeline",    "logged, named, costed"),
    ]
    edges = [(335, "who to seat"), (705, "meetings booked"),
             (1075, "conversations"), (1445, "named accounts")]
    parts = []
    for x, title, sub in boxes:
        parts.append(
            f'<rect x="{x}" y="28" width="300" height="78" fill="#FFFFFF" stroke="currentColor" stroke-width="1.5"/>'
            f'<text x="{x+20}" y="60" font-size="17" font-weight="700" fill="currentColor">{title}</text>'
            f'<text x="{x+20}" y="84" font-size="13" fill="{MUTED}">{sub}</text>')
    for cx, label in edges:
        parts.append(
            f'<line x1="{cx-27}" y1="67" x2="{cx+19}" y2="67" stroke="currentColor" stroke-width="1.5" '
            f'marker-end="url(#ar)"/>'
            f'<text x="{cx-4}" y="18" font-size="10.5" font-weight="700" letter-spacing="0.09em" '
            f'fill="{MUTED}" text-anchor="middle">{label.upper()}</text>')
    # return edge: outcomes rewrite who gets targeted next
    parts.append(
        '<path d="M 1630 106 L 1630 158 L 520 158 L 520 116" fill="none" stroke="currentColor" '
        'stroke-width="1.5" stroke-dasharray="7 5" marker-end="url(#ar)"/>'
        f'<rect x="890" y="144" width="372" height="28" fill="#FFFFFF"/>'
        f'<text x="1076" y="163" font-size="12.5" font-weight="600" fill="currentColor" '
        f'text-anchor="middle">Outcomes rewrite who gets targeted next</text>')
    return (
        '<figure style="margin:0;">'
        '<svg viewBox="0 0 1790 176" role="img" width="100%" height="auto" '
        'aria-label="The operating loop: the calendar sets who to seat, the target list produces booked meetings, '
        'the room produces conversations, follow-up produces named accounts, and the pipeline feeds back to rewrite '
        'who gets targeted next." style="display:block; color:#000000; overflow:visible;">'
        '<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
        'orient="auto-start-reverse"><path d="M 0 1 L 9 5 L 0 9 z" fill="currentColor"/></marker></defs>'
        + "".join(parts) + '</svg></figure>')

def ramp_svg():
    """The 90-day ramp laid over the dates that do not move."""
    D = 19.67  # px per day, 1 Sep to 30 Nov across 1790px
    bands = [(0, 586, "Days 0-30 · run the gauntlet", SAGE),
             (596, 1182, "Days 31-60 · the wedge quarter", "#FFFFFF"),
             (1192, 1790, "Days 61-90 · make it boring", "#FFFFFF")]
    above = [(413, "ProcureCon Köln"), (531, "ProcureCon Boston"),
             (1062, "SIG Chicago"), (1514, "SSOW Berlin")]
    below = [(256, "SSON San Diego"), (433, "B&amp;B NYC"), (570, "DPW Amsterdam"),
             (1101, "B&amp;B Munich"), (1534, "BME Berlin")]
    parts = []
    for x0, x1, label, fill in bands:
        stroke = "none" if fill != "#FFFFFF" else "currentColor"
        parts.append(
            f'<rect x="{x0}" y="6" width="{x1-x0}" height="30" fill="{fill}" stroke="{stroke}" stroke-width="1"/>'
            f'<text x="{x0+14}" y="26" font-size="11.5" font-weight="700" letter-spacing="0.09em" '
            f'fill="currentColor">{label.upper()}</text>')
    parts.append('<line x1="0" y1="76" x2="1790" y2="76" stroke="currentColor" stroke-width="1.5"/>')
    for x, label in above:
        parts.append(
            f'<line x1="{x}" y1="72" x2="{x}" y2="64" stroke="currentColor" stroke-width="1"/>'
            f'<circle cx="{x}" cy="76" r="4" fill="#FFFFFF" stroke="currentColor" stroke-width="1.5"/>'
            f'<text x="{x}" y="58" font-size="12" fill="currentColor" text-anchor="middle">{label}</text>')
    for x, label in below:
        parts.append(
            f'<line x1="{x}" y1="80" x2="{x}" y2="90" stroke="currentColor" stroke-width="1"/>'
            f'<circle cx="{x}" cy="76" r="4" fill="currentColor"/>'
            f'<text x="{x}" y="106" font-size="12" fill="currentColor" text-anchor="middle">{label}</text>')
    parts.append(
        '<rect x="0" y="70" width="7" height="12" fill="currentColor"/>'
        f'<text x="0" y="106" font-size="11.5" font-weight="700" letter-spacing="0.09em" '
        f'fill="{MUTED}">DAY 0</text>')
    return (
        '<figure style="margin:0;">'
        '<svg viewBox="0 0 1790 114" role="img" width="100%" height="auto" '
        'aria-label="The 90-day ramp plotted against the booked calendar. Five events fall inside the first thirty '
        'days, two inside the second thirty, and two inside the last thirty." '
        'style="display:block; color:#000000; overflow:visible;">'
        + "".join(parts) + '</svg></figure>')

S = {}

# ── 01 · Cover ────────────────────────────────────────────────────────────────
def stat(fig, label, note):
    return (f'<div><div class="stat">{fig}</div>'
            f'<div class="lbl" style="margin-top:12px;">{label}</div>'
            f'<div class="s" style="margin-top:7px;">{note}</div></div>')

S["Main"] = page_html(f"""
  <div style="font-size:13px; font-weight:500; letter-spacing:0.1em; text-transform:uppercase; color:#6B6C60;">
    Lio · Founders Associate · Munich</div>

  {STAR.format(s=430, c="#2E2F28", w=0.5, st="position:absolute; right:120px; top:110px;")}

  <div style="position:absolute; left:64px; top:498px; right:64px;">
    <div style="font-size:74px; font-weight:700; letter-spacing:-0.032em; line-height:1.1; color:{INK}; max-width:1320px;">
      I built your pipeline<br>before you hired me.</div>
    <div style="font-size:25px; font-weight:400; color:#5F6055; margin-top:34px;">
      Abir Khan · Founders Associate at SCAILE · Alvarez &amp; Marsal · Biome VC</div>
    <div style="font-size:19px; font-weight:700; color:{INK}; margin-top:18px; max-width:1320px;">
      You have 17 booked rooms and a 219-name buyer list waiting for an owner. Nobody below the founders has one.</div>
  </div>

  <div style="position:absolute; left:64px; right:64px; bottom:104px; border-top:1.5px solid {INK}; padding-top:32px;
       display:grid; grid-template-columns:repeat(3, minmax(0,1fr)); gap:60px;">
    {stat("219", "Named buyers, sourced", "Of 2,245 identified. 193 verified emails.")}
    {stat("17", "P1 events, re-verified", "&euro;929K and 204 staff-days, no owner.")}
    {stat("1 of 35", "Accounts with the assumed trigger", "The DACH door is a change event instead.")}
  </div>

  <div style="position:absolute; left:64px; bottom:44px; font-size:12px; font-weight:500; letter-spacing:0.09em;
       text-transform:uppercase; color:#6B6C60;">Abir Hilal Khan</div>
  <div style="position:absolute; right:64px; bottom:44px; font-size:12px; font-weight:500; letter-spacing:0.09em;
       text-transform:uppercase; color:#6B6C60;">Own research, 31 August 2026</div>
""", bg=SAGE)

# ── 02 · Who am I ─────────────────────────────────────────────────────────────
photo = (f'<div style="width:150px; height:150px; background:{GREY}; display:flex; align-items:center; '
         f'justify-content:center; flex-shrink:0;"><span class="lblm">Photo</span></div>')

def entry(name, meta, desc, last=False):
    cls = "" if last else ' class="hair"'
    return (f'<div{cls} style="padding:15px 0;">'
            f'<div style="display:flex; align-items:baseline; gap:14px; flex-wrap:wrap;">'
            f'<span class="name">{name}</span><span class="meta">{meta}</span></div>'
            f'<div class="b" style="margin-top:5px;">{desc}</div></div>')

def why(n, title, body, last=False):
    cls = "" if last else ' class="hair"'
    return (f'<div{cls} style="display:flex; gap:22px; padding:19px 0;">'
            f'<div class="numg">{n}</div><div>'
            f'<div class="name">{title}</div><div class="b" style="margin-top:6px;">{body}</div></div></div>')

S["WhoAmI"] = page_html(f"""
  <div style="position:absolute; right:64px; top:44px;">{photo}</div>
  {head("Who I am, and what I bring.",
        "Consulting, venture capital, and now founding. All of it in the last three years.",
        right='<div style="width:150px; flex-shrink:0;"></div>')}

  <div style="display:grid; grid-template-columns:1.02fr 0.98fr; gap:86px; margin-top:40px;">
    <div>
      <div class="col">Experience</div>
      <div style="margin-top:6px;">
        {entry("SQRlane", "Founder, since Aug 2026",
               "AI agents for freight forwarding. Displacing spreadsheets and hours rather than a competing tool.")}
        {entry("SCAILE Technologies", "Strategy, AI and go-to-market, 2026",
               "B2B go-to-market engines built from scratch, from ICP research to outbound to AI search visibility.")}
        {entry("Alvarez &amp; Marsal", "Restructuring, 2024",
               "Advised Fortune 500 CEOs on restructuring financial liabilities worth over $100M.")}
        {entry("Biome VC", "Venture capital, 2023",
               "Built the investment thesis that shaped how a $170M fund picks companies.", last=True)}
      </div>

      <div class="col" style="margin-top:26px;">Education</div>
      <div style="margin-top:6px;">
        {entry("Nova School of Business and Economics, Lisbon", "MSc Finance",
               "Top 10% of class. Ranked #8 worldwide by the Financial Times.")}
        {entry("National case competitions", "15,000+ participants",
               "Won top prize. The same instinct that produced the three findings in this deck.", last=True)}
      </div>
    </div>

    <div>
      <div class="col">Why Lio</div>
      <div style="margin-top:6px;">
        {why("1", "Shortest path to founding my own.",
             "I am building SQRlane, AI agents for freight forwarding. Same bet as Lio one category over: a labour "
             "problem nobody has priced. I would rather learn how that scales inside your founders' office than "
             "guess from mine.")}
        {why("2", "Lio sells against a $180B line, not a $10B one.",
             "Everyone else builds procurement software. Lio replaces the execution labour at roughly 7% of the cost. "
             "It is the sharpest enterprise wedge I have seen since I started working in GTM.")}
        {why("3", "I have already done the work.",
             "219 named buyers of 2,245 identified, a 17-event programme re-verified against organiser sources, a "
             "60-post share-of-voice audit, and a falsifiable GTM hypothesis with kill criteria. All before day 0.",
             last=True)}
      </div>
    </div>
  </div>

  <div style="position:absolute; left:64px; right:64px; bottom:112px;">
    <div class="lbl">Day-to-day stack</div>
    <div style="margin-top:14px;">
      <span class="tag">Claude Code</span><span class="tag">Apollo</span><span class="tag">Clay</span>
      <span class="tag">HubSpot</span><span class="tag">Figma</span><span class="tag">Webflow</span>
      <span class="tag">Notion</span><span class="tag">Sheets</span></div>
  </div>

  <div style="position:absolute; left:64px; bottom:38px; display:flex; align-items:center; gap:16px;">
    <div style="display:flex; align-items:center; gap:9px;">{MARK.format(s=30, c=LOGO)}
      <span style="font-size:24px; font-weight:600; letter-spacing:-0.015em; color:{LOGO};">Lio</span></div>
    <span class="s">Applying for Founders Associate</span>
  </div>
  <div style="position:absolute; right:64px; bottom:38px; text-align:right;">
    <div style="font-size:15px; font-weight:700; color:{INK};">khan.abirhilal@gmail.com</div>
    <div class="s" style="margin-top:4px;">Free from September · on-site in Munich</div>
  </div>
""")

# ── 03 · Structure ────────────────────────────────────────────────────────────
def arow(n, text, chip, cls="chip", last=False):
    bb = "" if last else f" border-bottom:1px solid {HAIR};"
    return (f'<div style="display:flex; align-items:center; gap:20px; padding:15px 0;{bb}">'
            f'<div class="numg" style="width:30px;">{n}</div>'
            f'<div style="flex-grow:1; font-size:18px; font-weight:600; color:{INK};">{text}</div>'
            f'<span class="{cls}">{chip}</span></div>')

S["Agenda"] = page_html(f"""
  {head("The what, why and how.",
        "How this deck is structured, and what I would drive once I join the team.")}

  <div style="display:grid; grid-template-columns:1.02fr 0.98fr; gap:86px; margin-top:40px;">
    <div>
      <div class="col">How the deck is structured</div>
      <div style="margin-top:6px;">
        {arow("01", "Who buys Lio, sourced and counted", "Findings")}
        {arow("02", "Where they gather, re-verified", "Findings")}
        {arow("03", "What the market hears on LinkedIn", "Findings")}
        {arow("04", "What I would own from day 0", "Strategy", "chip chip-dark")}
        {arow("05", "Why hire me, and what you get back", "The offer", "chip chip-dark")}
        {arow("06", "What it costs, and what it returns", "The ask", "chip chip-dark", last=True)}
      </div>
      <div class="callout" style="margin-top:26px;">
        <div class="lbl">The short version</div>
        <div class="b" style="margin-top:10px; color:{BODY};">Three findings built from public sources before day 0,
          one machine to run them, and one ask priced against what that machine returns.</div>
      </div>
    </div>

    <div>
      <div class="col">What I would go after</div>
      <div style="margin-top:20px;">
        <div class="lbl">Short term</div>
        <div class="b" style="margin-top:10px;"><b>Own event ops end to end for Q3 and Q4.</b> Target lists per room,
          founder briefs, the sidecar dinners, and the next-day follow-ups nobody has time for.</div>
        <div class="b" style="margin-top:10px;"><b>Stand up the outbound engine.</b> Keep the named-buyer list alive
          in Apollo, feed sequences with the AEs, and report what converts.</div>
        <div class="b" style="margin-top:10px;"><b>Give Keil and Wagner leverage.</b> Prep, notes, pipeline hygiene
          and the analysis layer of the $10M Challenge. Founders get hours back, every week.</div>
      </div>
      <div style="border-top:1px solid {HAIR}; margin-top:26px; padding-top:22px;">
        <div class="lbl">Long term</div>
        <div class="b" style="margin-top:10px;"><b>Own a slice of the US field engine</b> as the NYC pod scales. The
          Q2-27 calendar already requires a field-marketing layer.</div>
        <div class="b" style="margin-top:10px;"><b>Run the displacement campaign end to end,</b> from the SSOW and SIG
          rooms to qualified pilots. The 93%-cheaper story deserves its own funnel.</div>
        <div class="b" style="margin-top:10px;"><b>Earn ownership of a revenue line,</b> the way Lio defines new roles
          for its own customers.</div>
      </div>
    </div>
  </div>
  <div style="position:absolute; left:64px; right:64px; bottom:74px;">
    <div class="lbl" style="margin-bottom:7px;">The machine those findings feed</div>
    <div style="border-top:1.5px solid {INK}; padding-top:16px;">{machine_svg()}</div>
    <div class="s" style="margin-top:10px; font-size:13.5px;">Every step exists today. The dashed edge does not,
      which is why each renewal is argued from memory rather than from what the last room produced.</div>
  </div>
  {foot("Structure follows the three themes set for this application: who I am and why Lio, what I would own from "
        "day 0, and why hire me.", 3)}
""")

# ── 04 · ICP ──────────────────────────────────────────────────────────────────
G4 = "grid-template-columns: 300px 120px 120px 1fr 1fr; gap:30px;"
def icp(seg, sub, apollo, listed, centre, approach, last=False):
    cls = "" if last else ' class="hair"'
    return (f'<div{cls} style="display:grid; {G4} padding:22px 0;">'
            f'<div><div class="name" style="font-size:17.5px;">{seg}</div>'
            f'<div class="s" style="margin-top:5px; font-size:13.5px;">{sub}</div></div>'
            f'<div><div style="font-size:26px; font-weight:700; color:{INK}; letter-spacing:-0.02em;">{apollo}</div>'
            f'<div class="lblm" style="font-size:10px; margin-top:4px;">In Apollo</div></div>'
            f'<div><div style="font-size:26px; font-weight:700; color:{INK}; letter-spacing:-0.02em;">{listed}</div>'
            f'<div class="lblm" style="font-size:10px; margin-top:4px;">On the list</div></div>'
            f'<div class="b" style="font-size:14.5px;">{centre}</div>'
            f'<div class="b" style="font-size:14.5px;">{approach}</div></div>')

S["IcpFindings"] = page_html(f"""
  {head("The market is countable. The trigger is not the one the plan assumed.",
        "219 named buyers are ready for outbound. The renewal trigger behind them holds in FS and the US, and breaks "
        "in DACH.", lock_sub="01 · Findings")}

  <div style="display:grid; {G4} margin-top:30px; padding-bottom:8px; border-bottom:1.5px solid {INK};">
    <div class="lbl">Segment</div><div class="lbl">Buyers</div><div class="lbl">Named</div>
    <div class="lbl">The buying centre</div><div class="lbl">How to approach</div>
  </div>
  {icp("DACH industrial backbone",
       "Searched &euro;1-12B · <b style='color:#000; font-weight:600;'>bullseye &euro;2.8-4.7B, 8-30K staff</b>",
       "851", "60",
       "<b>CPO sponsors, COO or CFO signs</b> via the SSC and FTE line. Procurement Excellence champions, CIO gatekeeps.",
       "<b>Trust-first, German, in person, timed to a change event.</b> The DACH trigger is the captive SSC, not a BPO "
       "renewal: carve-outs, post-merger integration, hub migrations.")}
  {icp("Insurance and financial services", "100% indirect spend · Munich Re, ERGO class", "156", "40",
       "<b>Head of Procurement or Sourcing and Vendor Management.</b> Compliance-heavy, auditability opens the door.",
       "<b>Where the real renewals sit.</b> Zurich-Genpact, running since 2012, is the one confirmed third-party "
       "procurement BPO in 35 swept accounts.")}
  {icp("US F500 GBS and BPO owners", "The people who sign outsourcing renewals · SSOW and SIG audience", "895", "60",
       "<b>VP GBS, Head of P2P, GPOs.</b> A persona classic procurement marketing barely reaches.",
       "<b>Budget capture, and the segment where renewals actually concentrate.</b> Every renewal is a qualified "
       "opportunity with a price to beat by 93%.")}
  {icp("DACH utilities and mobility", "Regulated, process-heavy · Deutsche Bahn, SWM, Lufthansa class", "343", "59",
       "<b>Leiter Einkauf</b> plus digitalisation leads. Works councils in the room from day one.",
       "<b>Follow the Deutsche Bahn breadcrumb.</b> Regulated buyers move on references and auditability.", last=True)}

  <div style="display:flex; align-items:center; gap:40px; margin-top:26px; background:{SAGE}; padding:24px 30px;">
    <div style="flex-shrink:0;">
      <div style="font-size:62px; font-weight:700; letter-spacing:-0.03em; line-height:1; color:{INK};">219</div>
      <div class="lbl" style="margin-top:9px;">Named buyers<br>122 companies</div>
    </div>
    <div class="bd" style="color:#2E2E28;"><b>The outbound cold-start problem is solved before day 0.</b> Every contact
      carries title, company, location and LinkedIn URL. 193 carry verified work emails, including prospect CPOs at
      Allianz, Deutsche Bahn, E.ON, ServiceNow, Citi, Beiersdorf and Miele. Apollo identifies <b>2,245 titled buyers</b>
      on the same filters, so the refill pool is documented and reusable.</div>
  </div>

  <div class="callout" style="margin-top:16px;">
    <div class="lbl">H1 radar sweep</div>
    <div class="b" style="margin-top:9px; font-size:15px;">35 accounts swept for BPO and SSC evidence: <b>one true
      third-party procurement BPO</b> (Zurich-Genpact) plus one Accenture JV, 4 captive centres with a live change
      event, 16 stable captives, 9 clean controls. <b>The DACH displacement target is the captive SSC, which has no
      renewal date,</b> so the trigger there is a change event and the renewal-timed motion belongs to FS and the US.</div>
  </div>
  {foot("Sourced via Apollo, 31 August 2026. Search totals are Apollo database counts, not TAM. Radar sweep and "
        "evidence grades per Lio_H1_Test_Scorecard.csv and 17-gtm-hypothesis-and-test-roadmap.md.", 4)}
""")

# ── 05 · Rooms ────────────────────────────────────────────────────────────────
def ev(text, kind="solid"):
    st = {"solid": f"background:{INK}; color:#FFFFFF;",
          "own": f"background:{SAGE}; color:{INK};",
          "dim": f"background:{GREY}; color:{BODY};"}[kind]
    return f'<div style="{st} font-size:12.5px; font-weight:500; padding:8px 11px; margin-top:7px; line-height:1.3;">{text}</div>'

S["EventFindings"] = page_html(f"""
  {head("The events are booked. The programme has no owner.",
        "&euro;929K and 204 staff-days across 17 events, with four starting in two weeks and no single owner below "
        "the founders.", lock_sub="02 · Findings")}

  <div style="display:grid; grid-template-columns:200px repeat(4, minmax(0,1fr)); gap:24px; margin-top:32px;">
    <div></div>
    <div class="lbl" style="background:{INK}; color:#FFF; text-align:center; padding:8px 0;">Q3-2026 · in 2 weeks</div>
    <div class="lbl" style="background:{INK}; color:#FFF; text-align:center; padding:8px 0;">Q4-2026</div>
    <div class="lbl" style="background:{GREY}; color:{BODY}; text-align:center; padding:8px 0;">Q1-2027</div>
    <div class="lbl" style="background:{GREY}; color:{BODY}; text-align:center; padding:8px 0;">Q2-2027</div>

    <div style="padding-top:6px;">
      <div class="name" style="font-size:16px;">The gauntlet runs</div>
      <div class="s" style="font-size:12.5px; margin-top:6px;">4 P1 events plus Bots &amp; Buyers NYC. 18 days,
        2 continents.</div>
    </div>
    <div>{ev("SSON San Diego · Sep 14-17")}{ev("+ Bots &amp; Buyers NYC · Sep 23 (own)", "own")}
      {ev("ProcureCon EU Köln · Sep 22-24")}{ev("ProcureCon East Boston · Sep 28-30 · lead")}
      {ev("DPW Amsterdam · Sep 30-Oct 1")}</div>
    <div>{ev("SIG Fall Chicago · Oct 25-28 · Petras", "own")}{ev("SSOW DACH Berlin · Nov 17-19", "own")}
      {ev("BME-Symposium Berlin · Nov 18-19", "own")}
      <div class="s" style="font-size:12.5px; margin-top:9px;">Berlin double-week holds. B&amp;B EU Munich collides
        with SIG Chicago. <b style="color:{INK};">Split settled: Petras to Chicago, Keil and Wagner to Munich,</b>
        conditional on SIG scheduling the buy-side session Oct 25-26.</div></div>
    <div>{ev("ProcureCon West Vegas · Mar 8-10", "dim")}{ev("SSOW Orlando · Mar 8-11 · BPO keynote", "dim")}
      {ev("APC · Mar 22-24 · now New Orleans", "dim")}
      <div class="s" style="font-size:12.5px; margin-top:9px;">Same-week collision resolved: Keil to Orlando,
        Petras to Vegas.</div></div>
    <div>{ev("Handelsblatt Apr 6-7 · Gartner May 3-5", "dim")}{ev("eLösungstage May 11-12 · WPC May 18-20", "dim")}
      {ev("DPW NY Jun 2-3 · Proc. Summit Jun 23-24", "dim")}
      <div class="s" style="font-size:12.5px; margin-top:9px;">7 events. Breaks the current team without the Jan-27
        field-marketing hire.</div></div>

    <div></div>
    <div class="s" style="text-align:center; margin-top:10px; font-size:12.5px;">&euro;165K new + &euro;70K committed · 65 staff-days</div>
    <div class="s" style="text-align:center; margin-top:10px; font-size:12.5px;">&euro;87K · 32 staff-days · cheapest, sharpest</div>
    <div class="s" style="text-align:center; margin-top:10px; font-size:12.5px;">&euro;108K + &euro;35K committed · 31 staff-days</div>
    <div class="s" style="text-align:center; margin-top:10px; font-size:12.5px;">&euro;376K · 76 staff-days · the heavy quarter</div>
  </div>

  <div style="display:flex; align-items:center; gap:34px; margin-top:30px;">
    <div style="flex-shrink:0;">
      <div style="font-size:52px; font-weight:700; letter-spacing:-0.03em; line-height:1; color:{INK};">17</div>
      <div class="lbl" style="margin-top:8px;">P1 events<br>Q3-26 to Q2-27</div>
    </div>
    <div class="bd" style="border-left:3px solid {INK}; padding-left:26px;">
      <b>&euro;736K new plus &euro;105K committed plus contingency, about &euro;929K. 204 staff-days. 10 sidecar
      dinners, &euro;120K of the total and the line to protect last.</b><br>
      The 17 verified customers cluster at <b>&euro;2.8-4.7B revenue and 8-30K staff,</b> exactly the German
      practitioner fairs' demographic. The US circuit aims a tier higher against zero verified US customers.</div>
  </div>
  <div style="display:grid; grid-template-columns:repeat(4, minmax(0,1fr)); gap:40px; margin-top:34px;
       border-top:1px solid {HAIR}; padding-top:22px;">
    <div><div class="lbl">Sponsor · the CPO</div><div class="b" style="font-size:14px; margin-top:8px;">Handelsblatt,
      WPC, DPW and the dinners. Owns the mandate and converts in closed rooms.</div></div>
    <div><div class="lbl">Economic buyer · COO or CFO</div><div class="b" style="font-size:14px; margin-top:8px;">SSOW
      three times, SIG, SSON San Diego. Signs when the BPO or FTE line moves.</div></div>
    <div><div class="lbl">Champion · Procurement Excellence</div><div class="b" style="font-size:14px; margin-top:8px;">
      The German BME fairs. Runs the evaluation and the pilot.</div></div>
    <div><div class="lbl">Gatekeeper · CIO or CISO</div><div class="b" style="font-size:14px; margin-top:8px;">
      BME IT-Sourcing, SAP Connect, Gartner. Cannot say yes, can say no.</div></div>
  </div>
  <div class="s" style="margin-top:16px; font-size:14px;"><b style="color:#000; font-weight:600;">The buying committee
    has four seats and no single event reaches more than two.</b> Preparation differs per seat, which is what the
    T-7 brief is for.</div>
  {foot("Figures from the Lio P1 budget and staffing plan, July 2026, mid-range estimates. Dates re-verified against "
        "organiser sources on 31 August 2026. Seat map per 20-event-strategy-and-icp-baseline.md.", 5)}
""")

# ── 06 · Share of voice ───────────────────────────────────────────────────────
def bar(label, sub, n, width, hi=False):
    box = (f'background:{SAGE}; padding:14px 12px;' if hi else f'padding:14px 0; border-bottom:1px solid {HAIR};')
    return (f'<div style="display:flex; align-items:center; gap:18px; {box}">'
            f'<div style="width:250px; flex-shrink:0;">'
            f'<div style="font-size:16px; font-weight:{"700" if hi else "600"}; color:{INK};">{label}</div>'
            f'<div class="s" style="font-size:12.5px; margin-top:2px;">{sub}</div></div>'
            f'<div style="display:flex; align-items:center; gap:14px; flex-grow:1;">'
            f'<div style="height:16px; width:{width}px; background:{INK};"></div>'
            f'<div style="font-size:15px; font-weight:700; color:{INK};">{n}</div></div></div>')

def obs(title, body):
    return (f'<div class="callout"><div class="name" style="font-size:17px;">{title}</div>'
            f'<div class="b" style="font-size:14.5px; margin-top:7px;">{body}</div></div>')

S["VoiceFindings"] = page_html(f"""
  {head("One voice carries the category, and the customer wall is silent.",
        "60 indexed posts. Keil authors 40% of them, and customers author none.", lock_sub="03 · Findings")}

  <div style="display:grid; grid-template-columns:1.05fr 0.95fr; gap:76px; margin-top:36px;">
    <div>
      <div class="col">Posts found, by who is talking</div>
      <div style="margin-top:6px;">
        {bar("Vladimir Keil (CEO)", "the channel, effectively", "24", 400)}
        {bar("Lio company page", "including the askLio era", "9", 150)}
        {bar("Third-party commentary", "analysts, influencers, reactions", "9", 150)}
        {bar("Heinzmann and Wagner", "CTO and COO", "7", 117)}
        {bar("Lio team", "Petras, new-hire posts, FDE Night", "7", 117)}
        {bar("Investors and network", "YC and a16z orbit", "4", 67)}
        <div style="margin-top:10px;">{bar("Customers", "despite a 150+ enterprise logo wall", "0 posts found", 4, True)}</div>
      </div>
      <div class="s" style="font-size:12.5px; margin-top:14px;">Found via search-engine indexing of linkedin.com, so
        this is a floor rather than a census. The login wall hides an unknown share of posts.</div>
    </div>

    <div style="display:flex; flex-direction:column; gap:14px;">
      {obs("One voice carries 40% of the channel",
           "Keil authors 24 of 60 indexed posts, and the founder team together 31. That is a single point of failure, "
           "and also the cheapest amplifier available. Founder-content ops multiplies an asset that already works.")}
      {obs("The logo wall is silent",
           "Zero customer-authored posts, despite award-grade stories at Schaeffler, REHAU and Surventis. Every "
           "go-live, award and dinner should ship with a co-marketing ask. Nobody owns that ask today.")}
      {obs("Moments, not a cadence",
           "Activity spikes at the YC launch, the BME award and the Series A, then goes quiet. The 17-room calendar is "
           "a built-in content engine if every room produces posts before, during and after. That loop needs an owner.")}
    </div>
  </div>

  <div style="display:flex; align-items:center; gap:34px; margin-top:28px; background:{SAGE}; padding:24px 30px;">
    <div style="flex-shrink:0;">
      <div style="font-size:56px; font-weight:700; letter-spacing:-0.03em; line-height:1; color:{INK};">60</div>
      <div class="lbl" style="margin-top:8px;">Distinct posts<br>in the register</div>
    </div>
    <div class="bd" style="color:#2E2E28;"><b>Share of voice is founder-heavy and customer-silent. That is an ops gap,
      not a budget gap, and the events to content to advocacy loop I would run closes it.</b> Full register with URLs,
      authors, dates and themes ships as 14-linkedin-posts.md.</div>
  </div>
  {foot("Compiled via an 8-angle search sweep. Dates decoded from LinkedIn activity IDs. Logo count, awards and "
        "customer facts per the Lio site, newsroom and press, August 2026.", 6)}
""")

# ── 07 · Day 0 ────────────────────────────────────────────────────────────────
def own(title, chip, chip_cls, body, bar_colour):
    return (f'<div style="border-left:4px solid {bar_colour}; padding:2px 0 2px 22px; margin-bottom:26px;">'
            f'<div style="display:flex; align-items:center; gap:14px;">'
            f'<span class="name">{title}</span><span class="{chip_cls}">{chip}</span></div>'
            f'<div class="b" style="margin-top:7px;">{body}</div></div>')

def ramp(days, title, body, last=False):
    cls = "" if last else ' class="hair"'
    return (f'<div{cls} style="padding:16px 0;"><div class="lbl">{days}</div>'
            f'<div class="name" style="margin-top:8px;">{title}</div>'
            f'<div class="b" style="margin-top:6px;">{body}</div></div>')

S["DayZero"] = page_html(f"""
  {head("What I would own, and how I would ramp.",
        "The machine between the founders and the pipeline: the list, the rooms, and the follow-through.",
        lock_sub="04 · Strategy")}

  <div style="display:grid; grid-template-columns:1.02fr 0.98fr; gap:86px; margin-top:40px;">
    <div>
      <div class="col" style="margin-bottom:26px;">Where I go deep</div>
      {own("Event operations", "Deep", "chip", "Target lists per room, founder briefs, the sidecar dinners, and the "
           "next-day follow-ups. 17 rooms and 10 dinners currently have no owner below the founders.", INK)}
      {own("Outbound engine", "Deep", "chip", "The 219-name list stays alive in Apollo, sequences run with the AEs, "
           "and every cohort gets a report on what converted and what did not.", INK)}
      {own("The H1 test", "Cover", "chip chip-grey", "Renewal Radar maintained, change events tracked, loss reasons "
           "logged. The hypothesis reaches its decision gate with real data behind it.", SAGE)}
      {own("Founder leverage", "Cover", "chip chip-grey", "Prep, notes, pipeline hygiene, and the analysis layer of "
           "the $10M Challenge. Hours back for Keil and Wagner, every week.", SAGE)}
    </div>

    <div>
      <div class="col">The ramp</div>
      <div style="margin-top:6px;">
        {ramp("Days 0-30", "Run the gauntlet.",
              "Four P1 events plus Bots &amp; Buyers NYC in 18 days across two continents, starting in two weeks. "
              "The buyer list goes into sequences before the first flight.")}
        {ramp("Days 31-60", "Work the wedge quarter.",
              "Berlin double-week and SIG Chicago, the rooms where the budget owners sit: third-party BPO in the US "
              "and FS rooms, captive SSC and GBS heads in the DACH ones. First outbound-cohort report ships.")}
        {ramp("Days 61-90", "Make it boring.",
              "Calendar to list to room to follow-up to pipeline, measured weekly and running without heroics. The "
              "Q1-27 US quarter starts planned, staffed and booked early instead of rushed.", last=True)}
      </div>
    </div>
  </div>

  <div style="position:absolute; left:64px; right:64px; bottom:190px;">
    <div class="lbl" style="margin-bottom:7px;">The ramp, against the dates that do not move</div>
    <div style="border-top:1.5px solid {INK}; padding-top:14px;">{ramp_svg()}</div>
    <div class="s" style="margin-top:8px; font-size:13.5px;">The first thirty days are not onboarding. Five rooms land
      inside them, and two early-bird deadlines close on 30 September.</div>
  </div>

  <div class="callout" style="position:absolute; left:64px; right:64px; bottom:104px;">
    <div class="lbl">This is a proposal, not an audit</div>
    <div class="b" style="margin-top:8px; font-size:15px;">I do not know your internal pipeline, your pricing
      mechanics, or what the AEs are already running. Every priority here can be reordered in week one.</div>
  </div>
  {foot("Agent roster and the 85% claim per lio.ai/product, company-reported. Event figures per the P1 budget plan.", 7)}
""")

# ── 08 · Why hire me ──────────────────────────────────────────────────────────
S["WhyMe"] = page_html(f"""
  {head("Why me. Four things, with proof.",
        "Not potential. Output you can inspect before day 0.", lock_sub="05 · The offer")}

  <div style="display:grid; grid-template-columns:1.1fr 0.9fr; gap:80px; margin-top:40px;">
    <div>
      <div class="col">What you get</div>
      <div style="margin-top:6px;">
        {why("1", "An operator who ships unmanaged.",
             "This deck, the named-buyer list, the re-verified event programme, the LinkedIn audit and the H1 "
             "hypothesis test were <b>built before day 0, from public information.</b> That is the working speed you "
             "hire, not a promise of it.")}
        {why("2", "The outbound cold-start problem, already solved.",
             "219 named, titled, LinkedIn-linked buyers across four ICP segments, 193 of them with verified work "
             "emails, and an approach playbook for each. <b>The AEs and SDRs start warm.</b>")}
        {why("3", "A programme of about &euro;1M run with owner-level care.",
             "17 P1 events, 204 staff-days, 10 sidecar dinners. The highest-ROI line in the GTM budget currently has "
             "<b>no single owner below the founders.</b> I am that owner.")}
        {why("4", "A profile that spans the room.",
             "Consulting rigour at A&amp;M, investor pattern-matching at Biome VC, hands-on GTM engineering at SCAILE. "
             "<b>CFO-grade analysis down to SDR-grade execution.</b>", last=True)}
      </div>
    </div>

    <div>
      <div class="col">The guarantee</div>
      <div style="background:{SAGE}; padding:26px 30px; margin-top:24px;">
        <span class="chip chip-dark">Zero bullshit</span>
        <div class="b" style="margin-top:16px; color:#2E2E28;">Lio promises customers <b>$10M in identified value, or
          donates $100K.</b> Same energy, scaled to me:</div>
        <div style="font-size:20px; line-height:1.42; font-weight:700; color:{INK}; margin-top:14px;">
          If after 90 days you would not enthusiastically re-hire me, I hand over the machine (documented, running,
          transferable) and we shake hands.</div>
        <div class="b" style="margin-top:14px; color:#43443C;">No ramp-up excuses. No knowledge hostage-taking.</div>
      </div>
      <div style="display:flex; align-items:flex-end; gap:24px; margin-top:44px;">
        <div style="font-size:96px; font-weight:700; letter-spacing:-0.035em; line-height:0.9; color:{INK};">90</div>
        <div class="lbl" style="padding-bottom:10px;">Days to prove it.<br>
          <span style="color:{MUTED}; font-weight:600;">The machine stays either way.</span></div>
      </div>
    </div>
  </div>
  {foot("The $10M-or-$100K challenge is Lio's own public offer, at lio.ai/10-million.", 8)}
""")

# ── 09 · The ask ──────────────────────────────────────────────────────────────
def scen(fig, chip, chip_cls, title, body, tag="", last=False):
    cls = "" if last else ' class="hair"'
    tg = f' <span class="lblm" style="font-size:10.5px;">{tag}</span>' if tag else ""
    return (f'<div{cls} style="display:flex; gap:26px; align-items:flex-start; padding:26px 0;">'
            f'<div style="width:190px; flex-shrink:0; font-size:34px; font-weight:700; letter-spacing:-0.025em; '
            f'color:{INK}; line-height:1;">{fig}</div><div>'
            f'<span class="{chip_cls}">{chip}</span>{tg}'
            f'<div class="name" style="margin-top:11px; font-size:18px;">{title}</div>'
            f'<div class="b" style="margin-top:6px; font-size:15px;">{body}</div></div></div>')

S["TheAsk"] = page_html(f"""
  {head("The base case returns the year-one salary thirteen times over.",
        "A market-anchored ask, priced against the H1 thesis in three scenarios.", lock_sub="06 · The ask")}

  <div style="display:grid; grid-template-columns:1.12fr 0.88fr; gap:80px; margin-top:38px;">
    <div>
      <div class="col">The return, H1 thesis ARR in year one</div>
      <div style="margin-top:6px;">
        {scen("&euro;0-175K", "Kill · rotate", "chip chip-grey", "The funnel fails its own gate.",
              "0 to 1 contracts. Assessment to POC under 10%, POC to contract under 20%, which are <b>file 17's own "
              "kill thresholds.</b> The motion rotates to the next-best hypothesis. Phase 0 costs about &euro;0, "
              "which is the whole point of testing before spending.")}
        {scen("&euro;1.35M", "Refine · narrow", "chip", "Signal in FS only. DACH stays captive.",
              "About 2 FS-anchor wins at &euro;500K plus 2 DACH change-event wins at &euro;175K. <b>This is already "
              "today's read.</b> Zurich-Genpact is the one confirmed third-party BPO in 35 swept accounts.",
              tag="Base case")}
        {scen("&euro;2.4M", "Confirm · scale", "chip chip-dark", "Both segments clear the confirm bar.",
              "About 3 FS and 5 DACH wins as the Renewal Radar scales from 35 to roughly 75 accounts and conversion "
              "clears <b>assessment to POC at 30%, POC to contract at 50%.</b> Carries into the funded Q1 and Q2-27 "
              "US wave once SOC 2 closes.", last=True)}
      </div>

      <div class="callout" style="margin-top:22px;">
        <div class="lbl">What moves these numbers</div>
        <div style="display:grid; grid-template-columns:repeat(3, minmax(0,1fr)); gap:26px; margin-top:12px;">
          <div class="b" style="font-size:14px;"><b>ACV.</b> No public ACV exists. 7% of displaced cost is Lio's own
            disclosed mechanic. One verified POC replaces the whole estimate.</div>
          <div class="b" style="font-size:14px;"><b>Radar scale.</b> 35 accounts swept, 50 to 100 targeted. Every 10
            added yields about 2 more Group-A triggers at today's 17% hit rate.</div>
          <div class="b" style="font-size:14px;"><b>Segment mix.</b> An FS win is worth about 3 times a DACH win.
            Invert which segment converts and the base case roughly halves.</div>
        </div>
      </div>
    </div>

    <div>
      <div class="col">The ask</div>
      <div style="background:{SAGE}; padding:26px 30px; margin-top:24px;">
        <span class="chip chip-dark">Market-anchored</span>
        <div style="font-size:46px; font-weight:700; letter-spacing:-0.03em; color:{INK}; margin-top:16px;
          line-height:1;">&euro;95-120K</div>
        <div class="lbl" style="margin-top:11px;">Base, year 1 · anchor &euro;105K</div>
        <div class="b" style="margin-top:15px; color:#2E2E28;"><b>Plus 0.05 to 0.15% equity,</b> standard 4-year vest
          with a 1-year cliff.</div>
        <div class="b" style="margin-top:9px; color:#2E2E28;"><b>Re-rated twice:</b> at day 90, against the guarantee
          on the previous slide, and at the H1 decision gate in Jan or Feb 2027.</div>
        <div style="font-size:13.5px; line-height:1.5; color:#5E5F55; margin-top:16px; border-top:1px solid #C6C6BC;
          padding-top:14px;">Munich and Berlin founders-associate postings run &euro;51-90K per Glassdoor 2026. Scoped
          above that median for a CEO-and-CTO-office mandate and A&amp;M and Biome-VC seniority, and deliberately under
          the US Series-A chief-of-staff band. A proposed anchor, not a demand.</div>
      </div>

      <div style="display:flex; align-items:flex-end; gap:24px; margin-top:40px;">
        <div style="font-size:88px; font-weight:700; letter-spacing:-0.035em; line-height:0.9; color:{INK};">13x</div>
        <div class="lbl" style="padding-bottom:8px;">Base-case ARR over year-1 base.<br>
          <span style="color:{MUTED}; font-weight:600;">Confirm case clears it 23 times. Only kill does not,<br>
          which is exactly what the test is for.</span></div>
      </div>
    </div>
  </div>
  {foot("Modeled, not forecast. ACV at about 7% of displaced BPO or SSC cost per file 08, funnel per file 17's "
        "decision gate. Full math in 21-compensation-and-arr-scenarios.md. Salary per Glassdoor Munich and Berlin, 2026.", 9)}
""")

# ── 10 · Thank you ────────────────────────────────────────────────────────────
S["ThankYou"] = page_html(f"""
  <div style="display:flex; justify-content:space-between; align-items:flex-start;">
    <div style="display:flex; align-items:center; gap:11px;">{MARK.format(s=34, c=SAGE)}
      <span style="font-size:29px; font-weight:600; letter-spacing:-0.015em; color:{SAGE};">Lio</span></div>
    <div style="font-size:12.5px; font-weight:500; letter-spacing:0.24em; text-transform:uppercase; color:#9A9B8E;
         padding-top:10px;">Abir Khan</div>
  </div>

  {STAR.format(s=400, c=SAGE, w=0.45, st="position:absolute; right:170px; top:210px;")}

  <div style="position:absolute; left:64px; bottom:190px;">
    <div style="font-size:12.5px; font-weight:500; letter-spacing:0.2em; text-transform:uppercase; color:#9A9B8E;">
      One for all. All for procurement.</div>
    <div style="font-size:112px; font-weight:500; letter-spacing:-0.03em; line-height:1.02; color:{SAGE};
         margin-top:26px;">Thank you</div>
    <div style="font-size:24px; font-weight:400; color:#B9BAAC; margin-top:28px;">
      Ready to start before day 0. The machine is already running.</div>
  </div>

  <div style="position:absolute; left:64px; right:64px; bottom:52px; display:flex; justify-content:space-between;
       align-items:flex-end;">
    <div style="font-size:12px; font-weight:500; letter-spacing:0.18em; text-transform:uppercase; color:#9A9B8E;">
      Founders Associate application</div>
    <div style="text-align:right;">
      <a href="https://www.linkedin.com/in/abir-khan-1143211ab/" style="display:block; font-size:14px;
        font-weight:600; text-decoration:underline; color:{SAGE};">LinkedIn</a>
      <div style="font-size:12.5px; color:#9A9B8E; margin-top:5px;">khan.abirhilal@gmail.com</div>
    </div>
  </div>
""", bg=INK)

# ── 11 · Appendix ─────────────────────────────────────────────────────────────
def frow(chip, name, desc, last=False):
    cls = "" if last else ' class="hair"'
    return (f'<div{cls} style="padding:22px 0;"><span class="chip chip-grey">{chip}</span>'
            f'<div class="name" style="font-size:16.5px; margin-top:11px;">{name}</div>'
            f'<div class="b" style="font-size:14.5px; margin-top:5px;">{desc}</div></div>')

S["Appendix"] = page_html(f"""
  {head("Appendix: the working files.",
        "Every claim in this deck has a file behind it. Nothing here is slideware.", lock_sub="Receipts")}

  <div style="display:grid; grid-template-columns:repeat(2, minmax(0,1fr)); gap:86px; margin-top:38px;">
    <div>
      {frow("Spreadsheet", "Lio_ICP_Prospect_List.xlsx · 13-icp-prospect-list.md",
            "Named-buyer list across 4 ICP segments. Companies, titled contacts with LinkedIn URLs, Apollo match "
            "totals, per-persona approach playbook, executive summary.")}
      {frow("Spreadsheet", "16-event-status-update.md + Lio_P1_Event_Status_2026-08-31.csv",
            "60 scored events across US, UK and EU-DACH in P1, P2 and P3 tiers. Every P1 date, venue and deadline "
            "re-verified against organiser sources.")}
      {frow("Spreadsheet", "Lio_P1_Budget_Staffing.csv",
            "Quarter-by-quarter budget and staffing for the 17-event P1 programme. &euro;736K new plus &euro;105K "
            "committed plus contingency, 204 staff-days, hiring triggers.")}
      {frow("Hypothesis", "17-gtm-hypothesis-and-test-roadmap.md · 18-trigger-group-outreach-angles.md · "
            "Lio_H1_Test_Scorecard.csv",
            "The strongest GTM bet as a falsifiable card with kill criteria and decision gates, the 35-account Renewal "
            "Radar with an evidence grade per row, and first-touch drafts for the six trigger accounts.", last=True)}
    </div>
    <div>
      {frow("Register", "14-linkedin-posts.md",
            "Every publicly indexed LinkedIn post about Lio found across 8 search angles: company, founders, team, "
            "events, customers, investors, German-language and third-party commentary.")}
      {frow("Knowledge base", "00 to 12 · Lio knowledge base",
            "The sourced dossier this work builds on: company, product, pain points, competitive map, customer proof "
            "and strategic levers, every fact graded for reliability.")}
      {frow("Playbook", "19-september-action-sheet.md · 20-event-strategy-and-icp-baseline.md",
            "29 September actions ordered by due date with the three calls that cannot slip, plus recomputed ICP "
            "firmographics, the seat-per-room map and the preparation protocol by tier.")}
      {frow("Model", "21-compensation-and-arr-scenarios.md",
            "The math behind the ask. Salary benchmarked to Munich and Berlin market data, and three H1 ARR scenarios "
            "built on file 17's own decision-gate thresholds.")}
      {frow("This deck", "15-deck-design.md · deck-design/build_slides.py",
            "The design spec and the generator that writes all 11 artboards from one shared system.", last=True)}
    </div>
  </div>
  {foot("All files ship in the repository accompanying this application.", 11)}
""")

# ── standalone SVG exports ────────────────────────────────────────────────────
def _standalone(fragment: str, w: int, h: int, title: str, desc: str) -> str:
    inner = fragment.split("</defs>")[-1] if "</defs>" in fragment else fragment
    defs = ""
    if "<defs>" in fragment:
        defs = "<defs>" + fragment.split("<defs>")[1].split("</defs>")[0] + "</defs>"
    inner = inner.replace("</svg>", "").replace("</figure>", "")
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'color="#000000" font-family="Inter, \'Helvetica Neue\', Arial, sans-serif" role="img">\n'
            f'  <title>{title}</title>\n  <desc>{desc}</desc>\n'
            f'  <rect x="0" y="0" width="{w}" height="{h}" fill="#FFFFFF"/>\n'
            f'  {defs}\n  {inner}\n</svg>\n')

def write_svgs():
    d = OUT / "diagrams"; d.mkdir(exist_ok=True)
    m = machine_svg().split("<svg", 1)[1].split(">", 1)[1]
    r = ramp_svg().split("<svg", 1)[1].split(">", 1)[1]
    (d / "machine-loop.svg").write_text(_standalone(
        m, 1790, 176, "The operating loop",
        "Calendar to target list to room to follow-up to pipeline, with a dashed feedback edge from pipeline back "
        "to the target list marked as the step nobody runs today."), encoding="utf-8")
    (d / "ramp-90-days.svg").write_text(_standalone(
        r, 1790, 114, "The 90-day ramp against the booked calendar",
        "Five events fall inside the first thirty days, two inside the second thirty, two inside the last thirty."),
        encoding="utf-8")
    print("wrote 2 standalone SVGs to deck-design/diagrams/")


# ── write ─────────────────────────────────────────────────────────────────────
ORDER = [("Main", "01 · Cover"), ("WhoAmI", "02 · Who I am"), ("Agenda", "03 · The what, why and how"),
         ("IcpFindings", "04 · Findings 01 · the ICP"), ("EventFindings", "05 · Findings 02 · the rooms"),
         ("VoiceFindings", "06 · Findings 03 · share of voice"), ("DayZero", "07 · What I would own"),
         ("WhyMe", "08 · Why me"), ("TheAsk", "09 · The ask"),
         ("ThankYou", "10 · Thank you"), ("Appendix", "11 · Appendix")]

for name, _ in ORDER:
    (OUT / f"{name}.dc.html").write_text(S[name], encoding="utf-8")

artboards = [{"file": f"{n}.dc.html", "x": (i % 5) * 2040, "y": (i // 5) * 1280,
              "w": 1920, "h": 1080, "title": t} for i, (n, t) in enumerate(ORDER)]
canvas = {"artboards": artboards,
          "annotations": [{"id": "note-owed", "x": 0, "y": -430, "w": 520,
                           "text": "Design follows the Prior Labs founder-associate deck: sage cover, white content "
                                   "slides, bold headline over a full-width rule, subtitle under it, Lio lockup top "
                                   "right, small-caps column labels, grey numerals, left-bar priority rows.\n\nOwed "
                                   "by Abir before sending:\n1. Headshot photo (slide 02, top right)\n2. Confirm the "
                                   "LinkedIn URL\n3. The shell mark is redrawn from the Lio logo. Swap in the real "
                                   "asset if Lio shares one."}],
          "launch": {"view": "canvas"}}
(OUT / "canvas.json").write_text(json.dumps(canvas, indent=2, ensure_ascii=False), encoding="utf-8")
write_svgs()
print(f"wrote {len(ORDER)} slides + canvas.json")
