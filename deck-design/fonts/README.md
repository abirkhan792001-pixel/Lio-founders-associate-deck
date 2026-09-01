# Deck typefaces: Inter + Geist Mono

The type system for the Founders Associate deck, matched to **lio.ai** and saved here so the deck
never depends on a network. Wired into every artboard in [`deck-design/`](../) (embedded as data-URIs
so PNG/PDF exports keep the real faces) and available to any other tool via [`fonts.css`](fonts.css).

## What's in this folder

| File | What it is |
|---|---|
| `Inter-Variable-latin.woff2` | Inter variable-weight subset (latin), one file covers weights 100-900; the deck uses 400/500/600/800 |
| `Inter-{400,500,600,700,800}.ttf` | Static TrueType instances. Install these locally if you open the deck in Keynote/PowerPoint/Figma |
| `GeistMono-{400,500}-latin.woff2` | Geist Mono latin subsets (regular + medium) |
| `GeistMono-{400,500}.ttf` | Static TrueType instances of the same |
| `fonts.css` | `@font-face` rules pointing at the files above (relative paths) |

## How the fonts were identified

`lio.ai` (and `asklio.ai`, and archive mirrors) are blocked by this workspace's network egress
policy, so the site's CSS could not be read directly. Identification, 2026-08-31:

1. Lio's own privacy page (`lio.ai/datenschutz`, via search index) states the site loads its fonts
   from **Google Fonts**, which narrows the field to Google Fonts families.
2. The exact hero headline ("The world's first multi-agent system…") and the industry-chip labels
   ("Industrial Manufacturing", "Energy & Utilities"…) from Abir's homepage screenshots were
   re-rendered in 13 candidate grotesques and 10 candidate monos at matching size, and compared
   letter by letter.
3. **Sans → Inter.** Matches every observable trait: single-story `g` with open hook, straight-tailed
   `y`, slant-cut `t`, straight apostrophe, short hyphen, neutral Swiss proportions. Eliminated:
   Archivo (stubby ascenders), Geist/Host Grotesk (long hyphens), Manrope/Figtree/Jakarta/Onest
   (geometric/rounded), Familjen (too compact). Runner-ups if Lio ever corrects us: Mona Sans,
   Hanken Grotesk.
4. **Mono → Geist Mono.** Matches the chips' double-story `a`, single-story `g`, conventional `&`,
   moderate x-height, airy width. Eliminated: Space Mono (quirky `&`, double-story `g`), DM Mono
   (single-story `a`), JetBrains (x-height too tall), Azeret (too wide). Runner-ups: Roboto Mono,
   IBM Plex Mono.

This is a visual identification, not a CSS read, so treat it as high-confidence rather than certain. If the
real families turn out to differ, swap the files here and the `@font-face` blocks in the artboards;
family names are referenced in exactly one place per file.

## Provenance & license

All files were downloaded 2026-08-31 from Google Fonts' official servers (`fonts.googleapis.com`
CSS API → `fonts.gstatic.com` binaries), unmodified:

- **Inter**: © The Inter Project Authors (Rasmus Andersson), SIL Open Font License 1.1,
  https://fonts.google.com/specimen/Inter
- **Geist Mono**: © Vercel, SIL Open Font License 1.1,
  https://fonts.google.com/specimen/Geist+Mono

The OFL permits bundling, redistribution and commercial use (not selling the fonts on their own):
https://openfontlicense.org
