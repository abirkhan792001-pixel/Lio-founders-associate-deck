# 15 · Founders Associate Deck: Design Spec

← [Index](00-INDEX.md) · Companion: the **[live design canvas](https://claude.ai/code/artifact/f7102cdb-c805-45f6-9676-e241267d395d)**. Every slide is editable in place and exportable as PNG/PDF. Source artboards: [deck-design/](deck-design/). Brand-language register: **[19-lio-brand-language-and-agents.md](19-lio-brand-language-and-agents.md)**.

> **Canvas state:** carries **v3, all 11 artboards**, re-seeded 2026-08-31 from `deck-design/`. It had been stranded on v1, because the v2 rebuild never reached it. Treat the canvas as a publish target rather than a source: it is re-seeded *from* the working files, and any edit made in the canvas GUI must be pulled back into `deck-design/` before the next `build_slides.py` run overwrites it.

**Purpose:** Abir Khan's application deck for the Founders Associate role (CEO & CTO office) at Lio. Theme set by Abir: (1) who I am & why Lio · (2) what I would own from day 0, in one line · (3) why hire me / what Lio gets in return.

**Design source (v4, 2026-09-01):** the **Prior Labs founder-associate deck** Abir supplied as a PDF reference. Colours were sampled off its pages (`#DBDBCD` sage, `#EFEFED` grey, `#000000` ink, white content ground), and the layout idioms were lifted from the artwork rather than described from memory. The Prior Labs wordmark is replaced throughout by the Lio lockup. This supersedes v3 (MBB formatting in the Zeit AI house style), v2 (Lio's dark teal brand language) and v1; all remain in git history.

The palette is unchanged from v3. What changed is the typographic and structural treatment, which is where the reference actually differs:

| Element | v3 | v4, per the reference |
|---|---|---|
| Headlines | 47px, weight 500 | **54px, weight 700**, tighter tracking |
| Title block | rule under the section head | **full-width rule under the title, subtitle below it** |
| Brand | small mark top-right | **Lio lockup top-right over a small-caps section line** |
| Column heads | 20px/700 | **12.5px/700 small caps over a 1.5px rule** |
| List numerals | small, black | **large and grey (`#BDBDBD`)** |
| Priority rows | plain | **4px left bar**, black for deep, sage for cover, plus a chip |
| Callouts | sage panels | **full-width grey panels** with a small-caps label |
| Cover | headline and subtitle | **eyebrow, starburst, headline low-left, three-stat row over a rule** |

## Design system (v4)

| Token | Value | Used for |
|---|---|---|
| Content base | `#FFFFFF` | Every content slide background |
| Sage | `#DBDBCD` | Cover ground · Thank-You ink · chips · verdict panels · left bars |
| Ink | `#000000` | Headlines, rules, big numbers, solid chips and event bars |
| Body / muted / faint | `#3C3C3C` / `#767676` / `#9A9A9A` | Body copy / subtitles and secondary / source lines |
| Grey | `#EFEFED` | Callout panels, tags, dim event bars, photo placeholder |
| Logo ink | `#2B2E30` | The Lio lockup, matching the supplied logo file |
| Hairline | `#E2E2E2` | Between rows |

- **Type: Inter only**, one variable file embedded per artboard, so canvas, offline viewing and PDF export keep the real face with no network. Scale: cover 74px/700 · titles 54px/700 · subtitles 21px · column heads 12.5px/700 caps · body 16px · stats 34-96px/700 · caps labels 11-12.5px/700 at `.1em`.
- **The logo.** The Prior Labs mark is gone. In its place is the Lio lockup: the redrawn shell mark (3 nested SVG arcs) plus the "Lio" wordmark in `#2B2E30`, matching the logo file Abir supplied. It sits top-right on content slides, bottom-left on slide 02, and in sage on the closing slide. The mark is still an approximation, so swap in the real asset if Lio shares one.
- **Uniformity is enforced by construction:** all 11 artboards come from one generator with a single shared CSS block, so tokens and spacing cannot drift between slides.
- **Copy discipline carried over from v3:** no em dashes, no en dashes, plain hyphens, and the prose checked against the humanize writing guides.

## How the deck is built and exported

The artboards are generated, not hand-written. The generator holds the CSS system plus each slide's content, writes all 11 `.dc.html` files and `canvas.json`, then Chromium prints each artboard at exact page size (`@page { size:1920px 1080px; margin:0 }`) and the pages are merged into [deck-design/Lio_FA_Deck_draft.pdf](deck-design/Lio_FA_Deck_draft.pdf): 11 pages, 1440×810pt (= 1920×1080 CSS px at 96 dpi), ~744KB.

> **Rendering note.** Screenshotting these artboards with `--window-size=1920,1080` silently clips the bottom ~87px, because the headless viewport is only 993px tall. That is how the footer and page number can appear "missing". Verify against the printed PDF, or render with a taller window.

### Two SVG sets

`deck-design/export_pdf.py` also writes **outlined** SVGs to `deck-design/slides-svg/`. Every glyph is a filled path, so the file is pixel-identical everywhere and needs no font installed, at the cost of 200 to 770KB per slide and text that cannot be retyped. Use these for print or for anyone who does not have Inter.

`deck-design/export_svg.py` writes **editable** SVGs to `deck-design/slides-svg-editable/`. These are 2 to 20KB, and each rendered line is one live `<text>` element carrying its real font size, weight, colour and letter-spacing, so Figma, Illustrator and Inkscape all open them as type. Use these when the slide has to be edited.

The editable exporter reads the rendered DOM rather than the printed PDF, because Chromium embeds the variable Inter as dozens of Type3 fonts and every run comes back as `font-family="Type3 (255 0 R)"`, which resolves nowhere. It measures each word by wrapping it in a span, and it chops words after hyphens and slashes first. A span that straddles a line break reports the union of its two line boxes, which would drag the whole line's `x` back to the paragraph edge and print the run on top of the bold run before it.

## Slide-by-slide blueprint (11 artboards)

| # | Slide | Job | Key design/content beats |
|---|---|---|---|
| 01 | **Cover**: "Pipeline, rooms & proof" | Set the frame | Sage field, 104px headline, eyebrow line (application · office · date), plan paragraph, thin-line starburst right, ABIR KHAN top-right, and a footer rule carrying the "every number ships with a working file" promise |
| 02 | **Who am I and what do I bring to the table?** | Theme #1 | Experience (SCAILE · A&M >$100M · Biome VC $170M) + Education (Nova SBE, FT #8 sage chip, top 10%) left; **Why Lio ×3** right as numbered rows; day-to-day stack row and photo placeholder |
| 03 | **The what, why and how** | Contract for the deck | 01-03 FINDINGS (sage chips) · 04 STRATEGY · 05 THE OFFER · 06 THE ASK (black chips); sage **Brief summary** panel; goals column; and a full-width **inline SVG** across the lower third drawing the operating loop (calendar, target list, room, follow-up, pipeline) with a dashed feedback edge back to the list, labelled as the step nobody runs today |
| 04 | **Findings 01: Who buys Lio** | Proof of work: ICP | 4 segments as a 5-column table with Apollo counts set large, sage verdict panel: **219** + `Lio_ICP_Prospect_List.xlsx`. Carries the **bullseye band** (€2.8-4.7B / 8-30K staff) against the searched band, and closes on an **H1 RADAR SWEEP** strip: 1 true third-party BPO in 35 accounts, with the DACH trigger being the captive SSC and its change events (per [17](17-gtm-hypothesis-and-test-roadmap.md)) |
| 05 | **Findings 02: The rooms** | Proof of work: events | Quarter headers (black = open quarters, grey = later), event bars (black = P1 booked, sage = own franchise, outlined = later), money row per quarter, grey status panel, verdict **17** + €929K. October collision now reads **settled** (Petras→Chicago, Keil+Wagner→Munich, Heinzmann→demo stage, conditional on SIG scheduling Oct 25-26); closing two-column strip carries the **seat-per-room map** and the recomputed-ICP read on the spend (per [20](20-event-strategy-and-icp-baseline.md)) |
| 06 | **Findings 03: Share of voice** | Proof of work: LinkedIn audit | Solid black bars scaled to post counts, **Customers · 0 posts** row on a sage band, 3 grey observation panels, sage verdict panel with **60** |
| 07 | **What I would own from day 0** | Theme #2: the one line | 56px statement line, then LIVE / NEXT / ONGOING columns (the live column marked by a 2px black rule and sage chip) + **the 16-agent roster as outlined chips anchored above the footer**. The wedge-quarter column names both budget owners: third-party BPO in the US/FS rooms, captive SSC/GBS heads in DACH |
| 08 | **Why hire me: what you get in return** | Theme #3 | 4 numbered value points; sage guarantee panel with a black **ZERO BULLSHIT** chip mirroring the $10M Challenge; verdict **90 DAYS TO PROVE IT** |
| 09 | **The ask: what this costs and returns** | Theme #3, priced | Eyebrow **06 · THE ASK**. Left: three H1 ARR scenarios as chip+figure rows: **€0-175K** (KILL, outlined chip) · **€1.35M** (REFINE, sage chip, base case) · **€2.4M** (CONFIRM, black chip); right: sage panel with **€95-120K** base ask, equity band and the two re-rate points, then verdict **13×** (base-case ARR ÷ year-1 base). Sourced to [21-compensation-and-arr-scenarios.md](21-compensation-and-arr-scenarios.md) |
| 10 | **Thank you** | Close | Black field, sage type: mission line **ONE FOR ALL. ALL FOR PROCUREMENT.**, 118px Thank you, thin-stroke sage starburst, contacts on a footer rule |
| 11 | **Appendix, the working files** | Receipts | Every deliverable by filename with sage file-type chips, 9 entries across two columns, including the **HYPOTHESIS** set ([17](17-gtm-hypothesis-and-test-roadmap.md)/[18](18-trigger-group-outreach-angles.md) + the H1 scorecard), the **PLAYBOOK** set ([19](19-september-action-sheet.md)/[20](20-event-strategy-and-icp-baseline.md)), the comp/ARR **MODEL** ([21](21-compensation-and-arr-scenarios.md)) and the deck spec |

## Open items owed by Abir before sending

1. Headshot photo (slide 02, top-right placeholder)
2. LinkedIn links are set to `linkedin.com/in/abir-khan-1143211ab` (found via public search), confirm it's yours
3. The shell mark is a redrawn approximation of Lio's logo, swap in the real asset if Lio shares one internally; the fonts and the rest of the system need no substitution (all files in-repo, OFL-licensed)

*Slide 09's figures are **modeled, not observed**, the salary band is public market benchmarking (Glassdoor Munich/Berlin, 2026) and the ARR scenarios are built on file [17](17-gtm-hypothesis-and-test-roadmap.md)'s own decision-gate thresholds plus file [08](08-strategic-value-levers.md)'s disclosed ACV rule of thumb (~7% of displaced BPO/SSC cost). Derivation and caveats: [21-compensation-and-arr-scenarios.md](21-compensation-and-arr-scenarios.md).*

*Numbers on slides 04-06 are filled from the session's research (Apollo counts, organizer-verified dates, the LinkedIn register), each slide footnotes its source and date. Fonts, texture and brand mapping documented in [deck-design/fonts/README.md](deck-design/fonts/README.md) and [19-lio-brand-language-and-agents.md](19-lio-brand-language-and-agents.md).*
