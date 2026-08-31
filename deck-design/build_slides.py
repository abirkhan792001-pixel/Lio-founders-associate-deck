#!/usr/bin/env python3
"""Build the Lio founders-associate deck.

MBB formatting in the Zeit AI house style, Inter only. Writes all 11 .dc.html artboards
and canvas.json from one shared CSS system, so the slides cannot drift apart.
Run:  python3 deck-design/build_slides.py  then  python3 deck-design/export_pdf.py
"""
import base64, json, pathlib

OUT = pathlib.Path(__file__).resolve().parent
FONT = (OUT / "fonts" / "Inter-Variable-latin.woff2").read_bytes()
FONT_B64 = base64.b64encode(FONT).decode()

INK, BODY, MUTED, FAINT = "#000000", "#3A3A3A", "#767676", "#9A9A9A"
SAGE, GREY, HAIR = "#DBDBCD", "#EFEFED", "#DCDCDC"

CSS = f"""
    @font-face {{ font-family:'Inter'; font-style:normal; font-weight:100 900; font-display:block;
      src:url(data:font/woff2;base64,{FONT_B64}) format('woff2'); }}
    * {{ box-sizing:border-box; }}
    @page {{ size:1920px 1080px; margin:0; }}
    html, body {{ width:1920px; height:1080px; }}
    body {{ margin:0; font-family:'Inter','Helvetica Neue',Arial,sans-serif; color:{BODY}; background:#FFFFFF;
      -webkit-font-smoothing:antialiased; -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
    a {{ color:inherit; }}
    .slide {{ width:1920px; height:1080px; position:relative; overflow:hidden; background:#FFFFFF; padding:46px 56px 0; }}
    .hd {{ display:flex; justify-content:space-between; align-items:flex-start; gap:48px; }}
    .eyebrow {{ font-size:11.5px; font-weight:700; letter-spacing:0.13em; text-transform:uppercase; color:{MUTED}; }}
    .eyebrow em {{ font-style:normal; color:{INK}; }}
    h1 {{ font-size:47px; font-weight:500; letter-spacing:-0.022em; line-height:1.13; margin:11px 0 0; color:{INK};
      max-width:1480px; }}
    .sub {{ font-size:20.5px; font-weight:400; line-height:1.38; color:{MUTED}; margin-top:13px; max-width:1420px; }}
    .brand {{ display:flex; align-items:center; gap:10px; flex-shrink:0; }}
    .brand span {{ font-size:25px; font-weight:500; letter-spacing:-0.01em; color:{INK}; }}
    .sec {{ font-size:20px; font-weight:700; color:{INK}; padding-bottom:9px; border-bottom:2px solid {INK}; }}
    .lbl {{ font-size:11px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:{MUTED}; }}
    .hair {{ border-bottom:1px solid {HAIR}; }}
    .chip {{ display:inline-block; font-size:11px; font-weight:700; letter-spacing:0.09em; text-transform:uppercase;
      padding:6px 12px; background:{SAGE}; color:{INK}; white-space:nowrap; }}
    .chip-dark {{ background:{INK}; color:#FFFFFF; }}
    .chip-line {{ background:transparent; border:1px solid #C6C6BC; color:#5A5A5A; font-weight:600; }}
    .panel {{ background:{SAGE}; padding:24px 30px; }}
    .panel-grey {{ background:{GREY}; padding:22px 26px; }}
    .b {{ font-size:16.5px; line-height:1.58; color:{BODY}; }}
    .b b, .b strong {{ color:{INK}; font-weight:600; }}
    .s {{ font-size:14.5px; line-height:1.5; color:{MUTED}; }}
    .rowh {{ font-size:19.5px; font-weight:600; color:{INK}; }}
    .num {{ font-size:22px; font-weight:700; color:{INK}; flex-shrink:0; }}
    .stat {{ font-size:84px; font-weight:700; letter-spacing:-0.035em; line-height:0.9; color:{INK}; }}
    .statcap {{ font-size:10.5px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:{MUTED};
      line-height:1.45; }}
    .foot {{ position:absolute; left:56px; right:56px; bottom:24px; display:flex; justify-content:space-between;
      align-items:flex-end; gap:48px; border-top:1px solid {HAIR}; padding-top:12px; }}
    .src {{ font-size:9.5px; font-weight:500; letter-spacing:0.06em; text-transform:uppercase; color:{FAINT};
      line-height:1.55; max-width:1330px; }}
    .pg {{ font-size:9.5px; font-weight:500; letter-spacing:0.06em; text-transform:uppercase; color:{FAINT};
      text-align:right; white-space:nowrap; line-height:1.55; }}
"""

MARK = ('<svg width="{s}" height="{s}" viewBox="0 0 48 48" fill="none" stroke="{c}" stroke-width="3.4" '
        'stroke-linecap="round" aria-hidden="true">'
        '<path d="M 24.00 44.00 A 20 20 0 1 1 42.13 15.55"></path>'
        '<path d="M 24.00 43.50 A 13.5 13.5 0 1 1 34.34 21.32"></path>'
        '<path d="M 24.00 43.20 A 8 8 0 1 1 28.59 28.65"></path></svg>')

STAR = ('<svg width="{s}" height="{s}" viewBox="0 0 48 48" stroke="{c}" stroke-width="{w}" stroke-linecap="round" '
        'fill="none" style="{st}" aria-hidden="true"><path d="M 30 24 L 44 24 M 28.24 28.24 L 38.14 38.14 '
        'M 24 30 L 24 44 M 19.76 28.24 L 9.86 38.14 M 18 24 L 4 24 M 19.76 19.76 L 9.86 9.86 M 24 18 L 24 4 '
        'M 28.24 19.76 L 38.14 9.86"></path></svg>')

def brand(size=30, colour=INK):
    return f'<div class="brand">{MARK.format(s=size, c=colour)}<span>Lio</span></div>'

def header(eyebrow, title, sub=None, right=None):
    eb = f'<div class="eyebrow">{eyebrow}</div>' if eyebrow else ""
    sb = f'<div class="sub">{sub}</div>' if sub else ""
    rt = right if right is not None else brand()
    return f'<div class="hd"><div>{eb}<h1>{title}</h1>{sb}</div>{rt}</div>'

def footer(src, page):
    return (f'<div class="foot"><div class="src">{src}</div>'
            f'<div class="pg">khan.abirhilal@gmail.com<br>{page} / 11</div></div>')

def page(body, bg=None):
    style = f' style="background:{bg};"' if bg else ""
    return (f'<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
            f'  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n  <style>{CSS}  </style>\n'
            f'</helmet>\n<div class="slide"{style}>\n{body}\n</div>\n</x-dc>\n</body>\n</html>\n')

S = {}

# ─────────────────────────────────────────────────────────── 01 · Cover
S["Main"] = page(f"""
  <div style="display:flex; justify-content:space-between; align-items:flex-start;">
    <div class="brand">{MARK.format(s=40, c=INK)}<span style="font-size:33px;">Lio</span></div>
    <div style="font-size:12px; font-weight:600; letter-spacing:0.3em; color:{INK}; padding-top:12px;">ABIR KHAN</div>
  </div>

  <div style="position:absolute; left:56px; top:250px; max-width:1000px;">
    <div style="font-size:12px; font-weight:700; letter-spacing:0.16em; text-transform:uppercase; color:#5F6055;">
      Founders Associate application · CEO &amp; CTO office · September 2026</div>
    <div style="font-size:104px; font-weight:500; letter-spacing:-0.03em; line-height:1.04; color:{INK}; margin-top:30px;">
      Pipeline,<br>rooms &amp; proof</div>
    <div style="font-size:26px; font-weight:400; line-height:1.42; color:#5F6055; margin-top:40px; max-width:760px;">
      A day-0 plan for the founders&#39; office. Who buys Lio, where they gather,
      and the machine I would run to get them there.</div>
  </div>

  {STAR.format(s=560, c="#3C3D35", w=0.55, st="position:absolute; right:150px; top:230px;")}

  <div style="position:absolute; left:56px; bottom:60px; right:56px; display:flex; justify-content:space-between;
       align-items:flex-end; border-top:1px solid #BFBFB2; padding-top:16px;">
    <div style="font-size:13px; font-weight:600; letter-spacing:0.02em; color:{INK};">
      Every number in this deck ships with a working file: the list, the calendar, the budget, the register.
      <span style="color:#6B6C60; font-weight:400;">Receipts in the appendix.</span></div>
    <div style="font-size:11px; font-weight:500; letter-spacing:0.06em; text-transform:uppercase; color:#6B6C60;">
      khan.abirhilal@gmail.com</div>
  </div>
""", bg=SAGE)

# ─────────────────────────────────────────────────────────── 02 · Who am I
photo = (f'<div style="width:158px; height:158px; background:{GREY}; border:1px solid {HAIR}; display:flex; '
         f'align-items:center; justify-content:center;"><span class="lbl">Photo</span></div>')
S["WhoAmI"] = page(f"""
  {header("", "Who am I and what do I bring to the table?",
          "Experience spans consulting to VC. Now driving Strategy, AI and GTM at SCAILE.",
          right=f'<div style="display:flex; align-items:flex-start; gap:34px; flex-shrink:0;">{photo}{brand()}</div>')}

  <div style="display:grid; grid-template-columns:repeat(2, minmax(0,1fr)); gap:88px; margin-top:46px;">
    <div>
      <div class="sec">Experience</div>
      <div class="hair" style="padding:23px 0 20px;">
        <div class="rowh">SCAILE Technologies</div>
        <div class="b" style="margin-top:5px;">Driving Strategy, AI and GTM. I build B2B go-to-market engines from scratch,
          from ICP research through outbound to AI search visibility.</div>
      </div>
      <div class="hair" style="padding:20px 0;">
        <div class="rowh">Alvarez &amp; Marsal</div>
        <div class="b" style="margin-top:5px;">Advised Fortune 500 CEOs on restructuring financial liabilities
          worth &gt;$100M.</div>
      </div>
      <div style="padding:20px 0;">
        <div class="rowh">Biome VC</div>
        <div class="b" style="margin-top:5px;">Built an investment thesis that shaped the investment philosophy of a
          $170M VC fund.</div>
      </div>

      <div class="sec" style="margin-top:20px;">Education</div>
      <div class="hair" style="padding:23px 0 18px;">
        <div style="display:flex; align-items:center; gap:14px; flex-wrap:wrap;">
          <div class="rowh">Nova School of Business and Economics, Lisbon</div>
          <span class="chip">FT #8 worldwide</span>
        </div>
        <div class="b" style="margin-top:5px;">MSc Finance. <b>Top 10% of class.</b></div>
      </div>
      <div style="padding:19px 0;">
        <div class="b">Won top prize in National Case Study Competitions (among 15,000+ participants).</div>
      </div>
    </div>

    <div>
      <div class="sec">Why Lio</div>
      <div class="hair" style="display:flex; gap:20px; padding:26px 0 23px;">
        <div class="num">1</div>
        <div>
          <div class="rowh">Shortest path to founding my own.</div>
          <div class="b" style="margin-top:6px;">I want to found my own startup, and nothing gets me closer than the
            founders&#39; office of a company at its inflection point. Fresh off a $30M a16z Series A, rebranding into
            a category, opening the US. This is the phase where I learn to lay the bricks.</div>
        </div>
      </div>
      <div class="hair" style="display:flex; gap:20px; padding:23px 0;">
        <div class="num">2</div>
        <div>
          <div class="rowh">Lio sells against a $180B line, not a $10B one.</div>
          <div class="b" style="margin-top:6px;">Everyone else builds procurement software. Lio replaces the execution
            labour, the same BPO scope at ~7% of cost. It is the sharpest enterprise wedge I have seen since I started
            working in GTM, and the market has barely heard it yet.</div>
        </div>
      </div>
      <div style="display:flex; gap:20px; padding:23px 0;">
        <div class="num">3</div>
        <div>
          <div class="rowh">I like building things.</div>
          <div class="b" style="margin-top:6px;">As a VC analyst I spent 100+ hours with founders and operators,
            learning what breaks. At SCAILE I build the playbook from scratch. For this application I already built
            Lio&#39;s: 219 named buyers of 2,245 identified, a re-verified 17-event programme, and a 60-post
            share-of-voice audit. All of it ships as working files.</div>
        </div>
      </div>
    </div>
  </div>

  <div style="position:absolute; left:56px; bottom:86px; display:flex; align-items:center; gap:20px;">
    <span class="lbl">Day-to-day stack</span>
    <span style="font-size:14px; color:{BODY};">Claude Code · Apollo · Clay · Figma · Webflow · Notion · HubSpot · Sheets</span>
  </div>
  {footer("Company facts per Lio&#39;s Series A release (2026-03-05) and the Lio/a16z $180B-vs-$10B thesis · "
          "own figures as in the Zeit AI deck", 2)}
""")

# ─────────────────────────────────────────────────────────── 03 · Structure
def agenda_row(n, text, chip, cls="chip", last=False):
    bb = "" if last else f" border-bottom:1px solid {HAIR};"
    return (f'<div style="display:flex; align-items:center; gap:20px; padding:23px 0;{bb}">'
            f'<div class="num" style="width:38px; font-size:19px; color:{MUTED};">{n}</div>'
            f'<div style="flex-grow:1; font-size:18px; font-weight:500; color:{INK};">{text}</div>'
            f'<span class="{cls}">{chip}</span></div>')

S["Agenda"] = page(f"""
  {header("", "The what, why and how",
          "How this deck is structured, and what I would drive once I join the team.")}

  <div style="display:grid; grid-template-columns:repeat(2, minmax(0,1fr)); gap:88px; margin-top:46px;">
    <div>
      <div class="sec">How the deck is structured</div>
      <div style="margin-top:6px;">
        {agenda_row("01", "Who buys Lio, sourced and counted", "Findings")}
        {agenda_row("02", "Where they gather: the event pipeline, re-verified", "Findings")}
        {agenda_row("03", "What the market hears on LinkedIn", "Findings")}
        {agenda_row("04", "What I would own from day 0", "Strategy", "chip chip-dark")}
        {agenda_row("05", "Why hire me, and what you get in return", "The offer", "chip chip-dark")}
        {agenda_row("06", "What it costs, and what it returns", "The ask", "chip chip-dark", last=True)}
      </div>

      <div class="panel" style="margin-top:34px;">
        <div style="font-size:17px; font-weight:700; color:{INK};">Brief summary</div>
        <ol style="margin:12px 0 0; padding-left:19px; font-size:15px; line-height:1.55; color:#2E2E28;">
          <li><b>The ICP is countable.</b> 219 named buyers of the 2,245 identified, across 4 segments. Outbound
            can start on day 0.</li>
          <li><b>The trigger is not the one we assumed.</b> One true third-party BPO in 35 swept accounts. In DACH
            the target is the captive SSC, and what starts the conversation is a change event.</li>
          <li><b>The event plan is live now.</b> The late-September gauntlet starts in two weeks, and every date is
            re-verified against organiser sources.</li>
          <li><b>Share of voice is founder-heavy and customer-silent.</b> The company posts, the market barely
            echoes, and nobody owns the fix.</li>
          <li><b>Everything ships with working files.</b> Spreadsheets, CSVs, registers. Not slideware.</li>
        </ol>
      </div>
    </div>

    <div>
      <div class="sec">Goals I want to achieve</div>
      <div style="margin-top:20px;">
        <div class="rowh">Short term</div>
        <div class="b" style="margin-top:10px;">1. <b>Own event ops end to end for Q3/Q4:</b> target lists per room,
          founder briefs, the sidecar dinners, and the next-day follow-ups nobody has time for.</div>
        <div class="b" style="margin-top:9px;">2. <b>Stand up the ICP outbound engine:</b> keep the named-buyer list
          alive in Apollo, feed sequences with the AEs, and report what converts.</div>
        <div class="b" style="margin-top:9px;">3. <b>Give Keil and Wagner leverage:</b> prep, notes, pipeline hygiene
          and the analysis layer of the $10M Challenge. Founders get hours back, every week.</div>
      </div>
      <div style="border-top:1px solid {HAIR}; margin-top:24px; padding-top:20px;">
        <div class="rowh">Long term</div>
        <div class="b" style="margin-top:10px;">1. <b>Own a slice of the US field engine</b> as the NYC pod scales. The Q2-27 calendar
          already requires a field-marketing layer.</div>
        <div class="b" style="margin-top:9px;">2. <b>Run the displacement campaign end to end:</b> from the SSOW/SIG
          rooms to qualified pilots. The &ldquo;93% cheaper&rdquo; story deserves its own funnel.</div>
        <div class="b" style="margin-top:9px;">3. <b>Earn ownership of a revenue line:</b> complete ownership of one
          repeatable motion, the way Lio defines new roles for its customers.</div>
      </div>
      <div class="panel-grey" style="margin-top:24px;">
        <div class="b"><b>The through-line:</b> three findings built from public sources before day 0, one machine to
          run them, and one ask priced against what that machine returns.</div>
      </div>
    </div>
  </div>
  {footer("Structure mirrors the three themes set for this application: who I am and why Lio · what I would own from "
          "day 0 · why hire me", 3)}
""")

# ─────────────────────────────────────────────────────────── 04 · ICP
GRID4 = "grid-template-columns: 330px 132px 132px 1fr 1fr; gap:26px;"
def icp_row(seg, sub, apollo, listed, centre, approach, last=False):
    bb = "" if last else f' class="hair"'
    return (f'<div{bb} style="display:grid; {GRID4} padding:26px 0;">'
            f'<div><div style="font-size:16.5px; font-weight:600; color:{INK};">{seg}</div>'
            f'<div class="s" style="margin-top:6px; font-size:13.6px;">{sub}</div></div>'
            f'<div><div style="font-size:27px; font-weight:700; color:{INK}; letter-spacing:-0.02em;">{apollo}</div>'
            f'<div class="statcap" style="font-size:9.5px; margin-top:3px;">Titled matches</div></div>'
            f'<div><div style="font-size:27px; font-weight:700; color:{INK}; letter-spacing:-0.02em;">{listed}</div>'
            f'<div class="statcap" style="font-size:9.5px; margin-top:3px;">Named · LinkedIn</div></div>'
            f'<div class="b" style="font-size:14.8px;">{centre}</div>'
            f'<div class="b" style="font-size:14.8px;">{approach}</div></div>')

S["IcpFindings"] = page(f"""
  {header("<em>01</em> · Findings · sourced from Apollo against Lio&#39;s reverse-engineered ICP",
          "The market is countable. The trigger is not the one the plan assumed",
          "219 named buyers are ready for outbound. The renewal trigger behind them holds in FS and the US, "
          "and breaks in DACH.")}

  <div style="display:grid; {GRID4} margin-top:26px; padding-bottom:9px; border-bottom:2px solid {INK};">
    <div class="lbl">Segment</div><div class="lbl">Buyers in Apollo</div><div class="lbl">On the list</div>
    <div class="lbl">The buying centre</div><div class="lbl">How to approach</div>
  </div>
  {icp_row("DACH industrial backbone",
           "Searched &euro;1&ndash;12B · <b style='color:#000;'>bullseye &euro;2.8&ndash;4.7B, 8&ndash;30K staff</b> "
           "· ~&#8532; family/foundation-owned", "851", "60",
           "<b>CPO sponsors, COO/CFO signs</b> via the SSC/FTE line; Procurement Excellence champions; CIO gatekeeps.",
           "<b>Trust-first, German, in person, and timed to a change event.</b> The DACH trigger is the captive SSC/GBS, "
           "not a BPO renewal: carve-outs, post-merger integration, hub migrations.")}
  {icp_row("Insurance &amp; financial services", "100% indirect spend · Munich Re, ERGO class", "156", "40",
           "<b>Head of Procurement / Sourcing &amp; Vendor Mgmt</b>; compliance-heavy, auditability opens the door.",
           "<b>Where the real renewals sit.</b> Zurich&ndash;Genpact (since 2012) is the one confirmed third-party "
           "procurement BPO in 35 swept accounts. Lead with the 93%-cheaper wedge.")}
  {icp_row("US F500 GBS &amp; BPO owners", "The people who sign outsourcing renewals · SSOW/SIG audience", "895", "60",
           "<b>VP GBS / Shared Services, Head of P2P, GPOs.</b> A persona classic procurement marketing barely reaches.",
           "<b>Budget capture, and the segment where renewals actually concentrate.</b> Every renewal is a qualified "
           "opp with a price to beat by 93%; Petras + Walmart engagement as credibility.")}
  {icp_row("DACH utilities &amp; mobility", "Regulated, process-heavy · DB (&ldquo;Loom&rdquo;), SWM, Lufthansa class",
           "343", "59",
           "<b>Leiter Einkauf / Beschaffung</b> + digitalisation leads; works councils in the room from day one.",
           "<b>Follow the Deutsche Bahn breadcrumb.</b> Regulated buyers move on references and auditability; "
           "German-language webinars &rarr; Bots &amp; Buyers &rarr; pilot.", last=True)}

  <div style="display:flex; align-items:center; gap:40px; margin-top:20px; background:{SAGE}; padding:22px 30px;">
    <div style="flex-shrink:0;">
      <div class="stat" style="font-size:76px;">219</div>
      <div class="statcap" style="margin-top:7px;">Named buyers on the list<br>122 companies</div>
    </div>
    <div class="b" style="font-size:15.5px; color:#2E2E28;">
      <b>The outbound cold-start problem is solved before day 0.</b> Every contact carries title, company, location and
      LinkedIn URL; 193 carry verified work emails, including prospect CPOs at Allianz, Deutsche Bahn, E.ON,
      ServiceNow, Citi, Beiersdorf and Miele. Apollo identifies <b>2,245 titled buyers</b> on the same filters
      (851 DACH industrial · 156 insurance/FS · 895 US GBS · 343 utilities/mobility). The refill pool is documented
      and reusable. Full list, companies tab and approach playbook: <b>Lio_ICP_Prospect_List.xlsx</b>
    </div>
  </div>

  <div style="display:flex; align-items:flex-start; gap:24px; margin-top:16px;">
    <div class="lbl" style="flex-shrink:0; padding-top:2px; color:{INK};">H1 radar sweep &rarr;</div>
    <div class="b" style="font-size:14.5px;">35 accounts swept for BPO/SSC evidence: <b>one true third-party
      procurement BPO</b> (Zurich&ndash;Genpact) plus one Accenture JV, 4 captive centres with a live change event,
      16 stable captives, 9 clean controls. <b>The DACH displacement target is the captive SSC, which has no renewal
      date</b>, so the trigger there is a change event, and the renewal-timed motion belongs to FS and the US.</div>
  </div>
  {footer("Sourced via Apollo · 31 August 2026 · search totals are Apollo database counts, not TAM · radar sweep and "
          "evidence grades per Lio_H1_Test_Scorecard.csv and 17-gtm-hypothesis-and-test-roadmap.md", 4)}
""")

# ─────────────────────────────────────────────────────────── 05 · Rooms
def ev(text, kind="solid"):
    styles = {
        "solid": f"background:{INK}; color:#FFFFFF;",
        "own":   f"background:{SAGE}; color:{INK};",
        "dim":   f"background:#FFFFFF; color:{BODY}; border:1px solid {HAIR};",
    }
    return (f'<div style="{styles[kind]} font-size:12.5px; font-weight:500; padding:8px 11px; margin-top:7px; '
            f'line-height:1.3;">{text}</div>')

S["EventFindings"] = page(f"""
  {header("<em>02</em> · Findings · the P1 programme, re-verified against organiser sources · 31 August 2026",
          "The rooms are picked and the dates hold. The programme now needs one owner",
          "&euro;929K and 204 staff-days across 17 events, with four starting in two weeks and no single owner "
          "below the founders.")}

  <div style="display:grid; grid-template-columns:216px repeat(4, minmax(0,1fr)); gap:24px; margin-top:26px;">
    <div></div>
    <div style="background:{INK}; color:#FFFFFF; font-size:12.5px; font-weight:700; letter-spacing:0.08em;
      text-transform:uppercase; text-align:center; padding:8px 0;">Q3-2026 · in 2 weeks</div>
    <div style="background:{INK}; color:#FFFFFF; font-size:12.5px; font-weight:700; letter-spacing:0.08em;
      text-transform:uppercase; text-align:center; padding:8px 0;">Q4-2026</div>
    <div style="background:{GREY}; color:{BODY}; font-size:12.5px; font-weight:700; letter-spacing:0.08em;
      text-transform:uppercase; text-align:center; padding:8px 0;">Q1-2027</div>
    <div style="background:{GREY}; color:{BODY}; font-size:12.5px; font-weight:700; letter-spacing:0.08em;
      text-transform:uppercase; text-align:center; padding:8px 0;">Q2-2027</div>

    <div style="padding-top:8px;">
      <div style="font-size:15.5px; font-weight:700; color:{INK};">The gauntlet runs</div>
      <div class="s" style="font-size:12.5px; margin-top:5px;">4 P1 events + Bots &amp; Buyers NYC · 18 days ·
        2 continents. Split: Keil+Heinzmann&rarr;Amsterdam, Wagner+Petras&rarr;Boston.</div>
    </div>
    <div>
      {ev("SSON San Diego · Sep 14–17")}{ev("+ Bots &amp; Buyers NYC · Sep 23 (own)", "own")}
      {ev("ProcureCon EU Köln · Sep 22–24")}{ev("ProcureCon East Boston · Sep 28–30 · lead")}
      {ev("DPW Amsterdam · Sep 30–Oct 1")}
    </div>
    <div>
      {ev("SIG Fall Chicago · Oct 25–28 · Petras", "own")}{ev("SSOW DACH Berlin · Nov 17–19", "own")}
      {ev("BME-Symposium Berlin · Nov 18–19", "own")}
      <div class="s" style="font-size:12.5px; margin-top:9px;">Berlin double-week holds. B&amp;B EU Munich
        (Oct 27–28, own) collides with SIG Chicago. <b style="color:{INK};">Split settled: Petras&rarr;Chicago,
        Keil+Wagner&rarr;Munich, Heinzmann&rarr;demo stage</b>, conditional on SIG scheduling the buy-side session
        Oct 25–26.</div>
    </div>
    <div>
      {ev("ProcureCon West Vegas · Mar 8–10 · committed", "dim")}{ev("SSOW Orlando · Mar 8–11 · BPO keynote", "dim")}
      {ev("APC · Mar 22–24 · now New Orleans", "dim")}
      <div class="s" style="font-size:12.5px; margin-top:9px;">Same-week collision resolved: Keil&rarr;Orlando,
        Petras&rarr;Vegas.</div>
    </div>
    <div>
      {ev("Handelsblatt Apr 6–7 · Gartner SC May 3–5 · NAPES tbd", "dim")}
      {ev("eLösungstage May 11–12 · WPC London May 18–20", "dim")}
      {ev("DPW NY Jun 2–3 · Proc. Summit HH Jun 23–24", "dim")}
      <div class="s" style="font-size:12.5px; margin-top:9px;">7 events. Breaks the current team without the Jan-27
        field-marketing hire.</div>
    </div>

    <div></div>
    <div class="statcap" style="text-align:center; margin-top:10px;">&euro;165K new + &euro;70K committed · 65 staff-days</div>
    <div class="statcap" style="text-align:center; margin-top:10px;">&euro;87K · 32 staff-days · cheapest, sharpest</div>
    <div class="statcap" style="text-align:center; margin-top:10px;">&euro;108K + &euro;35K committed · 31 staff-days</div>
    <div class="statcap" style="text-align:center; margin-top:10px;">&euro;376K · 76 staff-days · the heavy quarter</div>
  </div>

  <div class="panel-grey" style="margin-top:20px;">
    <div class="b"><b>Status check, six weeks after the plan was written:</b> all four gauntlet dates hold. New since
      the plan: <b>Bots &amp; Buyers went transatlantic.</b> NYC Sep 23 (application-only, mid-gauntlet) and the EU
      flagship Oct 27–28, <b>colliding with SIG Chicago (Oct 25–28)</b>. The split is now settled, with Oct 25–26
      scheduling made a condition of the SIG booking. APC 2027 moved <b>Miami &rarr; New Orleans</b>. NAPES&#39;
      reported Denver move is <b>unverified</b>, so hold the &euro;35K. Two early-birds close <b>Sep 30</b>: BME-Symposium (&euro;100)
      and eLösungstage (&euro;300).</div>
  </div>

  <div style="display:flex; align-items:center; gap:34px; margin-top:18px;">
    <div style="flex-shrink:0;">
      <div class="stat" style="font-size:64px;">17</div>
      <div class="statcap" style="margin-top:6px;">P1 events<br>Q3-26 &rarr; Q2-27</div>
    </div>
    <div class="b" style="border-left:3px solid {INK}; padding-left:26px;">
      <b>&euro;736K new + &euro;105K committed + 12% contingency &asymp; &euro;929K envelope · 204 staff-days ·
      10 sidecar dinners (&euro;120K of the total, and the line to protect last).</b><br>
      This programme currently has no single owner below the founders. That is the job I am applying to do,
      starting with the four events that begin in two weeks.</div>
  </div>

  <div style="display:grid; grid-template-columns:1fr 1fr; gap:52px; margin-top:18px; border-top:1px solid {HAIR};
       padding-top:14px;">
    <div>
      <div class="lbl" style="color:{INK};">Which seat each room holds</div>
      <div class="b" style="font-size:14px; margin-top:8px;">The buying committee has four seats and <b>no single event
        reaches more than two.</b> Sponsor (CPO) sits in Handelsblatt, WPC, DPW and the dinners; economic buyer
        (COO/CFO) in SSOW ×3, SIG and SSON San Diego; champion in the German BME fairs; gatekeeper (CIO/CISO) in
        IT-Sourcing and the Gartner symposia.</div>
    </div>
    <div>
      <div class="lbl" style="color:{INK};">What the recomputed ICP says about this spend</div>
      <div class="b" style="font-size:14px; margin-top:8px;">The 17 verified customers cluster at <b>&euro;2.8–4.7B
        revenue, 8–30K staff</b>. That is exactly the German practitioner fairs&#39; demographic, and the cheapest fit per
        euro on the calendar. The US circuit aims a tier higher against <b>zero verified US customers.</b></div>
    </div>
  </div>
  {footer("Figures: Lio P1 budget &amp; staffing plan (Jul 2026), mid-range estimates · dates re-verified 31 Aug 2026 "
          "· seat map and ICP bullseye per 20-event-strategy-and-icp-baseline.md", 5)}
""")

# ─────────────────────────────────────────────────────────── 06 · Share of voice
def bar(label, sub, n, width, highlight=False):
    ink = INK
    lab_w = "268px"
    fill = INK if not highlight else INK
    box = (f'background:{SAGE}; padding:15px 12px;' if highlight else 'padding:15px 0;'
           f' border-bottom:1px solid {HAIR};')
    return (f'<div style="display:flex; align-items:center; gap:18px; {box}">'
            f'<div style="width:{lab_w}; flex-shrink:0;">'
            f'<div style="font-size:15.5px; font-weight:{"700" if highlight else "500"}; color:{ink};">{label}</div>'
            f'<div class="s" style="font-size:12.5px; margin-top:2px;">{sub}</div></div>'
            f'<div style="display:flex; align-items:center; gap:14px; flex-grow:1;">'
            f'<div style="height:17px; width:{width}px; background:{fill};"></div>'
            f'<div style="font-size:15px; font-weight:700; color:{ink};">{n}</div></div></div>')

S["VoiceFindings"] = page(f"""
  {header("<em>03</em> · Findings · every publicly indexed LinkedIn post about Lio · 8 search angles · 31 August 2026",
          "One voice carries the category, and the 150-logo customer wall is silent",
          "60 indexed posts. Keil authors 40% of them, and customers author none.")}

  <div style="display:grid; grid-template-columns:1.08fr 0.92fr; gap:72px; margin-top:30px;">
    <div>
      <div class="sec" style="font-size:17px;">Posts found, by who is talking</div>
      {bar("Vladimir Keil (CEO)", "the channel, effectively", "24", 430)}
      {bar("Lio company page", "incl. the askLio era", "9", 161)}
      {bar("Third-party commentary", "analysts, influencers, reactions", "9", 161)}
      {bar("Heinzmann &amp; Wagner (CTO/COO)", "&nbsp;", "7", 125)}
      {bar("Lio team (&ldquo;Lions&rdquo;)", "Petras, new-hire posts, FDE Night", "7", 125)}
      {bar("Investors &amp; network", "YC, a16z orbit", "4", 71)}
      <div style="margin-top:8px;">{bar("Customers", "despite a 150+ enterprise logo wall", "0 posts found", 4, True)}</div>
      <div class="s" style="font-size:12.5px; margin-top:12px;">Found via search-engine indexing of linkedin.com, so this is
        a floor rather than a census. The login wall hides an unknown share of posts. Direction is what matters.</div>
    </div>

    <div style="display:flex; flex-direction:column; gap:14px;">
      <div class="panel-grey">
        <div class="rowh" style="font-size:16.5px;">One voice carries 40% of the channel</div>
        <div class="b" style="font-size:14px; margin-top:7px;">Keil authors 24 of 60 indexed posts; the founder team
          together, 31. That is a single point of failure, and also the cheapest amplifier available. Founder-content ops
          (drafts, recaps, clips) multiplies an asset that already works.</div>
      </div>
      <div class="panel-grey">
        <div class="rowh" style="font-size:16.5px;">The logo wall is silent</div>
        <div class="b" style="font-size:14px; margin-top:7px;">Zero customer-authored posts, despite award-grade
          stories at Schaeffler (MOU), REHAU (BME + Porsche Consulting AI Impact Award 2026) and Surventis. Every
          go-live, award and dinner should ship with a co-marketing ask. Nobody owns that ask today.</div>
      </div>
      <div class="panel-grey">
        <div class="rowh" style="font-size:16.5px;">Moments, not a cadence</div>
        <div class="b" style="font-size:14px; margin-top:7px;">Activity spikes at the YC launch, the BME award,
          Schaeffler milestones and the Series A, then goes quiet. The 17-room P1 calendar, plus Lio&#39;s own
          franchises, is a built-in content engine if every room produces before/during/after posts. That loop needs
          an owner.</div>
      </div>
    </div>
  </div>

  <div style="display:flex; align-items:center; gap:34px; margin-top:26px; background:{SAGE}; padding:22px 30px;">
    <div style="flex-shrink:0;">
      <div class="stat" style="font-size:68px;">60</div>
      <div class="statcap" style="margin-top:6px;">Distinct posts<br>in the register</div>
    </div>
    <div class="b" style="color:#2E2E28;"><b>Share of voice is founder-heavy and customer-silent. That is an ops gap, not a budget gap,
      and the events &rarr; content &rarr; advocacy loop I would run closes it.</b> Full register with URLs,
      authors, dates and themes: <b>14-linkedin-posts.md</b></div>
  </div>
  {footer("Compiled via 8-angle search sweep · dates decoded from LinkedIn activity IDs · logo count, awards and "
          "customer facts per Lio site/newsroom and press (Aug 2026)", 6)}
""")

# ─────────────────────────────────────────────────────────── 07 · Day 0
AGENTS = ["Freetext Agent","Search Agent","Guided Buying Agent","Approvals Agent","RFQ Agent","PR Review Agent",
          "Supplier Onboarding Agent","Order Confirmation Agent","Goods Receipt Agent","Invoice Agent",
          "Sourcing Agent","Negotiation Agent","Contract Negotiation Agent","Lio Assistant",
          "Procurement Intelligence","Agent Supervisor"]
agent_chips = "".join(f'<span style="display:inline-block; font-size:12.5px; color:{BODY}; border:1px solid {HAIR}; '
                      f'padding:9px 13px; margin:0 8px 9px 0; font-size:13.5px;">{a}</span>' for a in AGENTS)

S["DayZero"] = page(f"""
  {header("<em>04</em> · Strategy · what I would own from day 0", "")}
  <div style="margin-top:6px; font-size:56px; font-weight:500; letter-spacing:-0.025em; line-height:1.14;
       max-width:1620px; color:{INK};">
    I own the machine between the founders and the pipeline: the list, the rooms, and the follow-through.</div>
  <div class="sub" style="margin-top:20px;">One line, because that is the job: everything repeatable that stands
    between a named buyer and a booked founder conversation. In practice, the first 90 days:</div>

  <div style="display:grid; grid-template-columns:repeat(3, minmax(0,1fr)); gap:52px; margin-top:66px;">
    <div style="border-top:2px solid {INK}; padding-top:26px;">
      <span class="chip">Live · day 0–30</span>
      <div class="rowh" style="margin-top:14px;">The gauntlet</div>
      <div class="b" style="margin-top:9px;">Four P1 events plus Bots &amp; Buyers NYC in 18 days across two
        continents, starting in two weeks. I run the ops: <b>target lists per room, founder briefs, the sidecar
        dinners, next-day follow-ups.</b> The 219-name buyer list goes into sequences before the first flight.</div>
    </div>
    <div style="border-top:1px solid {HAIR}; padding-top:26px;">
      <span class="chip chip-line">Next · day 30–60</span>
      <div class="rowh" style="margin-top:14px;">The wedge quarter</div>
      <div class="b" style="margin-top:9px;">Berlin double-week + SIG Chicago, the rooms where the budget owners sit:
        <b>third-party BPO in the US/FS rooms, captive SSC and GBS heads in the DACH ones.</b> I own room prep and the
        follow-up motion, pipe every conversation into the CRM, and ship the first outbound-cohort report.</div>
    </div>
    <div style="border-top:1px solid {HAIR}; padding-top:26px;">
      <span class="chip chip-line">Ongoing · day 60–90</span>
      <div class="rowh" style="margin-top:14px;">The machine, boring on purpose</div>
      <div class="b" style="margin-top:9px;">Calendar &rarr; list &rarr; room &rarr; follow-up &rarr; pipeline,
        <b>measured weekly and running without heroics.</b> Founders get hours back; the Q1-27 US quarter starts
        planned, staffed and booked early instead of rushed.</div>
    </div>
  </div>

  <div style="position:absolute; left:56px; right:56px; bottom:104px; border-top:1px solid {HAIR}; padding-top:26px;">
    <div class="lbl" style="color:{INK}; margin-bottom:12px;">The workforce I&#39;d be selling ·
      &ldquo;85% of procurement operations are done by Lio Agents&rdquo;</div>
    <div style="max-width:1780px;">{agent_chips}</div>
  </div>
  {footer("Agent roster per lio.ai/product via 02-product-and-features.md · 85% claim is Lio&#39;s own, "
          "company-reported", 7)}
""")

# ─────────────────────────────────────────────────────────── 08 · Why hire me
def why(n, title, body, last=False):
    cls = "" if last else ' class="hair"'
    return (f'<div{cls} style="display:flex; gap:22px; padding:33px 0;">'
            f'<div class="num" style="width:34px;">{n}</div><div>'
            f'<div class="rowh">{title}</div><div class="b" style="margin-top:6px;">{body}</div></div></div>')

S["WhyMe"] = page(f"""
  {header("<em>05</em> · The offer", "Why hire me, and what you get in return",
          "Not potential. Output you can inspect before day 0.")}

  <div style="display:grid; grid-template-columns:1.15fr 0.85fr; gap:80px; margin-top:48px;">
    <div>
      <div class="sec">What you get</div>
      {why("01", "An operator in the founders&#39; office who ships unmanaged.",
           "This deck, the named-buyer ICP list, the re-verified event programme, the LinkedIn audit and the H1 "
           "hypothesis test were <b>built before day 0, from public information.</b> That is the working speed you "
           "hire, not a promise of it.")}
      {why("02", "The outbound cold-start problem, already solved.",
           "219 named, titled, LinkedIn-linked buyers across four ICP segments, 193 of them with verified work "
           "emails, and an approach playbook for each. <b>The AEs and SDRs start warm</b>, and the list machine "
           "keeps refilling it.")}
      {why("03", "A ~&euro;1M event programme run with owner-level care.",
           "17 P1 events, 204 staff-days, 10 sidecar dinners. The highest-ROI line in the GTM budget currently has "
           "<b>no single owner below the founders.</b> I am that owner. Deadlines tracked, rooms prepped, every "
           "conversation followed up.")}
      {why("04", "A profile that spans the room.",
           "Consulting rigour (A&amp;M, Fortune 500 CFO work), investor pattern-matching (Biome VC) and hands-on GTM "
           "engineering (SCAILE). <b>CFO-grade analysis down to SDR-grade execution</b>, the exact range a founders&#39; "
           "associate needs.", last=True)}
    </div>

    <div>
      <div class="sec">The guarantee</div>
      <div class="panel" style="margin-top:34px;">
        <span class="chip chip-dark">Zero bullshit</span>
        <div class="b" style="margin-top:16px; color:#2E2E28;">Lio promises customers <b>$10M in identified value, or donates $100K.</b> Same energy, scaled to me:</div>
        <div style="font-size:20px; line-height:1.45; font-weight:600; color:{INK}; margin-top:14px;">
          If after 90 days you would not enthusiastically re-hire me, I hand over the machine (documented, running,
          transferable) and we shake hands.</div>
        <div class="b" style="margin-top:14px;">No ramp-up excuses. No knowledge hostage-taking.</div>
      </div>
      <div style="display:flex; align-items:flex-end; gap:26px; margin-top:56px;">
        <div class="stat" style="font-size:112px;">90</div>
        <div class="statcap" style="padding-bottom:10px; color:{INK};">Days to prove it.<br>
          <span style="color:{MUTED};">The machine stays either way.</span></div>
      </div>
    </div>
  </div>
  {footer("The $10M-or-$100K challenge is Lio&#39;s own public offer (lio.ai/10-million)", 8)}
""")

# ─────────────────────────────────────────────────────────── 09 · The ask
def scen(fig, chip, chip_cls, title, body, tag="", last=False):
    cls = "" if last else ' class="hair"'
    tg = (f' <span class="lbl" style="font-size:10.5px;">{tag}</span>') if tag else ""
    return (f'<div{cls} style="display:flex; gap:24px; align-items:flex-start; padding:31px 0;">'
            f'<div style="width:208px; flex-shrink:0; font-size:38px; font-weight:700; letter-spacing:-0.025em; '
            f'color:{INK}; line-height:1;">{fig}</div><div>'
            f'<span class="{chip_cls}">{chip}</span>{tg}'
            f'<div class="rowh" style="margin-top:11px;">{title}</div>'
            f'<div class="b" style="margin-top:6px;">{body}</div></div></div>')

S["TheAsk"] = page(f"""
  {header("<em>06</em> · The ask", "The base case returns the year-one salary thirteen times over",
          "A market-anchored ask, priced against the H1 thesis in three scenarios.")}

  <div style="display:grid; grid-template-columns:1.15fr 0.85fr; gap:80px; margin-top:46px;">
    <div>
      <div class="sec">The return · H1 thesis ARR, year 1</div>
      {scen("&euro;0–175K", "Kill · rotate", "chip chip-line", "The funnel fails its own gate.",
            "0–1 contracts. Assessment&rarr;POC under 10%, POC&rarr;contract under 20%, which are <b>file 17&#39;s own kill "
            "thresholds.</b> The motion rotates to the next-best hypothesis. Phase 0 costs ~&euro;0, which is the "
            "whole point of testing before spending.")}
      {scen("&euro;1.35M", "Refine · narrow", "chip", "Signal in FS only. DACH stays captive.",
            "~2 FS-anchor wins at ~&euro;500K + ~2 DACH change-event wins at ~&euro;175K. <b>This is already today&#39;s "
            "read:</b> Zurich&ndash;Genpact is the one confirmed third-party BPO in 35 swept accounts. DACH runs on "
            "captive-SSC change events with no renewal date.", tag="Base case")}
      {scen("&euro;2.4M", "Confirm · scale", "chip chip-dark", "Both segments clear the confirm bar.",
            "~3 FS + ~5 DACH wins as the Renewal Radar scales 35 &rarr; ~75 accounts and conversion clears "
            "<b>assessment&rarr;POC 30%, POC&rarr;contract 50%</b>. Carries into the already-funded Q1/Q2-27 US wave "
            "once SOC 2 closes.", last=True)}

      <div style="margin-top:20px; border-top:1px solid {HAIR}; padding-top:16px;">
        <div class="lbl" style="color:{INK}; margin-bottom:12px;">What moves these numbers · the three load-bearing assumptions</div>
        <div style="display:grid; grid-template-columns:repeat(3, minmax(0,1fr)); gap:26px;">
          <div class="b" style="font-size:14px;"><b>ACV.</b> No public ACV exists. ~7% of displaced cost is Lio&#39;s
            own disclosed mechanic. One verified POC replaces the whole estimate.</div>
          <div class="b" style="font-size:14px;"><b>Radar scale.</b> 35 accounts swept, 50–100 targeted. Every 10 added
            yields ~2 more Group-A triggers at today&#39;s 17% hit rate.</div>
          <div class="b" style="font-size:14px;"><b>Segment mix.</b> An FS win is worth ~3× a DACH win. Invert which
            segment converts and the base case roughly halves.</div>
        </div>
      </div>
    </div>

    <div>
      <div class="sec">The ask</div>
      <div class="panel" style="margin-top:34px;">
        <span class="chip chip-dark">Market-anchored</span>
        <div style="font-size:50px; font-weight:700; letter-spacing:-0.03em; color:{INK}; margin-top:16px;
          line-height:1;">&euro;95–120K</div>
        <div class="lbl" style="color:{INK}; margin-top:10px;">Base, year 1 · anchor &euro;105K</div>
        <div class="b" style="margin-top:14px; color:#2E2E28;"><b>+ 0.05–0.15% equity</b>, standard 4-year vest,
          1-year cliff.</div>
        <div class="b" style="margin-top:9px; color:#2E2E28;"><b>Re-rated twice:</b> at day 90 (the guarantee,
          previous slide) and at the H1 decision gate, Jan–Feb 2027.</div>
        <div style="font-size:13.5px; line-height:1.5; color:#5E5F55; margin-top:15px; border-top:1px solid #C6C6BC;
          padding-top:13px;">Munich/Berlin founders-associate postings run &euro;51–90K (Glassdoor 2026). Scoped above
          that median for a CEO-and-CTO-office mandate and A&amp;M / Biome-VC seniority, and deliberately under the US
          Series-A chief-of-staff band. A proposed anchor, not a demand.</div>
      </div>

      <div style="display:flex; align-items:flex-end; gap:24px; margin-top:52px;">
        <div class="stat" style="font-size:104px;">13×</div>
        <div class="statcap" style="padding-bottom:8px; color:{INK};">Base-case ARR &divide; year-1 base.<br>
          <span style="color:{MUTED};">Confirm case clears it 23×. Only kill doesn&#39;t,<br>which is exactly what the
          test is for.</span></div>
      </div>
    </div>
  </div>
  {footer("Modeled, not forecast. ACV at ~7% of displaced BPO/SSC cost (file 08) · funnel per file 17&#39;s decision "
          "gate. Full math: 21-compensation-and-arr-scenarios.md · salary: Glassdoor Munich/Berlin 2026", 9)}
""")

# ─────────────────────────────────────────────────────────── 10 · Thank you
S["ThankYou"] = page(f"""
  <div style="display:flex; justify-content:space-between; align-items:flex-start;">
    <div class="brand">{MARK.format(s=40, c=SAGE)}<span style="font-size:33px; color:{SAGE};">Lio</span></div>
    <div style="font-size:12px; font-weight:600; letter-spacing:0.3em; color:{SAGE}; padding-top:12px;">ABIR KHAN</div>
  </div>

  <div style="position:absolute; left:56px; top:330px;">
    <div style="font-size:12.5px; font-weight:700; letter-spacing:0.2em; text-transform:uppercase; color:#9A9B8E;">
      One for all. All for procurement.</div>
    <div style="font-size:118px; font-weight:500; letter-spacing:-0.03em; line-height:1.02; color:{SAGE};
      margin-top:26px;">Thank you</div>
    <div style="font-size:25px; font-weight:400; color:#B9BAAC; margin-top:34px; max-width:860px; line-height:1.42;">
      Ready to start before day 0. The machine is already running.</div>
  </div>

  {STAR.format(s=430, c=SAGE, w=0.5, st="position:absolute; right:210px; top:300px;")}

  <div style="position:absolute; left:56px; right:56px; bottom:56px; display:flex; justify-content:space-between;
       align-items:flex-end; border-top:1px solid #3A3B33; padding-top:16px;">
    <div style="font-size:12px; font-weight:500; letter-spacing:0.06em; text-transform:uppercase; color:#9A9B8E;">
      Founders Associate application · CEO &amp; CTO office</div>
    <div style="text-align:right;">
      <a href="https://www.linkedin.com/in/abir-khan-1143211ab/" style="display:block; font-size:13px; font-weight:600;
        text-decoration:underline; color:{SAGE};">LinkedIn</a>
      <div style="font-size:12px; color:#9A9B8E; margin-top:5px;">khan.abirhilal@gmail.com</div>
    </div>
  </div>
""", bg=INK)

# ─────────────────────────────────────────────────────────── 11 · Appendix
def filerow(chip, name, desc, last=False):
    cls = "" if last else ' class="hair"'
    return (f'<div{cls} style="padding:29px 0;"><span class="chip">{chip}</span>'
            f'<div style="font-size:16px; font-weight:600; color:{INK}; margin-top:11px;">{name}</div>'
            f'<div class="b" style="font-size:14px; margin-top:5px;">{desc}</div></div>')

S["Appendix"] = page(f"""
  {header("", "Appendix: the working files",
          "Every claim in this deck has a file behind it. Nothing here is slideware.")}

  <div style="display:grid; grid-template-columns:repeat(2, minmax(0,1fr)); gap:88px; margin-top:44px;">
    <div>
      {filerow("Spreadsheet", "Lio_ICP_Prospect_List.xlsx · 13-icp-prospect-list.md",
               "Named-buyer list across 4 ICP segments. Companies, titled contacts with LinkedIn URLs, Apollo match "
               "totals, per-persona approach playbook, executive summary.")}
      {filerow("Spreadsheet", "16-event-status-update.md + Lio_P1_Event_Status_2026-08-31.csv",
               "60 scored events across US/UK/EU-DACH in P1/P2/P3 tiers. Every P1 date, venue and deadline re-verified "
               "against organiser sources; passed deadlines flagged, changes annotated.")}
      {filerow("Spreadsheet", "Lio_P1_Budget_Staffing.csv",
               "Quarter-by-quarter budget and staffing for the 17-event P1 programme: &euro;736K new + &euro;105K "
               "committed + contingency &asymp; &euro;929K, 204 staff-days, founder allocation, hiring triggers.")}
      {filerow("Hypothesis", "17-gtm-hypothesis-and-test-roadmap.md · 18-trigger-group-outreach-angles.md · "
               "Lio_H1_Test_Scorecard.csv",
               "The strongest GTM bet as a falsifiable card with kill criteria and decision gates, the 35-account "
               "Renewal Radar with an evidence grade per row, and first-touch drafts for the six trigger accounts.",
               last=True)}
    </div>
    <div>
      {filerow("Register", "14-linkedin-posts.md",
               "Every publicly indexed LinkedIn post about Lio found across 8 search angles: company, founders, team, "
               "events, customers, investors, German-language, third-party commentary.")}
      {filerow("Knowledge base", "00–12 · Lio knowledge base",
               "The sourced dossier this work builds on: company, product, pain points, competitive map, customer "
               "proof, strategic levers. Every fact graded for reliability.")}
      {filerow("Playbook", "19-september-action-sheet.md · 20-event-strategy-and-icp-baseline.md",
               "29 September actions ordered by due date with the three calls that cannot slip, plus recomputed ICP "
               "firmographics, the seat-per-room map and the preparation protocol by tier.")}
      {filerow("Model", "21-compensation-and-arr-scenarios.md",
               "The math behind the ask. Salary benchmarked to Munich/Berlin market data, and three H1 ARR scenarios "
               "built on file 17&#39;s own decision-gate thresholds. Every figure marked modeled, not forecast.")}
      {filerow("This deck", "15-deck-design.md · 19-lio-brand-language-and-agents.md",
               "The design spec: MBB formatting, Inter (saved in deck-design/fonts/), the brand/tone register, and "
               "the placeholders still owed (photo).", last=True)}
    </div>
  </div>
  {footer("All files in the repository accompanying this application", 11)}
""")

# ─────────────────────────────────────────────────────────── write
ORDER = [("Main", "01 · Cover"), ("WhoAmI", "02 · Who am I & why Lio"), ("Agenda", "03 · The what, why and how"),
         ("IcpFindings", "04 · Findings 01 · the ICP"), ("EventFindings", "05 · Findings 02 · the rooms"),
         ("VoiceFindings", "06 · Findings 03 · share of voice"), ("DayZero", "07 · What I'd own from day 0"),
         ("WhyMe", "08 · Why hire me"), ("TheAsk", "09 · The ask · comp & ARR scenarios"),
         ("ThankYou", "10 · Thank you"), ("Appendix", "11 · Appendix · working files")]

for name, _ in ORDER:
    (OUT / f"{name}.dc.html").write_text(S[name], encoding="utf-8")

artboards = []
for i, (name, title) in enumerate(ORDER):
    artboards.append({"file": f"{name}.dc.html", "x": (i % 5) * 2040, "y": (i // 5) * 1280,
                      "w": 1920, "h": 1080, "title": title})
canvas = {"artboards": artboards,
          "annotations": [{"id": "note-owed", "x": 0, "y": -430, "w": 520,
                           "text": "Design: MBB formatting in the Zeit AI style. Bone/sage (#DBDBCD), white content "
                                   "slides, black ink, Inter only (saved in deck-design/fonts/). Action titles, "
                                   "section rules, source line and page number on every slide.\n\nOwed by Abir before "
                                   "sending:\n1. Headshot photo (slide 02, top right)\n2. LinkedIn links are set to "
                                   "linkedin.com/in/abir-khan-1143211ab - confirm it's yours\n3. The shell mark is a "
                                   "redrawn approximation - swap for the real logo asset if Lio shares one."}],
          "launch": {"view": "canvas"}}
(OUT / "canvas.json").write_text(json.dumps(canvas, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"wrote {len(ORDER)} slides + canvas.json")
