# 17 · GTM Hypothesis & Test Roadmap — BPO-Renewal Displacement (H1)

← [P1 Budget & Staffing](12-p1-budget-staffing.md) | [Index](00-INDEX.md)

> **Companion data:** the enriched outbound contact pool (219 named buyers with emails across 4 ICP segments) lives in [13-icp-prospect-list.md](13-icp-prospect-list.md) + [Lio_ICP_Prospect_List.xlsx](Lio_ICP_Prospect_List.xlsx). This file adds the *experiment* on top of that pool: the renewal-trigger lens, group assignment, and the funnel scorecard ([Lio_H1_Test_Scorecard.csv](Lio_H1_Test_Scorecard.csv)).

> Synthesis file, drafted 2026-08-31. This turns the analysis in files [03](03-pain-points-and-solutions.md)–[08](08-strategic-value-levers.md) and [10](10-events-and-icp.md)–[12](12-p1-budget-staffing.md) into **one testable go-to-market bet** and a concrete plan to confirm or kill it. Everything here is inference and planning built on those sourced files — not company-reported fact. All numeric thresholds are **planning placeholders to calibrate with the sales team before the test starts** (then locked), not industry benchmarks. Companion tracking template: [Lio_H1_Test_Scorecard.csv](Lio_H1_Test_Scorecard.csv).

## The hypothesis in plain words

Many large European companies pay outside firms (BPO/SSC providers, often offshore) to do their transactional procurement work. Those contracts renew on fixed cycles. **Lio's strongest go-to-market bet is to find companies whose BPO contract expires in the next 6–18 months and displace it at ~7% of its cost — proven against the customer's own invoice in a 2-week deployment.**

## The formal hypothesis card

| Element | Content |
|---|---|
| **For** | European Global 2000: DACH industrials (€2–12B, SAP estates — primary ICP per [10](10-events-and-icp.md)) + indirect-heavy insurers/FS (fastest agentic-BPO math) |
| **With trigger** | A procurement BPO/SSC contract renewing in ≤18 months (a *nameable, listable* event) |
| **We win with** | Attach to the renewal: "BPO invoice check" assessment ($10M-Challenge mechanics applied to the BPO line) → 2-week POC → displacement at ~7% of contract cost |
| **Because** | The price-to-beat is already on an invoice (budget capture, not creation — [08](08-strategic-value-levers.md)); no incumbent defends the line (suites sell software budgets, Zip doesn't attack BPO, the BPO provider can't price-match without destroying its own arbitrage — [06](06-market-and-competition.md)); in DACH it displaces offshore jobs, not domestic ones (works-council-cheap — [08](08-strategic-value-levers.md)) |
| **Proven by** | Per-account verification against the customer's own contract — immune to the "all metrics are company-reported" discount ([07](07-customers-and-proof-points.md)) |
| **Measured by** | Trigger-group vs control-group funnel: meetings → assessments → POCs → contracts; cycle time; ACV vs identified savings; loss reasons |
| **Killed if** | POCs stall past ~2 quarters (MIT "pilot purgatory" pattern), losses to "renew cheaper with incumbent BPO" dominate, or savings verification disputes block conversion |

Supporting roles (not competing bets): the DACH conviction-room circuit ([10](10-events-and-icp.md)) is the **channel**; the intake experience is the **wow moment inside the POC**, not the lead message (that ground is contested — SAP Intake Agent GA'd Jun 2026, free through Dec 2026; Coupa×Tonkean); the US is the **next wave, gated on SOC 2** (still open as of 2026-08-31).

## The test, designed as an experiment

- **Unit of test:** named account.
- **Group A (trigger):** accounts with an estimated BPO/SSC renewal ≤18 months out.
- **Group B (control):** ICP-fit accounts with no known renewal.
- Same message, same events, same offer to both groups. **The difference between the groups is the hypothesis signal** — if renewal-window accounts don't convert meaningfully better, the "renewal trigger" theory is wrong even if some deals close.

## Roadmap

### Phase 0 — Foundations (2 weeks, Sep 2026, desk work, ~€0)

| # | Action | Output |
|---|---|---|
| 0.1 | Sign off the hypothesis card above with sales leadership; lock the Phase-2 thresholds | Agreed card + frozen scorecard thresholds |
| 0.2 | Build the **Renewal Radar**: 50–100 named accounts with a procurement BPO/SSC relationship. Sources: BPO providers' own case studies and press releases (Accenture, Capgemini, Genpact, Infosys BPM, IBM, WNS routinely name clients), annual reports mentioning outsourcing partners, SSON/SIG/SSOW speaker and attendee lists (self-identifying GBS owners), LinkedIn GBS/SSC titles, job posts ("BPO transition manager" etc.) | Populated [scorecard](Lio_H1_Test_Scorecard.csv): account, provider, scope, est. contract value, est. renewal date **with an evidence grade per row** (A confirmed / B inferred / C guessed — same discipline as [09](09-sources.md)) |
| 0.3 | Assign Group A / Group B; map each account to its next touchpoint in the P1 event program ([12](12-p1-budget-staffing.md)) | Groups + event mapping columns filled |
| 0.4 | Define the standard **"BPO invoice check"** offer (assessment scope, data asked of the prospect, output format) so every AE runs the identical play | One-page offer definition |

### Phase 1 — Run the test on the already-funded event program (Sep–Dec 2026)

The test vehicle is the P1 program already budgeted in [12](12-p1-budget-staffing.md) — no new spend, only instrumentation:

- **Q3-2026:** SSON San Diego · ProcureCon EU Cologne · ProcureCon East Boston · DPW Amsterdam
- **Q4-2026:** SIG Chicago · SSOW DACH Berlin · BME Symposium Berlin (SIG/SSON/SSOW rooms are literally "owners of the line item Lio attacks" — [11](11-target-event-pipeline.md))

Standard motion per event: pre-book meetings with Radar accounts → make the invoice-check offer in every meeting → seat renewal-window accounts first at the sidecar dinners → log every outcome and **every loss reason** (renewed with incumbent / stalled / security-compliance blocker / price / other) in the scorecard. Weekly scorecard update; monthly funnel review.

### Phase 2 — Decision gate (Jan–Feb 2027, on Q3+Q4 data)

| Metric | Confirm signal (placeholder) | Kill signal (placeholder) |
|---|---|---|
| Meeting → assessment rate, Group A vs B | A ≥ 2× B | A ≈ B |
| Assessment → POC | ≥ 30% | < 10% |
| POC → contract | ≥ 50% | < 20%, or POCs open > 2 quarters |
| Sales cycle, Group A | ≤ ~90 days | ≥ typical 6–9-month enterprise cycle |
| Dominant loss reason | price/timing objections (fixable) | "renewed with incumbent BPO anyway" or compliance blockers (structural) |

Three exits, decided at the gate and not before:
1. **Confirm → double down:** scale the Renewal Radar, productize the "BPO displacement playbook," carry the motion into the Q1/Q2-2027 US events, launch the US wave when SOC 2 closes.
2. **Refine → narrow:** signal in one sub-segment only (e.g. insurers convert, industrials don't) → re-scope the ICP and re-run one quarter.
3. **Kill → rotate:** fall back to the next-best hypotheses (intake-led land-and-expand, or conviction-circuit-first) with the same test discipline.

## Phase 0.2 executed — desk-research readout (2026-08-31)

All 35 Radar accounts swept for BPO/SSC evidence (4 parallel research passes over provider case studies, annual reports, careers pages, commercial registers, trade press; ~35 accounts, 100+ searches; every finding source-linked in the [scorecard](Lio_H1_Test_Scorecard.csv)). Result:

| Bucket | Count | Accounts (highlights) |
|---|---|---|
| **A-cand** — external partner confirmed in procurement ops, timing unknown | 2 | **Zurich (Genpact P2P/AP since 2012 — grade A, the anchor target)**, Generali AT (GOSP JV, 5% Accenture) |
| **A2-chg** — captive SSC/GBS **plus a live change event** | 4 | KOSTAL (Budapest migration amid German job cuts), Vitesco (integration into Schaeffler GBS post-merger), Innomotics (PE carve-out rebuilding its back office), LEONI (StaRUG restructuring) |
| **captive** — stable captive SSC/GBS confirmed | 16 | Knorr-Bremse (4-hub GBS), Kärcher (own GBS entity incl. indirect procurement), Dürr (onshore AP entity), KION (Kraków ~750 FTE), TRUMPF (Warsaw incl. purchasing), Givaudan (3-hub GBS), BENTELER (Czech hubs), Allianz (Allianz Services ~7,300), HDI Service AG, Swiss Re, Bosch Rexroth (Bosch-group GBS — hard target), FORVIA HELLA, KUKA, SMS, ANDRITZ, GEA |
| **B-ctrl** — no BPO/SSC evidence (control group) | 9 | Festo, Krones, Mubea, Jungheinrich, STIHL, KSB, Endress+Hauser, Hannover Re, R+V |
| **excl-cust** — existing Lio customer (expansion track, out of the net-new experiment) | 3 | Brose, Munich Re, ERGO |
| **merged** — duplicate | 1 | Talanx (= HDI Group) |

**What this changes about H1 (important):** in the DACH industrial ICP, the third-party BPO renewal trigger **barely exists** — 1 true procurement BPO in 35 accounts, and it sits at a Swiss insurer. The displacement target in DACH is the **captive SSC/GBS** (nearshore hubs in Poland/Czechia/Hungary/Romania and onshore German service GmbHs), which has **no renewal date** — so the trigger becomes **change events**: carve-outs, post-merger integrations, center migrations, restructuring programs. Consequences:

1. The DACH message shifts from *"your BPO renewal is a price check"* to *"your captive center's cost-per-transaction vs. agents"* — same 93% math, different door. The KB anticipated this (the Lio newsroom piece covers SSCs *and* BPO), but the test design must score A2-chg accounts as the DACH trigger group, not wait for renewals that never come.
2. The **pure renewal-trigger motion lives in FS and the US**: Zurich–Genpact here, plus the US GBS/BPO-owner segment in [13-icp-prospect-list.md](13-icp-prospect-list.md) — which is where actual third-party contracts concentrate.
3. GEA's contested 2015 Accenture SSC plan (blocked noise from IG Metall) is a **concrete works-council precedent** validating risk #7 in [08](08-strategic-value-levers.md) — and an argument for the "displace offshore hubs, keep German supervision jobs" framing.
4. Nine clean controls (B-ctrl) exist, so the Group A-vs-B comparison from the test design still runs — with A = (A-cand + A2-chg) for the readout.

## Guardrails (be honest about these)

- **Small numbers.** Dozens of accounts, not thousands — read direction, not decimals; don't claim statistical significance.
- **Economics are company-reported until POCs verify them.** The 93%/7% claim is Lio's own number ([07](07-customers-and-proof-points.md)); the first verified POCs are themselves a test output.
- **Keep the US out of the EU signal.** SOC 2 friction will depress US conversion for reasons unrelated to the hypothesis — track US accounts separately.
- **Renewal dates are estimates.** Grade every date A/B/C and weight the readout toward A/B rows.

## What can start today vs. what needs Lio

**Today, from a desk, no permission needed:** the hypothesis card, the Renewal Radar method and a first list pass from public sources, the scorecard, the event mapping — all delivered in this file + the CSV.
**Needs Lio internally:** real pipeline data, pricing mechanics (open question #2 in [08](08-strategic-value-levers.md)), sign-off on the assessment offer, AE/FDE staffing per event ([12](12-p1-budget-staffing.md)).

*Built from files [03](03-pain-points-and-solutions.md), [04](04-what-lio-replaces.md), [06](06-market-and-competition.md), [07](07-customers-and-proof-points.md), [08](08-strategic-value-levers.md), [10](10-events-and-icp.md), [11](11-target-event-pipeline.md), [12](12-p1-budget-staffing.md); source register: [09](09-sources.md).*
