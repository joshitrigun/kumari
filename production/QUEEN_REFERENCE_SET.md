# The King's Regret — Queen Reference Set (for Seedance 2.5)

How to build and feed the **Queen (Daya Lakshmi figure)**'s reference images. She is a Newar royal woman and the story's **conscience** — the human witness who reads the sacred covenant, and the first mortal to see it break. She is **not** a jealous wife and **not** a romantic rival; keep her sympathetic.

> She appears mainly in Act 1 (Shot 4, peering through the carved lattice) with a returning glance at the moment of breaking (Shot 6). She is almost always seen **through the ankhijhyal lattice** — that framing is her signature and her prison.

---

## 1. The Identity Anchor (never changes, every still)

Paste verbatim into **every** Queen image prompt.

> `An adult 40-year-old Nepali Newar noblewoman. Medium warm brown skin, almond eyes with subtle kohl. A constant tear-line highlight on the lower lid — aching gaze, not jealousy. Mouth closed or slightly parted in silent concern. Dark hair in a traditional compact Newar bun. Painted in traditional Newar paubha style — flat mineral pigment, ink outlines, historically grounded, never photoreal.`

**Queen negative prompt (always append):**

> `Malaysian songket, shiny palace costume, Thai crown, Southeast Asian queen crown, generic sari princess, jealous wife, seductive expression, exposed shoulder glamour, fantasy queen, tiara, pale face.`

Constant wardrobe/jewelry to append: `Malla queen's royal court dress — a deep wine/plum silk sari with richly woven gold-thread (kastha) borders and a brocade (kinkhab) panel, draped in elegant Newar court style over an embroidered silk cholo (fitted blouse), with a gold-brocade patuka sash and a dark maroon makhamali (velvet) veil-shawl. Heavy authentic Newar repoussé gold: the grand Tayo (serpent-headed lozenge-pendant ceremonial necklace, coral and turquoise), a Naugedi gold-bead necklace and a Kantha choker, a Luswa gold head-disk at the crown with Nyapu Shikha (five gold chains draped across the hair), a Sirbandi head-binding ornament, a Tikma forehead ornament, heavy basket-drop Makasi earrings, and gold bangles. This is royal court dress — NOT the plain black-cotton Haku Patasi of common Newar women, and NOT the pan-Nepali large Bulaki nose-ring. Plum/gold keeps her distinct from Taleju's vermillion temple brocade.`

---

## 2. What to generate

She has fewer looks than the King, so build **one core set** plus a couple of framing/expression variants. **3 stills minimum; 4 better.** Include a clean front and a three-quarter; because she is usually seen *through lattice*, generate both a **clear (no-lattice) identity plate** and **lattice-framed** variants.

### Core set — Witness at the Lattice (Act 1 / Shot 4, and Shot 6 glance)

| # | Still | Angle / framing | Lighting / expression |
| --- | --- | --- | --- |
| 1 | `queen_front_clear` | Front, **no lattice** (clean identity plate) | Warm oil-lamp; jewelry glinting; aching calm |
| 2 | `queen_lattice_front` | Front, **seen through carved dark-wood lattice (ankhijhyal)** | Geometric lattice shadows across face; longing |
| 3 | `queen_lattice_3q` | Three-quarter through lattice | Makasi earrings and Luswa/Nyapu Shikha head gold catching sharp candle highlight — the "signal in the dark" (no nose-ring) |
| 4 | `queen_dread` *(opt.)* | Tight on eyes, through lattice | Dawning dread at the moment of breaking (Shot 6) — she *reads* the rupture |

Framing note to append for lattice stills: `seen close-up through an intricately carved dark sal-wood lattice window (ankhijhyal), the lattice casting geometric shadow bars across her face; natural oil-lamp light glinting off the gold and off the tear on her lower lid.`

> The **clear front plate** (#1) is important: Seedance locks identity better from an unobstructed face, then you apply the lattice framing in the shot. Feed the clear plate *plus* a lattice variant together.

---

## 3. Feeding Seedance

- For Shot 4 and the Shot 6 glance, feed the **clear front plate + at least one lattice variant** together — the clear plate holds the face, the lattice variant holds the framing/light.
- Restate the Identity Anchor + wardrobe line in the shot prompt every time.
- Keep the **emotional guardrail in the prompt**: `aching, sympathetic witness — never jealous, never seductive`. She drifts toward "jealous wife" if you drop it.
- If the face drifts, add a second three-quarter clear plate rather than changing wording.

---

## 4. Naming convention

```
character_sheets/approved/
  queen_front_clear.png   queen_lattice_front.png   queen_lattice_3q.png   queen_dread.png
```

---

## 5. Consistency check before you approve a set

- [ ] Clear plate and lattice variants are the **same** 40-year-old Newar face.
- [ ] The **tear-line highlight** on the lower lid is present in every still.
- [ ] Tayo, Luswa/Nyapu Shikha head gold, and the wine/plum silk-and-gold court sari read as authentically Newar **royalty** — not the common black-cotton Haku Patasi, not a large Bulaki nose-ring, not a generic glossy Bollywood sari.
- [ ] Expression is **sympathetic witness / aching longing / dawning dread** — never jealous, never seductive.
- [ ] Lattice variants show real **geometric shadow bars** across the face and gold catching light.
