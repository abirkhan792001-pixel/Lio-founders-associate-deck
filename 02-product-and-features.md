# 02 · Product & Features

← [Company Overview](01-company-overview.md) | Next: [Pain Points & Solutions](03-pain-points-and-solutions.md) →

## What Lio is selling

**An AI procurement workforce, not a procurement suite.** Every purchase request is handled by specialized agents working **in parallel** — "a single request enters the system; within seconds, multiple agents research, negotiate, validate, and complete the order." The product sits **on top of** existing ERP/P2P systems (which remain the system of record) and executes the work humans and BPO providers do today. Humans move "on the loop" as **Agent Supervisors**; escalation happens **by exception, not by default**.

The company's own framing: **"Five layers. One transformation."**

## Layer 1 — Agent-Augmented Buying (the requester experience)

The intake wedge. Employees "buy in two clicks," in natural language, in their mother tongue (175+ languages claimed), inside tools they already use (Microsoft Teams, Outlook, or embedded in Ariba/Coupa) — no new logins, no forms-first taxonomy.

| Agent | What it does |
|---|---|
| **Freetext Agent** | Converts unstructured input — free text, dialogues, uploaded quotations, even **photos** — into standardized, policy-complete procurement requests (auto GL-mapping/categorization at intake) |
| **Search Agent** | Finds catalog items, preferred vendors, existing framework agreements before new spend is created |
| **Guided Buying Agent** | "Virtual coach" steering requesters through company guidelines ("high-service buying" questions defined by procurement) |
| **Approvals Agent** | Routes to the correct *available* approver; preserves existing approval workflows |
| **RFQ Agent** | Lets requesters independently create competition and collect quotes from multiple suppliers |

## Layer 2 — Operational Automation (procurement ops)

The claim anchoring the headline metric: **"85% of procurement operations are done by Lio Agents."**

| Agent | What it does |
|---|---|
| **PR Review Agent / "No-Touch POs"** | Validates purchase requests and converts them to POs in the ERP without human intervention |
| **Supplier Onboarding Agent** | Evaluates + onboards suppliers using internal and external data |
| **Lio Supplier Portal** | Suppliers self-upload catalogs; buyers keep approval control |
| **Order Confirmation Agent** | Chases suppliers for confirmations; resolves disputes autonomously |
| **Goods Receipt Agent(s)** | Matches deliveries against PO/order confirmations and guidelines |
| **Invoice Agent** | 24/7 autonomous **3-way matching** (invoice / PO / goods receipt) |

## Layer 3 — Scaled Savings (sourcing & negotiation)

| Agent | What it does |
|---|---|
| **Sourcing Agent** | Compresses RFQ cycles "from weeks to days" |
| **Negotiation Agent** | Runs end-to-end autonomous negotiations — explicitly targeted at **"previously uneconomic negotiations"** (tail spend nobody had capacity to negotiate) → the "10% incremental savings" claim |
| **Negotiation Preparation** | Market benchmarks before strategic calls; live support during calls |
| **Contract Negotiation Agent** | Monitors contracts for renegotiation potential; "contract reviews 120 → 2 min" |

## Layer 4 — Buyer Enablement (supercharge the humans)

| Capability | What it does |
|---|---|
| **Lio Assistant** | Personal buyer copilot with customizable "skills"; customers feed it docs, meeting notes, internal podcasts → an **"agent-ready knowledge base"** (TÜV SÜD: "our single source of truth… lets us scale even as teams change") |
| **Procurement Intelligence Agent** | Identifies savings opportunities, suggests strategies (analytics layer) |

## Layer 5 — Workforce Management (the orchestration/control plane)

The strategic differentiator and the rebrand's meaning:

- **Agent Operating Procedures (AOPs)** — the signature mechanism: a company's existing SOPs, manuals, and policies are rebuilt as **agent-executable workflows**. This is how Lio encodes client-specific process logic instead of shipping a one-size-fits-all workflow.
- **Agent Supervisor** — dashboard for managing the agentic workforce: performance, optimization, **human-on-the-loop controls for critical decisions**.
- **New human roles the product defines:** Agent Process Designer, Procurement Agent Builder, Procurement Agent Supervisor — Lio is explicitly selling a *future org design*, not just software (see the "From Operational Buyer to Agent Supervisor" newsroom piece).
- ("Lio X" appears in the site nav as a strategic-procurement component but is never described — watch item.)

## How a request flows (synthesized end-to-end picture)

1. Employee describes need in free text/photo/quote-upload in Teams → **Freetext Agent** structures it; **Search Agent** checks catalogs/framework agreements; **Guided Buying Agent** applies policy questions; GL-coding happens at intake.
2. If sourcing is needed: **RFQ/Sourcing Agent** creates competition; **Negotiation Agent** negotiates (or preps the human buyer for strategic calls).
3. **Approvals Agent** routes; **PR Review Agent** validates → **No-Touch PO** created in the existing ERP (SAP et al. stay the single source of truth, bidirectional sync, no shadow data).
4. **Supplier Onboarding Agent** + **Supplier Portal** handle new-vendor setup in parallel.
5. Post-PO: **Order Confirmation Agent** chases/resolves; **Goods Receipt Agent** matches; **Invoice Agent** 3-way-matches — 24/7.
6. **Agent Supervisor** + AOPs govern everything; humans handle exceptions only; **Procurement Intelligence** mines the resulting data for savings.

## Integrations & technical posture

- **Named systems:** SAP, SAP Ariba, Coupa, Oracle, Microsoft Dynamics, Workday, Ivalua; **Microsoft Teams and Outlook** as front-ends. "Seamlessly integrate with your existing P2P/ERP systems" via standard APIs/middleware.
- **Integration claim:** live in **< 2 weeks** including approvals, implementation, training, hypercare (vs 8–30 months for suite rollouts — see [05](05-lio-vs-legacy.md)).
- **Architecture stance:** operates *inside* existing platforms; ERP remains system of record; bidirectional sync; preserves existing approval/compliance logic; no rip-and-replace, modular adoption.
- **Delivery model:** cloud SaaS on **Microsoft Azure Europe**; Microsoft Official Partner; agents run 24/7. Delivery is FDE/implementation-engineer-led (see [01](01-company-overview.md)).

## Security & compliance

- **ISO 27001 certified** · **EU-GDPR compliant** · Azure Europe hosting · SCCs for US transfers.
- **Gaps to know:** no SOC 2 claim anywhere; no public trust/security page; first dedicated Security, Risk & Compliance Manager currently being hired; privacy page lags (old address listed). For US enterprise sales, SOC 2 will likely be table stakes — an execution item post-Series A.
- Auditability is a core pitch element vs BPO's "black box": agents are described as **24/7 auditable**, with real-time policy control and escalation after repeated failures.

## Pricing

- **No public pricing.** No pricing page, no tiers. Fully consultative enterprise motion: free consultation, "Value Consultants," and the **$10M Challenge** (identify $10M in value or donate $100K). Everything signals **value-based pricing** anchored on labor/BPO savings rather than per-seat SaaS (consistent with the $180B-labor thesis; see [08](08-strategic-value-levers.md)).

## Product evolution in one line

**2023:** "askLio — AI copilot for procurement teams" (free-text intake in Teams) → **2026:** "Lio — the multi-agent system that *is* your procurement operations." The intake copilot became the wedge; the agent workforce became the product.

*Sources: lio.ai, lio.ai/product, lio.ai/about-us, lio.ai/demo, newsroom articles — full register in [09-sources.md](09-sources.md).*
