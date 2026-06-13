"""
assemble_animatic.py
Assembles the 17 animatic PNGs into a timed video (5:00 @ 24fps).
Each shot is held for its exact duration from SHOT_REFERENCE.md.

Output: animatic_output/animatic.mp4  (H.264, no audio — drop music in DaVinci Resolve)

Usage:
    python3 assemble_animatic.py

Requires: ffmpeg  (brew install ffmpeg)
"""

import os
import subprocess
import sys

PRODUCTION_DIR = os.path.dirname(os.path.abspath(__file__))
FRAMES_DIR = os.path.join(PRODUCTION_DIR, "animatic_frames")
OUTPUT_DIR = os.path.join(PRODUCTION_DIR, "animatic_output")
CONCAT_FILE = os.path.join(OUTPUT_DIR, "concat_list.txt")
OUTPUT_VIDEO = os.path.join(OUTPUT_DIR, "animatic.mp4")

# (shot_filename, start_frame, end_frame, duration_frames)
# Source: SHOT_REFERENCE.md — 24fps, 7200 total frames
SHOTS = [
    ("shot01.png",     1,    120,  120),   # 0:00–0:05   5s
    ("shot02.png",   121,    360,  240),   # 0:05–0:15  10s
    ("shot03.png",   361,    720,  360),   # 0:15–0:30  15s
    ("shot04.png",   721,   1200,  480),   # 0:30–0:50  20s
    ("shot05.png",  1201,   1752,  552),   # 0:50–1:13  23s
    ("shot06.png",  1753,   2400,  648),   # 1:13–1:40  27s
    ("shot07.png",  2401,   2712,  312),   # 1:40–1:53  13s
    ("shot08.png",  2713,   3336,  624),   # 1:53–2:19  26s
    ("shot09.png",  3337,   3840,  504),   # 2:19–2:40  21s
    ("shot10.png",  3841,   4320,  480),   # 2:40–3:00  20s
    ("shot11.png",  4321,   4680,  360),   # 3:00–3:15  15s
    ("shot12.png",  4681,   5016,  336),   # 3:15–3:29  14s
    ("shot13.png",  5017,   5712,  696),   # 3:29–3:58  29s
    ("shot14.png",  5713,   6024,  312),   # 3:58–4:11  13s
    ("shot15.png",  6025,   6720,  696),   # 4:11–4:40  29s
    ("shot16.png",  6721,   7080,  360),   # 4:40–4:55  15s
    ("shot17.png",  7081,   7200,  120),   # 4:55–5:00   5s
]

FPS = 24


def check_ffmpeg():
    try:
        result = subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True, text=True
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def build_concat_file():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    lines = []
    total_seconds = 0
    for filename, start_f, end_f, dur_f in SHOTS:
        path = os.path.join(FRAMES_DIR, filename)
        if not os.path.exists(path):
            print(f"  WARNING: missing {path}")
            continue
        duration_sec = dur_f / FPS
        total_seconds += duration_sec
        # ffmpeg concat format requires absolute paths or relative-to-concat-file paths
        lines.append(f"file '{path}'")
        lines.append(f"duration {duration_sec:.6f}")

    # Repeat last file without duration (required by ffmpeg concat demuxer)
    last_path = os.path.join(FRAMES_DIR, SHOTS[-1][0])
    lines.append(f"file '{last_path}'")

    with open(CONCAT_FILE, "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Concat list written: {CONCAT_FILE}")
    print(f"Total duration: {total_seconds:.1f}s ({total_seconds/60:.2f} min)")
    return total_seconds


def run_ffmpeg():
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", CONCAT_FILE,
        "-vf", f"fps={FPS},scale=1920:1080:flags=lanczos",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-color_primaries", "bt709",
        "-color_trc", "bt709",
        "-colorspace", "bt709",
        OUTPUT_VIDEO,
    ]
    print(f"\nRunning ffmpeg...")
    print(" ".join(cmd))
    print()
    result = subprocess.run(cmd)
    return result.returncode == 0


def print_manual_instructions():
    print("\n" + "="*60)
    print("ffmpeg not found. Install it first:")
    print()
    print("  brew install ffmpeg")
    print()
    print("Then run this script again, or run ffmpeg directly:")
    print()
    print(f"  ffmpeg -y \\")
    print(f"    -f concat -safe 0 \\")
    print(f"    -i '{CONCAT_FILE}' \\")
    print(f"    -vf 'fps={FPS},scale=1920:1080' \\")
    print(f"    -c:v libx264 -preset fast -crf 18 \\")
    print(f"    -pix_fmt yuv420p \\")
    print(f"    '{OUTPUT_VIDEO}'")
    print("="*60)


def print_davinci_tip():
    print("\n--- DaVinci Resolve next steps ---")
    print(f"1. File > Import Media > {OUTPUT_VIDEO}")
    print("2. Drag animatic to timeline (it will be 5:00 exactly)")
    print("3. Import your music file and align to the animatic")
    print("4. Critical sync checks:")
    print("   • 1:13 (frame 1753) — lighting shift, dissonant chord")
    print("   • 1:53 (frame 2713) — her vanishing begins, flute solo")
    print("   • 4:11 (frame 6025) — Kumari appears, hopeful motif")
    print("   • 5:00 (frame 7200) — end, chorus returns")


def main():
    print("=== The King's Regret — Animatic Assembler ===\n")

    # Verify frames exist
    missing = [s[0] for s in SHOTS if not os.path.exists(os.path.join(FRAMES_DIR, s[0]))]
    if missing:
        print(f"ERROR: Missing frames: {missing}")
        print(f"Run generate_png_frames.py first.")
        sys.exit(1)

    print(f"Found all {len(SHOTS)} shot frames.")
    total = build_concat_file()

    if not check_ffmpeg():
        print_manual_instructions()
        print(f"\n(Concat list is ready at {CONCAT_FILE} — just needs ffmpeg to run)")
        sys.exit(0)

    success = run_ffmpeg()
    if success:
        size_mb = os.path.getsize(OUTPUT_VIDEO) / (1024 * 1024)
        print(f"\nOutput: {OUTPUT_VIDEO}  ({size_mb:.1f} MB)")
        print(f"Duration: {total:.1f}s at {FPS}fps")
        print_davinci_tip()
    else:
        print("\nffmpeg failed. Check the error above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
