from PIL import Image, ImageDraw, ImageFont
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), 'animatic_frames')
os.makedirs(OUT_DIR, exist_ok=True)

frames = [
    ("shot01.png", "#FFE680", "Shot 1", "0:00–0:02 — Wide interior: establish room"),
    ("shot02.png", "#F4E4C1", "Shot 2", "0:02–0:12 — Dolly to game table"),
    ("shot03.png", "#D4AF37", "Shot 3", "0:12–0:30 — Close on hands and token"),
    ("shot04.png", "#FFE680", "Shot 4", "0:30–0:50 — Two-shot: King & Taleju"),
    ("shot05.png", "#F4E4C1", "Shot 5", "0:50–1:13 — Eyes meeting, intimacy peak"),
    ("shot06.png", "#A8D8F0", "Shot 6", "1:13–1:40 — Lighting shift; his desire flashes"),
    ("shot07.png", "#7BA8C4", "Shot 7", "1:40–1:53 — He reaches; she recoils"),
    ("shot08.png", "#4A6FA5", "Shot 8", "1:53–2:19 — Vanishing: she dissolves; token falls"),
    ("shot09.png", "#FFE680", "Shot 9", "2:19–2:40 — Flashback: her smile (memory)"),
    ("shot10.png", "#9BB3CC", "Shot 10", "2:40–3:00 — King walks in rain (transition)"),
    ("shot11.png", "#C9D9E8", "Shot 11", "3:00–3:15 — Dream: Taleju in mist"),
    ("shot12.png", "#7B8FA3", "Shot 12", "3:15–3:29 — King meditates; fasting montage"),
    ("shot13.png", "#5D6D7B", "Shot 13", "3:29–3:58 — Montage: candles, board, incense"),
    ("shot14.png", "#E8D4B8", "Shot 14", "3:58–4:11 — Dream peak: Taleju's instruction"),
    ("shot15.png", "#FFD4A3", "Shot 15", "4:11–4:40 — Kumari appears: child with token"),
    ("shot16.png", "#F4C2A0", "Shot 16", "4:40–4:55 — People bow; King watches"),
    ("shot17.png", "#F5E6D3", "Shot 17", "4:55–5:00 — Token rests; King at peace"),
]

W, H = 1920, 1080

# Try to load a nice system font; fall back to default
try:
    FONT_LG = ImageFont.truetype("/Library/Fonts/Arial.ttf", 96)
    FONT_SM = ImageFont.truetype("/Library/Fonts/Arial.ttf", 40)
except Exception:
    FONT_LG = ImageFont.load_default()
    FONT_SM = ImageFont.load_default()

for filename, color, title, subtitle in frames:
    path = os.path.join(OUT_DIR, filename)
    img = Image.new('RGB', (W, H), color)
    draw = ImageDraw.Draw(img)
    # Title
    # Title (centered)
    try:
        bbox = draw.textbbox((0, 0), title, font=FONT_LG)
        w_title = bbox[2] - bbox[0]
        h_title = bbox[3] - bbox[1]
    except Exception:
        w_title, h_title = FONT_LG.getsize(title)
    draw.text(((W - w_title) / 2, H * 0.42), title, fill=(51, 42, 24), font=FONT_LG)
    # Subtitle (centered)
    try:
        bbox_sub = draw.textbbox((0, 0), subtitle, font=FONT_SM)
        w_sub = bbox_sub[2] - bbox_sub[0]
        h_sub = bbox_sub[3] - bbox_sub[1]
    except Exception:
        w_sub, h_sub = FONT_SM.getsize(subtitle)
    draw.text(((W - w_sub) / 2, H * 0.55), subtitle, fill=(51, 42, 24), font=FONT_SM)
    img.save(path)
    print(f"Saved {path}")

print("All frames generated.")
