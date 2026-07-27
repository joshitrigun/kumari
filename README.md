# Kumari — "The King's Regret"

A production package for a **5-minute animated music video** retelling the legend of the **Kumari** (the Living Goddess) — King Jayaprakash Malla, the goddess Taleju, and the founding of a tradition in the 18th-century Kathmandu Valley.

This repository holds the complete creative and production bible. It is a **prompt-based, keyframe-driven** package: you paint character references and per-shot keyframes with an image model, then animate them into shots.

## The film at a glance

| Item | Spec |
| --- | --- |
| Format | 5-minute music video (17 shots, 7200 frames @ 24 fps, 1920×1080) |
| Visual style | **Newar paubha / thangka 2D animation** — a traditional Nepalese sacred scroll-painting brought to gentle motion. Flat mineral pigments, gold-leaf, ink outlines, sacred halos, gods rendered as icons. **Not** photoreal, 3D-Pixar, or anime. |
| Pipeline | Paint paubha keyframes (Midjourney / Imagen / Flux) → animate with **Seedance 2.5** (image-to-video) → assemble in any editor |
| Story | A one-sided love: a king desires the goddess who withdraws; his transgression, his penance, and the birth of the Kumari tradition |

## Where everything lives

All working documents are in **[`production/`](production/)**. Start with its README:

➡️ **[production/README.md](production/README.md)** — the package index and director's overview.

Key documents:
- [production/PROMPT_WORKFLOW.md](production/PROMPT_WORKFLOW.md) — start-to-finish, beginner-friendly guide
- [production/PRODUCTION_MASTER.md](production/PRODUCTION_MASTER.md) — the 17-shot table (frames, inputs, acceptance criteria)
- [production/ANIMATOR_BRIEF.md](production/ANIMATOR_BRIEF.md) — full creative brief (story, characters, environments)
- [production/PROMPTS.md](production/PROMPTS.md) — per-shot generation prompts + the shared STYLE / NEGATIVE blocks
- [production/CHARACTER_IMAGE_PROMPTS.md](production/CHARACTER_IMAGE_PROMPTS.md) + the four `*_REFERENCE_SET.md` files — character reference generation
- [production/CHARACTER_LOOK_BIBLE.md](production/CHARACTER_LOOK_BIBLE.md), [production/REALITY_REFERENCE.md](production/REALITY_REFERENCE.md), [production/COLOR_PALETTE.md](production/COLOR_PALETTE.md) — look, cultural accuracy, and color
- [production/steps.md](production/steps.md) — working checklist

## Recent design decisions

- **Visual style → Newar paubha / thangka 2D animation.** Replaced the earlier photoreal approach. This lets the sacred figures (Taleju, the newborn Kumari) read as holy icons rather than uncanny real people, and holds character identity far better across 17 shots. Prompts describe a *still painting*; motion is added at the animation stage.
- **Pipeline → keyframe-driven.** An illustration model paints the paubha keyframes; Seedance 2.5 animates them. No photoreal/Veo step — Shot 6's warm→cold shift is a palette change between two painted keyframes.
- **The King → a strong, handsome king in his prime.** Tall, athletic, sharply intelligent, commanding at 50. His fall hurts more because he starts high.
- **Act 3 penance → dignified longing, not a beggar.** Restaged from a rain-soaked alley to his **palace terrace at misty dawn**, praying across the square toward Taleju's temple. The board-vigil and the token's "empty place" are preserved.
- **The Queen → authentic Malla court dress.** Replaced the common **Haku Patasi** (a Jyapu/everyday garment) with royal wine/plum **silk + gold brocade**, and corrected her ornaments to the authentic Newar set (**Tayo, Naugedi, Kantha, Luswa, Nyapu Shikha, Sirbandi, Tikma, Makasi**) — no pan-Nepali Bulaki nose-ring.

## Cultural note

This is a reverent retelling of a living sacred tradition. Depicting it in the **paubha idiom** — its own visual language — is a strength, but a **Newar/Nepalese cultural review** should be completed before any final export, especially for the depiction of Taleju and the newborn Kumari.
