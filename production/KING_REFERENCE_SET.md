# The King's Regret — King Reference Set (for Seedance 2.5)

How to build and feed the King's reference images so his identity stays locked across all four acts. Seedance accepts many references per generation; the goal here is a small, disciplined set that pins his **face** while letting his **wardrobe and condition** change by act.

> The King is the film's spine — he appears in Acts 1, 3, and 4 and must read as *the same man* who has been broken and rebuilt. This is the single most important identity lock in the film.

---

## 1. The Identity Anchor (never changes, every act, every still)

Copy this block verbatim into **every** King image prompt, in every act. Do not paraphrase — the exact wording is what holds the face.

> `A 50-year-old Nepali Newar man. Medium brown skin. Tired, hollowed cheeks, firm jaw. Deep-set dark eyes with heavy upper lids. Slight mustache and short stubble beard. Red vermillion tika on the forehead. Heavy, burdened expression. Fully historically grounded, photoreal, ethnographic.`

**King negative prompt (always append):**

> `Malaysian tengkolok, songkok, Thai crown, Mughal turban plume, Rajput armor, fantasy king armor, shiny songket, overdecorated gold costume, smiling prince, villain sneer, pale European face, Disney prince, CGI glow, plastic skin.`

What changes between acts is **only** the wardrobe, the physical condition (grief/exhaustion), and the lighting. The face above is constant.

---

## 2. What to generate per act

For each act, generate a small **reference set** — the same face from a few angles and one signature lighting, so Seedance has enough to triangulate identity. **3 stills per act is the floor; 4 is better.** Always include at least one clean **front** and one **three-quarter**, because Seedance fuses angles.

Save every approved still to `character_sheets/approved/` using the naming convention in §4.

### Act 1 — Court (the covenant)
Full Malla court dress; reverent, glowing devotion. Warm gold.

| # | Still | Angle | Lighting / expression |
| --- | --- | --- | --- |
| 1 | `king_act1_front` | Front, head-and-shoulders | Warm oil-lamp key; calm, devoted |
| 2 | `king_act1_3q` | Three-quarter | Same warm key; eyes slightly lowered |
| 3 | `king_act1_seated` | Seated wide, headpiece visible | Warm 3-point; dignified posture |
| 4 | `king_act1_eyes` *(opt.)* | Tight close on eyes | Lamp catchlight; reverence |

Wardrobe to append: `traditional Malla-style tight-fitting madder-dyed cotton upper garment (tapalan), thick wound waist cloth (patuka), pleated lower skirt-wrap (jama), and a multi-tiered gold repoussé headpiece hammered and sitting low on dark brushed-back hair. No turban.`

### Act 2 — The Crack (the breaking)
Same court dress, but **one single strand of hair falls loose** from the headpiece; the eye-glint sharpens to a metallic edge. Cold slate-blue side light. *(Not a new man — the Act 1 face, hardening.)*

| # | Still | Angle | Lighting / expression |
| --- | --- | --- | --- |
| 1 | `king_act2_front` | Front | Cool side key; hardened, tightening |
| 2 | `king_act2_3q` | Three-quarter | Cold rim; a single loose hair strand |
| 3 | `king_act2_desire` | Tight on eyes/hand | Metallic eye-glint; the flash of desire |

Wardrobe to append: `the same Malla court dress and gold repoussé headpiece as Act 1, but a single strand of dark hair has fallen loose across the temple. Cold slate-blue side lighting.`

### Act 3 — Penance (rock bottom)
**Bareheaded**, wet loose hair, plain damp grey unbleached cotton body-wrap (khen) and simple shawl. Gaunt, exhausted, paler with "grief texture." Desaturated cold rain light.

| # | Still | Angle | Lighting / expression |
| --- | --- | --- | --- |
| 1 | `king_act3_front` | Front | Overcast rain light; hollow, penitent |
| 2 | `king_act3_3q` | Three-quarter | Wet hair falling loose; exhaustion lines |
| 3 | `king_act3_prayer` | Half-body, hands folded | Single incense-lamp warm accent in cold scene |

Wardrobe to append: `stripped of all royal gear, bareheaded with wet dark hair falling loose, wearing only a plain damp grey unbleached cotton body-wrap (khen) and a simple shawl. Skin paler with deep exhaustion lines. Cold desaturated monsoon-rain light.`

### Act 4 — Humbled (restoration)
Simple Nepali cotton shawl; transformed, humble posture, no restored vanity. At peace, accepting. Soft warm dawn (gentler than Act 1).

| # | Still | Angle | Lighting / expression |
| --- | --- | --- | --- |
| 1 | `king_act4_front` | Front | Soft dawn key; calm, at peace |
| 2 | `king_act4_3q` | Three-quarter | Warm low sun; humble, lowered head |
| 3 | `king_act4_tear` *(opt.)* | Tight on eyes | Single tear catchlight; acceptance |

Wardrobe to append: `a simple humble Nepali cotton shawl over bare shoulders, hair neatly settled, no headpiece and no royal ornament. Transformed, humble, at-peace posture. Soft warm dawn light.`

---

## 3. How to feed Seedance per shot

1. **Identify the act** the shot belongs to (see `PRODUCTION_MASTER.md` frame ranges).
2. Feed **that act's full reference set** (all 3–4 stills) as Seedance references — the front and three-quarter are the minimum non-negotiable pair.
3. **Never mix acts in one shot.** An Act 3 shot gets only Act 3 refs. Mixing wardrobes confuses the fusion and drifts the face.
4. In the shot prompt itself, restate the **Identity Anchor** (§1) plus that act's wardrobe line — references + text pulling in the same direction is what locks him.
5. If the face still drifts, add a 4th reference (a second three-quarter from the other side) rather than changing the prompt wording.

---

## 4. Naming convention

```
character_sheets/approved/
  king_act1_front.png     king_act1_3q.png     king_act1_seated.png    king_act1_eyes.png
  king_act2_front.png     king_act2_3q.png     king_act2_desire.png
  king_act3_front.png     king_act3_3q.png     king_act3_prayer.png
  king_act4_front.png     king_act4_3q.png     king_act4_tear.png
```

`king_<act>_<angle-or-role>.png` — lowercase, so the log entries in `PROMPT_WORKFLOW.md` (e.g. `Refs: king_act2_front.png, king_act2_3q.png`) map directly to files.

---

## 5. Consistency check before you approve a set

- [ ] Front and three-quarter clearly show the **same** man (cheekbones, jaw, eye-lids, nose).
- [ ] The tika, mustache, and stubble match across the set.
- [ ] Wardrobe is correct for the act (headpiece Acts 1–2, bareheaded Act 3, humble shawl Act 4).
- [ ] Reads as **Nepali/Newar Malla** — not Mughal, Rajput, Thai, or a generic royal.
- [ ] Act 3 looks like the *same face* as Act 1, only broken — this is the hardest and most important match.

> Once the King set passes, repeat this pattern for **Taleju**, the **Queen**, and the **newborn Kumari** (Kumari needs extra care — carried/resting, still, reverent, never cute or spooky).
