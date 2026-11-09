# The King's Regret — Production Master Sheet

This document is the **Single Source of Truth** for the AI Video Generation phase. It merges timing, assets, and technical requirements into one actionable table.

---

## 🛠️ Global Production Settings
*   **Resolution:** 1920×1080 (Full HD)
*   **Frame Rate:** 24 fps
*   **Style Anchor:** `STYLE_ANCHOR.png` (Generate from Shot 1 first)
*   **Character Reference Source:** Use `REALITY_REFERENCE.md` and `CHARACTER_IMAGE_PROMPTS.md` to generate or source approved bitmap character references. Save `3:4` master paintings to `character_sheets/approved/` and use the pre-built `2560×1440` (`16:9`) First-Frame plates in `character_sheets/approved/16x9/` for Dreamina Video.
*   **Total Frames:** 7200 (300 seconds)

---

## 📊 The Master Production Table

| Shot | Priority | Frames (Start-End) | Scene & Key Action | Required Inputs (`approved/16x9/` First Frame) | Acceptance Criteria (Definition of Done) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | **MUST** | 1 – 192 | **The Waiting King:** Inside the hushed candlelit palace sanctum at midnight, the King sits alone on his throne in quiet, reverent longing as warm golden divine light begins to enter from the right. | **I:** `16x9/king_act1_court.png` (First-Frame animate) | 100% face consistency; slow push-in; warm lamp flicker; incoming golden light on right side of face; no new wall medallions. |
| **02** | **MUST** | 193 – 432 | **The Goddess Appears:** Wide two-shot inside the candlelit chamber as Goddess Taleju is revealed enthroned in crimson and gold opposite the humble King. | **I:** `16x9/taleju_act1_front.png` (First-Frame animate) | Smooth slow push-in; golden aura shimmer and flickering oil lamps; no extra objects appearing. |
| **03** | **MUST** | 433 – 720 | **The Excuse of the Game / One-Sided Devotion:** Reverse angle on the King behind the low *tripasa* table; his hand rests near the dice as a pretext while his eyes are fixed 100% on Taleju in spellbound adoration. | **I:** `16x9/king_act1_board.png` (First-Frame animate) | Single-frame animation prevents table pop-in; his gaze stays locked on her radiant presence. |
| **04** | **MUST** | 721 – 1200 | **The Intoxication of the King's Heart:** Slow, hypnotic close-up push-in on Taleju's serene divine face and third eye as the King's devotion quietly clouds into mortal fascination and desire. | **I:** `16x9/taleju_act1_enthroned.png` (First-Frame animate) | Mesmerizing slow push-in on `16x9/taleju_act1_enthroned.png`; warm 2700K lamp light and golden dust motes. |
| **05** | **MUST** | 1201 – 1752 | **Intimacy Peak (5A/5B/5C):** Alternating ECUs — King's gaze, Taleju's gaze, hands hovering near token. | **I:** `16x9/king_act1_court.png` + `16x9/taleju_act1_enthroned.png` + `16x9/king_act1_board.png` | Both faces are warm human skin; Taleju's divinity is a gold nimbus and rim-light *around* her (gold-leaf washes), not glowing flesh; hands do not touch. |
| **06** | **MUST** | 1753 – 2400 | **The Breaking (6A/6B/6C):** Devotion overflows into mortal desire (loose hair strand) → Taleju's eyes read the shift in his heart → King reaches & lamps gutter into cold blue. | **I:** `16x9/king_act1_court.png` + `16x9/taleju_act1_enthroned.png` + `16x9/king_act2_reach.png` | **CRITICAL:** 6A holds Act 1 warm gold while his gaze clouds with desire; Taleju reads his heart in 6B; palette drains to 8000K slate-blue as he reaches in 6C. |
| **07** | **COULD** | 2401 – 2712 | **Confrontation:** Reaching and recoiling in cold gloom. | **I:** `16x9/taleju_act2_recede.png` + `16x9/king_act2_reach.png` | Taleju's withdrawal is wounded sacred authority, not anger; room now in cold 8000K slate-blue shadow. |
| **08** | **MUST** | 2713 – 3336 | **The Vanishing:** Dissolve / Token falls / King lunges and misses. | **I:** `16x9/taleju_act2_recede.png` (8A) + `16x9/king_act2_reach_2.png` (8B) | Dissolve is upward painted gold particles; token rolls into shadow and King's hand misses on empty air. |
| **09** | **COULD** | 3337 – 3840 | **Aftermath & Memory (9A/9B):** Empty chamber in cold silence → brief golden flashback of Taleju. | **I:** `16x9/shot01_empty_chamber.png` + `16x9/taleju_act1_enthroned.png` | 9A holds the cold empty chamber first; 9B blooms briefly in Act 1 warmth. |
| **10** | **SHOULD** | 3841 – 4320 | **The Vigil Begins:** Stripped of crown and gold in simple cotton robes, the King stands barefoot on his misty palace terrace praying in *namaskar* toward Taleju's temple. | **I:** `16x9/king_act3_prayer.png` | Reads as dignified penance and heartbreak (no game board); cream cotton robes; hands in prayer toward the distant temple; misty dawn. |
| **11** | **COULD** | 4321 – 4680 | **Dream Taleju:** Translucent silhouette in mist above the terrace watching his penance. | **I:** `16x9/taleju_act3_silhouette.png` | Dawn mist passes THROUGH the translucent silhouette. |
| **12** | **COULD** | 4681 – 5016 | **Depth of Penance:** Stilled vigil before flickering prayer *diyas* on the cold stone parapet. | **I:** `16x9/king_act3_prayer.png` | King humbled and dignified (not emaciated); grief in his bearing; hands pressed in prayer, eyes lifted toward the temple. |
| **13** | **COULD** | 5017 – 5712 | **Montage (13A/13B/13C):** Flickering prayer *diyas* / Silent locked Taleju Temple in mist / Incense & King bowing into exhausted sleep. | **I:** `16x9/STYLE_ANCHOR1.png` + `16x9/taleju_act3_silhouette.png` + `16x9/king_act3_prayer.png` | Stable frames; painted candle flame flickers with a warm gold-leaf glow; transitions smoothly into dream. |
| **14** | **SHOULD** | 5713 – 6024 | **The Instruction / Dream Peak (14A/14B):** Taleju's offering gesture (child height) → King's tear of acceptance. | **I:** `16x9/taleju_act3_instruction.png` + `16x9/king_act3_prayer.png` | 14A clearly reads as Taleju's silent instruction (finger to lips, lowered offering palm); 14B shows King's shift from pain to peace with a single tear. |
| **15** | **MUST** | 6025 – 6720 | **Kumari Appears (15A/15B):** 15A carried entrance across white cloth; 15B resting still on cushion with token on chest. | **I:** `16x9/kumari_entrance.png` (15A) + `16x9/kumari_cushion.png` (15B) | Infant carried (15A) and resting on cushion (15B) — never walking; extreme stillness; token placed on chest (not gripped). |
| **16** | **MUST** | 6721 – 7080 | **The Founding (true climax):** people accept the child as the living goddess; King in simple shawl lowers himself among them. | **I:** `16x9/kumari_cushion.png` + `16x9/king_act3_prayer.png` | Reads as a *tradition being born*, not just a crowd bowing; King is clearly among/below the people in humble cotton shawl; movement slow and deep. |
| **17** | **SHOULD** | 7081 – 7200 | **Coda:** Token at rest with the child in clean dawn light. | **I:** `16x9/kumari_portrait.png` / `16x9/kumari_cushion.png` | Reads as coda, not climax; lotus token rests peacefully on the child's crimson brocade/cushion; profound stillness; dawn light clean and airy. |

---

## 🚦 Priority Key (MoSCoW)
*   **MUST:** Mission critical. Needs multiple AI passes to perfect. Highest consistency requirement.
*   **SHOULD:** Important for story flow. Needs good character acting.
*   **COULD:** Can be simplified. Stills with light motion or simple loops are acceptable if behind schedule.

## 📝 Usage
1.  **Character Lock:** For every shot with a face, upload the relevant approved **bitmap** portrait from `character_sheets/approved/` (generated via `CHARACTER_IMAGE_PROMPTS.md`) to the **Identity / Reference Image** slot of your video tool.
2.  **Style Lock:** Once Shot 01 is generated and approved, save it as `STYLE_ANCHOR.png` and use it as a **Style Reference** for all remaining shots.
3.  **Environment:** The `E:` column names the setting for the shot. Describe that space in your prompt using the environment details in [ANIMATOR_BRIEF.md](ANIMATOR_BRIEF.md) and the act palette in [COLOR_PALETTE.md](COLOR_PALETTE.md) — the painted keyframe defines the environment; there are no separate sketch files to upload.
