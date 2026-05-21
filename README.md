<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Olfactory NYC — Store Scorecards 2026</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/umd/react.production.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0/umd/react-dom.production.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/7.23.2/babel.min.js"></script>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: #F1F5F9; font-family: 'Inter', system-ui, -apple-system, sans-serif; }
    button { font-family: inherit; }
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: #F1F5F9; }
    ::-webkit-scrollbar-thumb { background: #CBD5E1; border-radius: 3px; }
    table { border-collapse: collapse; }
    @media (max-width: 768px) {
      .store-layout { grid-template-columns: 1fr !important; }
      .store-sidebar { display: flex !important; flex-direction: row !important; overflow-x: auto; }
      .store-sidebar button { min-width: 140px; flex-shrink: 0; }
    }
  </style>
</head>
<body>
  <!-- Password Gate -->
  <div id="gate" style="display:flex;align-items:center;justify-content:center;min-height:100vh;">
    <div style="background:#fff;border-radius:16px;padding:40px 36px;width:100%;max-width:360px;box-shadow:0 4px 24px rgba(0,0,0,0.08);text-align:center;">
      <div style="font-size:32px;margin-bottom:8px;">🌿</div>
      <h1 style="font-size:18px;font-weight:600;color:#0F172A;margin-bottom:4px;">Olfactory NYC</h1>
      <p style="font-size:13px;color:#64748B;margin-bottom:28px;">Store Scorecards 2026</p>
      <input id="pw-input" type="password" placeholder="Enter password"
        style="width:100%;padding:10px 14px;border:1.5px solid #CBD5E1;border-radius:8px;font-size:14px;outline:none;margin-bottom:10px;font-family:inherit;transition:border 0.15s;"
        onkeydown="if(event.key==='Enter')checkPw()"
        onfocus="this.style.borderColor='#6366F1'" onblur="this.style.borderColor='#CBD5E1'" />
      <div id="pw-error" style="color:#991B1B;font-size:12px;margin-bottom:10px;display:none;">Incorrect password — please try again.</div>
      <button onclick="checkPw()"
        style="width:100%;padding:10px;background:#0F172A;color:#fff;border:none;border-radius:8px;font-size:14px;font-weight:500;cursor:pointer;font-family:inherit;">
        Enter
      </button>
    </div>
  </div>

  <!-- App (hidden until password correct) -->
  <div id="root" style="display:none;"></div>

  <script>
    function checkPw() {
      var val = document.getElementById('pw-input').value;
      if (val === 'customscent') {
        document.getElementById('gate').style.display = 'none';
        document.getElementById('root').style.display = 'block';
        if (window.initApp) { window.initApp(); }
        else { window._appReady = true; }
      } else {
        document.getElementById('pw-error').style.display = 'block';
        document.getElementById('pw-input').value = '';
        document.getElementById('pw-input').focus();
      }
    }
  </script>

  <script type="text/babel">
    const { useState } = React;

// Ancillary sales — YTD Jan 1–May 14 (Philadelphia QTD Apr 1–May 11)
// pct_chg = YoY change in ancillary net sales %
const ANCILLARY = {
  "BLK":   { anc_net: 50522.40, anc_pct: 5.6,  anc_orders: 1078, py_net: 41397.79, pct_chg: +22.0  },
  "ATL":   { anc_net: 29820.18, anc_pct: 5.1,  anc_orders: 619,  py_net: 4305.91,  pct_chg: +592.5 },
  "UNION": { anc_net: 28445.24, anc_pct: 5.9,  anc_orders: 630,  py_net: 5960.43,  pct_chg: +377.2 },
  "WBG":   { anc_net: 27511.61, anc_pct: 7.0,  anc_orders: 589,  py_net: 17321.01, pct_chg: +58.8  },
  "MOT":   { anc_net: 27051.83, anc_pct: 5.3,  anc_orders: 562,  py_net: 26299.90, pct_chg: +2.9   },
  "GEO":   { anc_net: 23753.55, anc_pct: 5.5,  anc_orders: 517,  py_net: 11998.30, pct_chg: +98.0  },
  "BOS":   { anc_net: 21031.51, anc_pct: 4.8,  anc_orders: 488,  py_net: 15453.97, pct_chg: +36.1  },
  "DAL":   { anc_net: 15876.12, anc_pct: 5.1,  anc_orders: 353,  py_net: 0,        pct_chg: null   },
  "MIA":   { anc_net: 15755.99, anc_pct: 5.5,  anc_orders: 292,  py_net: 2333.63,  pct_chg: +575.1 },
  "PHL":   { anc_net: 13361.66, anc_pct: 6.9,  anc_orders: 249,  py_net: 0,        pct_chg: null   },
};

// Google Maps ratings (sourced May 2026) — all Olfactory NYC locations
const RATINGS = {
  "BLK":   { google: 4.9, google_count: 850,  note: null },
  "MOT":   { google: 4.8, google_count: 1528, note: null },
  "WBG":   { google: 4.9, google_count: 397,  note: null },
  "PHL":   { google: 4.7, google_count: 39,   note: null },
  "ATL":   { google: 4.8, google_count: 149,  note: null },
  "BOS":   { google: 4.8, google_count: 403,  note: null },
  "UNION": { google: 4.7, google_count: 62,   note: null },
  "GEO":   { google: 4.9, google_count: 526,  note: null },
  "MIA":   { google: 4.9, google_count: 173,  note: null },
  "DAL":   { google: 5.0, google_count: 81,   note: null },
};

// Event revenue (Jan–Apr 2026) — in-store events only, offsites excluded
// Source: HB booking sheets, col A (deposit) + col C (remaining balance)
// Excludes any line where col G contains "offsite"
const EVENT_REVENUE = {
  "BLK":  84734.03,
  "BOS":  24360.28,
  "UNION":37495.05,
  "GEO":   4404.38,
  "ATL":   8861.48,
  "MIA":  10957.71,
  "DAL":   8644.64,
  "PHL":  11752.56,
  "MOT":      0.00,
  "WBG":      0.00,
};

// Seats per store (customer seating capacity)
const SEATS = {"BLK":22,"MOT":12,"WBG":15,"BOS":17,"GEO":11,"DAL":18,"MIA":22,"ATL":20,"UNION":22,"PHL":28};

// Lease data — 2026 total rent (base + additional) and square footage
// Sales/Rent uses per-store annualization via STORE_DAYS
const LEASE = {
  "BLK":   { sqft: 1400, rent: 287500.00 },
  "MOT":   { sqft: 680,  rent: 108400.85 },
  "WBG":   { sqft: 800,  rent: 103776.95 },
  "PHL":   { sqft: 2420, rent: 266234.57 },
  "ATL":   { sqft: 1199, rent: 135657.00 },
  "BOS":   { sqft: 1101, rent: 214700.00 },
  "UNION": { sqft: 1200, rent: 109890.00 },
  "GEO":   { sqft: 690,  rent: 206844.00 },
  "MIA":   { sqft: 1400, rent: 136657.96 },
  "DAL":   { sqft: 1073, rent: 100991.07 },
};

// Turnover data — last 6 months, annualized (×2). NYC cluster combined.
const TURNOVER = {
  "BLK":   { headcount: 92, terminated: 12, involuntary: 0,  voluntary: 12, rate6m: 13.0, rateAnnual: 26.1, isNYC: true  },
  "MOT":   { headcount: 92, terminated: 12, involuntary: 0,  voluntary: 12, rate6m: 13.0, rateAnnual: 26.1, isNYC: true  },
  "WBG":   { headcount: 92, terminated: 12, involuntary: 0,  voluntary: 12, rate6m: 13.0, rateAnnual: 26.1, isNYC: true  },
  "PHL":   { headcount: 17, terminated: 3,  involuntary: 2,  voluntary: 1,  rate6m: 17.6, rateAnnual: 35.3, isNYC: false },
  "ATL":   { headcount: 29, terminated: 4,  involuntary: 1,  voluntary: 3,  rate6m: 13.8, rateAnnual: 27.6, isNYC: false },
  "BOS":   { headcount: 32, terminated: 2,  involuntary: 1,  voluntary: 1,  rate6m:  6.2, rateAnnual: 12.5, isNYC: false },
  "UNION": { headcount: 22, terminated: 4,  involuntary: 0,  voluntary: 4,  rate6m: 18.2, rateAnnual: 36.4, isNYC: false },
  "GEO":   { headcount: 28, terminated: 1,  involuntary: 0,  voluntary: 1,  rate6m:  3.6, rateAnnual:  7.1, isNYC: false },
  "MIA":   { headcount: 18, terminated: 4,  involuntary: 1,  voluntary: 3,  rate6m: 22.2, rateAnnual: 44.4, isNYC: false },
  "DAL":   { headcount: 16, terminated: 4,  involuntary: 1,  voluntary: 3,  rate6m: 25.0, rateAnnual: 50.0, isNYC: false },
};


// Labor costs from Rippling clock-in hours — each store uses its own clock-in data
// NYC_CLUSTER retained only for turnover display (shared headcount metric)
const NYC_CLUSTER = ["BLK", "MOT", "WBG"];

// Period lengths — YTD Jan 1–May 14 except Philadelphia (QTD Apr 1–May 11, new store)
const STORE_DAYS = {
  BLK:134, MOT:134, WBG:134, ATL:134, BOS:134,
  UNION:134, GEO:134, MIA:134, DAL:134, PHL:41
};
const ANNUALIZATION = 365 / 134; // default YTD; per-store: 365/STORE_DAYS[code]

// AUTO:STORES
const stores = [
  { name: "Bleecker Street",      code: "BLK",   city: "New York, NY",       gross_sales: 1062009,   net_sales: 898217.12 +  84734.03, discounts: -160963.7, returns: -2828.18, labor_cost: 194192.47, hours: 9252.73, headcount: 48, event_rev:  84734.03 },
  { name: "Atlanta Ponce Market", code: "ATL",   city: "Atlanta, GA",        gross_sales: 643843,    net_sales: 583683.09 +   8861.48, discounts: -58131.75, returns: -2028.16, labor_cost: 123930.04, hours: 6285.96, headcount: 21, event_rev:   8861.48 },
  { name: "281 Mott Street",      code: "MOT",   city: "New York, NY",       gross_sales: 579648,    net_sales: 510544.89 +       0.00, discounts: -67555.0,  returns: -1548.11, labor_cost: 86774.11,  hours: 4520.64, headcount: 36, event_rev:      0.00 },
  { name: "Union Market",         code: "UNION", city: "Washington, DC",     gross_sales: 549483,    net_sales: 483368.30 +  37495.05, discounts: -64137.6,  returns: -1977.10, labor_cost: 102458.05, hours: 4800.16, headcount: 20, event_rev:  37495.05 },
  { name: "Boston Newbury",       code: "BOS",   city: "Boston, MA",         gross_sales: 500828,    net_sales: 436253.76 +  24360.28, discounts: -61558.75, returns: -3015.49, labor_cost: 91417.94,  hours: 4286.01, headcount: 13, event_rev:  24360.28 },
  { name: "Georgetown",           code: "GEO",   city: "Washington, DC",     gross_sales: 471770,    net_sales: 430274.95 +   4404.38, discounts: -40873.25, returns: -621.80,  labor_cost: 103894.90, hours: 4530.47, headcount: 13, event_rev:   4404.38 },
  { name: "Williamsburg",         code: "WBG",   city: "Brooklyn, NY",       gross_sales: 429264,    net_sales: 392099.23 +       0.00, discounts: -35576.5,  returns: -1588.27, labor_cost: 86854.99,  hours: 4250.29, headcount: 28, event_rev:      0.00 },
  { name: "Philadelphia",         code: "PHL",   city: "Philadelphia, PA",   gross_sales: 214063,    net_sales: 192153.29 +  11752.56, discounts: -20475.2,  returns: -1434.51, labor_cost: 38286.91,  hours: 1957.10, headcount: 15, event_rev:  11752.56 },
  { name: "Dallas",               code: "DAL",   city: "Dallas, TX",         gross_sales: 343849,    net_sales: 310988.96 +   8644.64, discounts: -31318.75, returns: -1541.29, labor_cost: 80365.19,  hours: 3903.92, headcount: 14, event_rev:   8644.64 },
  { name: "Wynwood",              code: "MIA",   city: "Miami, FL",          gross_sales: 323431,    net_sales: 287032.35 +  10957.71, discounts: -34706.65, returns: -1692.00, labor_cost: 64707.32,  hours: 3168.51, headcount: 11, event_rev:  10957.71 },
];
// END:STORES

// All stores now use individual labor figures
// Step 1: compute raw metrics for every store
const _raw = stores.map(s => {
  const isNYC  = NYC_CLUSTER.includes(s.code);
  const lcp    = (s.labor_cost / s.net_sales) * 100;
  const rplc   = s.net_sales / s.labor_cost;
  const splh   = s.net_sales / s.hours;
  const disc_pct = Math.abs(s.discounts / s.gross_sales) * 100;
  const anc    = ANCILLARY[s.code]?.anc_pct ?? 0;
  const google = RATINGS[s.code]?.google ?? 0;
  const turn   = TURNOVER[s.code]?.rateAnnual ?? 999;
  const l      = LEASE[s.code];
  const annSales = s.net_sales * (365 / (STORE_DAYS[s.code] || 134));
  const splr    = l ? annSales / l.rent  : 0;
  const splseat = SEATS[s.code] ? annSales / SEATS[s.code] : 0;
  return { ...s, isNYC, lcp: +lcp.toFixed(1), rplc: +rplc.toFixed(2), splh: +splh.toFixed(2), disc_pct: +disc_pct.toFixed(1), anc, google, turn, splr: +splr.toFixed(2), splseat: +splseat.toFixed(0) };
});

// Step 2: rank each store per metric (1 = best)
function rankMetric(arr, key, higherIsBetter) {
  const sorted = [...arr].sort((a, b) => higherIsBetter ? b[key] - a[key] : a[key] - b[key]);
  const rankMap = {};
  sorted.forEach((s, i) => { rankMap[s.code] = i + 1; });
  return rankMap;
}
const ranks = {
  rplc:    rankMetric(_raw, "rplc",    true),
  turn:    rankMetric(_raw, "turn",    false),
  google:  rankMetric(_raw, "google",  true),
  anc:     rankMetric(_raw, "anc",     true),
  splr:    rankMetric(_raw, "splr",    true),
  splseat: rankMetric(_raw, "splseat", true),
};

// Step 3: weighted rank score — weights in priority order
const WEIGHTS = { rplc: 30, turn: 25, google: 15, anc: 15, splr: 10, splseat: 5 };
const N = stores.length;
const enriched = _raw.map(s => {
  const score = Math.round(
    Object.entries(WEIGHTS).reduce((sum, [k, w]) => {
      return sum + w * (N + 1 - ranks[k][s.code]) / N;
    }, 0)
  );
  return { ...s, score, ranks: { rplc: ranks.rplc[s.code], turn: ranks.turn[s.code], google: ranks.google[s.code], anc: ranks.anc[s.code], splr: ranks.splr[s.code], splseat: ranks.splseat[s.code] } };
});
enriched.sort((a, b) => b.score - a.score);

const fmt$ = v => "$" + Math.round(v).toLocaleString();
const fmtK = v => "$" + (v / 1000).toFixed(1) + "K";
const fmtPct = v => v.toFixed(1) + "%";

function scoreStyle(s) {
  if (s >= 70) return { bg: "#DCFCE7", text: "#166534", border: "#86EFAC" };
  if (s >= 45) return { bg: "#FEF9C3", text: "#854D0E", border: "#FDE047" };
  return { bg: "#FEE2E2", text: "#991B1B", border: "#FCA5A5" };
}

function lcpStyle(v) {
  if (v <= 21) return "#166534";
  if (v <= 24) return "#854D0E";
  return "#991B1B";
}

function RankBadge({ rank, total = 10 }) {
  const bg   = rank <= 3 ? "#DCFCE7" : rank <= 6 ? "#FEF9C3" : "#FEE2E2";
  const text = rank <= 3 ? "#166534" : rank <= 6 ? "#854D0E" : "#991B1B";
  return (
    <div title={`Ranked #${rank} of ${total}`} style={{ width: 22, height: 22, borderRadius: "50%", background: bg, color: text, fontSize: 11, fontWeight: 700, display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0, border: `1.5px solid ${text}`, lineHeight: 1 }}>
      {rank}
    </div>
  );
}

function KpiCard({ label, value, sub, highlight, rank }) {
  return (
    <div style={{ background: "#F8FAFC", borderRadius: 10, padding: "14px 16px", border: "1px solid #E2E8F0" }}>
      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 4 }}>
        <div style={{ fontSize: 11, color: "#64748B", fontWeight: 500, textTransform: "uppercase", letterSpacing: "0.06em" }}>{label}</div>
        {rank != null && <RankBadge rank={rank} />}
      </div>
      <div style={{ fontSize: 20, fontWeight: 600, color: highlight || "#0F172A" }}>{value}</div>
      {sub && <div style={{ fontSize: 12, color: "#94A3B8", marginTop: 2 }}>{sub}</div>}
    </div>
  );
}

function MiniBar({ pct, color }) {
  return (
    <div style={{ flex: 1, height: 6, background: "#E2E8F0", borderRadius: 3, overflow: "hidden" }}>
      <div style={{ width: `${pct}%`, height: "100%", background: color || "#6366F1", borderRadius: 3, transition: "width 0.5s ease" }} />
    </div>
  );
}

function App() {
  const [selected, setSelected] = useState(enriched[0].code);
  const [view, setView] = useState("detail"); // "detail" | "table"
  const store = enriched.find(s => s.code === selected);
  const ss = scoreStyle(store.score);
  const allNetMax = Math.max(...enriched.map(s => s.net_sales));

  return (
    <div style={{ fontFamily: "'Inter', system-ui, sans-serif", background: "#F1F5F9", minHeight: "100vh", padding: "24px 20px" }}>
      {/* Header */}
      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 20 }}>
        <div>
          <h1 style={{ margin: 0, fontSize: 20, fontWeight: 600, color: "#0F172A" }}>Store Scorecards</h1>
          <p style={{ margin: "3px 0 0", fontSize: 13, color: "#64748B" }}>// AUTO:PERIOD_LABEL
Jan 1 – May 14, 2026 YTD · Shopify POS + Rippling <span style={{color:"#94A3B8"}}>(Philadelphia QTD from Apr 1)</span>
// END:PERIOD_LABEL</p>
        </div>
        <div style={{ display: "flex", gap: 8 }}>
          {["detail", "table"].map(v => (
            <button key={v} onClick={() => setView(v)}
              style={{ padding: "6px 14px", borderRadius: 8, border: "1px solid #CBD5E1", background: view === v ? "#0F172A" : "#fff", color: view === v ? "#fff" : "#475569", fontSize: 13, cursor: "pointer", fontWeight: 500 }}>
              {v === "detail" ? "Store view" : "Leaderboard"}
            </button>
          ))}
        </div>
      </div>

      {view === "table" ? (
        // Rank Matrix Leaderboard
        <div style={{ background: "#fff", borderRadius: 14, border: "1px solid #E2E8F0", overflow: "auto" }}>
          <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 13 }}>
            <thead>
              <tr style={{ background: "#F8FAFC", borderBottom: "2px solid #E2E8F0" }}>
                <th style={{ padding: "14px 16px", textAlign: "left", fontWeight: 600, color: "#0F172A", fontSize: 12, whiteSpace: "nowrap", position: "sticky", left: 0, background: "#F8FAFC", zIndex: 1 }}>Store</th>
                {[
                  { key: "rplc",   label: "Rev / Labor $",    sub: "higher = better" },
                  { key: "turn",   label: "Turnover",          sub: "lower = better"  },
                  { key: "google", label: "Google Rating",     sub: "higher = better" },
                  { key: "anc",    label: "Ancillary %",       sub: "higher = better" },
                  { key: "splr",   label: "Sales / Rent $",    sub: "higher = better" },
                  { key: "splseat", label: "Sales / Seat",     sub: "higher = better" },
                ].map(col => (
                  <th key={col.key} style={{ padding: "14px 20px", textAlign: "center", fontWeight: 500, color: "#64748B", fontSize: 11, textTransform: "uppercase", letterSpacing: "0.05em", whiteSpace: "nowrap" }}>
                    <div>{col.label}</div>
                    <div style={{ fontSize: 10, color: "#94A3B8", fontWeight: 400, textTransform: "none", letterSpacing: 0, marginTop: 2 }}>{col.sub}</div>
                  </th>
                ))}
                <th style={{ padding: "14px 20px", textAlign: "center", fontWeight: 500, color: "#64748B", fontSize: 11, textTransform: "uppercase", letterSpacing: "0.05em" }}>
                  <div>Overall</div>
                  <div style={{ fontSize: 10, color: "#94A3B8", fontWeight: 400, textTransform: "none", letterSpacing: 0, marginTop: 2 }}>score</div>
                </th>
              </tr>
            </thead>
            <tbody>
              {enriched.map((s, i) => {
                const ss2 = scoreStyle(s.score);
                const RANK_KEYS = ["rplc", "turn", "google", "anc", "splr", "splseat"];
                return (
                  <tr key={s.code}
                    onClick={() => { setSelected(s.code); setView("detail"); }}
                    style={{ borderBottom: "1px solid #F1F5F9", cursor: "pointer" }}
                    onMouseEnter={e => e.currentTarget.style.background = "#F8FAFC"}
                    onMouseLeave={e => e.currentTarget.style.background = "#fff"}>
                    {/* Store name cell */}
                    <td style={{ padding: "14px 16px", position: "sticky", left: 0, background: "#fff", zIndex: 1, borderRight: "1px solid #F1F5F9" }}>
                      <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                        <div style={{ width: 24, height: 24, borderRadius: "50%", background: "#F1F5F9", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 11, fontWeight: 700, color: "#64748B", flexShrink: 0 }}>
                          {i + 1}
                        </div>
                        <div>
                          <div style={{ fontWeight: 500, color: "#0F172A", fontSize: 13 }}>{s.name}</div>
                          <div style={{ fontSize: 11, color: "#94A3B8" }}>{s.city}</div>
                        </div>
                      </div>
                    </td>
                    {/* Rank badge cells */}
                    {RANK_KEYS.map(key => {
                      const rank = s.ranks[key];
                      const bg   = rank <= 3 ? "#DCFCE7" : rank <= 6 ? "#FEF9C3" : "#FEE2E2";
                      const text = rank <= 3 ? "#166534" : rank <= 6 ? "#854D0E" : "#991B1B";
                      const border = rank <= 3 ? "#86EFAC" : rank <= 6 ? "#FDE047" : "#FCA5A5";
                      return (
                        <td key={key} style={{ padding: "14px 20px", textAlign: "center" }}>
                          <div style={{ display: "inline-flex", alignItems: "center", justifyContent: "center", width: 34, height: 34, borderRadius: "50%", background: bg, border: `2px solid ${border}`, color: text, fontSize: 15, fontWeight: 700 }}>
                            {rank}
                          </div>
                        </td>
                      );
                    })}
                    {/* Overall score */}
                    <td style={{ padding: "14px 20px", textAlign: "center" }}>
                      <span style={{ background: ss2.bg, color: ss2.text, border: `1.5px solid ${ss2.border}`, borderRadius: 8, padding: "4px 12px", fontWeight: 700, fontSize: 14, display: "inline-block" }}>
                        {s.score}
                      </span>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
          {/* Legend */}
          <div style={{ display: "flex", gap: 16, padding: "12px 16px", borderTop: "1px solid #F1F5F9", background: "#FAFAFA" }}>
            <span style={{ fontSize: 11, color: "#64748B", fontWeight: 500 }}>Rank key:</span>
            {[["#DCFCE7","#86EFAC","#166534","#1 – 3 Top"],["#FEF9C3","#FDE047","#854D0E","#4 – 6 Mid"],["#FEE2E2","#FCA5A5","#991B1B","#7 – 10 Bottom"]].map(([bg,bd,tx,label]) => (
              <div key={label} style={{ display: "flex", alignItems: "center", gap: 5 }}>
                <div style={{ width: 18, height: 18, borderRadius: "50%", background: bg, border: `2px solid ${bd}`, display: "flex", alignItems: "center", justifyContent: "center" }}>
                  <span style={{ fontSize: 8, fontWeight: 700, color: tx }}>1</span>
                </div>
                <span style={{ fontSize: 11, color: "#64748B" }}>{label}</span>
              </div>
            ))}
            <span style={{ fontSize: 11, color: "#94A3B8", marginLeft: "auto" }}>Click any row to see full store detail →</span>
          </div>
        </div>
      ) : (
        <div style={{ display: "grid", gridTemplateColumns: "220px 1fr", gap: 16 }}>
          {/* Store List */}
          <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
            {enriched.map((s, i) => {
              const ss2 = scoreStyle(s.score);
              const active = s.code === selected;
              return (
                <button key={s.code} onClick={() => setSelected(s.code)}
                  style={{ textAlign: "left", padding: "11px 13px", borderRadius: 10, border: active ? "1.5px solid #6366F1" : "1px solid #E2E8F0", background: active ? "#EEF2FF" : "#fff", cursor: "pointer", transition: "all 0.15s" }}>
                  <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 4 }}>
                    <span style={{ fontSize: 12, color: "#94A3B8" }}>#{i + 1}</span>
                    <span style={{ background: ss2.bg, color: ss2.text, borderRadius: 5, padding: "1px 7px", fontSize: 11, fontWeight: 600 }}>{s.score}</span>
                  </div>
                  <div style={{ fontSize: 13, fontWeight: 500, color: active ? "#4338CA" : "#0F172A", lineHeight: 1.3 }}>{s.name}</div>
                  <div style={{ fontSize: 11, color: "#94A3B8", marginTop: 2 }}>{fmtK(s.net_sales)} net sales</div>
                </button>
              );
            })}
          </div>

          {/* Detail Panel */}
          <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
            {/* Store Header */}
            <div style={{ background: "#fff", borderRadius: 14, border: "1px solid #E2E8F0", padding: "20px 22px", display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
              <div>
                <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 2 }}>
                  <h2 style={{ margin: 0, fontSize: 18, fontWeight: 600, color: "#0F172A" }}>{store.name}</h2>
                  {store.isNYC && <span style={{ fontSize: 11, fontWeight: 600, background: "#EEF2FF", color: "#4338CA", border: "1px solid #C7D2FE", borderRadius: 5, padding: "2px 7px" }}>NYC Cluster</span>}
                </div>
                <p style={{ margin: 0, fontSize: 13, color: "#64748B" }}>📍 {store.city}</p>
                {store.isNYC && <p style={{ margin: "3px 0 0", fontSize: 12, color: "#94A3B8" }}>Workforce shared across Bleecker · Mott · Williamsburg (49 total)</p>}
              </div>
              <div style={{ textAlign: "center", background: ss.bg, border: `2px solid ${ss.border}`, borderRadius: "50%", width: 64, height: 64, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", flexShrink: 0 }}>
                <span style={{ fontSize: 22, fontWeight: 700, color: ss.text, lineHeight: 1 }}>{store.score}</span>
                <span style={{ fontSize: 10, color: ss.text, fontWeight: 500 }}>score</span>
              </div>
            </div>

            {/* Sales KPIs */}
            <div>
              <div style={{ fontSize: 11, fontWeight: 600, color: "#94A3B8", textTransform: "uppercase", letterSpacing: "0.07em", marginBottom: 8 }}>Sales Performance</div>
              <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 10 }}>
                <KpiCard label="Gross Sales" value={fmt$(store.gross_sales)} />
                <KpiCard label="Net Sales (Shopify)" value={fmt$(store.net_sales - store.event_rev)} highlight="#4338CA" />
                <KpiCard label="Event Revenue" value={store.event_rev > 0 ? fmt$(store.event_rev) : "—"} sub={store.event_rev > 0 ? `${((store.event_rev/store.net_sales)*100).toFixed(1)}% of total` : "no events"} highlight={store.event_rev > 0 ? "#166534" : "#94A3B8"} />
                <KpiCard label="Combined Net Sales" value={fmt$(store.net_sales)} highlight="#0F172A" />
              </div>
              <div style={{ display: "grid", gridTemplateColumns: "repeat(2, 1fr)", gap: 10, marginTop: 10 }}>
                <KpiCard label="Discounts" value={fmtPct(store.disc_pct)} sub={fmt$(Math.abs(store.discounts))} highlight={store.disc_pct > 18 ? "#991B1B" : "#166534"} />
                <KpiCard label="Returns" value={fmt$(Math.abs(store.returns))} />
              </div>
            </div>

            {/* Space & Rent */}
            {(() => {
              const l = LEASE[store.code];
              if (!l) return null;
              const storeAnn  = 365 / (STORE_DAYS[store.code] || 134);
              const annSales  = store.net_sales * storeAnn;
              const splseat   = SEATS[store.code] ? annSales / SEATS[store.code] : null;
              const splr      = annSales / l.rent;
              const maxSplseat = Math.max(...Object.keys(SEATS).map(c => {
                const s2 = enriched.find(x => x.code === c);
                return s2 ? s2.net_sales * (365 / (STORE_DAYS[c] || 134)) / SEATS[c] : 0;
              }));
              const maxSplr = Math.max(...Object.entries(LEASE).map(([c, d]) => {
                const s2 = enriched.find(x => x.code === c);
                return s2 ? s2.net_sales * (365 / (STORE_DAYS[c] || 134)) / d.rent : 0;
              }));
              const seatColor = splseat >= 90000 ? "#166534" : splseat >= 60000 ? "#854D0E" : "#991B1B";
              const rentColor = splr >= 10 ? "#166534" : splr >= 7 ? "#854D0E" : "#991B1B";
              return (
                <div>
                  <div style={{ fontSize: 11, fontWeight: 600, color: "#94A3B8", textTransform: "uppercase", letterSpacing: "0.07em", marginBottom: 8 }}>Space &amp; Rent <span style={{ fontWeight: 400, fontSize: 10, textTransform: "none" }}>(annualized — YTD 134 days, PHL QTD 41 days)</span></div>
                  <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 10, marginBottom: 12 }}>
                    <KpiCard label="Seats" value={SEATS[store.code] || "—"} sub="customer seating" />
                    <KpiCard label="Total Annual Rent" value={fmt$(l.rent)} sub="base + additional" />
                    <KpiCard label="Sales / Seat" value={splseat ? fmt$(splseat) : "—"} sub="annualized" highlight={seatColor} rank={store.ranks.splseat} />
                    <KpiCard label="Sales / Rent $" value={`$${splr.toFixed(2)}`} sub="per $1 of rent" highlight={rentColor} rank={store.ranks.splr} />
                  </div>
                  {/* Comparison bars */}
                  <div style={{ background: "#fff", borderRadius: 12, border: "1px solid #E2E8F0", padding: "14px 18px" }}>
                    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 20 }}>
                      <div>
                        <div style={{ fontSize: 11, fontWeight: 600, color: "#94A3B8", textTransform: "uppercase", letterSpacing: "0.07em", marginBottom: 10 }}>Sales / Seat</div>
                        {Object.keys(SEATS).sort((a, b) => {
                          const sa = enriched.find(x => x.code === a);
                          const sb = enriched.find(x => x.code === b);
                          return (sb ? sb.net_sales * (365/(STORE_DAYS[b]||134)) / SEATS[b] : 0) - (sa ? sa.net_sales * (365/(STORE_DAYS[a]||134)) / SEATS[a] : 0);
                        }).map(code => {
                          const s2 = enriched.find(x => x.code === code);
                          if (!s2) return null;
                          const val = s2.net_sales * (365/(STORE_DAYS[code]||134)) / SEATS[code];
                          const isActive = code === store.code;
                          return (
                            <div key={code} style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 7 }}>
                              <div style={{ width: 90, fontSize: 11, color: isActive ? "#4338CA" : "#475569", fontWeight: isActive ? 600 : 400, flexShrink: 0, textAlign: "right", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>{s2.name}</div>
                              <MiniBar pct={(val / maxSplseat) * 100} color={isActive ? "#6366F1" : "#CBD5E1"} />
                              <div style={{ width: 52, fontSize: 11, color: isActive ? "#4338CA" : "#64748B", fontWeight: isActive ? 600 : 400, flexShrink: 0 }}>{fmt$(val)}</div>
                            </div>
                          );
                        })}
                      </div>
                      <div>
                        <div style={{ fontSize: 11, fontWeight: 600, color: "#94A3B8", textTransform: "uppercase", letterSpacing: "0.07em", marginBottom: 10 }}>Sales / Rent $</div>
                        {Object.entries(LEASE).sort((a, b) => {
                          const sa = enriched.find(x => x.code === a[0]);
                          const sb = enriched.find(x => x.code === b[0]);
                          return (sb ? sb.net_sales * (365/(STORE_DAYS[b[0]]||134)) / b[1].rent : 0) - (sa ? sa.net_sales * (365/(STORE_DAYS[a[0]]||134)) / a[1].rent : 0);
                        }).map(([code, d]) => {
                          const s2 = enriched.find(x => x.code === code);
                          if (!s2) return null;
                          const val = s2.net_sales * (365/(STORE_DAYS[code]||134)) / d.rent;
                          const isActive = code === store.code;
                          return (
                            <div key={code} style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 7 }}>
                              <div style={{ width: 90, fontSize: 11, color: isActive ? "#4338CA" : "#475569", fontWeight: isActive ? 600 : 400, flexShrink: 0, textAlign: "right", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>{s2.name}</div>
                              <MiniBar pct={(val / maxSplr) * 100} color={isActive ? "#6366F1" : "#CBD5E1"} />
                              <div style={{ width: 40, fontSize: 11, color: isActive ? "#4338CA" : "#64748B", fontWeight: isActive ? 600 : 400, flexShrink: 0 }}>${val.toFixed(2)}</div>
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  </div>
                </div>
              );
            })()}

            {/* Workforce KPIs */}
            <div>
              <div style={{ fontSize: 11, fontWeight: 600, color: "#94A3B8", textTransform: "uppercase", letterSpacing: "0.07em", marginBottom: 8 }}>Workforce</div>
              <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 10 }}>
                <KpiCard label="Hours Worked" value={store.hours.toLocaleString()} sub="this period" />
                <KpiCard label="Labor Cost" value={fmt$(store.labor_cost)} />
                <KpiCard label="Labor Cost %" value={fmtPct(store.lcp)} highlight={lcpStyle(store.lcp)} />
                <KpiCard label="Rev / Labor $" value={`$${store.rplc.toFixed(2)}`} sub="per $1 of labor cost" highlight={store.rplc >= 4.5 ? "#166534" : store.rplc >= 3.5 ? "#854D0E" : "#991B1B"} rank={store.ranks.rplc} />
              </div>
              <div style={{ display: "grid", gridTemplateColumns: "repeat(2, 1fr)", gap: 10, marginTop: 10 }}>
                <KpiCard label="Sales / Labor Hour" value={`$${store.splh.toFixed(2)}`} sub="net sales per hour worked" highlight={store.splh >= 100 ? "#166534" : store.splh >= 85 ? "#854D0E" : "#991B1B"} />
                <KpiCard label="Headcount" value={store.headcount} sub="active employees" />
              </div>
            </div>

            {/* Ancillary Sales */}
            {(() => {
              const anc = ANCILLARY[store.code];
              if (!anc) return null;
              const ancColor = anc.anc_pct >= 9 ? "#166534" : anc.anc_pct >= 7.5 ? "#854D0E" : "#991B1B";
              const maxAncPct = Math.max(...Object.values(ANCILLARY).map(a => a.anc_pct));
              return (
                <div>
                  <div style={{ fontSize: 11, fontWeight: 600, color: "#94A3B8", textTransform: "uppercase", letterSpacing: "0.07em", marginBottom: 8 }}>Ancillary Sales (Upsell)</div>
                  <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 10, marginBottom: 12 }}>
                    <KpiCard label="Anc. % of Sales" value={fmtPct(anc.anc_pct)} sub="key upsell metric" highlight={ancColor} rank={store.ranks.anc} />
                    <KpiCard label="vs Prior Year" value={anc.pct_chg != null ? `${anc.pct_chg > 0 ? "+" : ""}${anc.pct_chg.toFixed(0)}%` : "N/A"} sub={anc.py_net ? `was $${Math.round(anc.py_net).toLocaleString()}` : "new location"} highlight={anc.pct_chg > 0 ? "#166534" : anc.pct_chg < 0 ? "#991B1B" : undefined} />
                    <KpiCard label="Anc. Net Sales" value={fmt$(anc.anc_net)} />
                    <KpiCard label="Anc. Orders" value={anc.anc_orders.toLocaleString()} />
                  </div>
                  {/* Ancillary % bar chart across all stores */}
                  <div style={{ background: "#fff", borderRadius: 12, border: "1px solid #E2E8F0", padding: "14px 18px" }}>
                    <div style={{ fontSize: 11, fontWeight: 600, color: "#94A3B8", textTransform: "uppercase", letterSpacing: "0.07em", marginBottom: 12 }}>Ancillary % of Sales — All Stores</div>
                    {Object.entries(ANCILLARY)
                      .sort((a, b) => b[1].anc_pct - a[1].anc_pct)
                      .map(([code, a]) => {
                        const s2 = enriched.find(x => x.code === code);
                        const isActive = code === store.code;
                        return (
                          <div key={code} style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 8 }}>
                            <div style={{ width: 120, fontSize: 12, color: isActive ? "#4338CA" : "#475569", fontWeight: isActive ? 600 : 400, flexShrink: 0, textAlign: "right", whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis" }}>{s2?.name || code}</div>
                            <MiniBar pct={(a.anc_pct / maxAncPct) * 100} color={isActive ? "#6366F1" : "#CBD5E1"} />
                            <div style={{ width: 44, fontSize: 12, color: isActive ? "#4338CA" : "#64748B", fontWeight: isActive ? 600 : 400, flexShrink: 0 }}>{fmtPct(a.anc_pct)}</div>
                            <div style={{ width: 50, fontSize: 11, color: a.pct_chg > 0 ? "#166534" : "#991B1B", flexShrink: 0 }}>{a.pct_chg != null ? (a.pct_chg > 0 ? "▲" : "▼") + Math.abs(a.pct_chg).toFixed(0) + "%" : "—"}</div>
                          </div>
                        );
                    })}
                  </div>
                </div>
              );
            })()}

            {/* Revenue Comparison */}
            <div style={{ background: "#fff", borderRadius: 14, border: "1px solid #E2E8F0", padding: "18px 20px" }}>
              <div style={{ fontSize: 11, fontWeight: 600, color: "#94A3B8", textTransform: "uppercase", letterSpacing: "0.07em", marginBottom: 14 }}>Net Sales by Store</div>
              {enriched.map(s => (
                <div key={s.code} style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 9 }}>
                  <div style={{ width: 120, fontSize: 12, color: s.code === selected ? "#4338CA" : "#475569", fontWeight: s.code === selected ? 600 : 400, flexShrink: 0, textAlign: "right", whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis" }} title={s.name}>{s.name}</div>
                  <MiniBar pct={(s.net_sales / allNetMax) * 100} color={s.code === selected ? "#6366F1" : "#CBD5E1"} />
                  <div style={{ width: 64, fontSize: 12, color: "#64748B", flexShrink: 0 }}>{fmtK(s.net_sales)}</div>
                </div>
              ))}
            </div>

            {/* Ratings */}
            {(() => {
              const r = RATINGS[store.code];
              if (!r) return null;
              const starColor = r.google >= 4.5 ? "#166534" : r.google >= 4.0 ? "#854D0E" : r.google ? "#991B1B" : "#94A3B8";
              const stars = r.google ? "★".repeat(Math.round(r.google)) + "☆".repeat(5 - Math.round(r.google)) : null;
              const maxRating = 5;
              return (
                <div>
                  <div style={{ fontSize: 11, fontWeight: 600, color: "#94A3B8", textTransform: "uppercase", letterSpacing: "0.07em", marginBottom: 8 }}>Customer Ratings</div>
                  <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: 10, marginBottom: 12 }}>
                    <KpiCard
                      label="Google Rating"
                      value={r.google ? `${r.google.toFixed(1)} ★` : "—"}
                      sub={r.google ? `${r.google_count} reviews` : r.note}
                      highlight={starColor}
                      rank={store.ranks.google}
                    />
                    <KpiCard label="Yelp Rating" value="—" sub="Not connected" />
                    <KpiCard label="Review Count" value={r.google_count || "—"} sub={r.note || "Google Maps"} />
                  </div>
                  {r.note && (
                    <div style={{ fontSize: 12, color: "#854D0E", background: "#FFFBEB", border: "1px solid #FDE68A", borderRadius: 8, padding: "8px 12px", marginBottom: 8 }}>
                      ⚠ {r.note} — confirm this matches your store location
                    </div>
                  )}
                  {/* Rating comparison bar chart */}
                  <div style={{ background: "#fff", borderRadius: 12, border: "1px solid #E2E8F0", padding: "14px 18px" }}>
                    <div style={{ fontSize: 11, fontWeight: 600, color: "#94A3B8", textTransform: "uppercase", letterSpacing: "0.07em", marginBottom: 12 }}>Google Rating — All Stores</div>
                    {Object.entries(RATINGS)
                      .filter(([, v]) => v.google !== null)
                      .sort((a, b) => b[1].google - a[1].google)
                      .map(([code, rat]) => {
                        const s2 = enriched.find(x => x.code === code);
                        const isActive = code === store.code;
                        const barClr = rat.google >= 4.5 ? "#86EFAC" : rat.google >= 4.0 ? "#FDE68A" : "#FCA5A5";
                        const activeClr = rat.google >= 4.5 ? "#16A34A" : rat.google >= 4.0 ? "#D97706" : "#DC2626";
                        return (
                          <div key={code} style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 8 }}>
                            <div style={{ width: 120, fontSize: 12, color: isActive ? "#4338CA" : "#475569", fontWeight: isActive ? 600 : 400, flexShrink: 0, textAlign: "right", whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis" }}>{s2?.name || code}</div>
                            <MiniBar pct={(rat.google / maxRating) * 100} color={isActive ? activeClr : barClr} />
                            <div style={{ width: 32, fontSize: 12, color: isActive ? "#4338CA" : "#64748B", fontWeight: isActive ? 600 : 400, flexShrink: 0 }}>{rat.google.toFixed(1)}</div>
                            <div style={{ width: 55, fontSize: 11, color: "#94A3B8", flexShrink: 0 }}>({rat.google_count})</div>
                            {rat.note && <span style={{ fontSize: 10, color: "#D97706" }}>⚠</span>}
                          </div>
                        );
                    })}
                    <div style={{ fontSize: 11, color: "#94A3B8", marginTop: 8, borderTop: "1px solid #F1F5F9", paddingTop: 8 }}>
                      Yelp ratings not yet connected
                    </div>
                  </div>
                </div>
              );
            })()}

            {/* Turnover */}
            {(() => {
              const tv = TURNOVER[store.code];
              if (!tv) return null;
              const turnColor = tv.rateAnnual >= 40 ? "#991B1B" : tv.rateAnnual >= 25 ? "#854D0E" : "#166534";
              const maxRate = Math.max(...Object.values(TURNOVER).filter((v,i,a) => a.indexOf(v)===i).map(v => v.rateAnnual));
              // deduplicated store entries for bar chart
              const tvEntries = Object.entries(TURNOVER).filter(([code]) => !["MOT","WBG"].includes(code));
              return (
                <div>
                  <div style={{ fontSize: 11, fontWeight: 600, color: "#94A3B8", textTransform: "uppercase", letterSpacing: "0.07em", marginBottom: 8 }}>Turnover (Last 6 Months)</div>
                  <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 10, marginBottom: 12 }}>
                    <KpiCard label="Annualized Rate" value={fmtPct(tv.rateAnnual)} sub="×2 of 6-month rate" highlight={turnColor} rank={store.ranks.turn} />
                    <KpiCard label="6-Month Rate" value={fmtPct(tv.rate6m)} sub={`${tv.terminated} terminated`} />
                    <KpiCard label="Voluntary" value={tv.voluntary} sub={`${tv.terminated > 0 ? Math.round(tv.voluntary/tv.terminated*100) : 0}% of exits`} />
                    <KpiCard label="Involuntary" value={tv.involuntary} sub={`${tv.terminated > 0 ? Math.round(tv.involuntary/tv.terminated*100) : 0}% of exits`} highlight={tv.involuntary > 2 ? "#991B1B" : undefined} />
                  </div>
                  <div style={{ background: "#fff", borderRadius: 12, border: "1px solid #E2E8F0", padding: "14px 18px" }}>
                    <div style={{ fontSize: 11, fontWeight: 600, color: "#94A3B8", textTransform: "uppercase", letterSpacing: "0.07em", marginBottom: 12 }}>Annualized Turnover — All Stores</div>
                    {tvEntries
                      .sort((a, b) => b[1].rateAnnual - a[1].rateAnnual)
                      .map(([code, t]) => {
                        const s2 = enriched.find(x => x.code === code);
                        const label = t.isNYC ? "NYC Cluster" : s2?.name || code;
                        const isActive = code === store.code || (tv.isNYC && t.isNYC);
                        const barColor = t.rateAnnual >= 40 ? "#FCA5A5" : t.rateAnnual >= 25 ? "#FDE68A" : "#86EFAC";
                        const activeBarColor = t.rateAnnual >= 40 ? "#DC2626" : t.rateAnnual >= 25 ? "#D97706" : "#16A34A";
                        return (
                          <div key={code} style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 8 }}>
                            <div style={{ width: 120, fontSize: 12, color: isActive ? "#4338CA" : "#475569", fontWeight: isActive ? 600 : 400, flexShrink: 0, textAlign: "right", whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis" }}>{label}</div>
                            <MiniBar pct={(t.rateAnnual / maxRate) * 100} color={isActive ? activeBarColor : barColor} />
                            <div style={{ width: 44, fontSize: 12, color: isActive ? "#4338CA" : "#64748B", fontWeight: isActive ? 600 : 400, flexShrink: 0 }}>{fmtPct(t.rateAnnual)}</div>
                            <div style={{ width: 60, fontSize: 11, color: "#94A3B8", flexShrink: 0 }}>{t.terminated} left</div>
                          </div>
                        );
                    })}
                  </div>
                </div>
              );
            })()}

            {/* Flags */}
            {(() => {
              const tv = TURNOVER[store.code];
              const flags = [];
              if (store.lcp > 30) flags.push(`Labor cost % of ${fmtPct(store.lcp)} is elevated — review scheduling`);
              if (store.disc_pct > 18) flags.push(`Discount rate of ${fmtPct(store.disc_pct)} is high — review promotional activity`);
              if (tv && tv.rateAnnual >= 40) flags.push(`Annualized turnover of ${fmtPct(tv.rateAnnual)} is critical — urgent retention action needed`);
              else if (tv && tv.rateAnnual >= 25) flags.push(`Annualized turnover of ${fmtPct(tv.rateAnnual)} is above healthy range`);
              if (tv && tv.involuntary >= 2) flags.push(`${tv.involuntary} involuntary terminations in 6 months — review management practices`);
              if (!flags.length) return null;
              return (
                <div style={{ background: "#FFF7ED", border: "1px solid #FED7AA", borderRadius: 12, padding: "14px 18px" }}>
                  <div style={{ fontSize: 12, fontWeight: 600, color: "#9A3412", marginBottom: 8 }}>⚠ Flags</div>
                  {flags.map((f, i) => <div key={i} style={{ fontSize: 13, color: "#9A3412", marginBottom: i < flags.length-1 ? 4 : 0 }}>• {f}</div>)}
                </div>
              );
            })()}
          </div>
        </div>
      )}
    </div>
  );
}

    window.initApp = function() {
      const rootEl = ReactDOM.createRoot(document.getElementById('root'));
      rootEl.render(<App />);
    };
    if (window._appReady) { window.initApp(); }
  </script>
</body>
</html>
