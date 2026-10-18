/* Hero figure: an edge-notched card sorter.
 *
 * The mechanism IS the site's mechanism. Each card is a syllabus item. A card
 * you can explain cold has its notch cut open to the top edge, so when the
 * needle lifts, that card stays in the tray. A card you cannot explain cold
 * still has a closed hole, so it rides up on the needle. Lifting the needle
 * therefore shows you exactly what is left — which is literally what the
 * tracker's "show: to-do" filter does.
 *
 * Counts are real: they come from the tracker's own totals, and the landing
 * page refreshes them from /api/pull.
 */
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "./kit/iso-kit.mjs";
import * as G from "./kit/lathe.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const arg = (n, d) => { const h = process.argv.find((a) => a.startsWith("--" + n + "=")); return h ? Number(h.split("=")[1]) : d; };

const TOTAL = arg("total", 360);
const COLD = arg("cold", 0);
const CARDS = 18;

const WIDTH = 760, HEIGHT = 470;
const PLATE = { x: -140, y: -70, w: 288, d: 140, r: 9 };
const PLATE_H = 13, FOOT_H = 6;

const TRAY = { x: -92, y: -32, w: 182, d: 64, r: 4 };
const WALL = 4.5, WALL_H = 19, FLOOR_Z = 1.5;

const CARD_T = 4.6, PITCH = 8.6, CARD_D = 46, CARD_H = 58;
const CARD_X0 = TRAY.x + 13;
const CARD_Y = -CARD_D / 2;
const CARD_TOP = FLOOR_Z + CARD_H;

const NEEDLE_R = 2.0, NEEDLE_Z = CARD_TOP - 11, NEEDLE_Y = 0;
const NEEDLE_X0 = TRAY.x - 16, NEEDLE_X1 = TRAY.x + TRAY.w + 26;
const LIFT = 19;

const POST = [TRAY.x + TRAY.w + 16, TRAY.y + TRAY.d - 9];
const DIAL = [104, -40], DIAL_R = 21, DIAL_Z = 30, DIAL_H = 9;

const P = k.fitProjection(
  [...k.boxCorners(PLATE, -PLATE_H - FOOT_H, 0),
   [NEEDLE_X1 + 16, 0, NEEDLE_Z + LIFT + 14],
   [CARD_X0, CARD_Y, CARD_TOP + LIFT + 10],
   [DIAL[0] + DIAL_R, DIAL[1], DIAL_Z + DIAL_H]],
  WIDTH, HEIGHT, { pad: 26, azimuth: 46 },
);

const at = (p) => k.iso(p, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (pts, style) => k.dotsSvg(pts, style);
const out = [];

/* how many of the drawn cards are mastered — real ratio, rounded */
const coldCards = TOTAL > 0 ? Math.round((COLD / TOTAL) * CARDS) : 0;

/* ---------------------------------------------------------------- base */
out.push(`<path class="iso-halo" d="${k.haloOf(PLATE, -PLATE_H - FOOT_H, PLATE_H, P)}"/>`);
const byDepth = (pts) => [...pts].sort((a, b) => k.depthOf([a[0], a[1], 0], P) - k.depthOf([b[0], b[1], 0], P));
for (const [x, y] of byDepth(k.corners(PLATE, 24))) {
  out.push(S(k.cylinder(x, y, 7.6, -PLATE_H - FOOT_H, 1.8, P, 28), { tone: "lo" }));
  out.push(S(k.cylinder(x, y, 5.8, -PLATE_H - FOOT_H + 1.8, FOOT_H - 1.8, P, 28), { tone: "mid" }));
}
out.push(S(k.slabOf(PLATE, -PLATE_H, PLATE_H, P, 9, 1.7), { tone: "mid" }));
out.push(L(k.planOutline(k.insetPlan(PLATE, 5.5), 0, P), { tone: "faint" }));
const screws = k.corners(PLATE, 11);
out.push(L(screws.map(([x, y]) => k.ring(x, y, 2.4, 0, P, 16)).join(""), { tone: "lo" }));
out.push(D(screws.map(([x, y]) => at([x, y, 0])), { size: 0.52 }));

/* ruler strip along the front edge, ticks hanging from its edge */
const strip = { x: PLATE.x + 14, y: PLATE.y + PLATE.d - 16, w: PLATE.w - 28, d: 7.5, r: 1 };
out.push(S(k.slabOf(strip, 0, 0.7, P, 3), { tone: "lo", crease: "none" }));
const ticks = k.topTicks(strip.x + 4, strip.x + strip.w - 4, 5, 5, strip.y + 0.9, 0.7, [2.2, 4], P);
out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));

/* Specimen card, lying flat in front of the tray.
   It is the legend made physical: one card showing all three notch states, so
   the mechanism stays legible even when nothing has been mastered yet and no
   card in the deck is notched. Left to right: hole closed (not started), hole
   closed with the guide scored (read it), notch cut open to the edge (can
   explain cold — this one slips off the needle). */
const SPEC = { x: -112, y: 33, w: 66, d: 26, r: 1.8 };
const SPEC_Z = 1.3;
out.push(S(k.slabOf(SPEC, 0, SPEC_Z, P, 3, 0.4), { tone: "hi" }));
out.push(L(k.planOutline(k.insetPlan(SPEC, 3), SPEC_Z, P), { tone: "faint" }));
const holeY = SPEC.y + 6.2;
for (let i = 0; i < 3; i++) {
  const hx = SPEC.x + 13 + i * 20;
  out.push(L(k.ring(hx, holeY, 2.6, SPEC_Z, P, 16), { tone: "mid" }));
  if (i === 1) out.push(L(k.pathOf([[hx, holeY - 2.6, SPEC_Z], [hx, SPEC.y + 0.8, SPEC_Z]].map(at)), { tone: "faint" }));
  if (i === 2) {
    /* cut right through to the edge: two walls, so the needle passes out */
    out.push(L(k.pathOf([[hx - 2.6, holeY, SPEC_Z], [hx - 2.6, SPEC.y + 0.8, SPEC_Z]].map(at)), { tone: "lit" }));
    out.push(L(k.pathOf([[hx + 2.6, holeY, SPEC_Z], [hx + 2.6, SPEC.y + 0.8, SPEC_Z]].map(at)), { tone: "lit" }));
  }
  /* a rule line under each, standing for its printed label */
  out.push(L(k.pathOf([[hx - 6, holeY + 8, SPEC_Z], [hx + 6, holeY + 8, SPEC_Z]].map(at)), { tone: "faint", free: true }));
  out.push(L(k.pathOf([[hx - 6, holeY + 11.5, SPEC_Z], [hx + (i === 2 ? 1 : 4), holeY + 11.5, SPEC_Z]].map(at)), { tone: "faint", free: true }));
}
out.push(D(k.corners(SPEC, 4).map(([x, y]) => at([x, y, SPEC_Z])), { size: 0.42 }));

/* ---------------------------------------------------------------- tray */
const trayWall = (plan) => out.push(S(k.slabOf(plan, 0, WALL_H, P, 2, 0.6), { tone: "lo" }));
out.push(S(k.slabOf(TRAY, 0, FLOOR_Z, P, 4, 0.4), { tone: "faint", crease: "none" }));
trayWall({ x: TRAY.x, y: TRAY.y, w: TRAY.w, d: WALL, r: 1.5 });                       /* back */
trayWall({ x: TRAY.x, y: TRAY.y, w: WALL, d: TRAY.d, r: 1.5 });                       /* left */
trayWall({ x: TRAY.x + TRAY.w - WALL, y: TRAY.y, w: WALL, d: TRAY.d, r: 1.5 });       /* right */
/* two guide posts the cards lean against */
for (const gx of [TRAY.x + 7, TRAY.x + TRAY.w - 9]) {
  out.push(S(k.cylinder(gx, TRAY.y + 2.4, 1.5, FLOOR_Z, CARD_H + 5, P, 18), { tone: "mid" }));
  out.push(S(k.cylinder(gx, TRAY.y + 2.4, 2.4, FLOOR_Z + CARD_H + 5, 1.6, P, 18), { tone: "hi" }));
}

/* ---------------------------------------------------------------- cards */
/* Drawn back to front along x so nearer cards cover further ones. Each card is
   one solid; its notch is a real cut at the top edge, open on a mastered card
   and closed on one still to learn. */
/* The needle is built first and painted BEFORE the cards: it runs through the
   deck, so the cards must cover it and only its protruding ends stay visible.
   Painting it last made it look like a rod resting on top of the stack. */
const needleF = G.frameAlong([NEEDLE_X0, NEEDLE_Y, NEEDLE_Z], [1, 0, 0]);
const len = NEEDLE_X1 - NEEDLE_X0;
const rod = S(G.lathe([[0, 1.1], [3, NEEDLE_R], [len - 34, NEEDLE_R], [len - 31, 3.2], [len - 8, 3.2]], needleF, P, { steps: 24 }), { tone: "lit" });
const handleF = G.frameAlong([NEEDLE_X0 + len - 34, NEEDLE_Y, NEEDLE_Z], [1, 0, 0]);
const handle = S(G.lathe([[0, 4.6], [2.4, 6.4], [24, 6.4], [26.4, 4.6]], handleF, P, { steps: 28, bevel: 0.4 }), { tone: "mid" });
const knurl = L(G.ribsOf(handleF, 3.4, 23, 6.45, 13, P, { seams: true }), { tone: "lo" });
const capF = G.frameAlong([NEEDLE_X0 + len - 8, NEEDLE_Y, NEEDLE_Z], [1, 0, 0]);
const cap = S(G.lathe([[0, 4.2], [3.4, 3.0]], capF, P, { steps: 20 }), { tone: "lo" });
out.push(`<g id="needle">${rod}${handle}${knurl}${cap}</g>`);

const cardSvg = [];
for (let i = 0; i < CARDS; i++) {
  const x = CARD_X0 + i * PITCH;
  const plan = { x, y: CARD_Y, w: CARD_T, d: CARD_D, r: 1 };
  const z = FLOOR_Z, cx = x + CARD_T / 2, hole = NEEDLE_Z;
  const body = S(k.slabOf(plan, z, CARD_H, P, 1, 0.45), { tone: "hi" });
  /* The notch is drawn on every card but only shown on a mastered one, so the
     page can reflect real progress without regenerating any geometry. */
  const notch =
    L(k.pathOf([[cx, NEEDLE_Y - 2.2, z + CARD_H], [cx, NEEDLE_Y - 2.2, hole]].map(at)), { tone: "lo" }) +
    L(k.pathOf([[cx, NEEDLE_Y + 2.2, z + CARD_H], [cx, NEEDLE_Y + 2.2, hole]].map(at)), { tone: "lo" }) +
    L(k.pathOf([[cx, NEEDLE_Y - 2.2, hole], [cx, NEEDLE_Y + 2.2, hole]].map(at)), { tone: "mid" });
  /* an index rule near the foot, running edge to edge so it ends on real edges */
  const rule = L(k.pathOf([[cx, CARD_Y + 5, z + 7], [cx, CARD_Y + CARD_D - 5, z + 7]].map(at)), { tone: "faint" });
  cardSvg.push({ x, svg: `${body}${rule}<g class="notch">${notch}</g>` });
}
/* back to front, so a nearer card covers the one behind it and the needle */
cardSvg.sort((a, b) => k.depthOf([a.x, 0, 0], P) - k.depthOf([b.x, 0, 0], P));
out.push(`<g id="deck">${cardSvg
  .map((c, i) => `<g class="cd" data-i="${i}">${c.svg}</g>`)
  .join("")}</g>`);

/* rest bracket the needle sits in when it is down */
out.push(S(k.slabOf({ x: POST[0] - 4, y: POST[1] - 4, w: 8, d: 8, r: 1.4 }, 0, NEEDLE_Z - 7, P, 2, 0.5), { tone: "lo" }));
out.push(S(k.cylinder(POST[0], POST[1], 4.6, NEEDLE_Z - 7, 3.2, P, 20), { tone: "mid" }));

/* ---------------------------------------------------------------- counter dial */
out.push(S(k.cylinder(DIAL[0], DIAL[1], DIAL_R + 2.6, 0, DIAL_Z, P, 40), { tone: "lo" }));
out.push(S(k.cylinder(DIAL[0], DIAL[1], DIAL_R, DIAL_Z, DIAL_H, P, 40), { tone: "mid" }));
const face = DIAL_Z + DIAL_H;
out.push(L(k.ring(DIAL[0], DIAL[1], DIAL_R - 3, face, P, 40), { tone: "lo" }));
const rt = k.radialTicks(DIAL[0], DIAL[1], DIAL_R - 4, 24, 6, face, [3, 5.5], P);
out.push(L(rt.minor, { tone: "lo" }), L(rt.major, { tone: "mid" }));
out.push(D([at([DIAL[0], DIAL[1], face])], { size: 0.7 }));
out.push(`<g id="dialneedle">${L(k.pathOf([[DIAL[0], DIAL[1], face + 0.4], [DIAL[0], DIAL[1] - (DIAL_R - 7), face + 0.4]].map(at)), { tone: "lit" })}</g>`);
for (const a of [0, 1]) {
  const x = DIAL[0] + (a ? 1 : -1) * (DIAL_R + 6.4);
  out.push(S(k.cylinder(x, DIAL[1], 2.2, 0, 2.4, P, 16), { tone: "lo" }));
  out.push(D([at([x, DIAL[1], 2.4])], { size: 0.46 }));
}

const svg = k.figureSvg({
  width: WIDTH, height: HEIGHT, body: out.join(""),
  className: "sorter",
  label: "An edge-notched card sorter: cards you can explain cold stay in the tray when the needle lifts",
});

/* The lift is precomputed as two transforms and crossfaded in CSS, so the page
   ships no geometry code at all — inlining the 35 KB kit to move one group up
   by 19 units would be a poor trade on a landing page. */
/* translateAlong gives SVG attribute syntax — "translate(0 -33.5)". CSS needs a
   comma and units, and silently drops the whole declaration without them. */
const [UPX, UPY] = k.translateAlong(P, [0, 0, LIFT]).match(/-?[\d.]+/g);
const UP = `translate(${UPX}px, ${UPY}px)`;
const frag = `${svg}
<style>
 .sorter .cd,.sorter #needle{transition:transform .72s cubic-bezier(.22,.61,.36,1)}
 .sorter .cd .notch{display:none}
 .sorter .cd.cold .notch{display:inline}
 .sorter.up .cd:not(.cold),.sorter.up #needle{transform:${UP}}
 @media (prefers-reduced-motion:reduce){.sorter .cd,.sorter #needle{transition:none}}
</style>
<script>
(function(){
 var svg=document.querySelector(".sorter");if(!svg)return;
 var calm=matchMedia("(prefers-reduced-motion:reduce)"),seen=false,timer=0;
 var set=function(on){svg.classList.toggle("up",on)};
 var loop=function(){if(calm.matches||!seen)return;set(!svg.classList.contains("up"));timer=setTimeout(loop,2600)};
 new IntersectionObserver(function(e){seen=e[e.length-1].isIntersecting;
   if(seen){clearTimeout(timer);timer=setTimeout(loop,700)}else{clearTimeout(timer);set(false)}},
   {rootMargin:"80px 0px"}).observe(svg);
 var stage=svg.closest(".hero-fig")||svg;
 stage.addEventListener("pointerenter",function(){clearTimeout(timer);set(true)});
 stage.addEventListener("pointerleave",function(){clearTimeout(timer);set(false);timer=setTimeout(loop,1600)});
})();
<\/script>`;
writeFileSync(join(HERE, "hero.svg.html"), frag.replace("<svg", `<svg data-cards="${CARDS}"`));
console.log(`wrote hero.svg.html — ${CARDS} cards, ${coldCards} mastered (${COLD}/${TOTAL})`);
