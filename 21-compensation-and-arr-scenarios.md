# 21 · The Ask — Compensation Benchmark & H1 ARR Scenarios

← [Event Strategy & ICP Baseline](20-event-strategy-and-icp-baseline.md) | [Index](00-INDEX.md) | Feeds: **[15-deck-design.md](15-deck-design.md)**, slide **06 · The Ask** ([deck-design/TheAsk.dc.html](deck-design/TheAsk.dc.html))

> Drafted 2026-08-31. Two separate models, both explicitly labelled as inference: (A) a market-benchmarked salary ask — Lio has published no comp data, so this is external benchmarking, not a demand; (B) three ARR scenarios for the H1 hypothesis ([17](17-gtm-hypothesis-and-test-roadmap.md)), built from that file's own decision-gate thresholds and the ACV rule-of-thumb already disclosed in [08](08-strategic-value-levers.md). **Neither is a forecast.** Recompute both once Phase 0 actuals exist.

## A · Compensation benchmark

No Lio-specific salary data exists anywhere in this knowledge base (file 01's fast facts list only non-cash benefits: stock options, EGYM Wellpass, meals, Apple equipment, mobility allowance). The figures below are public market aggregates, grade B (third-party aggregator, not Lio-confirmed).

| Source | Role / market | Range (annual) | Grade |
|---|---|---|---|
| Glassdoor, 2026 | Founders Associate, Munich | €50,625–€77,500 (25th–75th pctile), avg €62K | B |
| Glassdoor, 2026 | Founders Associate, Berlin | €53,900–€90,000 (25th–75th pctile), avg €75,450 | B |
| Job-posting synthesis | Munich FA/Chief-of-Staff-blended posting | €60K–€90K | B |
| Job-posting synthesis | Berlin FA posting, with equity + bonus | €70K–€90K | B |
| worldsalaries.com, 2026 | Chief of Staff, Germany (broad, non-startup-weighted) | median €49,820 | C — pulls in low-paying non-startup roles, weak anchor |
| recruitingfromscratch.com / topstartups.io, 2026 | Chief of Staff, US Series A/B (context only, not directly transferable) | $150K–$240K OTE + 0.05–0.4% equity | B (US market — directional, not a EU comp) |

**Reading it:** the generic Munich/Berlin "Founders Associate" posting clusters €50–90K — but those postings skew junior/generalist. This mandate is narrower and more senior than that median: **CEO-and-CTO-office** scope (not a single-founder EA/ops role), against a candidate profile with Alvarez & Marsal restructuring work (>$100M engagements), Biome VC investing experience ($170M fund), and Nova SBE top-10%/FT#8 credentials — closer to the "Chief of Staff" band than the "Associate" band, scoped to the EU market rather than the US figures above.

**Proposed ask:**

| Element | Value | Rationale |
|---|---|---|
| Base, Year 1 | **€95,000–€120,000** (central anchor ≈ €105K) | Top of the Munich/Berlin FA band, stepped up for CEO&CTO-office scope + seniority; still well under the US Series-A Chief-of-Staff band, deliberately — this is an EU-market ask |
| Equity | **0.05%–0.15%**, standard 4-year vest / 1-year cliff | Non-founder strategic-hire band; below the US 0.05–0.4% range cited above, consistent with a lower-cash, EU-market offer |
| Re-rate points | Day 90 (the guarantee already on slide 05 — [15-deck-design.md](15-deck-design.md)) and the H1 decision gate, Jan–Feb 2027 ([17](17-gtm-hypothesis-and-test-roadmap.md)) | Ties comp progression to the same proof milestones already built into the pitch, instead of a generic annual-review clause |

This is a proposed anchor for a negotiation, not a number Lio has agreed to — flagged the same way every other inferred figure in this KB is flagged.

## B · H1 ARR scenarios

### B.1 · The ACV assumption (the load-bearing inference)

File 08 states plainly: **"no public ACV data"** exists for Lio. It does disclose the mechanism twice:

- Lever 2 (BPO replacement): "same scope at ~7% of BPO price" → a 93% cost cut for the customer, which means **Lio's own price ≈ 7% of the displaced BPO/captive-SSC operating cost**.
- Lever 1 rule of thumb: automatable-FTE count × €60–90K loaded cost = the savings base (anchored to the flagship case: ~120 FTEs ≈ €7–9M/yr).

This file applies that same rule of thumb to the two live segments identified in file 17's Phase 0.2 readout, to get a segment-level ACV estimate — an inference built on Lio's own disclosed math, not a new claim:

| Segment | Group-A accounts today (of 6) | Est. FTE-equivalent scope | Est. annual operating cost (€60–90K/FTE loaded) | Lio ACV at ~7% of displaced cost |
|---|---|---|---|---|
| **FS/insurance anchor** (Zurich–Genpact grade A; Generali AT GOSP) | 2 | 60–120 FTE (mature, multi-country, group-wide scope — Zurich's Genpact contract covers source-to-pay across IT, professional services, marketing, HR, facilities, travel) | €3.6M–10.8M | **~€450–550K, central €500K** |
| **DACH industrial, change-event trigger** (KOSTAL, Vitesco, Innomotics, LEONI) | 4 | 20–40 FTE (captive SSC/GBS procurement-relevant slice, not the whole multi-function hub) | €1.2M–3.6M | **~€150–200K, central €175K** |

**Caveat, stated as plainly as file 17 states its own:** small numbers, modeled not observed. No POC has verified a real contract value yet — the first verified POCs are themselves a test output, exactly as file 17's guardrails already say about the 93%/7% claim itself.

### B.2 · The three scenarios

Modeled over the already-funded P1 test window (Q3-2026 → Q2-2027, per [12](12-p1-budget-staffing.md)), mapped one-to-one onto file 17's own three decision-gate exits — not a new scenario framework, the same one already governing the test.

| Scenario | Decision-gate exit ([17](17-gtm-hypothesis-and-test-roadmap.md)) | Year-1 funnel (illustrative, not a forecast) | Wins | ARR |
|---|---|---|---|---|
| **Kill · Rotate** | Assessment→POC <10%, POC→contract <20% (file 17's own kill signals) | Funnel dies at the gate by design | 0–1 | **€0–175K** |
| **Refine · Narrow** (base case) | "Signal in one sub-segment only" — FS converts, DACH industrial doesn't (**matches today's actual read**: Zurich is the one confirmed third-party BPO account; DACH runs on captive-SSC change events with no renewal date) | ~2 FS-anchor wins @ ~€500K + ~2 DACH change-event wins @ ~€175K | 4 | **≈€1.35M** |
| **Confirm · Scale** (bull case) | Both segments clear confirm thresholds (assessment→POC ≥30%, POC→contract ≥50%) as the Radar scales from 35 to ~75 accounts (file 17 §0.2 target) | ~3 FS + ~5 DACH wins, holding today's ~33/67 FS/DACH split across ~13 Group-A accounts at that scale | 8 | **≈€2.4M**, plus it unlocks the already-funded Q1/Q2-27 US wave once SOC 2 closes |

**Kill-case honesty check:** €0–175K is not "conservative," it's what the kill thresholds are defined to produce — the point of the scenario is that it fails the gate, not that it generates a specific dollar figure. Presenting it any other way would break the same discipline file 17 asks of the 93%/7% claim itself.

### B.3 · Return against the ask

Using the central comp anchor (€105K, base only — equity excluded, since it isn't cash return in Year 1):

- Refine/base case: €1.35M ÷ €105K ≈ **13×**
- Confirm/bull case: €2.4M ÷ €105K ≈ **23×**
- Kill case: €0–175K ÷ €105K ≈ **0–1.7×** — the only scenario that doesn't clear the comp, and it's the one the test is explicitly designed to catch early and cheaply (Phase 0 cost ≈ €0, per file 17)

## Guardrails

- **Every number here is modeled, not sourced from a Lio-confirmed figure.** The ACV assumption inherits file 08's own "no public ACV data" caveat; the scenarios inherit file 17's "small numbers, read direction not decimals."
- **This is not the H1 test's real scorecard.** The actual tracker is [Lio_H1_Test_Scorecard.csv](Lio_H1_Test_Scorecard.csv); this file is a downstream illustration built on top of it for the comp conversation, not a replacement for it.
- **Recompute at the decision gate.** Once Phase 0/Phase 1 actuals exist (Jan–Feb 2027 per file 17), replace the illustrative funnel splits with observed conversion and real ACVs from signed POCs.

*Built from [08-strategic-value-levers.md](08-strategic-value-levers.md) (ACV rule of thumb), [17-gtm-hypothesis-and-test-roadmap.md](17-gtm-hypothesis-and-test-roadmap.md) (decision-gate thresholds, Phase 0.2 readout), [12-p1-budget-staffing.md](12-p1-budget-staffing.md) (test window); salary sources per §A table above.*
