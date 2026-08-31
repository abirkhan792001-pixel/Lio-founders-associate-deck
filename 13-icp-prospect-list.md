# 13 · ICP Prospect List — Executive Summary

← [Index](00-INDEX.md) · Data file: **[Lio_ICP_Prospect_List.xlsx](Lio_ICP_Prospect_List.xlsx)** · Sourced & enriched via Apollo **2026-08-31** for the founders-associate application package.

## What was built

A **named-buyer outbound list for Lio**, sourced against the ICP reverse-engineered from Lio's own event history ([10-events-and-icp.md](10-events-and-icp.md)): four segments, explicit firmographic + title filters, every contact enriched to full name, work email and LinkedIn URL.

## The numbers

| Segment | On the list | Verified emails | Any email | Companies (list) | **Buyers in Apollo** | Companies in Apollo |
|---|---|---|---|---|---|---|
| DACH Industrial | 60 | 51 | 53 | 32 | **851** | 153 |
| Insurance & FS (DACH) | 40 | 30 | 33 | 30 | **156** | 34 |
| US GBS & BPO Owners | 60 | 55 | 55 | 30 | **895** | 1,665 |
| Utilities & Mobility (DACH) | 59 | 57 | 57 | 30 | **343** | 81 |
| **Total** | **219** | **193** | **198** | **122** | **2,245** | 1,933 |

- **Seniority mix:** 30 C-suite (CPOs) · 129 Head-of · 58 VP · 2 Director.
- "Buyers in Apollo" = Apollo's own `total_entries` for the identical filter set — the refill pool. The list is the top slice (pages 1–2 per search); **~2,000 more titled buyers remain unpulled** with the same, documented filters.
- Marquee names on the list: CPOs/heads at Allianz, Zurich, Deutsche Bahn, E.ON, EnBW, ServiceNow, Citi, Fidelity, Wells Fargo, Beiersdorf, Holcim, Bühler, Miele, TRUMPF, Knorr-Bremse, Dräger, GEA, KUKA, SCHOTT (Zeiss's foundation sister) and Giesecke+Devrient (already in Lio's orbit).

## The four segments in one line each

1. **DACH Industrial (primary):** €1–12B manufacturers, heavily family/foundation-owned, conservative SAP estates — Schaeffler/Brose/REHAU lookalikes. Trust-first, German, room-before-email.
2. **Insurance & FS (secondary):** 100% indirect spend → the fastest agentic-BPO math; Munich Re's "Agent Experience World" visit is the reference story. Compliance in the room from day one.
3. **US GBS & BPO owners (expansion):** the people who *sign outsourcing renewals* — VP/Head of GBS, Shared Services, P2P/S2P GPOs. Budget capture ("your BPO costs 93% too much"), email-first, Petras as the credible sender.
4. **Utilities & Mobility (quiet fourth):** regulated, process-heavy, works councils early; follow the Deutsche Bahn "Loom" breadcrumb; webinar → Bots & Buyers → pilot.

Full per-segment approach (buying center, lead message, channel sequence, best rooms, proof points, timing triggers): **Approach Playbook tab** of the xlsx.

## How it was sourced (reproducible)

- **Company search filters** (per segment): DACH industrial = DE/AT/CH · 5,001–50,000 employees · revenue ≥ $800M · NAICS 31–33. Insurance/FS = DE/AT/CH · 5,001–200,000 · NAICS 524/523/522. US GBS = US · 10,001–500,000 · revenue ≥ $2B. Utilities/mobility = DE/AT/CH · 2,001–500,000 · NAICS 22/48.
- **People search:** procurement/GBS title lists (CPO, Head of Procurement/Indirect/Excellence/Digital, Leiter Einkauf, VP GBS/Shared Services, Head of P2P/S2P, GPO…) × seniority c_suite/vp/head/director × the segment's company filters.
- **Enrichment:** Apollo People Match per person (bulk, 10 per call) — full name, work email + status, LinkedIn URL, org data. No phone reveals, no waterfall vendors used.

## Cost transparency (surfaced per Apollo MCP policy)

- Searches: free. **Enrichment: 219 lead credits (1/contact), 0 failed matches.**
- Team pool before this run: 120,030 lead credits, 368 used. After: ~587 used — **<0.5% of the annual pool**; ~37.9K general credits untouched by this run.

## Suggested first motion (what I would do with it on day 0)

1. Load the 193 verified-email contacts into segment sequences (German copy for DACH, BPO-wedge copy for US GBS) with the AEs as senders.
2. Cross-reference against the Sep–Nov room lists (SSON San Diego, Cologne, Boston, DPW Amsterdam, SIG Chicago, Berlin double-week) — meeting-booking outreach beats cold outreach for every contact attending.
3. Refill monthly from the documented filters; log replies/meetings per segment to learn which of the four ICPs converts — data Lio doesn't publicly have yet.

*Compliance: Apollo-licensed B2B data under the team's seat; DACH sequences should carry legitimate-interest framing + opt-out per GDPR practice.*
