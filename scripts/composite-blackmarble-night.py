from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
SUBJECT_PATH = ROOT / "assets" / "print-blackmarble-front-01.jpg"
BACKGROUND_PATH = Path(
    "/Users/jam/.codex/generated_images/019f4a5d-8b92-7050-9f46-fcfd9ade597e/"
    "exec-f1865020-4224-46f8-b299-d074f7926cf1.png"
)
OUTPUT_PATH = ROOT / "assets" / "gen" / "gen-scene-blackmarble-night-composite-01.png"


subject = Image.open(SUBJECT_PATH).convert("RGB")
rgb = np.asarray(subject)

# Select the near-white studio sweep. Cream regions in the garment remain well
# below this threshold because they contain visible texture and warm gray tone.
near_white = np.min(rgb, axis=2) >= 242
background_region = near_white

alpha = np.where(background_region, 0, 255).astype(np.uint8)
alpha_img = Image.fromarray(alpha, mode="L").filter(ImageFilter.GaussianBlur(1.1))

background = Image.open(BACKGROUND_PATH).convert("RGB")
target_ratio = subject.width / subject.height
background_ratio = background.width / background.height
if background_ratio > target_ratio:
    new_width = round(background.height * target_ratio)
    left = (background.width - new_width) // 2
    background = background.crop((left, 0, left + new_width, background.height))
else:
    new_height = round(background.width / target_ratio)
    top = (background.height - new_height) // 2
    background = background.crop((0, top, background.width, top + new_height))
background = background.resize(subject.size, Image.Resampling.LANCZOS)

foreground = subject.convert("RGBA")
foreground.putalpha(alpha_img)
composite = background.convert("RGBA")
composite.alpha_composite(foreground)
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
composite.convert("RGB").save(OUTPUT_PATH, quality=96)
print(OUTPUT_PATH)
