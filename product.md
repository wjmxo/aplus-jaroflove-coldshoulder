# product.md — ELARAISE 亨利领长袖修身上衣

## 基本信息
- **品牌**: ELARAISE
- **产品**: 女士长袖亨利领 V 领修身罗纹上衣(Long Sleeve Henley V Neck Slim Fit Ribbed Top)
- **ASIN**: B0H1X6VPMM(白色/M 变体)
- **类目**: Clothing › Women › Tops, Tees & Blouses › T-Shirts
- **价格带**: $9.99–$16.99(按颜色浮动)
- **变体**: 5 色(White / Red / Wine / Brown / Black)× 5 码(S–XXL)
- **面料**: 95% Viscose + 5% Spandex,机洗
- **现状**: 4.9 星 / 21 评,女士T恤类 BSR #5,493,2026年5月新上架

## 核心卖点(按转化优先级排序)
1. **Notched 亨利领设计**: 开衩小 V 领 + 2 颗大理石纹装饰纽扣,修饰颈线,是与普通圆领基础款的核心差异点
2. **修身不紧绷(Slim Fit)**: 贴合曲线但留有余量,"fitted without being tight" 是买家复述率最高的评价
3. **罗纹弹力面料**: 高弹罗纹针织,"buttery soft" 触感是差评为零的关键
4. **袖长充足**: 长手臂买家专门点名夸袖子够长(竞品普遍的痛点)
5. **多场景百搭**: 单穿 / 叠穿打底皆可,通勤(Business Casual)+ 日常 + 约会
6. **秋冬定位**: Fall/Winter 主打,但轻薄可四季打底

## 买家评论金句素材(改写后可用于文案方向,不得直接引用)
- 面料如黄油般柔软、弹性恰到好处
- 修身显身材但不勒
- 纽扣缝制牢固、走线整齐、无线头
- 长度够长可塞进裤腰(tuck in)
- 红色偏橘调番茄红(文案中颜色描述要准确)

## 已知注意点(A+ 中要主动化解的疑虑)
- **尺码偏修身**: 多位买家提到想宽松需买大一码 → A+ 尺码表模块要突出 FIT TYPE 游标标在 Slim,并加"想要宽松效果请选大一码"提示
- 纽扣是**装饰性**的(不可解开)→ 细节图注明 Decorative Buttons,避免收到货的心理落差
- 白色款可能涉及透光疑虑 → 可在面料模块用"双层/不透"类实拍打消(以实际产品为准,不得虚构)

## 与参考风格(ANRABESS)的适配策略
- 直接对标参考库 09-longsleeve-henley-ribbed 和 26-henley-button-slimfit 的模块结构
- 用 STYLE.md 全套规范:米白底、衬线大标题、细节三宫格(亨利领扣/罗纹面料/袖口)、
  面料漩涡特写(95% Viscose 5% Spandex)、四场景街拍(Work/Daily/Shopping/Date)、
  5 色圆点色板、双表尺码+三游标(STRETCH: Medium / FIT TYPE: Slim / THICKNESS: Middle)
- 差异化机会: 竞品价位 $19.99–24.99,本品 $9.99 起——A+ 不能提价格,
  但可通过"车缝工艺特写、面料成分诚实标注"传达同等质感,让性价比在对比中自然成立

## 品牌信息(已确定)
- **品牌 Slogan**: ELARAISE --- Effortless Essentials(可根据喜好调整)
- **Logo**: 见 assets/ 目录,提供 4 个文件
  - `logo.svg` / `logo.png` — 深酒红主色版,用于浅色背景
  - `logo-white.svg` / `logo-white.png` — 白色版,用于照片或深色背景
  - 形式为衬线字母标(Wordmark)+ 细线 + Slogan 小字,与 STYLE.md 的衬线标题体系一致

### 品牌色 Tokens(与 STYLE.md 配色兼容,已按产品5色系定制)
```css
--brand-primary: #5E2A35;   /* 深酒红:取自 Wine 色变体,秋冬调性,区别于ANRABESS的驼棕 */
--brand-accent:  #B08D6E;   /* 暖驼:分隔线、小标签、手写体点缀 */
--brand-bg:      #F4F2EE;   /* 暖米白底:与 STYLE.md 主背景一致 */
--brand-text:    #1F1B1A;   /* 近黑标题 */
--brand-muted:   #8A8378;   /* 灰褐正文辅助色 */
```
- 选色逻辑: Wine 是产品5色中最具品牌记忆点的颜色,深酒红做主色让"品牌色=产品色"形成呼应;
  底色和辅助色沿用 ANRABESS 验证过的暖米白体系,保证成图与参考风格同源
- 使用规则: 主色只用于 Logo、小标签、色带和强调词,不做大面积底色(遵守 STYLE.md 浅底原则)
