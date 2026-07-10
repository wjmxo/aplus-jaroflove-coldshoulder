from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FILES = sorted((ROOT / "assets").glob("*.jpg")) + sorted((ROOT / "assets" / "gen").glob("*.png"))
FILES = [path for path in FILES if "contact-sheet" not in path.name]
OUT = ROOT / "assets" / "gen" / "asset-contact-sheet-jaroflove.jpg"

thumb_w, thumb_h = 280, 360
label_h = 56
cols = 5
rows = (len(FILES) + cols - 1) // cols
sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), "white")
draw = ImageDraw.Draw(sheet)
font = ImageFont.load_default(size=14)

for index, path in enumerate(FILES):
    image = Image.open(path).convert("RGB")
    image.thumbnail((thumb_w - 16, thumb_h - 16), Image.Resampling.LANCZOS)
    x = (index % cols) * thumb_w
    y = (index // cols) * (thumb_h + label_h)
    px = x + (thumb_w - image.width) // 2
    py = y + (thumb_h - image.height) // 2
    sheet.paste(image, (px, py))
    prefix = "REAL" if path.parent.name == "assets" else "GEN"
    label = f"{prefix} | {path.stem}".replace("color-", "").replace("print-", "")
    draw.multiline_text((x + 8, y + thumb_h + 6), label, fill="black", font=font, spacing=2)
    draw.rectangle((x, y, x + thumb_w - 1, y + thumb_h + label_h - 1), outline="#b8b8b8")

OUT.parent.mkdir(parents=True, exist_ok=True)
sheet.save(OUT, quality=92)
print(OUT)
