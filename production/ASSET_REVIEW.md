# The King's Regret - Asset Review and Director Punch-Up

Review date: 2026-06-14

Scope: [animatic_frames/](animatic_frames/), [animatic_output/](animatic_output/), [character_sheets/](character_sheets/), and [environment_sheets/](environment_sheets/).

## Executive Read

The package is surprisingly complete for a non-animator workflow: every shot has a PNG/SVG control frame, the major characters have reference sheets, the three environments exist, and the animatic has an EDL path into editorial. The biggest improvement is not more drawing. It is sharper directing language, cleaner metadata, and stronger continuity rules so AI video tools understand what must stay consistent.

## What I Improved

- Corrected Shot 4's editorial label from a King/Taleju two-shot to the Queen witnessing the sacred fracture.
- Made [animatic_output/concat_list.txt](animatic_output/concat_list.txt) portable by replacing machine-specific absolute paths with relative paths.
- Updated [assemble_animatic.py](assemble_animatic.py) so future concat lists stay portable.
- Updated [export_edl.py](export_edl.py) so regenerated EDLs keep the corrected Shot 4 label.
- Removed the misleading character SVG sheets after review because they drifted toward generic/Malaysian-looking court fantasy rather than Nepali Newar/Malla visual culture.
- Updated missing-ffmpeg instructions for Windows.
- Tightened attire direction away from Malaysian/Southeast Asian costume drift and toward Nepali/Newar Malla court and Kumari references.
- Added [REALITY_REFERENCE.md](REALITY_REFERENCE.md) with web-grounded personality, attire, and cultural guardrails for Jayaprakash Malla, the Queen, Taleju, and Kumari.
- Added [CHARACTER_REFERENCE_REVIEW.md](CHARACTER_REFERENCE_REVIEW.md) to document where character look references are written and which files are reliable versus risky.
- Added [CHARACTER_LOOK_BIBLE.md](CHARACTER_LOOK_BIBLE.md) as the current source for character appearance, image prompts, and negative guardrails after the SVG sketch attempts failed.

## Animatic Frames Review

The 17-shot frame set gives the film a clear four-act rhythm. The strongest frames are the ones with a single readable idea: Shot 4's lattice witness, Shot 8's vanishing/token action, Shot 15's Kumari entrance, and Shot 17's token epilogue. Those should become the style anchors for the rest of the generation pass.

### Improvements To Push In Generation

| Shot | Current Function | Director Punch-Up |
| --- | --- | --- |
| 01 | Establish sacred chamber | Make the board/token visible as a tiny future clue, not just room decor. |
| 03 | Hands and token | This is the first tactile promise of the film. Require 5 fingers, real hand weight, and token contact shadow. |
| 04 | Queen witness | Keep her behind lattice. Her eyes should move from awe to ache; no jealousy. |
| 05 | Intimacy peak | Avoid romance framing. Ask for devotional closeness, liquid divine light, and still breath. |
| 06 | Transgression | Underplay it. One fallen hair strand, clenched hand, eye glint, and live color shift. |
| 08 | Vanishing | Make the token obey gravity while Taleju defies it. That contrast sells the myth. |
| 09 | Memory | Use as painful warmth, not a random flashback. Match Act 1 saturation exactly. |
| 12 | Penance | Keep him small, crownless, and physically reduced. Rain and stillness should dominate. |
| 13 | Montage | Treat as three sacred inserts: lamp, empty board, incense. No busy motion. |
| 15 | Kumari appears | The child should be quiet, small, and processional. Avoid superhero glow. |
| 17 | Epilogue | Let the final image breathe. Token, board, dawn, peace. No extra characters needed. |

## Animatic Output Review

[animatic_output/kings_regret_animatic.edl](animatic_output/kings_regret_animatic.edl) is usable for DaVinci Resolve and now has the corrected Shot 4 comment. [animatic_output/concat_list.txt](animatic_output/concat_list.txt) is now portable across Windows/macOS/Linux because it points to `../animatic_frames/...` instead of one local user path.

One note: [animatic_output/animatic.mp4](animatic_output/animatic.mp4) may be stale if it was created before these metadata fixes. Regenerate it after installing ffmpeg.

Windows install:

```powershell
winget install Gyan.FFmpeg
```

Then run:

```powershell
Set-Location production
python assemble_animatic.py
```

## Character Reference Review

The SVG character sheets in [character_sheets/](character_sheets/) were deleted after visual review. They should not be used as identity references. They were too schematic/cartoon-like and created a cultural drift problem.

Current character-look source of truth:

- [CHARACTER_LOOK_BIBLE.md](CHARACTER_LOOK_BIBLE.md) for concrete face, hair, costume, movement, and image-prompt direction.
- [REALITY_REFERENCE.md](REALITY_REFERENCE.md) for research-grounded character reality and cultural guardrails.
- [ANIMATOR_BRIEF.md](ANIMATOR_BRIEF.md) for production-facing character performance and costume evolution.
- [PROMPTS.md](PROMPTS.md) for shot-level generation language.
- [CHARACTER_REFERENCE_REVIEW.md](CHARACTER_REFERENCE_REVIEW.md) for a file-by-file audit of where character looks are written.

### King

The written references should treat him as a transforming character, not a static royal design. Keep the visual logic:

- Act 1: perfect posture, crown, disciplined robe, devotional softness.
- Act 2: same costume but cracked: loose hair strand, clenched hand, sharper eye glint.
- Act 3: crownless, wet grey wrap, thinner face, lowered body.
- Act 4: simple shawl, humbled posture, open hands, no restored vanity.

Reality note: play him as cultured and devotional, but politically embattled and proud. The danger is entitlement under pressure, not cartoon evil.

### Taleju

Taleju needs clearer written sacred makeup and garment notes: luminous bindi, refined kohl, cream-and-gold temple-devata drapes, yantra/triangular geometry, and light that trails like water. She should remain compassionate even when she withdraws. Do not prompt her as angry unless the anger is brief and divine; the dominant feeling should be wounded sorrow and boundary restored.

Reality note: she is the Malla royal tutelary goddess and tantric Durga/Tripura Sundari energy. Frame her as counsel, protection, and withdrawn legitimacy, not a romantic partner.

### Queen

The Queen is clarified as witness, not jealous spouse. Written references should keep tear-line highlights and restrained royal makeup cues, plus notes that her dress should melt into shadow while jewelry catches candlelight. Her production note should remain: awe first, ache second, sacred concern always.

Reality note: treat her as politically aware and spiritually perceptive. Her witnessing is not gossip or jealousy; it is awareness that the sacred order is breaking.

### Kumari Child

The child is the emotional landing point. Written references should specify hand-painted makeup asymmetry so the kohl and agni-chakshu do not look like a perfect mask, and clarify that the red/gold ceremonial dress should have weight rather than fantasy float. Keep her scale small against stone architecture. Her glow should be dawn-like and restrained, not the same supernatural intensity as Taleju.

## Environment Sheets Review

### Sacred Chamber

The chamber sheet is the strongest environment because it already contains both Act 1 warmth and Act 2 cold collapse. Use it to demand continuity: same table, same window/lattice, same room, changed moral temperature.

### Rain Alley

The rain alley should be less decorative than the chamber. Its job is penance: wet stone, closed doors, a single warm lamp, the King reduced by scale.

### Dawn Courtyard

The dawn courtyard should not feel like a new world; it should feel like the same spiritual geography washed clean. Keep architecture consistent with the alley and chamber, but let air, dawn, and space replace claustrophobia.

## New Golden Rule For AI Generation

Every shot prompt should answer this before generation:

1. What is the King's inner state here?
2. Where is the token, physically or emotionally?
3. What is the light doing to tell the story?
4. Is Taleju/Kumari being treated with reverence rather than spectacle?

If a generated clip is beautiful but fails one of those four questions, regenerate it.