# Character Reference Review

Date: 2026-06-14

## Decision

The four SVG character sheets were removed:

- `character_sheets/king.svg`
- `character_sheets/queen.svg`
- `character_sheets/taleju.svg`
- `character_sheets/kumari_child.svg`

Reason: the drawings were technically valid but visually wrong. They looked diagrammatic, cartoon-like, and closer to generic/Malaysian court fantasy than Nepali Newar/Malla visual culture. Keeping them would poison later AI image/video generations.

## Where Character Looks Are Currently Written

### 1. `REALITY_REFERENCE.md`

Status: strongest current source.

This file has the most grounded character direction. It correctly separates history, legend, personality, and visual guardrails.

What it covers well:

- Jayaprakash Malla as last Malla king of Kantipur: cultured, proud, politically embattled, finally humbled.
- Queen as Daya Lakshmi / symbolic witness: politically aware and spiritually perceptive, not jealous.
- Taleju as Malla royal tutelary goddess, tantric Durga / Tripura Sundari energy, not romantic partner.
- Kumari as living embodiment of Taleju: red/gold, topknot, agni-chakshu, stillness, protected framing.
- Strong guardrails against Malaysian, Thai, Balinese, generic princess, and generic fantasy silhouettes.

Recommendation:

Use this as the master character-look truth until proper visual references are generated or commissioned.

### 2. `ANIMATOR_BRIEF.md`

Status: useful but needs tightening.

The top `Character Descriptions` section contains the main production-facing look notes.

Currently useful:

- King: explicitly says Nepali/Newar Malla king and warns against Malaysian, Thai, or generic Southeast Asian silhouettes.
- King Act 1: mentions crossed upper wrap, patuka waist band, and dhaka-like trim.
- Queen: mentions Newar royal clothing inspired by haku patasi / patasi border language and warns against Malaysian palace styling.
- Kumari: notes hand-painted kohl, small scale, ritualistic glide, and reverent treatment.

Weak spots:

- Taleju is still too generic: `ethereal, glowing` is not enough. It should name her as Malla kuladevi / Taleju Bhawani / tantric Durga / Tripura Sundari.
- Kumari appearance is too general. It should explicitly include red/gold Kumari ceremonial attire, topknot, agni-chakshu/fire-eye, and feet-never-touch-ground visual logic.
- The shot table still has an older Shot 4 description as a King/Taleju two-shot, while other files now treat Shot 4 as Queen witness.

Recommendation:

Keep using this file, but update the Taleju, Kumari, and Shot 4 sections before generating final video.

### 3. `PROMPTS.md`

Status: usable for shot generation, but character descriptions need more cultural specificity.

Currently useful:

- Shot 4 gives a strong Queen reference: Newar Queen, ankhijhyal lattice, haku patasi / patasi border language, Bulaki/Nath, pote/tilhari feeling, no Malaysian costume/songket/Southeast Asian crown.
- Shot 6 warns against tengkolok/songkok for the King.
- Shot 15 warns against Malaysian tiara and generic princess crown for Kumari.

Weak spots:

- Shot 5 King/Taleju close-up is still generic. It says `regal Malla King` and `ethereal Goddess Taleju`, but does not lock Taleju as Malla kuladevi / tantric Durga / Tripura Sundari.
- Shot 7 says the King's face is `twisted with obsession`, which may push the model into villain melodrama. Better: proud devotional boundary collapsing into entitlement.
- Shot 9 says Taleju's eyes are full of `love and wisdom`. `Love` may accidentally romanticize the King/Taleju relationship. Better: compassion, blessing, divine counsel.
- Shot 15 should explicitly say Royal Kumari, Newar Shakya/Bajracharya tradition cue, red/gold ceremonial dress, topknot, agni-chakshu/fire-eye, composed stillness.

Recommendation:

Use `PROMPTS.md` for structure, but revise the character-specific shots before final generation.

### 4. `AI_PROMPT_LOG.md`

Status: historical log only. Do not use as current source of truth.

This file contains older prompt language. Some entries are useful for architecture and shot mood, but character guidance is inconsistent with the latest decisions.

Risks:

- Shot 4 still says `The Witness & The Gaze` and includes a King/Taleju two-shot with Queen in the background.
- Several Taleju lines can be read as romantic if used without the newer guardrails.
- Kumari description is less specific than the newer notes.

Recommendation:

Keep as prompt history, not final reference.

### 5. `ASSET_REVIEW.md`

Status: now partly outdated.

It documents prior SVG edits and redraw attempts. Because the SVGs have now been deleted, the file should be treated as review history, not current asset status.

Recommendation:

Update it to say the SVGs were removed after review and should not be used for visual reference.

### 6. `character_sheets/index.html`

Status: updated.

The page no longer embeds deleted SVGs. It now points to the written references and explains that the SVG character sheets were removed due to visual/cultural drift.

## Character-by-Character Current Look Direction

### King Jayaprakash Malla

Reliable direction:

- Middle-aged last Malla king of Kantipur.
- Strong jaw, slight beard, deep-set eyes, vermillion tika.
- Stiffly controlled court posture in Act 1.
- Nepali/Newar/Malla court attire, not generic royal robe.
- Crossed-front upper garment inspired by Newar tapalan / court jama logic.
- Patuka waist band, restrained gold jewelry, low structured Malla-era Nepali royal head ornament with red cloth and restrained gold edging.
- Act 2 crack: one loose hair strand, clenched hand, colder eyes.
- Act 3: crownless, wet grey cotton wrap, physically reduced.

Avoid:

- Malaysian tengkolok/songkok.
- Thai-style high crown.
- Generic fantasy king armor.
- Cartoon villain expression.
- Over-ornamented Southeast Asian palace robe.

### Queen / Daya Lakshmi Figure

Reliable direction:

- Politically aware Newar royal woman.
- Sacred witness, not jealous wife.
- Partly obscured through ankhijhyal lattice.
- Deep black/plum drape with red/gold border language inspired by haku patasi/patasi.
- Jewelry cues: Bulaki/Nath nose ornament, pote/tilhari feeling, heavy earrings, tikma-like hair/forehead ornament.
- Tear-line highlight, restrained kohl, awe and ache.

Avoid:

- Generic sari queen.
- Malaysian songket palace styling.
- Southeast Asian crown silhouette.
- Jealous or accusatory acting.
- Glamour pose.

### Taleju Bhawani

Reliable direction:

- Malla royal tutelary goddess / kuladevi.
- Tantric Durga / Tripura Sundari energy.
- Divine counsel, protection, boundary, legitimacy.
- Compassionate but sovereign.
- Yantra/triangular geometry as subtle sacred design language.
- Newar temple-devata-inspired cream/gold drapes.
- Luminous bindi and refined kohl; sacred, not decorative glamour.
- Recoil means wounded sacred boundary, not romantic rejection.

Avoid:

- Romantic goddess framing.
- Sexualized divine figure.
- Generic fantasy princess.
- Malaysian/Thai/Balinese costume shortcuts.
- Angry villain deity.

### Kumari Child

Reliable direction:

- Royal Kumari / living embodiment of Taleju.
- Young Newar girl, small against architecture.
- Red/gold ceremonial Kumari attire.
- Topknot and crown/hair ornament grounded in Kumari visual tradition.
- Agni-chakshu/fire-eye forehead makeup and hand-painted kohl.
- Composed, grave stillness; silence as power.
- Feet barely touch ground: glide or carried-presence visual logic.
- Dawn-like glow, restrained and protected.

Avoid:

- Cute princess.
- Horror child.
- Generic fantasy tiara.
- Malaysian costume.
- Superhero mask makeup.
- Adult glamour.

## Immediate Fixes Recommended

1. Update `ANIMATOR_BRIEF.md` Taleju description to include Malla kuladevi / tantric Durga / Tripura Sundari.
2. Update `ANIMATOR_BRIEF.md` Kumari description to include red/gold attire, topknot, agni-chakshu, stillness, and feet-not-touching-ground logic.
3. Fix the `ANIMATOR_BRIEF.md` shot table row for Shot 4 so it matches Queen witness.
4. Tighten `PROMPTS.md` Shot 5, Shot 7, Shot 9, and Shot 15 so they do not romanticize Taleju or under-specify Kumari.
5. Mark `ASSET_REVIEW.md` SVG redraw notes as removed/outdated.
6. Generate new visual references as bitmap paintings, not SVG diagrams.

## Stronger Look Source Added

Use `CHARACTER_LOOK_BIBLE.md` as the new source for character appearance prompts. It expands the weak visual descriptions into face, hair, costume, movement, light, image prompt, and negative prompt sections for each character.

The two later SVG study attempts were also removed because they were not acceptable visual references. The problem was both the drawing medium and the earlier looseness of the descriptions.

## Best Next Visual Reference Workflow

Do not redraw these characters manually in SVG unless the goal is only a schematic. For actual production art:

1. Use `CHARACTER_LOOK_BIBLE.md` and `REALITY_REFERENCE.md` as the master character brief.
2. Generate 3-5 painterly still references per character with AI image generation.
3. Reject anything that looks Malaysian, Thai, Balinese, generic princess, or fantasy royal.
4. Keep only the best one per character as the visual identity lock.
5. Save approved PNG/JPG references in `character_sheets/approved/`.
6. Use those approved images for video generation prompts and consistency references.
