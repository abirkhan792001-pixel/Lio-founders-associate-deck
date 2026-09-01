# 15 · Founders Associate Deck: Design Spec

← [Index](00-INDEX.md) · Companion: the **[live design canvas](https://claude.ai/code/artifact/f7102cdb-c805-45f6-9676-e241267d395d)**. Every slide is editable in place and exportable as PNG/PDF. Source artboards: [deck-design/](deck-design/). Brand-language register: **[19-lio-brand-language-and-agents.md](19-lio-brand-language-and-agents.md)**.

> **Canvas state:** carries **v3, all 11 artboards**, re-seeded 2026-08-31 from `deck-design/`. It had been stranded on v1, because the v2 rebuild never reached it. Treat the canvas as a publish target rather than a source: it is re-seeded *from* the working files, and any edit made in the canvas GUI must be pulled back into `deck-design/` before the next `build_slides.py` run overwrites it.

**Purpose:** Abir Khan's application deck for the Founders Associate role (CEO & CTO office) at Lio. Theme set by Abir: (1) who I am & why Lio · (2) what I would own from day 0, in one line · (3) why hire me / what Lio gets in return.

**Design source (v3, 2026-08-31):** **MBB-style consulting formatting in Abir's Zeit AI house style**. Bone/sage cover, white content slides, black ink, Inter only. Colours and layout idioms were sampled directly from the Zeit AI deck PDF (`#DBDBCD` sage, `#EFEFED` grey panels, square chips, 2px section rules). This supersedes v2 (Lio's own dark teal brand language, lime accent, Geist Mono) and v1; both remain recoverable from git history.

**Why v3:** the audience is a founders' office reading a strategy document, and MBB formatting (action titles that state the takeaway, one message per slide, section rules, a source line and page number on every page) carries the analytical rigour better than brand homage. The trade-off is real and worth naming: v2's dark Lio palette reflected the founders' own world back at them; v3 trades that mirror for the consulting read.

## Design system (MBB / Zeit AI)

| Token | Value | Used for |
|---|---|---|
| Content base | `#FFFFFF` | Every content slide background |
| Sage | `#DBDBCD` | Cover background · Thank-You ink · chips · verdict panels · summary boxes |
| Ink | `#000000` | Headlines, section heads, big numbers, solid chips and event bars |
| Body | `#3A3A3A` | Body copy |
| Muted / faint | `#767676` / `#9A9A9A` | Subtitles and small caps labels / source lines and page numbers |
| Grey panel | `#EFEFED` | Secondary observation cards, photo placeholder |
| Rules | `#000000` 2px / `#DCDCDC` 1px | Under section heads / between rows and above the footer |
| Chips | square, 11px/700, `.09em` caps | Sage = default · black = emphasis (STRATEGY, THE ASK, CONFIRM) · outlined = tertiary |

- **Type: Inter only**, in five weights from one variable file. Geist Mono is no longer used (files stay in the repo, unreferenced). `Inter-Variable-latin.woff2` is embedded as a data-URI in every artboard, so canvas, offline viewing and PDF export all keep the real face with no network, and each artboard is now ~72KB instead of ~115KB. Scale: cover 104px/500 · action titles 47px/500/-0.022em · subtitles 20.5px · section heads 20px/700 · body 16.5px · big stats 84-112px/700 · caps labels 9.5-11.5px/700 at `.1em`.
- **MBB conventions applied throughout:** every content slide carries an **action title** stating the takeaway rather than the topic (e.g. "The market is countable. The trigger is not the one the plan assumed"), a scope-setting subtitle, section heads over 2px rules, a **source line bottom-left** and **page number bottom-right** (`n / 11`).
- **Signature elements:** 8-spoke thin-line starburst on cover and Thank-You (from the Zeit AI cover) · redrawn **shell mark** (3 nested SVG arcs) + "Lio" wordmark, black on content slides, sage on Thank-You · sage verdict panels pairing a giant number with a one-sentence thesis · black/sage/outlined event bars encoding booked, own-franchise and later · **the 16-agent roster as outlined chips anchored above the footer on slide 07**.
- **Uniformity is enforced by construction:** all 11 artboards are generated from one template with a single shared CSS block, so tokens, chrome and spacing cannot drift between slides. Regenerating is a build step, not a hand-edit.

## How the deck is built and exported

The artboards are generated, not hand-written. The generator holds the CSS system plus each slide's content, writes all 11 `.dc.html` files and `canvas.json`, then Chromium prints each artboard at exact page size (`@page { size:1920px 1080px; margin:0 }`) and the pages are merged into [deck-design/Lio_FA_Deck_draft.pdf](deck-design/Lio_FA_Deck_draft.pdf): 11 pages, 1440×810pt (= 1920×1080 CSS px at 96 dpi), ~744KB.

> **Rendering note.** Screenshotting these artboards with `--window-size=1920,1080` silently clips the bottom ~87px, because the headless viewport is only 993px tall. That is how the footer and page number can appear "missing". Verify against the printed PDF, or render with a taller window.

## Slide-by-slide blueprint (11 artboards)

| # | Slide | Job | Key design/content beats |
|---|---|---|---|
| 01 | **Cover**: "Pipeline, rooms & proof" | Set the frame | Sage field, 104px headline, eyebrow line (application · office · date), plan paragraph, thin-line starburst right, ABIR KHAN top-right, and a footer rule carrying the "every number ships with a working file" promise |
| 02 | **Who am I and what do I bring to the table?** | Theme #1 | Experience (SCAILE · A&M >$100M · Biome VC $170M) + Education (Nova SBE, FT #8 sage chip, top 10%) left; **Why Lio ×3** right as numbered rows; day-to-day stack row and photo placeholder |
| 03 | **The what, why and how** | Contract for the deck | 01-03 FINDINGS (sage chips) · 04 STRATEGY · 05 THE OFFER · 06 THE ASK (black chips); sage **Brief summary** panel of the five findings; goals column closing on a grey through-line panel |
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
