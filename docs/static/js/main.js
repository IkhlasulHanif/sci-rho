// English-only results from Table 1 of the paper: [avg, worst] per subject.
const SUBJECTS = ["Mathematics", "Physics", "Chemistry", "Biology", "Comp. Sci."];
const RESULTS = [
  ["GPT-5.4", true, [[90.3, 72.4], [94.6, 84.6], [94.4, 78.8], [72.2, 47.8], [95.4, 84.6]]],
  ["Gemini-2.5-Pro", true, [[86.2, 66.3], [90.4, 69.2], [91.7, 70.1], [71.7, 43.5], [91.2, 75.0]]],
  ["Gemini-2.5-Flash", true, [[85.2, 61.8], [87.4, 63.1], [92.2, 67.9], [51.7, 30.4], [86.9, 63.5]]],
  ["Qwen3.5-122B-A10B", false, [[82.1, 49.2], [86.7, 49.2], [88.0, 43.1], [67.8, 26.1], [88.5, 57.7]]],
  ["Qwen3.5-27B", false, [[85.1, 60.3], [87.0, 56.4], [90.9, 65.7], [65.7, 39.1], [89.2, 63.5]]],
  ["Llama-4-Scout", false, [[71.4, 33.7], [78.8, 43.1], [84.7, 46.7], [44.3, 8.7], [68.7, 25.0]]],
  ["InternVL3.5-14B", false, [[58.5, 21.1], [69.2, 30.3], [76.8, 35.0], [30.9, 4.3], [64.6, 21.2]]],
  ["InternVL3.5-8B", false, [[64.8, 35.2], [73.8, 45.1], [79.3, 40.9], [36.5, 4.3], [61.0, 25.0]]],
  ["InternVL3.5-4B", false, [[54.0, 21.1], [65.3, 26.7], [72.6, 29.9], [23.9, 0.0], [55.2, 17.3]]],
  ["Qwen3-VL-8B-Instruct", false, [[61.5, 25.6], [70.3, 34.4], [83.6, 47.4], [53.5, 8.7], [67.1, 25.0]]],
  ["Qwen3-VL-4B-Instruct", false, [[31.7, 5.0], [40.4, 6.2], [35.8, 3.6], [17.8, 0.0], [23.8, 3.8]]],
  ["Molmo2-8B", false, [[46.5, 14.6], [61.9, 30.3], [56.6, 24.1], [26.1, 8.7], [40.8, 9.6]]],
  ["Molmo2-4B", false, [[40.9, 15.6], [54.6, 25.6], [49.6, 22.6], [16.5, 0.0], [31.5, 7.7]]],
  ["Gemma-3-12B-IT", false, [[61.7, 29.1], [65.4, 33.3], [60.1, 26.3], [34.3, 8.7], [65.6, 17.3]]],
  ["Gemma-3-4B-IT", false, [[46.2, 14.1], [44.3, 12.8], [43.4, 8.8], [16.1, 0.0], [36.5, 5.8]]],
  ["SEA-LION-v4-8B-VL", false, [[68.2, 32.2], [75.6, 44.6], [83.4, 49.6], [51.7, 4.3], [71.7, 36.5]]],
  ["SEA-LION-v4-4B-VL", false, [[53.0, 12.1], [53.6, 16.9], [63.6, 17.5], [26.5, 0.0], [44.2, 11.5]]],
];

// Step-level results from Table 2: [F1, F1_worst] per subject.
const REASONING_MODELS = ["GPT-5.4", "InternVL3.5-8B", "Qwen3-VL-8B", "Molmo2-8B", "Gemma-3-4B-IT"];
const REASONING = [
  ["Mathematics", [[88.0, 67.8], [66.2, 39.9], [62.7, 30.1], [51.5, 23.6], [51.2, 20.1]]],
  ["Physics", [[92.2, 79.2], [76.6, 53.9], [75.9, 51.7], [70.2, 44.0], [51.4, 21.4]]],
  ["Chemistry", [[93.4, 79.0], [80.7, 52.5], [83.5, 53.4], [71.9, 39.4], [57.6, 20.7]]],
  ["Biology", [[81.1, 60.3], [49.5, 24.0], [57.9, 22.9], [47.0, 20.6], [28.6, 7.7]]],
  ["Comp. Sci.", [[89.4, 75.1], [61.3, 32.4], [63.4, 33.2], [42.6, 15.5], [39.6, 14.1]]],
];

let subject = 0;
let sortKey = "avg";
const narrow = window.matchMedia("(max-width: 760px)");

function renderBars() {
  const el = document.getElementById("bars");
  const rows = RESULTS.map(([name, closed, s]) => {
    const [avg, wst] = s[subject];
    return { name, closed, avg, wst, delta: +(wst - avg).toFixed(1) };
  });
  const by = { avg: (a, b) => b.avg - a.avg, wst: (a, b) => b.wst - a.wst, delta: (a, b) => a.delta - b.delta };
  rows.sort(by[sortKey]);

  // Reuse row nodes keyed by model so widths animate between subjects.
  const existing = new Map([...el.children].map((n) => [n.dataset.name, n]));
  rows.forEach((r) => {
    let row = existing.get(r.name);
    if (!row) {
      row = document.createElement("div");
      row.className = "bar-row";
      row.dataset.name = r.name;
      row.innerHTML =
        `<div class="bar-name" title="${r.name}"><span class="dot${r.closed ? "" : " open"}"></span>${r.name}</div>` +
        `<div class="track"><div class="avg" style="width:0"></div><div class="wst" style="width:0"></div><span class="val"></span></div>` +
        `<div class="bar-delta"></div>`;
    }
    // Bars use part of the track so the value label always fits after them.
    const k = narrow.matches ? 0.58 : 0.8;
    row.querySelector(".avg").style.width = r.avg * k + "%";
    row.querySelector(".wst").style.width = r.wst * k + "%";
    const val = row.querySelector(".val");
    val.style.left = r.avg * k + "%";
    val.textContent = `${r.avg.toFixed(1)} / ${r.wst.toFixed(1)}`;
    row.querySelector(".bar-delta").textContent = r.delta.toFixed(1);
    row.setAttribute("aria-label", `${r.name}: average ${r.avg}, worst-case ${r.wst}, delta ${r.delta}`);
    el.appendChild(row);
  });
}

function setupControls() {
  const seg = document.getElementById("subject-seg");
  SUBJECTS.forEach((s, i) => {
    const b = document.createElement("button");
    b.textContent = s;
    b.setAttribute("role", "tab");
    b.className = i === subject ? "on" : "";
    b.addEventListener("click", () => {
      subject = i;
      [...seg.children].forEach((c, j) => c.classList.toggle("on", j === i));
      renderBars();
    });
    seg.appendChild(b);
  });
  document.querySelectorAll("#sort-seg button").forEach((b) =>
    b.addEventListener("click", () => {
      sortKey = b.dataset.sort;
      document.querySelectorAll("#sort-seg button").forEach((c) => c.classList.toggle("on", c === b));
      renderBars();
    })
  );
}

function heat(v) {
  // Interpolate from pale blue (low) to accent blue (high).
  const t = Math.max(0, Math.min(1, v / 100));
  const from = [234, 241, 251], to = [31, 95, 168];
  const c = from.map((f, i) => Math.round(f + (to[i] - f) * t));
  return { bg: `rgb(${c.join(",")})`, fg: t > 0.55 ? "#fff" : "#0a1a2f" };
}

function renderReasoning() {
  const t = document.getElementById("reasoning-table");
  let html = "<thead><tr><th>Subject</th>" + REASONING_MODELS.map((m) => `<th>${m}</th>`).join("") + "</tr></thead><tbody>";
  REASONING.forEach(([subj, vals]) => {
    html += `<tr><td>${subj}</td>`;
    vals.forEach(([f, w]) => {
      const { bg, fg } = heat(f);
      html += `<td style="background:${bg};color:${fg}">${f.toFixed(1)} <span class="w">/ ${w.toFixed(1)}</span></td>`;
    });
    html += "</tr>";
  });
  t.innerHTML = html + "</tbody>";
}

function setupReveal() {
  const els = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window)) {
    els.forEach((e) => e.classList.add("in"));
    return;
  }
  const io = new IntersectionObserver(
    (entries) => entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add("in");
        io.unobserve(e.target);
      }
    }),
    { rootMargin: "0px 0px -8% 0px" }
  );
  els.forEach((e) => io.observe(e));
}

function setupCopy() {
  const btn = document.getElementById("copy-bib");
  btn.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(document.getElementById("bibtex").textContent);
      btn.textContent = "Copied";
    } catch {
      btn.textContent = "Select and copy";
    }
    setTimeout(() => (btn.textContent = "Copy BibTeX"), 1800);
  });
}

setupControls();
renderBars();
narrow.addEventListener("change", renderBars);
renderReasoning();
setupReveal();
setupCopy();
