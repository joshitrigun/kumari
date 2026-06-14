# The King's Regret

Production package for a 5-minute animated music video inspired by the Kumari legend of King Jayaprakash Malla and Goddess Taleju. The package is built for AI-assisted 2D/2.5D animation, Blender layout, shot tracking, compositing, and final color grade.

## Project Specs

| Item | Spec |
| --- | --- |
| Format | Animated music video |
| Duration | 5:00 / 300 seconds |
| Timeline | 7200 frames at 24 fps |
| Resolution | 1920 x 1080 |
| Visual style | Cinematic 2.5D, painterly, shallow depth of field |
| Recommended tools | Blender, AI video generator, DaVinci Resolve or After Effects |
| Current stage | AI video generation package ready; priority shots pending generation |

## Start Here

1. Read [ANIMATOR_BRIEF.md](ANIMATOR_BRIEF.md) for story, character arcs, environments, and performance notes.
2. Use [PRODUCTION_MASTER.md](PRODUCTION_MASTER.md) as the source of truth for shots, frames, inputs, priorities, and acceptance criteria.
3. Use [PROMPTS.md](PROMPTS.md) for AI video generation prompts.
4. Use [SHOT_REFERENCE.md](SHOT_REFERENCE.md) during animation and editorial for timing, continuity, and music sync.
5. Use [COLOR_PALETTE.md](COLOR_PALETTE.md) for act-by-act lighting, color grading, and material swatches.
6. Open [shot_tracker.html](shot_tracker.html) in a browser to track completion.

## Package Contents

| Path | Purpose |
| --- | --- |
| [PRODUCTION_MASTER.md](PRODUCTION_MASTER.md) | Primary shot table with frame ranges, required inputs, priorities, and acceptance criteria. |
| [ANIMATOR_BRIEF.md](ANIMATOR_BRIEF.md) | Full creative brief for characters, acting, locations, atmosphere, and cultural handling. |
| [SHOT_REFERENCE.md](SHOT_REFERENCE.md) | Fast timing lookup, critical beats, camera movement guide, and continuity checklist. |
| [PROMPTS.md](PROMPTS.md) | Shot-specific AI video prompts and style/negative prompt blocks. |
| [COLOR_PALETTE.md](COLOR_PALETTE.md) | Exact act palettes, lighting temperatures, and implementation notes. |
| [TODOS.md](TODOS.md) | Current production task list and generation order. |
| [AI_PROMPT_LOG.md](AI_PROMPT_LOG.md) | Log for AI generation attempts and prompt outcomes. |
| [animatic_frames/](animatic_frames/) | SVG control frames for the 17-shot animatic. |
| [character_sheets/](character_sheets/) | Character identity/control references. |
| [environment_sheets/](environment_sheets/) | Environment references for chamber, alley, and courtyard. |
| [animatic_output/](animatic_output/) | Generated animatic outputs, EDL, and concat list. |
| [blender_setup.py](blender_setup.py) | Blender setup script for markers, lighting rigs, references, and scene prep. |
| [assemble_animatic.py](assemble_animatic.py) | Script for assembling animatic media. |
| [generate_png_frames.py](generate_png_frames.py) | Script for converting/generating frame assets. |
| [export_edl.py](export_edl.py) | Script for editorial export. |

## Director Review

The project has a strong emotional spine: sacred intimacy, rupture, penance, and rebirth. The recurring lotus/game token is the right cinematic anchor because it gives the audience something physical to track through an otherwise spiritual story. The best version of the film will keep every shot tied either to the King's inner transformation, Taleju's changing presence, or the token's symbolic passage into the Kumari.

### Highest-Impact Improvements

1. Clarify Shot 4 across all documents. [PRODUCTION_MASTER.md](PRODUCTION_MASTER.md) lists Shot 4 as the Queen's witness, while [SHOT_REFERENCE.md](SHOT_REFERENCE.md) describes it as King and Taleju close-up. Keep Shot 4 as the Queen; she is important because she externalizes the forbidden witnessing of the sacred relationship.
2. Fix the music cue frame math in [SHOT_REFERENCE.md](SHOT_REFERENCE.md). The critical beat table appears to list seconds in the Frame column for several cues, while the rest of the package uses true 24 fps frame numbers. For example, 1:13 should land around frame 1752/1753, not frame 31.
3. Add one explicit aftermath beat between Taleju's vanishing and the rain transition. There is a 20-second emotional space from 2:20 to 2:40 that should not feel like dead air. Use the empty board, the King's hand suspended in disbelief, and the room cooling into silence.
4. Give the Queen a clear emotional function. She should not read as jealous or merely curious. Her face should say: she understands the sacredness before the King does, and she sees the instant it is broken.
5. Make Shot 6 less melodramatic and more frighteningly small. The most powerful version is not a villain turn; it is a tiny human failure made cosmic. A tightening hand, a shifted breath, a single fallen hair strand, and a metallic eye glint are enough.
6. Make the Kumari entrance quieter than expected. Shot 15 should not feel like a triumphant reveal. It should feel like dawn deciding to enter the frame. Keep the child physically small against architecture and let the token's light carry the recognition.
7. Protect the token continuity. The token should be visible or emotionally implied in Shots 3, 8, 12/13, 15, and 17. It is the audience's thread through loss and renewal.
8. Separate Taleju's glow from the child's glow. Taleju can have liquid, caustic, divine light. The child should have gentler dawn radiance, less supernatural spectacle, and more quiet gravity.
9. Use stillness as a production advantage. Shots 12, 13, 14, and 17 do not need heavy movement; they need breath, rain, incense, and micro-expression. This will improve both production feasibility and emotional clarity.
10. Schedule a cultural review before final rendering. The brief is respectful, but the subject deserves a Newar/Nepalese cultural review for architecture, costume, ornament names, child depiction, and the balance between mythic symbolism and lived tradition.

### Story Notes

Act 1 works best if the sacred chamber feels like an inner sanctum, not a palace romance. Avoid romantic visual language that could make Taleju look like a love interest. Frame the intimacy as devotion becoming confused by human desire.

Act 2 should pivot on shame more than aggression. The King's reaching gesture can be dangerous, but the emotional center is his immediate recognition that something sacred has been lost because of him.

Act 3 needs one recurring visual grammar: rain falling vertically, lamp flame trembling, the empty board unmoving. That contrast will make his penance legible without adding exposition.

Act 4 should resolve without overexplaining. The child holding the token is the answer. The King's job is to understand, lower himself, and accept the new form of divine presence.

### Shot Priorities From A Director's View

| Priority | Shots | Direction |
| --- | --- | --- |
| Must perfect | 5, 6, 8, 15, 17 | These carry the film's emotional argument. Regenerate until the acting and symbolic clarity are right. |
| Must be coherent | 1, 4, 10, 14, 16 | These orient the audience and protect tone. They can be visually simpler but must read instantly. |
| Can simplify | 2, 3, 7, 9, 11, 12, 13 | Use slow motion, held frames, atmospheric loops, and strong compositions if schedule is tight. |

## Current Production Order

The next best generation order is:

1. Shot 4: Queen's Witness, to lock the witness perspective and lattice-light visual language.
2. Shot 5: Intimacy Peak, to lock King/Taleju facial identity and divine light.
3. Shot 6: Transgression, to test the live warm-to-cold lighting transition.
4. Shot 8: Vanishing, to solve the hardest VFX and token continuity beat.
5. Shot 15: Kumari Appears, to lock the rebirth image and child depiction.
6. Shot 17: Epilogue, to verify the final emotional stillness.

## Technical Workflow

1. Generate or approve Shot 1 and save the strongest frame as `STYLE_ANCHOR.png`.
2. For each shot, use the matching SVG from [animatic_frames/](animatic_frames/) as the control/depth/canny reference.
3. For face shots, add the matching identity reference from [character_sheets/](character_sheets/).
4. Use the shared style block and negative prompt from [PROMPTS.md](PROMPTS.md).
5. Log each generation attempt in [AI_PROMPT_LOG.md](AI_PROMPT_LOG.md).
6. Assemble generated clips to the frame ranges in [PRODUCTION_MASTER.md](PRODUCTION_MASTER.md).
7. Perform the final music-sync check against the critical beats in [SHOT_REFERENCE.md](SHOT_REFERENCE.md), after correcting the frame math.

## Quality Checklist

- [ ] Shot 4 clearly shows the Queen's sympathetic witness role.
- [ ] Shot 5 feels sacred and intimate without sexualizing Taleju.
- [ ] Shot 6 lighting changes live from warm to cold, not by hard cut.
- [ ] Shot 8 includes upward dissolution and physically weighted token motion.
- [ ] Act 3 maintains rain, lamp, empty board, and penitent body language.
- [ ] Shot 15 presents the child respectfully, with ritual stillness and no theatrical bounce.
- [ ] Shot 17 lands on peace, not spectacle.
- [ ] King identity remains consistent between Acts 1, 3, and 4.
- [ ] Taleju and Kumari light signatures are visually distinct.
- [ ] Cultural review is completed before final export.

## Export Targets

| Target | Setting |
| --- | --- |
| Master | ProRes or DNxHD/DNxHR, 1920 x 1080, 24 fps |
| Delivery | H.264 MP4, 1920 x 1080, 24 fps |
| Audio | AAC for delivery, WAV/PCM for master where possible |
| Color | Rec. 709 |
| Suggested bitrate | 15-20 Mbps for YouTube 1080p |

## Final Note

Treat the AI generator as the animator, but direct every shot like a performance. The film should never feel like a sequence of pretty mythic images; it should feel like one human mistake, one divine withdrawal, and one humble restoration.
