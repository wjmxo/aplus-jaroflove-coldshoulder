from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "assets/gen/gen-group-greyfloral-indigobark-beachclub-close-v2.png",
    ROOT / "assets/gen/gen-group-charcoal-greyfloral-studio-close-v2.png",
    ROOT / "assets/gen/gen-group-indigobark-charcoal-cafe-seated-v2.png",
    ROOT / "assets/gen/gen-group-greyfloral-charcoal-street-close-v2.png",
]
OUT = ROOT / "assets/gen/group-print-contact-sheet-04-v2.jpg"

cell_w, cell_h, label_h = 620, 500, 52
sheet = Image.new("RGB", (cell_w * 2, (cell_h + label_h) * 2), "#f4f2ee")
draw = ImageDraw.Draw(sheet)
font = ImageFont.load_default(size=17)

for index, path in enumerate(FILES):
    image = Image.open(path).convert("RGB")
    image.thumbnail((cell_w - 16, cell_h - 16), Image.Resampling.LANCZOS)
    x = (index % 2) * cell_w
    y = (index // 2) * (cell_h + label_h)
    sheet.paste(image, (x + (cell_w - image.width) // 2, y + (cell_h - image.height) // 2))
    draw.rectangle((x, y, x + cell_w - 1, y + cell_h + label_h - 1), outline="#b7aaa0", width=2)
    draw.text((x + 16, y + cell_h + 15), path.stem, fill="#5e2a35", font=font)

sheet.save(OUT, quality=92)
print(OUT)
