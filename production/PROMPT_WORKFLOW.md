# The King's Regret — Prompt-Only Production Guide

A start-to-finish guide for making this film using **only AI prompts** — no Blender, no animation software. If you're new, read this top to bottom once, then keep it open while you work.

You will do three things, in order:

1. **Generate character reference images** (locks how each person looks).
2. **Generate each of the 17 shots as short video clips** (using those references).
3. **Stitch the clips together** in a simple editor and add music.

---

## 0. What this film looks like

**Photoreal historical.** The goal is footage that looks like a real documentary filmed in 18th-century Kathmandu Valley — real skin, real woven cloth, real brick and carved wood, lit by oil lamps. It is **not** a cartoon, anime, 3D-Pixar, or painterly style. Every prompt in this package is written for that look, so don't fight it.

---

## 1. Pick your tools

You need two kinds of tool. Any modern option works; pick what you can access.

| Job | Good options |
| --- | --- |
| **Image generator** (character references, still frames) | Midjourney, Google Imagen, Flux, or your video tool's built-in image mode |
| **Video generator** (the actual shots) | Google **Veo**, **Kling**, **Runway**, or **Seedance** |

Prefer a video tool that lets you supply a **reference image** (sometimes called "image-to-video", "ingredients", or "identity reference"). This is how you keep the same face across shots. If your tool only does text-to-video, you can still work, but characters will drift more — see §5.

---

## 2. Generate the character references FIRST

Do this before any video. These images are your anchor — every shot points back to them.

1. Open [CHARACTER_IMAGE_PROMPTS.md](CHARACTER_IMAGE_PROMPTS.md).
2. Generate these portraits (the file has the exact prompts):
   - **King** — 4 looks: Act 1 court, Act 2 crack, Act 3 penance, Act 4 humbled
   - **Queen** — 2: lattice close-up, jewelry/costume study
   - **Taleju** — 3: Act 1 counsel, Act 2 wounded, Act 3 dream silhouette
   - **Kumari (newborn)** — 2: ceremonial portrait, dawn courtyard
3. For each one, generate several variations, pick the strongest, and **save it**:

```bash
mkdir -p character_sheets/approved
```

Save approved images there with clear names, e.g. `king_act1.png`, `taleju_act1.png`, `kumari_portrait.png`.

**Getting good references:**
- Always paste the **Global Style Prefix** and **Global Negative Prompt** from `CHARACTER_IMAGE_PROMPTS.md`.
- Judge them against [REALITY_REFERENCE.md](REALITY_REFERENCE.md) and [CHARACTER_LOOK_BIBLE.md](CHARACTER_LOOK_BIBLE.md). If it looks like a generic Bollywood royal, Mughal emperor, or fantasy princess, regenerate.
- Faces should read as **Nepali/Newar**, in real historical textiles, in warm lamp light.

> ⚠️ **The newborn Kumari and Taleju need extra care.** A newborn does not walk or grip anything — she is carried or rests on a cushion, perfectly still, with the token placed on her chest. Keep her depiction reverent and never cute-posed or spooky. This is the most culturally sensitive part of the film.

---

## 3. Lock the visual "style anchor"

1. Generate **Shot 1** (the establishing chamber) using its prompt in [PROMPTS.md](PROMPTS.md).
2. Pick the best-looking frame — the one whose light, color, and grain feel right for the whole film.
3. Save it as `STYLE_ANCHOR.png` in the project root.

From now on, if your tool accepts a **style reference image**, feed `STYLE_ANCHOR.png` into later shots so they match. This keeps all 17 shots feeling like one film.

---

## 4. Generate the shots (in priority order)

Don't go 1→17. Do the hardest, most important shots first — if the film works there, everything else is easier. Recommended order (from [PRODUCTION_MASTER.md](PRODUCTION_MASTER.md)):

**4 → 5 → 6 → 8 → 15 → 17**, then fill in the rest.

For **each** shot:

1. Copy its prompt from [PROMPTS.md](PROMPTS.md).
2. Paste in the shared **STYLE BLOCK** and **NEGATIVE PROMPT** from the top of that file.
3. If the shot shows a face, attach the matching character image from `character_sheets/approved/` as the reference/identity input.
4. If your tool supports it, attach `STYLE_ANCHOR.png` as the style reference.
5. Generate. Then **check it against the "Acceptance Criteria" for that shot in [PRODUCTION_MASTER.md](PRODUCTION_MASTER.md)** — that table tells you what "done" means (e.g. "lighting shift must be a live transition, not a cut").
6. If it fails, regenerate with a tighter, more specific instruction (see §6). Save the winners in a folder per shot, e.g. `outputs/shot04/`.

**How long should each clip be?** The exact durations are in `PRODUCTION_MASTER.md` (and the brief's shot table). Most AI tools cap clips at 5–10 seconds. For longer shots, generate 2–3 clips and join them, or generate a short clip and slow it down.

---

## 5. Keeping characters consistent (the #1 hard part)

Prompt-only video drifts — the King's face can change shot to shot. To fight this:

- **Reuse the same reference image** for a character in every shot they appear in.
- **Describe them identically** every time. Copy the exact wording from `CHARACTER_IMAGE_PROMPTS.md` (age, skin tone, beard, headpiece) — don't paraphrase.
- **Reuse the seed** if your tool exposes one and you got a good result.
- **Lean into stillness.** Slow, quiet, near-still shots (this film is full of them) hold a face far better than big movement. Shots 12, 13, 14, 17 barely move — let them be calm.
- Remember the **costume changes by act**: King is in full court dress (Act 1), one loose hair strand (Act 2), bareheaded rain-wrap (Act 3), humble shawl (Act 4). Use the matching reference image per act.

---

## 6. Keep a simple generation log

You'll try many versions. Track them in a plain text or markdown file so you don't repeat failures:

```
Shot 06 — attempt 3
Tool: Kling  |  Seed: 41822
Prompt: <what you used>
Result: warm→cold shift too abrupt, looks like a cut
Next: add "gradual 3-second color temperature transition, no hard cut"
```

---

## 7. Assemble the film

1. Put your approved clips in shot order (1→17) in any editor — CapCut, DaVinci Resolve (free), iMovie, Premiere.
2. Trim each clip to the duration in `PRODUCTION_MASTER.md`.
3. Add your music track.
4. Line the cuts up to the key musical beats (from [ANIMATOR_BRIEF.md](ANIMATOR_BRIEF.md)):
   - **1:13** — dissonant chord → the lighting hardens (Shot 6)
   - **1:53** — flute solo → Taleju vanishes (Shot 8)
   - **4:11** — new hopeful motif → the newborn Kumari appears (Shot 15)
   - **5:00** — resolution → token at rest (Shot 17)
5. Do a color pass so each act matches [COLOR_PALETTE.md](COLOR_PALETTE.md): Act 1 warm gold, Act 2 cold slate-blue, Act 3 desaturated rain, Act 4 soft dawn.

---

## 8. Before you call it done

Run the **Quality Checklist** in [README.md](README.md). Most important:

- The King's *face* stays recognizably the same person across all four acts.
- Taleju is sacred and sovereign, never a romantic/glamour figure.
- The newborn Kumari is still, reverent, carried/resting — never cute-posed or frightening.
- The token appears (or is clearly implied) in Shots 3, 8, 12/13, 15, and 17.
- Get a **Newar/Nepalese cultural review** before you publish. Photoreal depiction of the Kumari and Taleju deserves real cultural eyes.

---

## Quick reference: which doc for what

| I want to… | Open |
| --- | --- |
| Know the whole story and character arcs | `ANIMATOR_BRIEF.md` |
| Generate a character's look | `CHARACTER_IMAGE_PROMPTS.md` |
| Understand why a character looks that way | `CHARACTER_LOOK_BIBLE.md`, `REALITY_REFERENCE.md` |
| Generate a shot's video | `PROMPTS.md` |
| Know a shot's frames, order, and "done" criteria | `PRODUCTION_MASTER.md` |
| Get the colors and lighting per act | `COLOR_PALETTE.md` |
