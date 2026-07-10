# ELARAISE A+ Production Workflow

This repository stores the product facts, approved asset library, HTML module sources, rendered PNG outputs, and upload notes for the ELARAISE Premium A+ page.

## Four-Step Operation

1. Confirm product facts in `product.md`, including category, main color, target customer, verified fabric/content, size data, and claims.
2. Confirm the visual system in `STYLE.md`, especially module order, photography tone, typography, slicing rules, and self-check criteria.
3. Confirm or update copy in `copy.md`; keep Amazon compliance rules in `AGENTS.md` as always-on constraints.
4. Run the asset-production entry command:

   `$aplus-asset-production 为 {产品名} 执行素材生产`

After the asset library is accepted, use `$aplus-page-production` for page layout, slicing, rendering, visual self-check, and upload-package work.

## Key Directories

- `assets/color-*.jpg`: real product references for garment fidelity
- `assets/gen/`: approved generated asset library
- `modules/`: HTML source files
- `output/`: final rendered PNG files
- `compare/`: visual self-check and slice verification artifacts
- `.agents/skills/`: repository-level workflow skills
