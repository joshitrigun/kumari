# The King's Regret — Newborn Kumari Reference Set (for Seedance 2.5)

How to build and feed the **newborn Royal Kumari**'s reference images. She is an infant carrying divine presence — her power is **silence, stillness, and ritual gravity**, not cuteness. This is the most culturally sensitive part of the film; treat it with the utmost care and reverence.

> ⚠️ **Read this first.** The Kumari is a **newborn**. She does **not** walk, grip, pose, or smile. She is **carried by a caretaker or rests on a ceremonial cushion, perfectly still**, with the **token placed on her chest** — never gripped. Never cute-posed, never spooky/horror, never a doll. Content moderation on hosted models is strict here: keep the framing reverent, keep the makeup described as *hand-painted ritual*, and let the **token's light and the architecture** carry the recognition rather than a tight infant face.

---

## 1. The Identity Anchor (never changes, every still)

Paste verbatim into **every** Kumari image prompt.

> `A newborn Nepali Newar infant dressed as the authentic Royal Kumari (Living Goddess). Medium brown skin. A perfectly still, solemn, unsmiling expression. Authentic hand-painted thick black kohl extending to the temples, and a large red-and-yellow fire-eye (agni-chakshu) hand-painted over the entire forehead. A traditional high topknot scaled for an infant. Painted in traditional Newar paubha style — flat mineral pigment, ink outlines, reverent, historically and culturally accurate, never photoreal.`

**Kumari negative prompt (always append):**

> `cute princess, horror child, creepy doll, tiara, Thai crown, Malaysian costume, fantasy princess dress, superhero mask makeup, adult glamour, smiling mascot, plastic CGI, neon glow, playful baby, gripping object, walking baby.`

Constant wardrobe/ornament to append: `authentic miniature heavy crimson-red raw cotton and silk brocade layered ceremonial robes; a real hammered-gold Kumari necklace (Tayo) and miniature repoussé jewelry; enveloped in heavy restrictive textiles.`

---

## 2. What to generate

Keep the set **small and safe**. **3 stills is enough**; do not over-generate tight face close-ups. Always include one where she is **framed small against architecture** (this is both better filmmaking and safer generation). Save to `character_sheets/approved/`.

### Core set — the Reveal (Act 4, Shots 15–17)

| # | Still | Framing | Lighting / notes |
| --- | --- | --- | --- |
| 1 | `kumari_cushion` | Resting on a ceremonial embroidered cushion, **token placed on her chest** | Soft muted dawn; token casting gentle light on her face; uncanny stillness |
| 2 | `kumari_carried` | **Carried ceremonially by a traditional Newar caretaker** through a red-brick courtyard | Cold-to-warm dawn; infant small against Malla carved-wood struts |
| 3 | `kumari_portrait` | Head-and-shoulders, solemn, against a dark carved wooden courtyard window | Restrained dawn key; kohl and agni-chakshu organically applied on a tiny face |

Framing note to append: `held perfectly still or resting; the recurring token is placed on her chest or on the cushion beside her, casting soft light on her face — a newborn does not grip it. Kept physically small against genuine Malla-era carved dark-wood struts and terracotta-tiled architecture.`

> **Light signature:** the Kumari's glow is a **gentle dawn radiance / quiet gravity** — noticeably softer and less supernatural than Taleju's grounded lamp-light. Keep the two distinct (see `TALEJU_REFERENCE_SET.md`). Let the **token** carry the recognition, not a bright aura.

---

## 3. Feeding Seedance

- Feed the **full 3-still set** for any Act 4 shot with the child; the cushion and carried stills anchor the *pose and scale*, the portrait anchors the *face*.
- Restate the Identity Anchor + wardrobe + framing note in every shot prompt.
- **Keep the safety guardrails in the prompt every time**: `carried or resting, perfectly still, token placed not gripped, reverent, never cute or spooky`.
- If a hosted model refuses or distorts the infant, **widen the shot** (more architecture, smaller child, token-forward) rather than tightening on the face — this both passes moderation and matches the intended "dawn deciding to enter the frame" tone.
- Do **not** generate the child in motion (walking, reaching, grasping) — it is wrong for the story *and* the least reliable to generate.

---

## 4. Naming convention

```
character_sheets/approved/
  kumari_cushion.png   kumari_carried.png   kumari_portrait.png
```

---

## 5. Consistency check before you approve a set

- [ ] Clearly a **newborn/infant**, perfectly still, **unsmiling and solemn** — never cute, never spooky.
- [ ] Kohl-to-temples and the red/yellow **agni-chakshu** read as **hand-painted ritual**, organically on a tiny face — not a mask or sticker.
- [ ] The **token is placed** on her chest/cushion, **not gripped**; she is **carried or resting**, never walking.
- [ ] She is **small against real Malla architecture**; the light is **gentle dawn**, distinct from Taleju's lamp-glow.
- [ ] Reads with **reverence and gravity** — the hope of the story, treated with dignity.
- [ ] Passes a **Newar/Nepalese cultural review** before final render (required for this character above all).
