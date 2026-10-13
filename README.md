# 印刷实验室 · Print Labs

一组关于 Swiss、Riso 和半调网点的交互实验。`index.html` 是入口页，链接到各个实验室：

| 页面 | 内容 |
| --- | --- |
| `index.html` | 入口：三个实验室和它们的分工 |
| `print.html` | 01 印痕实验室：图像怎么变成墨点，墨点怎么落在纸上 |
| `layout.html` | 02 版式实验室：元素怎么在页面上排 |
| `object.html` | 03 实物实验室（简版）：拼版、出血、安全区、折线与裁切、骑马钉爬移、印前检查 |
| `element.html` | 04 元素实验室：把网页组件（导航、按钮、卡片、图标、分隔线、链接与状态、标签、作品列表）和几何、拟物、摄影、手绘元素一步步翻译进 Riso / Swiss 风格；照片可以裁切、镜像、抠图、切条、重复、错位复制、斜放、转剪影或线稿、放大网点、扫描拖影；“组合台”可以自定义一个或两个元素（形状、文字、照片、手绘、拟物），给每个元素套用单元素手段（裁切、抠图、镜像、切条、剪影 / 线稿、重复、扫描拖影、浓度、网点、错位复制），再比较叠印、不透明遮盖、镂空、补漏白、留白描边、硬阴影、反白、交织、布尔运算、同版内填、蒙版等组合手段；元素可在画布上拖动，套色错位可调，并检查错位下是否站得住 |

## 目录结构与构建

源文件在 `src/`：`shared.css` 是所有页面共用的样式（颜色、字体、页头、栏宽、控件尺寸），`links.js` 负责页面之间的链接，`home.html`、`print.html`、`layout.html` 是各页自己的内容。改完后运行：

```
python3 build.py
```

它会把共用样式和链接脚本内联进每一页，在仓库根目录生成 GitHub Pages 用的完整页面，并在 `dist/`（不进仓库）生成发布到 claude.ai 用的版本。根目录的 html 是生成的，不要直接改。

---

## 01 印痕实验室 · Print Texture Lab（`print.html`）

一个在浏览器里模拟印刷质感的交互小工具：网点加网、Riso 叠印、印刷瑕疵、相邻印刷工艺和 duotone。纯前端单文件，打开 `print.html` 即可使用，上传的照片只在本地处理。

## 功能

- **加网方式**：AM 圆点（圆 / 椭圆 / 菱形 / 方形）、线条网、交叉排线、Ben-Day、有序抖动（Bayer）、误差扩散（Floyd–Steinberg）、FM 调频网、阈值位图、连续调
- **工艺**：丝网、凸版、木刻、印章（朱文 / 白文）、拓印、复印（可调复印代数）、蓝晒、实物投影；选了工艺后由工艺自己决定痕迹。原图可选蕨叶（实物）和木纹（表面）
- **纸面图案**：坐标纸、点阵、横线本、账本、防窥纹
- **过渡对照**：同一个 A → B 变化用 AM 网点、FM 颗粒、有序抖动、叠印渐层、分墨渐变、平网阶梯、线条粗细、硬边与补漏白八种方式做出来
- **影调**：对比度、黑场、白场、中间调、色调分离
- **纸张**：非涂布 / 涂布 / 硫酸纸，9 种纸色（含牛皮纸和黑卡），白墨
- **反白**：每块版可单独反白，做空印和黑卡白墨
- **分版视图**：每块版一张黑白图，就是交给印厂的稿子
- **油墨模式**：单色、双色叠印、三色叠印、双色调、渐变映射（数字 duotone）；透明叠印 / 不透明遮盖
- **油墨**：12 种 Riso 油墨近似色（含白墨）
- **瑕疵**：套色错位、墨色颗粒、缺墨漏白、辊痕条带、纸张纹理、溢墨扩散、RGB 色差
- **预设**：27 张样张，每张都描述最终效果，列出必要 / 代表 / 可选特征和来源（设计、工艺、材料），特征可以逐个关掉
- **溯源**：每种加网方式、工艺、纸张、油墨模式和网点形状都附有历史来源与链接（悬停按钮可看简介）
- **中英双语**：右上角切换，选择会记在浏览器里

## 02 版式实验室 · Layout Lab（`layout.html`）

参数化海报生成器，参数分为：内容；网格（画幅、网页首屏的屏幕宽度与断点折叠、栏数、页边距、栏间距、基线）；字体排印（字体搭配、字号比例、层级数、标题大小 / 字重 / 字宽 / 行距 / 字距、正文行宽、标题处理：实心 / 油墨色 / 描边 / 镂空 / 双版叠印、对齐、全大写、竖排、中文排印（避头尾、标点挤压、中西文间距）、避免孤字）；构图（破格强度、留白、不对称度、旋转扰动、叠压层数、主轴角度、标题裁切、视觉焦点、出血）；动线与引导（Z / F / 中心放射阅读路径、引导箭头、尺寸渐变、框定重点、对比度阶梯、编号）；形状（词汇、数量、大小分布、实心比例、圆角、描边粗细、角度、吸附网格）；油墨（油墨数、颜色、纸张、文字油墨、面积比例、强调色元素数、叠印、满版底色与浓度）；整张海报的印刷质感（套色错位、墨色颗粒、缺墨、纸纹）；图像（网点处理、尺寸、矩形 / 圆形 / 拱形 / 去背、裁切、重复次数、空印：留纸色或填另一色、上传）；拼贴与印章（剪边、撕边、胶带、纸片阴影，朱文 / 白文印章）；约束规则（一切贴网格、形状不压文字、最多 3 种字号、比例和谐、一个主角，以及严格度）；多页节奏（1–4 页，交替或重复）；动效（悬停错位、视差、入场动画的时长与缓动）；印刷标记；随机种子。实时显示留白率、对齐度、视觉重心、字号比、正文对比度和孤字数，可以叠加网格线、重心和阅读顺序。每个参数旁都有 i 按钮：悬停看简介，点击固定说明和来源链接。在 GitHub Pages 上可以导出 PNG / SVG。内置 Swiss、半调海报、Riso zine、杂志、构成主义五种预设，每个预设都有风格卡（类别、年代、核心主张、特征、代表人物、与其他风格的区别、定义它的参数、来源），并可以和另一个预设并排对比，参数差异会高亮。参数清单是对设计实践的综合整理，并非出自某一本书。

## 使用

直接在浏览器打开 `index.html`（入口页），或用任意静态服务器托管（例如 GitHub Pages）。外部依赖只有 Google Fonts。

## 参考资料

页面底部列出了算法、印刷特性和油墨色值的出处。油墨色值为屏幕近似，实际印刷以印厂色卡为准。

---

## English

**Print Labs** is a set of interactive experiments with Swiss, Riso and halftone print styles. `index.html` is the hub; `print.html` is the Print Texture Lab and `layout.html` the Layout Lab; `object.html` is a lite Object Lab (imposition, bleed, safe area, folds and cuts, saddle-stitch creep, preflight); `element.html` is the Element Lab, which translates web components into the Riso / Swiss language step by step, with before/after and a sourced fit check. Sources live in `src/` (`shared.css` holds the styles every page shares, `links.js` the links between pages); run `python3 build.py` to generate the pages in the repo root for GitHub Pages and body-only versions in `dist/` for claude.ai. Do not edit the generated root html files.

**Print Texture Lab** is a browser playground for print textures: halftone screens, Riso-style overprinting, print flaws, related print processes and duotones. It is a single self-contained `print.html`; uploaded photos are processed locally and never leave the browser.

- **Screens**: AM dots (round / ellipse / diamond / square), line screen, cross-hatch, Ben-Day, ordered dither (Bayer), error diffusion (Floyd–Steinberg), FM stochastic, threshold, continuous tone
- **Processes**: screen print, letterpress, woodcut, seal stamp (zhuwen / baiwen), rubbing, photocopy with copy generations, cyanotype, photogram; a process makes its own marks. Sources include a fern (object) and wood grain (surface)
- **Printed-on patterns**: graph paper, dot grid, ruled, ledger, security tint
- **Transitions**: one A → B change made eight ways: AM dots, FM grain, ordered dither, overlap, split fountain, tint steps, line weight, hard edge and trapping
- **Tone**: contrast, black point, white point, midtones, posterize
- **Paper**: uncoated / coated / tracing stock, 9 paper colours including kraft and black card, white ink
- **Knockout**: invert any plate on its own for knockouts and white-on-black
- **Plate view**: one black-and-white file per plate, as you would send to a print shop
- **Ink modes**: mono, two-colour, three-colour, duotone, gradient map (digital duotone); overprint or opaque coverage
- **Inks**: 12 approximate Riso ink colours, including white
- **Flaws**: misregistration, ink grain, ink starvation, roller banding, paper texture, dot gain, RGB split
- **Presets**: 27 proofs, each described by its final look, with essential / representative / optional features and where each comes from (design, process, material); switch features off one by one
- **Provenance**: every screen, process, paper stock, ink mode and dot shape carries a fact-checked origin note with links (hover a button for a summary)
- **Bilingual**: switch between 中文 and English in the top-right corner

**Layout Lab** (`layout.html`) is a parametric poster generator. Its parameters cover content; grid (format, a web-hero screen width with breakpoint folding, columns, margins, gutters, baseline); typography (pairing, type scale, hierarchy levels, title size / weight / width / leading / tracking, body measure, title treatment: solid / in ink / outline / knockout / two plates, alignment, uppercase, vertical setting, CJK typesetting with line-break rules, punctuation trimming and Chinese–Latin spacing, orphan avoidance); composition (rule-breaking, whitespace, asymmetry, rotation jitter, overlap layers, axis angle, title crop, focal point, bleed); flow and guides (Z / F / radial reading paths, guide arrow, size progression, framing, contrast ladder, numbering); shapes (vocabulary, count, size spread, fill, corner radius, stroke width, angles, grid snapping); inks (count, colours, paper, text ink, area ratio, accent count, overprint, flood and tint); whole-poster print texture (misregistration, grain, ink starvation, paper); the image (screening, size, rectangle / circle / arch / cutout, crop, repeats, knockout left as paper or filled with another ink, upload); collage and seals (cut edge, torn edge, tape, shadow, zhuwen / baiwen seal); constraint rules (everything on the grid, shapes avoid text, at most three sizes, harmonic scale, one hero, plus strictness); multi-page rhythm (1–4 pages, alternate or repeat); motion (hover misregistration, parallax, intro duration and easing); print marks; and a random seed. It reports whitespace, alignment, balance, type ratio, body contrast and orphans live, can overlay the grid, balance and reading order, gives every setting an i button with a hover note and pinnable source links, and exports PNG / SVG on GitHub Pages. Presets: Swiss, Halftone, Riso zine, Editorial and Constructivist. Each has a style card (category, era, core idea, traits, key figures, how it differs, defining settings, sources) and can be compared side by side with another preset, with differing settings highlighted. The parameter list is a synthesis of design practice, not taken from any single book.

Open `index.html` (the hub) in a browser or host it on any static server such as GitHub Pages. The only external dependency is Google Fonts. Ink colours are on-screen approximations; check a print shop's physical swatches for real results.
