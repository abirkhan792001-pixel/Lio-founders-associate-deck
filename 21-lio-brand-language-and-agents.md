# 21 · Lio Brand Language — Agents, Tone & Copy (for the deck's design elements)

← [Index](00-INDEX.md) · Feeds: **[15-deck-design.md](15-deck-design.md)** and the artboards in [deck-design/](deck-design/).

**Why this file exists:** Abir asked for a crawl of the Lio (formerly askLio) website to harvest the agent roster, tone and copy for the deck. **Direct crawling is not possible from this workspace** — `lio.ai`, `www.lio.ai`, `asklio.ai` (and archive.org mirrors) are all blocked by the network egress policy, verified 2026-08-31. This register is reconstructed instead from (a) the knowledge base compiled from lio.ai in earlier sessions ([01](01-company-overview.md), [02](02-product-and-features.md), graded sources in [09](09-sources.md)), (b) the two homepage screenshots Abir supplied (hero + industries ring), and (c) public search snippets. Treat it as the working brand-language contract for the deck.

## 1 · The agent roster (the product, by name)

Lio's framing: **"Five layers. One transformation."** Every purchase request is handled by specialized agents **in parallel**; humans move on-the-loop as Agent Supervisors. The names below are Lio's own, per lio.ai/product (via [02](02-product-and-features.md)).

| Layer | Agents |
|---|---|
| 1 · Agent-Augmented Buying | **Freetext Agent** · **Search Agent** · **Guided Buying Agent** · **Approvals Agent** · **RFQ Agent** |
| 2 · Operational Automation | **PR Review Agent** ("No-Touch POs") · **Supplier Onboarding Agent** · **Order Confirmation Agent** · **Goods Receipt Agent** · **Invoice Agent** (+ Lio Supplier Portal) |
| 3 · Scaled Savings | **Sourcing Agent** · **Negotiation Agent** · **Contract Negotiation Agent** (+ Negotiation Preparation) |
| 4 · Buyer Enablement | **Lio Assistant** · **Procurement Intelligence Agent** |
| 5 · Workforce Management | **Agent Supervisor** (+ Agent Operating Procedures; human roles it creates: Agent Process Designer, Procurement Agent Builder, Procurement Agent Supervisor) |

Headline product claims that ride with the roster: **"85% of procurement operations are done by Lio Agents"** · "a single request enters the system; within seconds, multiple agents research, negotiate, validate, and complete the order" · live in **< 2 weeks** · contract reviews **120 → 2 min** · same BPO scope at **~7% of the cost**.

**Used in the deck:** slide 07 (Day 0) carries the full 16-agent roster as a mono chip constellation — the workforce Abir would be selling — labelled with the 85% claim.

## 2 · Tone of voice (how Lio sounds)

1. **Category-defining superlatives, stated flat:** "The world's first multi-agent system for procurement." No hedging, no "leading provider of".
2. **Workforce, not software:** agents are named like colleagues (Freetext Agent, Invoice Agent); the org chart is part of the product ("Agent Supervisor"). Keil's line: *"Instead of building software to help humans do procurement work faster, Lio deploys AI agents that execute the workflow themselves."* On the Series A video overlay: **"we're not building software."**
3. **Imperative, second person:** "Regain your strategic relevance!" · "Scale Savings Without Scaling Headcount" · "Make your users fall in love with procurement."
4. **Put-your-money-where-your-mouth-is:** the **$10M Challenge** (find $10M in value or donate $100K). Values said out loud: "Zero Bullshit", "Get Shit Done", Outlier/"S-tier people", Stay Hungry. "90+ Lions."
5. **Numbers before adjectives:** 85% · <2 weeks · 120→2 min · 1M+ users · 150+ enterprises · $30M a16z Series A.
6. **Terminal aesthetic for facts:** system-ish monospace labels for industries, tags and metadata (the industries ring: Airlines · Chemicals · Public Sector · Energy & Utilities · Industrial Manufacturing · OEMs · Consumer & Retail · Telecommunication · Banking · Insurance); sentence-case grotesque for the big statements.
7. **Mission line:** "One for all. All for procurement." Origin framing: "Procurement wasn't just a workflow problem. It was a language problem."

## 3 · Verbatim copy bank (safe to quote in the deck)

- "The world's first multi-agent system for procurement" — hero H1
- "Every purchase request is handled in parallel by specialized agents: they research suppliers, negotiate terms, manage approvals, and track deliveries." — hero paragraph (screenshot)
- "Regain your strategic relevance!" — hero close (screenshot)
- "Announcing Lio's $30M Series A, led by Andreessen Horowitz!" — banner (screenshot)
- "we're not building software." — Series A video overlay (screenshot)
- "Request a demo" / "Request Demo" — the one CTA, white pill
- "The Engine Behind a New Era of Procurement" · "Scale Savings Without Scaling Headcount" · "Make your users fall in love with procurement." · "One for all. All for procurement."
- "85% of procurement operations are done by Lio Agents."
- a16z (Seema Amble): "We're entering a phase in the enterprise where AI moves beyond workflow co-pilots to autonomous, multi-agent execution."

## 4 · How this lands in the deck's design elements

| Site element (screenshots) | Deck translation |
|---|---|
| Dark teal-black hero with blurred light streaks | Cover + Thank-You full-bleed texture (`lio-hero.jpg`, generated, in-repo); content slides on `#0B1416` with a faint teal wash |
| Sentence-case grotesque hero type, white, ~regular weight | Inter (see [fonts/README](deck-design/fonts/README.md)) — cover 500, titles 600, verdict numbers 800 |
| Monospace chips (industries ring, video-card caption) | Geist Mono chips everywhere metadata lives: eyebrows, FINDINGS/STRATEGY tags, segment names, agent roster, filenames, footers |
| Announcement banner strip | Cover top strip: the application banner |
| White pill CTA ("Request a demo") | Cover pill: "Request the 90 days"; STRATEGY/THE OFFER chips |
| Lime asterisk widget (right edge) | Lime `✳`-style 8-spoke starburst chip — cover, thank-you; lime = the single accent (verdict borders, LIVE chips) |
| Glassy video card, bottom-left of hero | Cover card: "WE'RE NOT BUILDING SLIDEWARE." — every number ships with a working file |
| Industries ring (mono labels on dark) | Slide 04 ICP segment chips; slide 07 agent-roster constellation |
| "Lio" wordmark + shell mark | Redrawn shell-arc SVG mark + Inter wordmark (swap for the real asset if used internally) |

**Boundary kept:** the deck states on the cover strip and thank-you that it is an *application by Abir Khan*, not a Lio-produced document — brand homage, no impersonation.
