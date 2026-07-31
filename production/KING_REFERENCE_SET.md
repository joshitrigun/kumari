# The King's Regret — King Reference Set (for Seedance 2.5)

How to build and feed the King's reference images so his identity stays locked across all four acts. Seedance accepts many references per generation; the goal here is a small, disciplined set that pins his **face** while letting his **wardrobe and condition** change by act.

> The King is the film's spine — he appears in Acts 1, 3, and 4 and must read as *the same man* who has been broken and rebuilt. This is the single most important identity lock in the film.

---

## 1. The Identity Anchor (never changes, every act, every still)

Copy this block verbatim into **every** King image prompt, in every act. Do not paraphrase — the exact wording is what holds the face.

> `A tall, strong-built 50-year-old Nepali Newar Malla king in his prime — commanding, athletic, handsome and sharply intelligent. Medium brown skin, strong balanced features, firm square jaw, high cheekbones, straight nose, well-groomed short beard and mustache. Deep-set dark eyes, keen and perceptive, with a quiet devotional depth. Red vermillion tika on the forehead. The cultured, dignified, magnetic bearing of a Kathmandu Valley king. Painted in traditional Newar paubha style — flat mineral pigment, ink outlines, historically grounded and mythic, never photoreal.`

> **Note on the arc:** this handsome, powerful prime carries through the whole film. He is never reduced to a beggar. In **Act 3** he is *humbled, not broken* — still tall and dignified, but stripped of regalia and pride, expressing penance as devotion (praying from his palace toward Taleju's temple). The change across acts is **bearing and wardrobe**, not a loss of stature: proud king → humbled devotee → man at peace.

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
Same court dress, but **one single strand of hair falls loose** from the headpiece; the devotional warmth in his eyes has tilted one degree too far — overflowing into something human and uncontained. **Warm brass-lamp light unchanged from Act 1.** *(Not a new man — the Act 1 face, overflowing.)*

| # | Still | Angle | Lighting / expression |
| --- | --- | --- | --- |
| 1 | `king_act2_front` | Front | Warm brass-lamp key; overflowing warmth, barely held |
| 2 | `king_act2_3q` | Three-quarter | Same warm key; single loose hair strand — the only crack |
| 3 | `king_act2_desire` | Tight on eyes | Overflowing warmth in his eyes; the flash of desire, not hardness |

Wardrobe to append: `the same Malla court dress and gold repoussé headpiece as Act 1, a single strand of dark hair fallen loose across the temple — the only visual crack. Same warm brass-lamp light as Act 1; the change is entirely in his eyes.`

### Act 3 — Penance (humbled devotion, prayer toward the temple)
**Humbled, not broken.** No regalia, no headpiece, no gold — simple undyed cream cotton robes and a plain sash, dark hair loosely tied. Still tall, strong, and dignified; his face carries quiet grief and unbroken longing, not exhaustion or emaciation. His penance is *devotion across distance*: praying from his palace toward Taleju's temple. Soft misty dawn light.

| # | Still | Angle | Lighting / expression |
| --- | --- | --- | --- |
| 1 | `king_act3_prayer_wide` | Three-quarter from behind, at the palace window overlooking the distant Taleju temple | Misty dawn; both hands pressed in prayer (namaskar); longing |
| 2 | `king_act3_front` | Front, hands in prayer at chest | Soft dawn key; quiet grief, dignified, eyes toward the temple |
| 3 | `king_act3_3q` | Three-quarter portrait | Gentle dawn light; humbled but composed, sorrowful longing |

Wardrobe to append: `humbled but dignified — no royal regalia, no headpiece, no gold; only simple undyed cream cotton robes and a plain sash, dark hair loosely tied, a single restrained mark of station. Still tall and strong. Standing at the carved ankhijhyal window of his palace terrace, both hands pressed together in prayer toward the distant multi-tiered Taleju temple across the brick square. Soft misty dawn light.`

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
