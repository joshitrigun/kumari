Quick steps to create the Blender animatic using `blender_setup.py` and the placeholder frames in `production/animatic_frames`.

1) Install Blender (if not installed)
   - Download from https://www.blender.org/download/

2) Open Blender and run the setup script
   - Open Blender
   - Switch to `Scripting` workspace
   - Open file: `production/blender_setup.py`
   - Press `Alt+P` to run the script
   - The script creates lighting rigs, color swatches, timeline markers, a camera, and a basic table reference

3) Import the placeholder storyboard frames as image empties (one per shot)
   - File > Import > Images as Planes (enable Add-on: `Import-Export: Import Images as Planes`)
   - Navigate to `production/animatic_frames`
   - Import each `shotXX.svg` or convert SVGs to PNGs if preferred
   - Position each plane in front of the camera at `Z=0` and scale to fill the frame

4) Place each image on the timeline matching `SHOT_REFERENCE.md` frame ranges
   - Select the image object, go to the Video Sequencer or the Object's animation properties
   - Insert keyframes for visibility or animate the plane's `hide_render` property across the start/end frames
   - Alternatively, use the Video Sequencer: Add > Image/Sequence and set start frame and length per shot

5) Import audio
   - Switch to the Video Sequencer
   - Add > Sound, select your song file (MP3/WAV)
   - Set the sequencer frame rate to 24fps (Scene Settings)

6) Sync and preview
   - Use the markers created by the script to check critical beats (ACT2_Transgression, ACT3_Penance, ACT4_Rebirth)
   - Play timeline and adjust shot durations if needed

7) Export a rough animatic
   - Render Properties: set `File Format` to `FFmpeg video`, `Container` MP4, `Codec` H.264
   - Output Properties: Resolution 1920x1080, 24fps, Frame Start 1, Frame End 7200 (or the range you want for the rough animatic)
   - Render > Render Animation (Ctrl+F12)

Notes
- The placeholder SVGs are simple visual markers; replace them with drawn storyboard frames or animatic sketches as you iterate.
- If Blender is slow for 7200 frames, render a lower-resolution range for review or render in segments.
- For straightforward animatic export, place images in the Video Sequencer rather than object planes.

Commands (if using Blender from terminal):

```bash
# Run Blender and execute the setup script (macOS/Linux)
blender --background --python production/blender_setup.py
```

