# The King's Regret

Production package for a 5-minute music video inspired by the Kumari legend of King Jayaprakash Malla and Goddess Taleju. The package is built for a **prompt-based workflow**: you generate character reference images and then per-shot video clips using an AI video generator, and assemble the clips in any simple editor.

## Project Specs

| Item | Spec |
| --- | --- |
| Format | 5-minute music video |
| Duration | 5:00 / 300 seconds |
| Timeline | 7200 frames at 24 fps |
| Resolution | 1920 x 1080 |
| Visual style | **Photoreal historical** — looks like real live-action footage of 18th-century Kathmandu Valley, ethnographic documentary realism, shallow depth of field. **Not** animation/CGI. |
| Recommended tools | **Seedance 2.5** (BytePlus / Dreamina) as the single video generator + any basic video editor. *(Veo 3.1 held in reserve for Shot 6's live lighting transition if needed — see PROMPT_WORKFLOW.md.)* |
| Current stage | Prompts and character bible ready; character references and shots pending generation |

## Start Here (prompt-only workflow)

1. Read [PROMPT_WORKFLOW.md](PROMPT_WORKFLOW.md) — the beginner, start-to-finish guide for generating this film with prompts.
2. Read [ANIMATOR_BRIEF.md](ANIMATOR_BRIEF.md) for story, character arcs, environments, and performance notes.
3. Use [CHARACTER_IMAGE_PROMPTS.md](CHARACTER_IMAGE_PROMPTS.md) to generate your locked character reference images first.
4. Use [PRODUCTION_MASTER.md](PRODUCTION_MASTER.md) as the source of truth for shots, frames, inputs, priorities, and acceptance criteria.
5. Use [PROMPTS.md](PROMPTS.md) for the per-shot AI video generation prompts.
6. Use [REALITY_REFERENCE.md](REALITY_REFERENCE.md) and [CHARACTER_LOOK_BIBLE.md](CHARACTER_LOOK_BIBLE.md) for cultural accuracy and the guardrails behind the prompts.
7. Use [COLOR_PALETTE.md](COLOR_PALETTE.md) for act-by-act lighting and color grading.

## Package Contents

| Path | Purpose |
| --- | --- |
| [PROMPT_WORKFLOW.md](PROMPT_WORKFLOW.md) | Beginner, prompt-only, start-to-finish production guide. **Read this first.** |
| [PRODUCTION_MASTER.md](PRODUCTION_MASTER.md) | Primary shot table with frame ranges, required inputs, priorities, and acceptance criteria. |
| [ANIMATOR_BRIEF.md](ANIMATOR_BRIEF.md) | Full creative brief for characters, acting, locations, atmosphere, and cultural handling. |
| [PROMPTS.md](PROMPTS.md) | Shot-specific AI video prompts and shared style/negative prompt blocks. |
| [CHARACTER_IMAGE_PROMPTS.md](CHARACTER_IMAGE_PROMPTS.md) | Prompts for generating the character reference images. |
| [KING_REFERENCE_SET.md](KING_REFERENCE_SET.md) | Per-act reference-image set for the King (angles, lighting, naming) to feed Seedance's multi-reference identity lock. |
| [TALEJU_REFERENCE_SET.md](TALEJU_REFERENCE_SET.md) | Reference-image set for the goddess Taleju (counsel / withdrawal / dream), with grounded-light guardrails. |
| [QUEEN_REFERENCE_SET.md](QUEEN_REFERENCE_SET.md) | Reference-image set for the Queen (clear plate + lattice-framed witness variants). |
| [KUMARI_REFERENCE_SET.md](KUMARI_REFERENCE_SET.md) | Reference-image set for the newborn Kumari — reverent, still, token-placed; extra cultural-safety guardrails. |
| [CHARACTER_LOOK_BIBLE.md](CHARACTER_LOOK_BIBLE.md) | Detailed look and material bible for each character. |
| [REALITY_REFERENCE.md](REALITY_REFERENCE.md) | Historical/cultural notes and depiction guardrails. |
| [COLOR_PALETTE.md](COLOR_PALETTE.md) | Exact act palettes, lighting temperatures, and implementation notes. |
| [environment_sheets/](environment_sheets/) | Environment references for chamber, alley, and courtyard. |

## Director Review

The project has a strong emotional spine: sacred intimacy, rupture, penance, and rebirth. The recurring lotus/game token is the right cinematic anchor because it gives the audience something physical to track through an otherwise spiritual story. The best version of the film will keep every shot tied either to the King's inner transformation, Taleju's changing presence, or the token's symbolic passage into the Kumari.

### Highest-Impact Improvements

1. Keep Shot 4 as the **Queen's witness**. [PRODUCTION_MASTER.md](PRODUCTION_MASTER.md) and [PROMPTS.md](PROMPTS.md) treat Shot 4 as the Queen peering through the lattice; [ANIMATOR_BRIEF.md](ANIMATOR_BRIEF.md) should match that. She matters because she externalizes the forbidden witnessing of the sacred relationship.
2. Trust the frame math in [PRODUCTION_MASTER.md](PRODUCTION_MASTER.md) as canonical — true 24 fps frame numbers (e.g. 1:13 = frame 1752/1753). When syncing to music, convert timecodes to frames the same way.
3. Add one explicit aftermath beat between Taleju's vanishing and the rain transition. The ~20-second space around 2:19–2:40 should not feel like dead air. Use the empty board, the King's hand suspended in disbelief, and the room cooling into silence.
4. Give the Queen a clear emotional function. She should not read as jealous or merely curious. Her face should say: she understands the sacredness before the King does, and she sees the instant it is broken.
5. Make Shot 6 less melodramatic and more frighteningly small. The most powerful version is not a villain turn; it is a tiny human failure made cosmic. A tightening hand, a shifted breath, a single fallen hair strand, and a metallic eye glint are enough.
6. Make the Kumari entrance quieter than expected. Shot 15 should not feel like a triumphant reveal. It should feel like dawn deciding to enter the frame. Keep the newborn physically small against architecture and let the token's light carry the recognition. Save the emotional peak for Shot 16, where the **people accept the child as the living goddess** — that founding of a tradition is the film's true climax, not the King's private coda in Shot 17.
7. Protect the token continuity. The token should be visible or emotionally implied in Shots 3, 8, 12/13, 15, and 17. It is the audience's thread through loss and renewal.
8. Separate Taleju's glow from the child's glow. Taleju can have liquid, caustic, divine light. The child should have gentler dawn radiance, less supernatural spectacle, and more quiet gravity.
9. Use stillness as a production advantage. Shots 12, 13, 14, and 17 do not need heavy movement; they need breath, rain, incense, and micro-expression. In a prompt workflow this also generates far more reliably than complex motion.
10. Schedule a cultural review before final rendering. The package is respectful, but the subject deserves a Newar/Nepalese cultural review for architecture, costume, ornament names, child depiction, and the balance between mythic symbolism and lived tradition. Photoreal depiction raises this bar.

### Story Notes

Act 1 works best if the sacred chamber feels like an inner sanctum, not a palace romance. Avoid romantic visual language that could make Taleju look like a love interest. Frame the intimacy as devotion becoming confused by human desire.

Act 2 should pivot on shame more than aggression. The King's reaching gesture can be dangerous, but the emotional center is his immediate recognition that something sacred has been lost because of him.

Act 3 needs one recurring visual grammar: rain falling vertically, lamp flame trembling, the empty board unmoving. That contrast will make his penance legible without adding exposition.

Act 4 should resolve without overexplaining. The newborn Kumari holding/wearing the token is the answer. The King's job is to understand, lower himself, and accept the new form of divine presence.

### Shot Priorities From A Director's View

| Priority | Shots | Direction |
| --- | --- | --- |
| Must perfect | 5, 6, 8, 15, 16 | These carry the film's emotional argument. Shot 16 is the **true climax** (the founding of the tradition), not just a crowd shot. Regenerate until the acting and symbolic clarity are right. |
| Must be coherent | 1, 4, 10, 14, 17 | These orient the audience and protect tone. Shot 17 is the coda. They can be visually simpler but must read instantly. |
| Can simplify | 2, 3, 7, 9, 11, 12, 13 | Use slow motion, held frames, atmospheric loops, and strong compositions if schedule is tight. |

## Current Production Order

The next best generation order is:

1. Shot 4: Queen's Witness, to lock the witness perspective and lattice-light visual language.
2. Shot 5: Intimacy Peak, to lock King/Taleju facial identity and divine light.
3. Shot 6: Transgression, to test the live warm-to-cold lighting transition.
4. Shot 8: Vanishing, to solve the hardest VFX and token continuity beat.
5. Shot 15: Kumari Appears, to lock the rebirth image and newborn depiction.
6. Shot 16: The Founding, to lock the film's true climax — the people accepting the child as the living goddess.
7. Shot 17: Coda, to verify the final emotional stillness.

## Prompt Workflow (summary)

Full detail is in [PROMPT_WORKFLOW.md](PROMPT_WORKFLOW.md). In short:

1. Generate the character reference images from [CHARACTER_IMAGE_PROMPTS.md](CHARACTER_IMAGE_PROMPTS.md) and save the approved ones in `character_sheets/approved/`.
2. Generate or approve Shot 1 and save the strongest still frame as `STYLE_ANCHOR.png`.
3. For each shot, use the matching prompt from [PROMPTS.md](PROMPTS.md), including the shared STYLE BLOCK and NEGATIVE PROMPT.
4. For face shots, supply the matching character reference image as the tool's identity/reference input.
5. Keep a simple generation log (shot, prompt, tool, seed, result, what to improve).
6. Review each clip against the acceptance criteria in [PRODUCTION_MASTER.md](PRODUCTION_MASTER.md) and the frame durations there.
7. Assemble the clips in order and run the final music-sync check against the beats in [ANIMATOR_BRIEF.md](ANIMATOR_BRIEF.md).

## Quality Checklist

- [ ] Shot 4 clearly shows the Queen's sympathetic witness role.
- [ ] Shot 5 feels sacred and intimate without sexualizing Taleju.
- [ ] Shot 6 lighting changes live from warm to cold, not by hard cut.
- [ ] Shot 8 includes upward dissolution and physically weighted token motion.
- [ ] Act 3 maintains rain, lamp, empty board, and penitent body language.
- [ ] Shot 15 presents the newborn respectfully, with ritual stillness and no theatrical bounce.
- [ ] Shot 16 reads as a tradition being born (people accept the child as the living goddess; King lowers himself), not just a crowd bowing.
- [ ] Shot 17 lands on peace as a coda, not spectacle.
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

Treat the AI generator like an actor and cinematographer you are directing shot by shot. The film should never feel like a sequence of pretty mythic images; it should feel like one human mistake, one divine withdrawal, and one humble restoration.
