# The King's Regret — Production Master Sheet

This document is the **Single Source of Truth** for the AI Video Generation phase. It merges timing, assets, and technical requirements into one actionable table.

---

## 🛠️ Global Production Settings
*   **Resolution:** 1920×1080 (Full HD)
*   **Frame Rate:** 24 fps
*   **Style Anchor:** `STYLE_ANCHOR.png` (Generate from Shot 1 first)
*   **Character Reference Source:** Use `REALITY_REFERENCE.md` and `CHARACTER_IMAGE_PROMPTS.md` to generate or source approved bitmap character references. Save to `character_sheets/approved/`.
*   **Total Frames:** 7200 (300 seconds)

---

## 📊 The Master Production Table

| Shot | Priority | Frames (Start-End) | Scene & Key Action | Required Inputs (Identity / Environment / Style) | Acceptance Criteria (Definition of Done) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | **SHOULD** | 1 – 120 | **Sacred Chamber:** Establish wide room. | **E:** Sacred Chamber (describe in prompt) | No flickering in painted brick; incense smoke reads as flowing ethereal painted ribbons. |
| **02** | **COULD** | 121 – 360 | **Dolly to Table:** Enter sacred space. | **S:** `STYLE_ANCHOR.png` | Smooth push-in; pillars don't "warp" as they exit frame. |
| **03** | **COULD** | 361 – 720 | **Hands & Token:** Close action on board. | **I:** written King + Taleju refs; approved bitmap refs TBD | Painted hands are anatomically clean (5 fingers); token reads with painted "weight." |
| **04** | **SHOULD** | 721 – 1200 | **Queen's Witness:** Peeking through lattice. | **I:** written Queen ref; approved bitmap ref TBD / **S:** `STYLE_ANCHOR.png` | Lattice cast geometric shadows on face; eyes show longing. |
| **05** | **MUST** | 1201 – 1752 | **Intimacy Peak (5A/5B/5C):** Alternating ECUs — King's gaze, Taleju's gaze, hands hovering near token. | **I:** King Act 1 + Taleju Act 1 refs | Both faces are warm human skin; Taleju's divinity is a gold nimbus and rim-light *around* her (gold-leaf washes), not glowing flesh; hands do not touch. |
| **06** | **MUST** | 1753 – 2400 | **The Breaking (6A/6B/6C):** Warmth overflows into desire (loose hair strand) → Queen's lattice witness → King reaches & lamps gutter into cold blue. | **I:** King Act 2 + Queen lattice refs | **CRITICAL:** 6A holds Act 1 warm gold while his gaze overflows; Queen sees the rupture in 6B; palette drains to 8000K slate-blue as he reaches in 6C. |
| **07** | **COULD** | 2401 – 2712 | **Confrontation:** Reaching and recoiling in cold gloom. | **I:** King Act 2 + Taleju Act 2 refs | Taleju's withdrawal is wounded sacred authority, not anger; room now in cold 8000K slate-blue shadow. |
| **08** | **MUST** | 2713 – 3336 | **The Vanishing:** Dissolve / Token falls / King lunges and misses. | **I:** Taleju Act 2 + King Act 2 refs | Dissolve is upward painted gold particles; token rolls into shadow and King's hand misses on empty air. |
| **09** | **COULD** | 3337 – 3840 | **Aftermath & Memory (9A/9B):** Empty board in cold silence → brief golden flashback of Taleju. | **I:** King Act 2 + Taleju Act 1 refs | 9A holds the cold empty chaupar board and suspended hand first (no dead air); 9B blooms briefly in Act 1 warmth. |
| **10** | **SHOULD** | 3841 – 4320 | **The Vigil Begins:** King carries the chaupar board to his palace terrace at dawn and prays toward Taleju's temple. | **E:** Palace terrace overlooking Taleju temple (describe in prompt) / **I:** King Act 3 refs | Reads as dignified penance, not a beggar; cream cotton robes; hands in prayer toward the distant temple; misty dawn. |
| **11** | **COULD** | 4321 – 4680 | **Dream Taleju:** Silhouette in mist above the terrace. | **I:** Taleju Act 3 + King Act 3 refs | Dawn mist passes THROUGH the translucent silhouette. |
| **12** | **COULD** | 4681 – 5016 | **Penance:** Stilled vigil at the chaupar board. | **E:** Palace terrace at misty dawn / **I:** King Act 3 refs | King humbled and dignified (not emaciated); grief in his bearing; one hand cupping the token's empty place, eyes toward the temple. |
| **13** | **COULD** | 5017 – 5712 | **Montage (13A/13B/13C):** Flickering diyas / Empty chaupar board / Incense & King bowing into sleep. | **S:** `STYLE_ANCHOR.png` / **I:** King Act 3 refs | Stable frames; painted candle flame flickers with a warm gold-leaf glow; transitions smoothly into dream. |
| **14** | **SHOULD** | 5713 – 6024 | **The Instruction / Dream Peak (14A/14B):** Taleju's offering gesture (child height) → King's tear of acceptance. | **I:** Taleju Act 3 + King Act 3/4 refs | 14A clearly reads as Taleju's silent instruction (finger to lips, lowered offering palm); 14B shows King's shift from pain to peace with a single tear. |
| **15** | **MUST** | 6025 – 6720 | **Kumari Appears (15A/15B):** 15A carried entrance across white cloth; 15B resting still on cushion with token on chest. | **I:** Kumari refs / **E:** Dawn Courtyard (describe in prompt) | Infant carried (15A) and resting on cushion (15B) — never walking; extreme stillness; token placed on chest (not gripped). |
| **16** | **MUST** | 6721 – 7080 | **The Founding (true climax):** people accept the child as the living goddess; King in simple shawl lowers himself among them. | **I:** King Act 4 + Kumari refs / **S:** `STYLE_ANCHOR.png` | Reads as a *tradition being born*, not just a crowd bowing; King is clearly among/below the people in humble cotton shawl; movement slow and deep. |
| **17** | **SHOULD** | 7081 – 7200 | **Coda:** Token at rest with the child in clean dawn light. | **I:** Kumari refs / **S:** `STYLE_ANCHOR.png` | Reads as coda, not climax; lotus token rests peacefully on the child's crimson brocade/cushion; profound stillness; dawn light clean and airy. |

---

## 🚦 Priority Key (MoSCoW)
*   **MUST:** Mission critical. Needs multiple AI passes to perfect. Highest consistency requirement.
*   **SHOULD:** Important for story flow. Needs good character acting.
*   **COULD:** Can be simplified. Stills with light motion or simple loops are acceptable if behind schedule.

## 📝 Usage
1.  **Character Lock:** For every shot with a face, upload the relevant approved **bitmap** portrait from `character_sheets/approved/` (generated via `CHARACTER_IMAGE_PROMPTS.md`) to the **Identity / Reference Image** slot of your video tool.
2.  **Style Lock:** Once Shot 01 is generated and approved, save it as `STYLE_ANCHOR.png` and use it as a **Style Reference** for all remaining shots.
3.  **Environment:** The `E:` column names the setting for the shot. Describe that space in your prompt using the environment details in [ANIMATOR_BRIEF.md](ANIMATOR_BRIEF.md) and the act palette in [COLOR_PALETTE.md](COLOR_PALETTE.md) — the painted keyframe defines the environment; there are no separate sketch files to upload.
