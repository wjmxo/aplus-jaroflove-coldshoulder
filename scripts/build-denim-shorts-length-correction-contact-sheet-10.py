from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "assets/gen/gen-scene-wine-bistro-denim-shorts-v10.png",
    ROOT / "assets/gen/gen-scene-red-shopping-denim-shorts-v10.png",
    ROOT / "assets/gen/gen-scene-whitefloral-garden-denim-shorts-v10.png",
]
OUT = ROOT / "assets/gen/denim-shorts-length-correction-contact-sheet-10.jpg"

cols, rows = 3, 1
cell_w, cell_h, label_h = 460, 560, 48
sheet = Image.new("RGB", (cell_w * cols, (cell_h + label_h) * rows), "#f7f7f5")
draw = ImageDraw.Draw(sheet)
font = ImageFont.load_default(size=14)

for index, path in enumerate(FILES):
    image = Image.open(path).convert("RGB")
    image.thumbnail((cell_w - 16, cell_h - 16), Image.Resampling.LANCZOS)
    x = index * cell_w
    sheet.paste(image, (x + (cell_w - image.width) // 2, (cell_h - image.height) // 2))
    draw.rectangle((x, 0, x + cell_w - 1, cell_h + label_h - 1), outline="#c5c5c0", width=2)
    draw.text((x + 10, cell_h + 14), path.stem, fill="#343434", font=font)

sheet.save(OUT, quality=92)
print(OUT)
