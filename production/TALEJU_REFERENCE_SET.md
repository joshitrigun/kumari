# The King's Regret — Taleju Reference Set (for Seedance 2.5)

How to build and feed the goddess **Taleju Bhawani**'s reference images so her identity holds across her appearances. She is the Malla royal tutelary goddess — tantric Durga, source of sacred legitimacy.

> **She appears in human form, but her aura is unmistakably a goddess's.** As in the legend, she comes to the King as a woman he can sit across from and play dice with — so she must read as a real, living, moving woman, **not** a rigid temple statue. Her skin is **warm human Newar brown** — she is the most radiant, beautiful face in the frame, but human, not gilded or glowing. Her divinity lives entirely in a grounded **aura around her**, not in her flesh: a faint halo/nimbus, a soft gold rim-light on her edges, the copper Shri Yantra behind her, temple crown and ornaments, and a sovereign, uncanny stillness no mortal has (one subtle not-quite-mortal tell). She is a **goddess wearing a human form** — a woman the King could mistake for mortal for a heartbeat (which is exactly his mistake) — never a seductive/glamour goddess or romantic partner.

> Taleju appears in Act 1 (counsel), Act 2 (the wounded withdrawal), and Act 3 (dream silhouette). Her aura/light must stay **grounded** — warm oil-lamp reflection and a soft nimbus, never fluorescent CGI glow. Keep her light signature clearly **distinct from the newborn Kumari's** gentler dawn radiance (Taleju's is a fuller, liquid divine glow).

---

## 1. The Identity Anchor (never changes, every act, every still)

Paste verbatim into **every** Taleju image prompt.

> `The goddess Taleju Bhawani in a perfect human form — a serene woman of flawless, idealized human beauty: a perfect human face and a graceful, perfectly proportioned human body. Warm human Newar brown skin, the most beautiful face in the frame but human, not gilded or glowing. Large, calm dark eyes with a serene, sovereign, boundary-setting depth no mortal has — one subtle not-quite-mortal tell. Refined kohl. A luminous red bindi. Her divinity is around her, not in her flesh: a faint golden halo/nimbus, a soft gold rim-light on her edges, and a subtle copper Shri Yantra behind her head. Painted in the Newar paubha idiom — flat mineral pigment, ink outlines, gold-leaf aura, sacred and iconic, never photoreal. A goddess wearing a human form; never seductive, never a glamour goddess.`

**Taleju negative prompt (always append):**

> `romantic goddess, sexy goddess, exposed costume, fairy, generic fantasy princess, tiara, Thai crown, Balinese dancer, Malaysian costume, neon aura, angry villain deity, plastic CGI, glamour makeup.`

What changes between acts is **only** how present or withdrawn she is, and how her grounded light behaves. The face, crown, and brocade above are constant.

---

## 2. What to generate per act

Same rule as the King: **3 stills per appearance is the floor; 4 is better**, always including a clean **front** and a **three-quarter**. Save to `character_sheets/approved/`.

Constant wardrobe to append to every act (unless noted): `heavy historically accurate Newar ceremonial brocade (Kinkhab) draping over her human form like real cloth (worn by a living goddess, not stiff like a statue), dominated by deep vermillion red and hammered antique gold; a three-tiered gold repoussé temple crown studded with coral and turquoise; a faint golden nimbus and a subtle copper Shri Yantra mandala behind her head. Lit by flickering mustard-oil brass lamps, with a soft grounded gold rim-light around her (aura, not glowing skin).`

### Act 1 — Divine Counsel (full presence)
Fully present, sovereign, calm. Warm grounded lamp light; a subtle non-glowing warmth from her and the token.

| # | Still | Angle | Lighting / expression |
| --- | --- | --- | --- |
| 1 | `taleju_act1_front` | Front, head-and-shoulders | Warm brass-lamp key; serene, sovereign |
| 2 | `taleju_act1_3q` | Three-quarter | Same warm key; crown and brocade clear |
| 3 | `taleju_act1_enthroned` | Seated wide at the game board | Living, serene stillness (not statue-stiff); halo + Shri Yantra behind |
| 4 | `taleju_act1_eyes` *(opt.)* | Tight on eyes | Lamp catchlight; calm intensity |

### Act 2 — Wounded Boundary (the withdrawal)
The **same** goddess, now stepping back into deep shadow of the red-brick shrine. Profound, unsmiling sacred sadness — wounded boundary, **not anger, not a breakup**. The brass lamps around her smoke and dim; the Shri Yantra feels distant.

| # | Still | Angle | Lighting / expression |
| --- | --- | --- | --- |
| 1 | `taleju_act2_front` | Front, receding | Dimming lamps; sacred sadness |
| 2 | `taleju_act2_3q` | Three-quarter, half into shadow | Cool falloff; stepping back |
| 3 | `taleju_act2_recede` | Wider, body turning into shadow | Smoke and dimming brass; distance growing |

Note to append: `stepping back into the dark shadows of a red-brick shrine, her warm human brown face showing profound unsmiling sacred sadness; the heavy brass oil lamps around her are smoking and dimming; absolutely no magical glowing CGI, only heavy textiles and shadow.`

### Act 3 — Dream Silhouette (memory / the instruction)
She appears in the King's dream as a **silhouette / mist**, ethereal but still grounded — soft-focus, slightly bleached, a halo of *real* light (lamp/dawn quality), not neon. Rain can pass *through* the translucent form.

| # | Still | Angle | Lighting / expression |
| --- | --- | --- | --- |
| 1 | `taleju_act3_silhouette` | Front, silhouette/mist | Soft backlit halo; translucent edges |
| 2 | `taleju_act3_3q` | Three-quarter, misted | Bleached soft-focus; serene |
| 3 | `taleju_act3_instruction` *(opt.)* | Half-body, open hand lowering | Dream light; offering gesture, finger to lips |

Note to append: `appearing as a soft-focus dream silhouette in mist, slightly bleached, with a subtle grounded halo of light (oil-lamp / dawn quality, never neon); translucent enough that rain passes through; ethereal but physically real, no CGI glow.`

---

## 3. Feeding Seedance

Same discipline as the King: identify the act, feed **that appearance's full set** (front + three-quarter minimum), **never mix appearances in one shot**, restate the Identity Anchor + that act's note in the shot prompt, and add a 4th angle before changing wording if she drifts.

**Extra rule for Taleju:** keep her grounded light in the prompt every time (`warm oil-lamp reflection, no neon, no CGI glow`) — she drifts toward fantasy-goddess faster than any other character.

---

## 4. Naming convention

```
character_sheets/approved/
  taleju_act1_front.png   taleju_act1_3q.png   taleju_act1_enthroned.png   taleju_act1_eyes.png
  taleju_act2_front.png   taleju_act2_3q.png   taleju_act2_recede.png
  taleju_act3_silhouette.png   taleju_act3_3q.png   taleju_act3_instruction.png
```

---

## 5. Consistency check before you approve a set

- [ ] Front and three-quarter are clearly the **same** warm-brown human face.
- [ ] Crown, coral/turquoise studding, and Kinkhab brocade match across the set.
- [ ] Reads as a **goddess in human form** — a serene, living woman with **warm human skin** and an unmistakable divine aura *around* her (faint nimbus, gold rim-light, Shri Yantra, uncanny stillness) — **not** a gilded/glowing-skinned deity, **not** a rigid temple statue, and **never** a glamour or romantic goddess.
- [ ] Light is **grounded** (lamp/dawn), with **no neon, no CGI aura**.
- [ ] Act 2 is the *same face* as Act 1, only withdrawing into sorrow — not a different woman, not angry.
- [ ] Her light is visibly **gentler and warmer-grounded than nothing**, but distinct from the Kumari's dawn glow (see `KUMARI_REFERENCE_SET.md`).
