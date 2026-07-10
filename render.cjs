const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const renders = [
  ["module-01-hero.html", "module-01-hero.png"],
  ["module-02-detail-grid.html", "module-02-detail-grid.png"],
  ["module-03-fabric.html", "module-03-fabric.png"],
  ["module-04-scenarios.html", "module-04-scenarios.png"],
  ["module-05-styling-color.html", "module-05-styling-color.png"],
  ["module-06-size-chart.html", "module-06-size-chart.png"],
  ["module-07-brand-story.html", "module-07-brand-story.png"],
];

(async () => {
  fs.mkdirSync(path.join(process.cwd(), "output"), { recursive: true });
  const browser = await chromium.launch({ headless: true });
  for (const [file, output] of renders) {
    const page = await browser.newPage({
      viewport: { width: 1464, height: 600 },
      deviceScaleFactor: 2,
    });
    await page.goto(`file://${path.join(process.cwd(), "modules", file)}`);
    await page.screenshot({
      path: path.join(process.cwd(), "output", output),
      fullPage: false,
    });
    await page.close();
  }
  await browser.close();
})();
