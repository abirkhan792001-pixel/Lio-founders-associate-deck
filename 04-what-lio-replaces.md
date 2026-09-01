# 04 · What Does Lio Actually Replace?

← [Pain Points & Solutions](03-pain-points-and-solutions.md) | Next: [Lio vs Legacy](05-lio-vs-legacy.md) →

This is the most important strategic question about Lio, and the answer is deliberately counter-intuitive:

> **Lio does NOT replace the ERP or the procurement suite. It replaces the *human execution labor* that operates them, in-house transactional work, BPO/SSC contracts, and the email/Excel intake layer.**

Their own words: *"We are not another procurement software. We are the agents operating the ones you already trust."* And the market math that justifies it: enterprises spend **~$180B/yr on procurement talent vs ~$10B/yr on procurement software**, with outsourcing costing up to **20×** software. Lio prices itself against the $180B line, not the $10B line.

## What is replaced, kept, and displaced

| Layer | Fate under Lio | Detail |
|---|---|---|
| **ERP / S2P system of record** (SAP, Ariba, Coupa, Oracle, Ivalua, Dynamics, Workday) | **KEPT, explicitly** | Remains single source of truth; bidirectional sync; no shadow data; existing approval/compliance logic preserved. Lio executes *inside* these systems via APIs/middleware. |
| **Manual transactional execution** (PR review, PO creation, order confirmation chasing, goods-receipt matching, invoice 3-way match, supplier onboarding admin) | **REPLACED** | The "85% of procurement operations" claim. Case study: 99.6% automation of the outsourced scope at 12 months, ~120 FTEs transitioned. Humans move to exception handling + supervision. |
| **BPO / Shared Service Center contracts** for procurement ops | **REPLACED, sharpest wedge** | "Agentic BPO": 24/7 auditable agents at ~7% of traditional BPO cost (93% reduction); enterprise "owns the execution layer" instead of renting offshore labor; AOPs built from the same SOPs the BPO used. Whitepaper: "The Rise of Agentic BPO." |
| **Email/Excel/SharePoint intake + tracking** (the *real* incumbent at most companies) | **REPLACED** | Free-text/photo intake in Teams/Outlook replaces "where do I request?" chaos. Greenfield: ~40% of large orgs have no true P2P at all; suites' intake modules see sub-40% engagement. |
| **Intake forms/portals of legacy suites** (the requester-facing front end of Ariba/Coupa) | **DISPLACED (overlaid)** | Employees stop touching the suite UI; Lio becomes the front door and the suite becomes plumbing. Politically framed as "augmenting" the suite, economically it commoditizes the suite's user-facing value. |
| **Tail-spend non-management** (the ~80% of transactions nobody negotiates) | **NEW COVERAGE, not replacement** | Negotiation Agent makes previously uneconomic negotiations economic → the 10% incremental savings. There was no incumbent here except "nothing." |
| **Consulting/analytics one-offs** (savings assessments) | **PARTIALLY ABSORBED** | Procurement Intelligence Agent + the $10M Challenge productize the classic consultant spend-analysis. |
| **Procurement people** | **RE-ROLED, not (officially) replaced** | Official line: "Our vision isn't about replacing people. It's about giving them their time back" → Agent Supervisors, Agent Process Designers, Agent Builders. Commercial reality in the case studies: ~120 FTEs "transitioned," 10 FTEs "freed", the value is monetized as labor capacity. Both truths matter; sequence the message by audience (HR/works councils vs CFO). |

## Why "replace labor, not software" is strategically smart (consultant read)

1. **18× bigger budget.** The labor+BPO line dwarfs the software line. Value-based pricing against FTE/BPO savings supports deal sizes seat-based SaaS can't reach.
2. **No rip-and-replace sale.** Suite replacements are 12-30-month CIO-sponsored megaprojects with procurement-of-procurement irony. An overlay that goes live in <2 weeks avoids the RFP gauntlet it would otherwise be subjected to.
3. **Avoids head-on war with SAP/Coupa, for now.** Positioning as "agents operating your suite" keeps the incumbents as nominal partners while quietly capturing the user relationship and the workflow data. (The incumbents understand this, hence Joule Intake Agent and Coupa buying Tonkean; see [06](06-market-and-competition.md).)
4. **BPO contracts are the perfect beachhead.** They're already quantified (a price per transaction/FTE exists), already outsourced (no internal job-loss fight), renewed on cycles (natural entry points), and universally disliked (slow, opaque). Displacing them at 7% of cost with better auditability is a nearly unarguable CFO case.
5. **The rebrand encodes the strategy.** "askLio" = a copilot you ask (software helping humans). "Lio" = a colleague/workforce (labor). The name change *is* the category change.

## The honest boundaries (what Lio does NOT do)

- Not an ERP, not a system of record, not an AP/payments platform, not a supplier network (it rides on existing ones).
- Strategic category management, complex capex sourcing, and relationship-heavy negotiations stay human (Lio preps them rather than replacing them. Negotiation Preparation, not Negotiation Agent).
- Direct-materials/production procurement depth (Jaggaer's home turf) is not visibly claimed; the case studies and agent catalog skew **indirect + transactional + tail**.
- "Lio X" (strategic procurement) is named but undescribed, the strategic layer is aspiration, not yet demonstrated product.

*Sources: newsroom ("Enterprise Systems Aren't the Bottleneck," "Agentic BPO/SSC," Series A release, manifesto), lio.ai product page, market research, full register in [09-sources.md](09-sources.md).*
