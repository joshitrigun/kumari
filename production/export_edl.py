"""
export_edl.py
Exports a CMX3600 EDL for DaVinci Resolve.
Imports as a 5:00 timeline with all 17 shots correctly positioned at 24fps.

Usage:
    python3 export_edl.py

Output: animatic_output/kings_regret_animatic.edl

In DaVinci Resolve:
    File > Import Timeline > Import AAF, EDL, XML...
    Select the .edl file, set frame rate to 24fps.
"""

import os

PRODUCTION_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(PRODUCTION_DIR, "animatic_output")
EDL_PATH = os.path.join(OUTPUT_DIR, "kings_regret_animatic.edl")

FPS = 24

SHOTS = [
    ("shot01", "Shot 01 – Sacred Chamber establish",    1,    120),
    ("shot02", "Shot 02 – Dolly to game table",        121,    360),
    ("shot03", "Shot 03 – Hands on game pieces",       361,    720),
    ("shot04", "Shot 04 - Queen witnesses sacred fracture", 721, 1200),
    ("shot05", "Shot 05 – Eyes meeting (ACT 1 PEAK)", 1201,   1752),
    ("shot06", "Shot 06 – Lighting shift (TRANSGRESS)",1753,  2400),
    ("shot07", "Shot 07 – He reaches, she recoils",   2401,   2712),
    ("shot08", "Shot 08 – Vanishing + token falls",   2713,   3336),
    ("shot09", "Shot 09 – Flashback: her smile",      3337,   3840),
    ("shot10", "Shot 10 – King walks in rain",        3841,   4320),
    ("shot11", "Shot 11 – Dream: Taleju in mist",     4321,   4680),
    ("shot12", "Shot 12 – King meditates",            4681,   5016),
    ("shot13", "Shot 13 – Montage: candles/incense",  5017,   5712),
    ("shot14", "Shot 14 – Dream peak: instruction",   5713,   6024),
    ("shot15", "Shot 15 – Kumari appears (ACT 4)",    6025,   6720),
    ("shot16", "Shot 16 – People bow",                6721,   7080),
    ("shot17", "Shot 17 – Epilogue: token, peace",    7081,   7200),
]


def frames_to_tc(frame_number, fps=FPS):
    """Convert absolute frame number (1-indexed) to SMPTE timecode string HH:MM:SS:FF."""
    f = frame_number - 1  # convert to 0-indexed
    ff = f % fps
    total_seconds = f // fps
    ss = total_seconds % 60
    mm = (total_seconds // 60) % 60
    hh = total_seconds // 3600
    return f"{hh:02d}:{mm:02d}:{ss:02d}:{ff:02d}"


def duration_tc(dur_frames, fps=FPS):
    """Convert a frame count to a timecode duration string."""
    ff = dur_frames % fps
    total_seconds = dur_frames // fps
    ss = total_seconds % 60
    mm = (total_seconds // 60) % 60
    hh = total_seconds // 3600
    return f"{hh:02d}:{mm:02d}:{ss:02d}:{ff:02d}"


def build_edl():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    lines = []
    lines.append("TITLE: The King's Regret – Animatic")
    lines.append("FCM: NON-DROP FRAME")
    lines.append("")

    for i, (reel, label, start_f, end_f) in enumerate(SHOTS, start=1):
        dur_frames = end_f - start_f + 1

        # Source: each still image, in/out is 00:00:00:00 to its duration
        src_in  = "00:00:00:00"
        src_out = duration_tc(dur_frames)

        # Record: where this shot sits in the master timeline
        rec_in  = frames_to_tc(start_f)
        rec_out = frames_to_tc(end_f + 1)

        lines.append(f"{i:03d}  {reel:<10}  V     C        {src_in} {src_out} {rec_in} {rec_out}")
        lines.append(f"* FROM CLIP NAME: {reel}.png")
        lines.append(f"* COMMENT: {label}")
        lines.append("")

    content = "\n".join(lines)
    with open(EDL_PATH, "w") as f:
        f.write(content)
    return content


def main():
    print("=== The King's Regret — EDL Exporter ===\n")
    content = build_edl()

    print(f"EDL written: {EDL_PATH}")
    print(f"Shots: {len(SHOTS)}")
    print(f"Timeline: 00:00:00:00 – {frames_to_tc(7201)}")
    print()
    print("--- Preview (first 3 edits) ---")
    for line in content.split("\n")[:15]:
        print(line)
    print("...")
    print()
    print("--- Import in DaVinci Resolve ---")
    print("  File > Import Timeline > Import AAF, EDL, XML...")
    print(f"  File: {EDL_PATH}")
    print("  Frame Rate: 24fps")
    print("  After import: link each clip to its animatic PNG from animatic_frames/")
    print("  Then drop your music file onto a new audio track and sync.")


if __name__ == "__main__":
    main()
