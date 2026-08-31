#!/usr/bin/env python3
"""Print each artboard to PDF at exact 1920x1080 and merge into Lio_FA_Deck_draft.pdf.

Needs Chromium (set $CHROME) and pymupdf. Pass a directory to also drop page PNGs there.
"""
import json, os, pathlib, subprocess, sys, tempfile
import pymupdf

DECK = pathlib.Path(__file__).resolve().parent
CHROME = os.environ.get("CHROME", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
TMP = pathlib.Path(tempfile.mkdtemp(prefix="deckpdf-"))

order = [a["file"] for a in json.loads((DECK / "canvas.json").read_text())["artboards"]]

parts = []
for i, f in enumerate(order, 1):
    out = TMP / f"{i:02d}.pdf"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                    "--virtual-time-budget=6000", f"--print-to-pdf={out}", f"file://{DECK / f}"],
                   check=True, capture_output=True)
    parts.append(out)

doc = pymupdf.open()
for p in parts:
    doc.insert_pdf(pymupdf.open(p))
target = DECK / "Lio_FA_Deck_draft.pdf"
doc.save(target, garbage=4, deflate=True)
print(f"{target}  pages={doc.page_count}  size={target.stat().st_size/1024:.0f}KB  "
      f"page0={doc[0].rect.width:.0f}x{doc[0].rect.height:.0f}")

# rasterise the real PDF pages for visual verification
outdir = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(".")
for i in range(doc.page_count):
    doc[i].get_pixmap(dpi=72).save(outdir / f"pdf_{i+1:02d}.png")
print("rasterised", doc.page_count, "pages ->", outdir)
