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
| **05** | **MUST** | 1201 – 1752 | **Intimacy Peak:** Eyes meeting close-up. | **I:** written King + Taleju refs; approved bitmap refs TBD | Painted inner glow on the faces; Taleju's divine light rendered as flat radiant gold-leaf washes, not photoreal skin. |
| **06** | **MUST** | 1753 – 2400 | **The Transgression:** Cold shift / Desire. | **I:** written King ref; approved bitmap ref TBD | **CRITICAL:** Lighting shift must be a live transition, not a cut. |
| **07** | **COULD** | 2401 – 2712 | **Confrontation:** Reaching and recoiling. | **I:** written King + Taleju refs; approved bitmap refs TBD | Taleju's movement is graceful even in fear; King looks obsessed. |
| **08** | **MUST** | 2713 – 3336 | **The Vanishing:** Dissolve / Token falls. | **I:** written Taleju ref; approved bitmap ref TBD | Dissolve is upward painted gold particles; token roll reads with believable weight. |
| **09** | **COULD** | 3337 – 3840 | **Memory:** Flashback to smile. | **I:** written Taleju ref; approved bitmap ref TBD | Soft-focus bloom; saturation matches Act 1 warmth. |
| **10** | **SHOULD** | 3841 – 4320 | **The Vigil Begins:** King carries the board to his palace terrace at dawn and prays toward Taleju's temple. | **E:** Palace terrace overlooking Taleju temple (describe in prompt) / **I:** written King ref; approved bitmap ref TBD | Reads as dignified penance, not a beggar; hands in prayer toward the distant temple; misty dawn. |
| **11** | **COULD** | 4321 – 4680 | **Dream Taleju:** Silhouette in mist. | **I:** written Taleju ref; approved bitmap ref TBD | Dawn mist passes THROUGH the translucent silhouette. |
| **12** | **COULD** | 4681 – 5016 | **Penance:** Stilled vigil at the board. | **E:** Palace terrace at misty dawn (describe in prompt) | King humbled and dignified (not emaciated); grief in his bearing; one hand cupping the token's empty place, eyes toward the temple. |
| **13** | **COULD** | 5017 – 5712 | **Montage:** Candles / Empty board. | **S:** `STYLE_ANCHOR.png` | Stable frames; painted candle flame flickers with a warm gold-leaf glow. |
| **14** | **SHOULD** | 5713 – 6024 | **Dream Peak:** instruction / Tear. | **I:** written King ref; approved bitmap ref TBD | Expression shift from pain to peace; single tear is visible. |
| **15** | **MUST** | 6025 – 6720 | **Kumari Appears:** Reveal of infant. | **I:** written Kumari ref; approved bitmap ref TBD / **E:** Dawn Courtyard (describe in prompt) | Infant carried or resting; extreme stillness; token on chest. |
| **16** | **MUST** | 6721 – 7080 | **The Founding (true climax):** people accept the child as the living goddess; King lowers himself among them. | **S:** `STYLE_ANCHOR.png` | Reads as a *tradition being born*, not just a crowd bowing; King is clearly among/below the people; silhouettes distinct; movement slow and deep. |
| **17** | **SHOULD** | 7081 – 7200 | **Coda:** Token at rest with the child. | **S:** `STYLE_ANCHOR.png` | Reads as coda, not climax; profound stillness; dawn light clean and airy. |

---

## 🚦 Priority Key (MoSCoW)
*   **MUST:** Mission critical. Needs multiple AI passes to perfect. Highest consistency requirement.
*   **SHOULD:** Important for story flow. Needs good character acting.
*   **COULD:** Can be simplified. Stills with light motion or simple loops are acceptable if behind schedule.

## 📝 Usage
1.  **Character Lock:** For every shot with a face, upload the relevant approved **bitmap** portrait from `character_sheets/approved/` (generated via `CHARACTER_IMAGE_PROMPTS.md`) to the **Identity / Reference Image** slot of your video tool.
2.  **Style Lock:** Once Shot 01 is generated and approved, save it as `STYLE_ANCHOR.png` and use it as a **Style Reference** for all remaining shots.
3.  **Environment:** The `E:` column names the setting for the shot. Describe that space in your prompt using the environment details in [ANIMATOR_BRIEF.md](ANIMATOR_BRIEF.md) and the act palette in [COLOR_PALETTE.md](COLOR_PALETTE.md) — the painted keyframe defines the environment; there are no separate sketch files to upload.
