# 15 · Founders Associate Deck — Design Spec

← [Index](00-INDEX.md) · Companion: the **[live design canvas](https://claude.ai/code/artifact/f7102cdb-c805-45f6-9676-e241267d395d)** — every slide editable in place, exportable as PNG/PDF. Source artboards: [deck-design/](deck-design/). Brand-language register: **[21-lio-brand-language-and-agents.md](21-lio-brand-language-and-agents.md)**.

**Purpose:** Abir Khan's application deck for the Founders Associate role (CEO & CTO office) at Lio. Theme set by Abir: (1) who I am & why Lio · (2) what I would own from day 0, in one line · (3) why hire me / what Lio gets in return.

**Design source (v2, 2026-08-31):** **Lio's own brand language**, rebuilt from the lio.ai homepage (hero + industries ring screenshots supplied by Abir) — the deck now reads as if it shipped from Lio's own design system, so the founders see their world reflected back at them. (v1 mirrored Abir's Zeit AI template — bone/white/Inter; superseded, recoverable from git history.)

## Design system (Lio brand)

| Token | Value | Used for |
|---|---|---|
| Base | `#0B1416` | Every slide background (content slides add faint teal radial washes) |
| Hero texture | `deck-design/lio-hero.jpg` | Cover + Thank-You full-bleed (generated: teal streak/glass-blur look of lio.ai's hero; 1600×821 JPEG, 33KB; Thank-You mirrors it with `scaleX(-1)`) |
| Ink | `#FFFFFF` / `#E9EFEE` | Headlines / primary text |
| Secondary | `#9FB3B2` / `#AFC0BF` | Subtitles / body secondary |
| Muted mono | `#7E9290` / `#8FA5A3` | Source footnotes, footer email |
| Hairline | `rgba(255,255,255,0.10–0.18)` | Row dividers, section rules, table heads |
| Glass panel | `rgba(255,255,255,0.045)` + 1px `rgba(255,255,255,0.10)` border, radius 14px | Summary boxes, observation panels, verdict bars, photo placeholder |
| Chip | mono 12–13px on `rgba(22,29,30,0.72)`, 1px `rgba(255,255,255,0.15)` border, radius 8px | FINDINGS tags, ICP segments, agent roster, file-type tags |
| **Lime accent** | `#D7F452` (chip ink `#161B04`; olive chip bg `#20260D`) | The single accent: LIVE/ZERO BULLSHIT chips, verdict left-borders (3px), section numbers, starburst, key filenames, headline emphasis |
| White pill | `#FFFFFF` on dark, radius 999px | CTA look: "Request the 90 days", STRATEGY/THE OFFER chips, open-quarter headers |
| Banner strip | `#14343C` | Cover top strip (site's announcement banner) |
| Bar fill | `linear-gradient(90deg, #9FC8CC, #5E96A0)` | Share-of-voice bars |

- **Type:** **Inter** (identified as lio.ai's sans) + **Geist Mono** (identified as its monospace) — identification method, runner-ups and licenses in [deck-design/fonts/README.md](deck-design/fonts/README.md). Files are **saved in the repo** ([deck-design/fonts/](deck-design/fonts/): latin woff2 subsets + installable TTFs + `fonts.css`) and **embedded as data-URIs in every artboard**, so the canvas, offline viewing and PNG/PDF export all keep the real faces with no network. Scale: cover headline 124px/500; slide titles 52–56px/600/-0.02em; body 15.5–16.5px/400; verdict numbers 84–120px/800; all metadata (eyebrows, chips, footers, filenames, figures rows) in Geist Mono 10.5–14px.
- **Signature elements:** mono chips for every piece of metadata (the site's industries-ring idiom) · lime 8-spoke line starburst (site's widget asterisk; olive chip on the cover edge, large thin-stroke on Thank-You) · redrawn **shell mark** (3 nested SVG arcs converging at the bottom) + "Lio" wordmark Inter 500 · glass panels with 3px lime left border for verdicts (giant Inter-800 number + mono label + thesis) · white pill CTAs · cover banner strip + "we're not building slideware." glass card (echoing the Series A video card) · **the 16-agent Lio workforce roster as a chip constellation on slide 07**.
- **Slide chrome:** cover & thank-you carry the logo top-left; content slides top-right. Mono eyebrow with lime section number top-left; mono `khan.abirhilal@gmail.com` bottom-right; mono source footnote bottom-left/right.
- **Tone:** per [21](21-lio-brand-language-and-agents.md) — numbers before adjectives, imperatives, workforce-not-software, "Zero Bullshit" energy. Site copy quoted verbatim where it carries weight (85% claim, $10M Challenge, mission line on Thank-You).

## Slide-by-slide blueprint (10 artboards)

| # | Slide | Job | Key design/content beats |
|---|---|---|---|
| 01 | **Cover** — "Pipeline, rooms & proof" | Set the frame, in Lio's hero language | Banner strip: FOUNDERS ASSOCIATE APPLICATION · texture bg · 124px headline · right-side plan paragraph + **"Request the 90 days"** pill · "WE'RE NOT BUILDING SLIDEWARE." card · lime asterisk chip · ABIR KHAN mono |
| 02 | **Who am I and what do I bring to the table?** | Theme #1 | Experience (SCAILE · A&M >$100M · Biome VC $170M) + Education (Nova SBE, FT#8 lime chip, top 10%) left; **Why Lio ×3** right with lime mono numerals; stack row + photo placeholder |
| 03 | **The what, why and how** | Contract for the deck | 01–03 FINDINGS (glass chips) · 04 STRATEGY · 05 THE OFFER (white chips); glass summary panel headed **THREE FINDINGS · ONE MACHINE · ONE OFFER**; goals column |
| 04 | **Findings 01 — Who buys Lio** | Proof of work: ICP | 4 segments as site-style mono chips, Apollo counts in Inter 800, verdict panel: **219** + `Lio_ICP_Prospect_List.xlsx` in lime mono |
| 05 | **Findings 02 — The rooms** | Proof of work: events | Quarter pills (open = white, later = glass), event chips (white = P1 booked, lime = own/⚠, dim = later), mono money row, status panel, verdict **17** + €929K |
| 06 | **Findings 03 — Share of voice** | Proof of work: LinkedIn audit | Teal gradient bars, **Customers · 0 posts** row in lime highlight, 3 glass observation panels, verdict **60** |
| 07 | **What I would own from day 0** | Theme #2 — the one line | Giant line with lime second half + LIVE (lime) / NEXT / ONGOING columns + **the 16-agent roster chips** under "THE WORKFORCE I'D BE SELLING — 85% …" |
| 08 | **Why hire me — what you get in return** | Theme #3 | 4 numbered value points; guarantee panel with **ZERO BULLSHIT** lime chip mirroring the $10M Challenge; verdict **90 DAYS TO PROVE IT** |
| 09 | **Thank you** | Close | Mirrored texture, mission line **ONE FOR ALL. ALL FOR PROCUREMENT.** in lime mono, 128px Thank you, thin-stroke lime starburst, contacts |
| 10 | **Appendix — the working files** | Receipts | Every deliverable by filename in Geist Mono with file-type chips; now also lists fonts + the brand register |

## Rebuilding the live canvas from these sources

The artboards are self-contained (fonts embedded as data-URIs) **except** the hero texture: `lio-hero.jpg` is a separate repo file that must be passed alongside the artboards whenever the canvas is re-seeded — the cover and Thank-You slides reference it by filename and fail silently (broken image) if it is omitted. A rebuild ships all ten `.dc.html` files + `canvas.json` + `lio-hero.jpg` together; opening any artboard directly from `deck-design/` in a browser also works offline, since the image sits next to it.

## Open items owed by Abir before sending

1. Headshot photo (slide 02, top-right placeholder)
2. LinkedIn links are set to `linkedin.com/in/abir-khan-1143211ab` (found via public search) — confirm it's yours
3. The shell mark is a redrawn approximation of Lio's logo — swap in the real asset if Lio shares one internally; the fonts and the rest of the system need no substitution (all files in-repo, OFL-licensed)

*Numbers on slides 04–06 are filled from the session's research (Apollo counts, organizer-verified dates, the LinkedIn register) — each slide footnotes its source and date. Fonts, texture and brand mapping documented in [deck-design/fonts/README.md](deck-design/fonts/README.md) and [21-lio-brand-language-and-agents.md](21-lio-brand-language-and-agents.md).*
