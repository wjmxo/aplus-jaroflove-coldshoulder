from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "assets/gen/gen-scene-blackmarble-rooftop-v8.png",
    ROOT / "assets/gen/gen-scene-bluebark-coastal-v8.png",
    ROOT / "assets/gen/gen-scene-wine-bistro-date-v8.png",
    ROOT / "assets/gen/gen-scene-black-commute-v8.png",
    ROOT / "assets/gen/gen-scene-turquoise-ornate-market-v8.png",
    ROOT / "assets/gen/gen-scene-red-shopping-v8.png",
    ROOT / "assets/gen/gen-scene-whitefloral-garden-v8.png",
    ROOT / "assets/gen/gen-scene-teal-plaza-v8.png",
]
OUT = ROOT / "assets/gen/multi-color-scene-contact-sheet-08.jpg"

cols, rows = 4, 2
cell_w, cell_h, label_h = 400, 500, 48
sheet = Image.new("RGB", (cell_w * cols, (cell_h + label_h) * rows), "#f7f7f5")
draw = ImageDraw.Draw(sheet)
font = ImageFont.load_default(size=14)

for index, path in enumerate(FILES):
    image = Image.open(path).convert("RGB")
    image.thumbnail((cell_w - 16, cell_h - 16), Image.Resampling.LANCZOS)
    x = (index % cols) * cell_w
    y = (index // cols) * (cell_h + label_h)
    sheet.paste(image, (x + (cell_w - image.width) // 2, y + (cell_h - image.height) // 2))
    draw.rectangle((x, y, x + cell_w - 1, y + cell_h + label_h - 1), outline="#c5c5c0", width=2)
    draw.text((x + 10, y + cell_h + 14), path.stem, fill="#343434", font=font)

sheet.save(OUT, quality=92)
print(OUT)
