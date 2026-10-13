# 印痕实验室 · Print Texture Lab

一个在浏览器里模拟印刷质感的交互小工具：网点加网、Riso 叠印、印刷瑕疵、相邻印刷工艺和 duotone。纯前端单文件，打开 `index.html` 即可使用，上传的照片只在本地处理。

## 功能

- **加网方式**：AM 圆点（圆 / 椭圆 / 菱形 / 方形）、线条网、交叉排线、Ben-Day、有序抖动（Bayer）、误差扩散（Floyd–Steinberg）、FM 调频网、阈值位图、丝网、凸版、木刻、连续调
- **油墨模式**：单色、双色叠印、三色叠印、双色调、渐变映射（数字 duotone）；透明叠印 / 不透明遮盖
- **油墨与纸张**：11 种 Riso 油墨近似色、5 种纸色
- **瑕疵**：套色错位、墨色颗粒、缺墨漏白、辊痕条带、纸张纹理、溢墨扩散、RGB 色差
- **预设**：17 张样张，点击即可载入参数
- **溯源**：每种加网方式、油墨模式和网点形状都附有历史来源与链接（悬停按钮可看简介）
- **中英双语**：右上角切换，选择会记在浏览器里

## 版式实验室（`layout.html`）

参数化海报生成器，参数分为：内容；网格（画幅、网页首屏的屏幕宽度与断点折叠、栏数、页边距、栏间距、基线）；字体排印（字体搭配、字号比例、层级数、标题大小 / 字重 / 字宽 / 行距 / 字距、正文行宽、标题处理：实心 / 油墨色 / 描边 / 镂空、对齐、全大写、竖排）；构图（破格强度、留白、不对称度、旋转扰动、叠压层数、主轴角度、标题裁切、视觉焦点、出血）；动线与引导（Z / F / 中心放射阅读路径、引导箭头、尺寸渐变、框定重点、对比度阶梯、编号）；形状（词汇、数量、大小分布、实心比例、圆角、描边粗细、角度、吸附网格）；油墨（油墨数、颜色、纸张、文字油墨、面积比例、强调色元素数、叠印）；整张海报的印刷质感（套色错位、墨色颗粒、缺墨、纸纹）；图像（网点处理、尺寸、矩形 / 圆形 / 拱形 / 去背、裁切、上传）；约束规则（一切贴网格、形状不压文字、最多 3 种字号、比例和谐、一个主角，以及严格度）；多页节奏（1–4 页，交替或重复）；动效（悬停错位、视差、入场动画的时长与缓动）；印刷标记；随机种子。实时显示留白率、对齐度、视觉重心、字号比和正文对比度，可以叠加网格线、重心和阅读顺序。每个参数旁都有 i 按钮：悬停看简介，点击固定说明和来源链接。在 GitHub Pages 上可以导出 PNG / SVG。内置 Swiss、半调海报、Riso zine、杂志、构成主义五种预设。参数清单是对设计实践的综合整理，并非出自某一本书。

## 使用

直接在浏览器打开 `index.html`，或用任意静态服务器托管（例如 GitHub Pages）。外部依赖只有 Google Fonts。

## 参考资料

页面底部列出了算法、印刷特性和油墨色值的出处。油墨色值为屏幕近似，实际印刷以印厂色卡为准。

---

## English

**Print Texture Lab** is a browser playground for print textures: halftone screens, Riso-style overprinting, print flaws, related print processes and duotones. It is a single self-contained `index.html`; uploaded photos are processed locally and never leave the browser.

- **Screens**: AM dots (round / ellipse / diamond / square), line screen, cross-hatch, Ben-Day, ordered dither (Bayer), error diffusion (Floyd–Steinberg), FM stochastic, threshold, screen print, letterpress, woodcut, continuous tone
- **Ink modes**: mono, two-colour, three-colour, duotone, gradient map (digital duotone); overprint or opaque coverage
- **Inks & paper**: 11 approximate Riso ink colours, 5 paper tones
- **Flaws**: misregistration, ink grain, ink starvation, roller banding, paper texture, dot gain, RGB split
- **Presets**: 17 proofs that load their settings in one click
- **Provenance**: every screen, ink mode and dot shape carries a fact-checked origin note with links (hover a button for a summary)
- **Bilingual**: switch between 中文 and English in the top-right corner

**Layout Lab** (`layout.html`) is a parametric poster generator. Its parameters cover content; grid (format, a web-hero screen width with breakpoint folding, columns, margins, gutters, baseline); typography (pairing, type scale, hierarchy levels, title size / weight / width / leading / tracking, body measure, title treatment: solid / in ink / outline / knockout, alignment, uppercase, vertical setting); composition (rule-breaking, whitespace, asymmetry, rotation jitter, overlap layers, axis angle, title crop, focal point, bleed); flow and guides (Z / F / radial reading paths, guide arrow, size progression, framing, contrast ladder, numbering); shapes (vocabulary, count, size spread, fill, corner radius, stroke width, angles, grid snapping); inks (count, colours, paper, text ink, area ratio, accent count, overprint); whole-poster print texture (misregistration, grain, ink starvation, paper); the image (screening, size, rectangle / circle / arch / cutout, crop, upload); constraint rules (everything on the grid, shapes avoid text, at most three sizes, harmonic scale, one hero, plus strictness); multi-page rhythm (1–4 pages, alternate or repeat); motion (hover misregistration, parallax, intro duration and easing); print marks; and a random seed. It reports whitespace, alignment, balance, type ratio and body contrast live, can overlay the grid, balance and reading order, gives every setting an i button with a hover note and pinnable source links, and exports PNG / SVG on GitHub Pages. Presets: Swiss, Halftone, Riso zine, Editorial and Constructivist. The parameter list is a synthesis of design practice, not taken from any single book.

Open `index.html` in a browser or host it on any static server such as GitHub Pages. The only external dependency is Google Fonts. Ink colours are on-screen approximations; check a print shop's physical swatches for real results.
