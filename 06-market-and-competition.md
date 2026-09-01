# 06 · Market & Competitive Landscape

← [Lio vs Legacy](05-lio-vs-legacy.md) | Next: [Customers & Proof Points](07-customers-and-proof-points.md) →

## Market sizing

| Market | Size / forecast | Source quality |
|---|---|---|
| Procurement **software** | ~$10.1B (2025) → ~$21.3B (2033), ~10% CAGR | Grand View; corroborated $8.9-9.5B by Precedence/FBI/Polaris |
| Procurement **orchestration platforms** | $4.1B (2024) → $12.9B (2033), 13.7% CAGR | Dataintelo, second-tier, directional only |
| **Agentic AI in supply chain/procurement** | <$2B (2025) → **$53B (2030), 93.5% CAGR**; advanced autonomous agents $492M → $15.9B; non-AI SCM software *declining* -9.3%/yr; 70% of SCM vendors with agentic capabilities by end-2027 (vs 1% in 2024) | Gartner figures **via Opstream's summary**, not Gartner directly |
| **Labor being targeted** | $180B/yr procurement talent; BPO up to 20× software cost | Lio/a16z pitch framing |
| Gartner adoption predictions | 40% of procurement teams with ≥1 AI agent by 2028; 90% of B2B buying AI-agent-intermediated by 2028 ($15T+ through agent exchanges); 1 in 4 enterprise software purchases made by agents with no human in loop by 2028 | Gartner via trade press |

**Read:** the software TAM alone doesn't justify a16z's bet; the labor-substitution TAM does. Gartner's forecast of *declining* non-AI SCM software is the clearest signal that value is migrating from licenses to agents.

## Incumbents and their agentic counter-moves

| Vendor | Position | Known weaknesses | Agentic response (as of Jul 2026) |
|---|---|---|---|
| **SAP Ariba** | S2P suite + network; Gartner MQ Leader '25 & '26 | "Click tax" UI, steep learning curve, complex implementations, supplier network fees | Next-gen Ariba on BTP with **Joule agents**: Bid Analysis GA Q1'26, **Intake Agent GA Jun 2026** (chat/email/Teams, routes across SAP *and non-SAP*); Joule Agent Runtime **free through Dec 31, 2026** |
| **Coupa** | BSM suite; MQ Leader, highest execution | Supplier portal friction, cluttered legacy admin; $250K+ enterprise cost | Most aggressive: **Navi** multi-agent portfolio + Agent Studio/Orchestrator; 4 agentic acquisitions, Cirtuo, Scoutbee, Rossum, and **Tonkean (May 2026, est. hundreds of $M)** to own intake/orchestration outright |
| **Ivalua** | Configurable S2P; MQ Leader ×3 | 8-12-month rollouts; global programs 18-30 months; partner-heavy | **IVA + IVA Studio**, "the agentic operating system for procurement" (platform v10) |
| **Jaggaer** | S2P, direct-materials strength | Behind Coupa on ease of use | **JAI** multi-agent orchestrator, policy-grounded, source-cited, multi-model (Gemini + Claude), marketed on "eliminating hallucination risk" |
| **Oracle** | Fusion Cloud Procurement; MQ Leader | ERP gravity, procurement UX secondary | AI agents embedded in Fusion roadmap |
| **GEP** | S2P + services; MQ Leader; tops Spend Matters SolutionMap incl. Intake & Orchestration | Services-led | **GEP Quantum (Qi)**, network of autonomous agents across S2P |
| **Zycus** | MQ Visionary | Mid-tier perception | **Merlin** agentic platform (autonomous negotiation, intake, analytics agents) |
| **Email/Excel** | The real incumbent |, | None. Greenfield. |

**Strategic pattern:** every suite has announced agents *inside its own walls*, and the suites are absorbing standalone intake (SAP native agent, Coupa×Tonkean). Spend Matters flagged this in April 2025 as "an emerging threat to the standalone intake and orchestration market." The counter-argument (Lio's): requests don't live inside one suite, execution spans ERP + inbox + contracts + open web, and suite agents are bolt-ons to legacy data models.

## The startup competitive set

| Company | Funding / scale | Positioning | vs Lio |
|---|---|---|---|
| **Zip** (SF) | $190M Series D @ **$2.2B valuation** (Oct 2024, BOND); ~$360M+ total; $107B+ spend processed; Anthropic, Arm, Canva, Coinbase, Snowflake as customers; **only orchestration platform in the 2026 S2P MQ (Visionary)** | Workflow-first intake-to-pay orchestration, AI added on; ~8-week deployments | The category gorilla, US-centric. Workflow/forms-first vs Lio's agent-first execution; routes work vs *does* work. Lio differentiates on autonomy depth + DACH/European enterprise (ERP estates, works councils, language). |
| **ORO Labs** (US) | $100M Series C (Mar 2026, Brighton Park + Goldman Growth); $160M total; 300% rev growth; Coca-Cola, Pfizer, Novartis, Thermo Fisher | "Agentic procurement orchestration" atop ERP/S2P; SAP-ecosystem-strong | **Most direct thesis analogue.** ORO orchestrates guided workflows with agents; Lio claims end-to-end autonomous execution incl. open-web research + negotiation. Better funded post-C. |
| **Omnea** (London) | $50M Series B (Sep 2025, Insight + Khosla); $75M+ total; 5× growth; Spotify, Wise, MongoDB, Monzo | CFO-led intake + AI supplier-risk/SRM | Nearest **European** rival for the intake wedge; sells governance to the CFO vs Lio's execution-to-COO/CPO. |
| **Levelpath** (US) | $55M+ Series B (Jun 2025, Battery, Neeraj Agrawal, ex-Coupa board); $100M+ total | AI-native full S2P platform ("Hyperbridge"), mobile-first, + autonomous agents | Closest US analogue on "AI-native + agents" but sells suite **replacement**; Lio's overlay posture is less rip-and-replace. |
| **Tonkean** | ~$84M raised; **acquired by Coupa May 2026** | No-code intake orchestration, 250+ connectors | Removed from the independent field; validates category + incumbent M&A appetite (and marks exit comps). |
| **Pactum** (US/EE) | $54M Series C (Insight); $100M+ total; 489% growth in AI-handled spend; Honeywell, Novartis, Tetra Pak, Walmart heritage | **Autonomous negotiation only** | The depth benchmark Lio's Negotiation Agent is judged against. Lio bundles negotiation as one agent of many. |
| **Globality** | ~$356M total | Autonomous sourcing for services spend; Fidelity, Santander, BT, Tesco | Sourcing-event point solution; not request-to-PO execution. |
| **Fairmarkit** | $78M total | Autonomous RFQs for tail/spot buys | A feature inside Lio's scope. |
| **Keelvar** | $43M total | Sourcing-optimization bots (logistics strength) | Point solution. |
| **Mercanis** (Berlin) | €17.3M Series A (Jun 2025, Partech) | Agentic sourcing/SRM for upper-mittelstand | Lio's most local competitor, a funding class below. |

Aggregate: the orchestration/agentic-procurement field has raised **$1.2B+**. Lio's $30M is mid-pack, its edge must come from product depth + DACH enterprise beachhead + the BPO wedge, not capital.

## Analyst consensus & risk map

**Bullish:** McKinsey, agentic AI will transform **≥75% of procurement activities**; AI-guided negotiations delivered 10-15% savings; 25-40% productivity potential. Hackett, early adopters ~10% productivity, leaders 25%+; intake triage/supplier-risk/PO processing are proven use cases; 64% of procurement leaders say AI will transform their jobs. Gartner Hype Cycle 2025, intake at Peak of Inflated Expectations; orchestration "transformational."

**Bearish / risks:**
- Gartner: **>40% of agentic AI projects will be canceled by end-2027** (poor planning, unclear governance, undefined human-oversight boundaries).
- MIT NANDA: ~**95% of enterprise GenAI pilots deliver no measurable P&L impact**, though buying from specialized vendors succeeds ~67% vs ~⅓ as often for internal builds (argument *for* vendors like Lio, warning about pilot purgatory).
- Forrester 2026: $10B+ enterprise value destroyed by ungoverned GenAI; buyers will demand **proof of outcomes over AI claims**.
- Hackett: data quality is the #1 barrier; hallucination remains a live compliance concern (Jaggaer markets *against* it).

## Where Lio wins / loses (synthesis)

**Wins:** (1) the adoption gap *is* the market, intake UX is the quantified root cause of maverick spend; (2) time-to-value asymmetry, 2 weeks vs 12-30 months; (3) labor economics incumbents can't price against without self-cannibalizing; (4) incumbent agents are single-suite bolt-ons; (5) the BPO wedge has no incumbent defender.

**Loses:** (1) suite bundling at price-zero ("good-enough" free agents inside the invoice the CFO already pays); (2) Zip's category ownership + capital in the US; (3) governance/trust drag in regulated Global 2000 (Munich Re-class buyers demand auditability before autonomous negotiation); (4) point-solution squeeze per agent (Pactum et al.) while suites squeeze from above; (5) every headline metric is company-reported, outcome proof (Forrester's 2026 buyer demand) is the battleground.

*Attribution: [09-sources.md](09-sources.md).*
