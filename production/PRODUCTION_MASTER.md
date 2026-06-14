# The King's Regret — Production Master Sheet

This document is the **Single Source of Truth** for the AI Video Generation phase. It merges timing, assets, and technical requirements into one actionable table.

---

## 🛠️ Global Production Settings
*   **Resolution:** 1920×1080 (Full HD)
*   **Frame Rate:** 24 fps
*   **Style Anchor:** `STYLE_ANCHOR.png` (Generate from Shot 1 first)
*   **Character Reference Source:** Use `REALITY_REFERENCE.md`, `CHARACTER_REFERENCE_REVIEW.md`, and approved bitmap references. Do not use deleted SVG character sheets.
*   **Total Frames:** 7200 (300 seconds)

---

## 📊 The Master Production Table

| Shot | Priority | Frames (Start-End) | Scene & Key Action | Required Inputs (Control / Identity / Style) | Acceptance Criteria (Definition of Done) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | **SHOULD** | 1 – 120 | **Sacred Chamber:** Establish wide room. | **C:** `shot01.svg` / **E:** `sacred_chamber.svg` | No flickering in brick textures; smoke is volumetric/ethereal. |
| **02** | **COULD** | 121 – 360 | **Dolly to Table:** Enter sacred space. | **C:** `shot02.svg` / **S:** `STYLE_ANCHOR.png` | Smooth push-in; pillars don't "warp" as they exit frame. |
| **03** | **COULD** | 361 – 720 | **Hands & Token:** Close action on board. | **C:** `shot03.svg` / **I:** written King + Taleju refs; approved bitmap refs TBD | Hands look human (5 fingers); token has a physical "weight." |
| **04** | **SHOULD** | 721 – 1200 | **Queen's Witness:** Peeking through lattice. | **C:** `shot04.svg` / **I:** written Queen ref; approved bitmap ref TBD / **S:** `STYLE_ANCHOR.png` | Lattice cast geometric shadows on face; eyes show longing. |
| **05** | **MUST** | 1201 – 1752 | **Intimacy Peak:** Eyes meeting close-up. | **C:** `shot05.svg` / **I:** written King + Taleju refs; approved bitmap refs TBD | Sub-surface scattering on skin; liquid light ripples on faces. |
| **06** | **MUST** | 1753 – 2400 | **The Transgression:** Cold shift / Desire. | **C:** `shot06.svg` / **I:** written King ref; approved bitmap ref TBD | **CRITICAL:** Lighting shift must be a live transition, not a cut. |
| **07** | **COULD** | 2401 – 2712 | **Confrontation:** Reaching and recoiling. | **C:** `shot07.svg` / **I:** written King + Taleju refs; approved bitmap refs TBD | Taleju's movement is graceful even in fear; King looks obsessed. |
| **08** | **MUST** | 2713 – 3336 | **The Vanishing:** Dissolve / Token falls. | **C:** `shot08.svg` / **I:** written Taleju ref; approved bitmap ref TBD | Dissolve is upward particles; token roll has realistic physics. |
| **09** | **COULD** | 3337 – 3840 | **Memory:** Flashback to smile. | **C:** `shot09.svg` / **I:** written Taleju ref; approved bitmap ref TBD | Soft-focus bloom; saturation matches Act 1 warmth. |
| **10** | **SHOULD** | 3841 – 4320 | **Rain Transition:** King walks in rain. | **C:** `shot10.svg` / **E:** `rain_alley.svg` / **I:** written King ref; approved bitmap ref TBD | Rain looks like streaks, not noise; King's robes look damp. |
| **11** | **COULD** | 4321 – 4680 | **Dream Taleju:** Silhouette in mist. | **C:** `shot11.svg` / **I:** written Taleju ref; approved bitmap ref TBD | Rain passes THROUGH the translucent silhouette. |
| **12** | **COULD** | 4681 – 5016 | **Penance:** Stilled meditation. | **C:** `shot12.svg` / **E:** `dawn_courtyard.svg` (Dark) | King looks emaciated/strained; breathing is slow and shallow. |
| **13** | **COULD** | 5017 – 5712 | **Montage:** Candles / Empty board. | **C:** `shot13.svg` | Stable frames; candle flame has realistic flickering/glow. |
| **14** | **SHOULD** | 5713 – 6024 | **Dream Peak:** instruction / Tear. | **C:** `shot14.svg` / **I:** written King ref; approved bitmap ref TBD | Expression shift from pain to peace; single tear is visible. |
| **15** | **MUST** | 6025 – 6720 | **Kumari Appears:** Reveal of infant. | **C:** `shot15.svg` / **I:** written Kumari ref; approved bitmap ref TBD / **E:** `dawn_courtyard.svg` | Infant carried or resting; extreme stillness; token on chest. |
| **16** | **COULD** | 6721 – 7080 | **People Bow:** Collective reverence. | **C:** `shot16.svg` / **S:** `STYLE_ANCHOR.png` | Silhouettes are distinct; movement is slow and deep. |
| **17** | **SHOULD** | 7081 – 7200 | **Epilogue:** Token at rest. | **C:** `shot17.svg` | Profound sense of stillness; dawn light is clean and airy. |

---

## 🚦 Priority Key (MoSCoW)
*   **MUST:** Mission critical. Needs multiple AI passes to perfect. Highest consistency requirement.
*   **SHOULD:** Important for story flow. Needs good character acting.
*   **COULD:** Can be simplified. Stills with light motion or simple loops are acceptable if behind schedule.

## 📝 Usage for Technical Director
1.  **Reference Input:** Always use the `.svg` from `animatic_frames/` as a **Canny** or **Depth** control map.
2.  **Character Lock:** For every shot with a face, upload the relevant `.svg` from `character_sheets/` to the **Identity Reference** slot.
3.  **Style Lock:** Once Shot 01 is generated and approved, save it as `STYLE_ANCHOR.png` and use it as a **Style Reference** for all remaining shots.
