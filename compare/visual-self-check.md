# Visual Self-Check

## Generated Asset Rule
- `assets/color-*.jpg` is now used only as garment reference input and is not directly referenced by the active module artwork.
- New generated assets are stored in `assets/gen/` and documented in `assets/gen/INDEX.md`.
- Final cutout model PNGs use transparent backgrounds with white sticker-style outline and soft shadow in the HTML.

## Continuous Canvas 01-03
- Source: `modules/continuous-01-03.html`
- Output master: `output/continuous-01-03.png`
- Slice outputs: `module-01-hero.png`, `module-02-detail-grid.png`, `module-03-fabric.png`
- Slice safety: y=600 crosses the soft camel transition band and the lower body of the wine/white cutout model; y=1200 crosses a neutral transition band. Faces, headlines, button macro cards, and key text stay away from the slice line.
- Layout change: main model is a cutout sticker, not a rectangular photo card. Detail and fabric images remain rectangular white cards as allowed small/detail images.
- Required decorative elements: two-line brown script titles, watermark letters, # tags, and curled dashed arrows are present.
- Verdict: pass after moving script titles behind the key headings.

## Continuous Canvas 04-05
- Source: `modules/continuous-04-05.html`
- Output master: `output/continuous-04-05.png`
- Slice outputs: `module-04-scenarios.png`, `module-05-styling-color.png`
- Slice safety: y=600 falls through the camel divider and lower leg/feet area of the cutout models, not through faces or titles.
- Layout change: all main models are transparent cutout stickers. The color module uses generated cutout models plus the generated accessory flat-lay group instead of direct product-photo crops.
- Required decorative elements: two-line `Outfit Notes` and `Color Story` script titles plus curled dashed arrows are present.
- Verdict: pass after moving the script layer behind models and core text.

## Module 06 - Size Chart
- Source: `modules/module-06-size-chart.html`
- Output: `output/module-06-size-chart.png`
- Result: right side now uses a real generated cutout model, not a placeholder or CSS/SVG garment drawing.
- Measurement marks: white dashed BUST / LENGTH / SLEEVE labels are overlaid directly on the model area.
- Table style: rows use alternating light pink and light camel stripes.
- Verdict: pass.

## Module 07 - Brand Story Closing
- Source: `modules/module-07-brand-story.html`
- Output: `output/module-07-brand-story.png`
- Result: color cards now use generated cutout model assets from `assets/gen/` instead of direct `assets/color-*.jpg` crops.
- Verdict: pass.

## Residual Risk
- Generated model identity is close enough for a unified A+ page but not perfectly identical across every pose.
- The generated garment details passed the visible check for notched split V neckline, two marble-look buttons, long sleeves, rib texture, and color family, but final production proof can still be improved with real photography later.
