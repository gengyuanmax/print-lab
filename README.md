# 印刷实验室 · Print Labs

通过交互实验探索瑞士风格的版式、Riso 孔版印刷与半色调网点。调整参数，观察图像的印刷质感、图文编排、纸张折叠装订后的变化，以及网页组件的风格改造。

| 页面 | 内容 |
| --- | --- |
| `index.html` | 首页：四个实验室的入口，以及从原稿到成品的流程演示 |
| `print.html` | 01 印痕实验室：调整网点、油墨和纸张，模拟印刷效果 |
| `layout.html` | 02 版式实验室：调整网格、字体和构图，生成海报 |
| `object.html` | 03 实物实验室（简版）：查看拼版、折页、裁切和装订，了解印前要求 |
| `element.html` | 04 元素实验室：改造网页组件与视觉元素、处理照片；在组合台编辑一个或两个元素并比较组合效果 |

## 使用

在浏览器中打开 `index.html`，或通过静态服务器访问（如 GitHub Pages）。项目只使用前端代码；字体从 Google Fonts 加载，版式导出时会按需加载 html-to-image。上传的图片只在浏览器本地处理。

右上角可切换中文和英文，浏览器会记住所选语言。

## 目录结构与构建

修改 `src/` 中的源文件：

- `home.html`、`print.html`、`layout.html`、`object.html`、`element.html`：各页面的内容和交互逻辑。
- `shared.css`：共用的颜色、字体、页头、栏宽和控件样式。
- `links.js`：页面之间的导航链接。

修改后运行：

```sh
python3 build.py
```

构建会将共用样式和链接脚本嵌入各页，在仓库根目录生成供 GitHub Pages 使用的完整 HTML，同时在 `dist/` 中生成供 claude.ai 发布的版本。根目录的 HTML 是生成文件，请勿直接编辑；`dist/` 不纳入版本管理。

## 01 印痕实验室 · Print Texture Lab

选择加网方式、印刷工艺、油墨和纸张，观察它们如何改变图像。可使用内置测试图，也可上传照片。

- **加网与影调**：AM 调幅网（圆形、椭圆、菱形、方形）、线条网、交叉排线、Ben-Day 网点、有序抖动（Bayer）、误差扩散（Floyd–Steinberg）、FM 调频网、阈值位图和连续调。可调整对比度、黑场、白场、中间调及色调分离。
- **工艺模拟**：丝网、凸版、木刻、印章（朱文、白文）、拓印、复印、蓝晒与物影摄影。选择工艺后，纹理由该工艺决定；复印效果可调整翻印次数。原图除测试画面外，还可选印文、蕨叶（实物）、木纹（表面）和木活字演出海报。凸版模式可调整活字磨损，模拟字形缺口、色块木纹、局部墨色不匀和压痕。纸张做旧可模拟泛黄、纸边旧痕、褐斑（foxing）、对折或十字折痕，以及折痕处的墨层开裂。
- **油墨与过渡**：单色、双色叠印、三色叠印、双色调、渐变映射和过渡映射；支持透明叠印或不透明遮盖。可比较 AM 调幅网、FM 调频网、有序抖动、叠印渐变、分墨渐变、平网阶梯、线条粗细、硬边与陷印八种过渡方式。
- **纸张与纹理**：非涂布纸、涂布纸、硫酸纸，以及 9 种纸色；可添加方格、点阵、横线、账本格线和信封防窥底纹。提供 12 种油墨近似色（含白墨），以及套色错位、墨色颗粒、缺墨、墨辊条纹、纸纹、网点扩大和 RGB 通道偏移。
- **印版与反白**：分版视图展示各色对应的黑白分色稿，便于理解制版。可分别对 A、B 版反相，交换着墨与留白区域；搭配纸色和白墨可尝试不同效果。实际制版文件仍需符合印厂要求。
- **预设与说明**：28 张样张附有核心、典型和可选特征，并标注其来自设计、工艺还是材料。可逐项关闭效果进行比较；各类加网方式、工艺和材料也附有原理说明及参考资料。

## 02 版式实验室 · Layout Lab

通过参数生成海报，内置瑞士风格、半色调海报、Riso 小志、杂志、构成主义和木活字海报六种预设。木活字海报提供“逐行满排”：分别调整每行字号和字宽，排满设定行宽。可加入手工排字偏差，模拟字位浮动、轻微歪斜和字距不均，并搭配星形与放射纹装饰。点击“换一张”，按当前规则生成新的布局。

- **网格与文字**：画幅、响应式栏数、页边距、栏间距、基线间距、字体搭配、字号层级、行距、字距、正文行宽、对齐与竖排。中文排版支持行首行尾禁则、标点调整、中西文间距和减少孤字。
- **构图与引导**：留白、不对称、随机旋转、元素叠压、主轴角度、标题裁切、焦点和出血；可用阅读路径、箭头、逐渐放大的形状、色块和对比度分级引导视线。
- **形状与配色**：选择形状类型、数量、大小、描边和圆角，设置网格吸附；调整油墨种类、颜色分配、文字用色、满版底色和叠印效果。
- **图像与质感**：加网、裁切、去底、重复、挖空，以及套色错位、颗粒、缺墨和纸纹；可添加剪纸边缘、撕边、胶带、投影和朱文或白文印章。
- **规则与多页**：通过网格对齐、避让文字、限制字号、统一比例和突出主体等规则控制布局；支持 1–4 页，交替安排不同类型的页面，或重复相同布局规则。
- **动效与标记**：悬停错位、视差、入场动画，以及套准标记、裁切线、色彩控制条和页码。

页面显示留白率、对齐度、视觉重心、字号比、正文对比度和孤字数，也可叠加网格线、重心与阅读顺序。指标用于比较方案，是本页简化算法的估算结果。

将鼠标移到参数旁的 `i` 上查看简介，点击后可固定完整说明和参考资料。风格卡介绍各预设的特点与关键参数；并排对比时，会高亮不同的参数。在 GitHub Pages 版本中可导出 PNG 或 SVG。

## 03 实物实验室 · Object Lab

选择单张海报、8 页折页小册、对折页、三折页或骑马钉小册子，查看拼版方式和阅读顺序。可调整尺寸、出血、安全距离、纸张克重和印刷方式。

页面标出裁切线、折线、安全区和出血范围，并估算骑马钉小册子的爬移。Riso 预览按 A3 纸张和四周 5 mm 不可印区域模拟；检查结果供理解工艺和准备文件时参考，具体规格以印厂要求为准。

## 04 元素实验室 · Element Lab

选择导航、按钮、卡片、图标、分隔线、链接与状态、标签、作品列表，或几何图形、实物、照片和手绘，尝试“瑞士风格 · 线条与文字”“Riso · 色块”“纸品造型”三种方案。页面按元素类型提供配色、明暗、线条、网点、对齐和字体等调整步骤，可分别开关，对照改造前后的效果。

照片支持裁切、镜像、按颜色去底、条带错位、重复、异色错位复制、倾斜、剪影或线稿、放大网点和扫描拖影。去底采用简化的颜色判断，不等同于精细抠图。

“组合台”可自定义一个或两个元素（形状、文字、照片、手绘、实物），分别设置油墨、大小、角度和单元素处理（裁切、去底、镜像、条带错位、剪影或线稿、重复、扫描拖影、色调深浅、网点、异色错位复制），并在画布上直接拖动。两个元素时可比较叠印、不透明遮盖、挖空、陷印、留白描边、硬边投影、反白、交织、并集、交集、排除重叠、同版填充和剪切蒙版，套色偏差可在 0–3 mm 之间调节。同色元素的主体使用同一色版，无需彼此套准；异色复制和投影等效果仍可能引入其他色版。

页面标注各步骤的参考来源，区分印前建议、视觉设计方法与本页示例。“规则启用情况”仅显示开关状态，“套色偏差提示”按预设组合方式给出说明，二者均不能替代实际印前检查。浅色效果通过网点或透明度模拟；85% 来自 MICA 对大色块的具体建议，实际制版以承印方要求为准。

## 中文文案与术语

说明先讲作用和操作，再补充原理与历史。控件使用简短、具体的名称，避免逐字翻译英文比喻。Riso、Ben-Day、Bayer 等专名保留原文；小志（zine）指自主制作、发行的小型刊物。

| 术语 | 本项目的用法 |
| --- | --- |
| 半色调（halftone） | 用网点表现连续的明暗层次；AM 为调幅加网，FM 为调频加网 |
| 挖空（knockout） | 移除下层油墨，让纸色或另一色显露 |
| 反白 | 在深色背景中留出图文，呈现纸色的视觉效果 |
| 印版反相 | 交换单块印版的着墨与留白区域；其他色版仍可能在此处着墨 |
| 陷印（trapping） | 使相邻颜色的边缘略微重叠，减少套印不准造成的白缝 |
| 网点扩大（dot gain） | 印刷后网点覆盖面积增大的现象 |
| 物影摄影（photogram） | 将物体放在感光材料上曝光，无需相机即可成像 |
| 爬移（creep） | 折叠套入的内层纸张因厚度而向外突出的现象 |
| 逐行满排（set to measure） | 在本页中逐行调整字号与字宽，使文字占满设定行宽，模拟木活字海报的排字方式 |
| 褐斑（foxing） | 纸张上随老化出现的褐色或红褐色斑点；成因不一，不等同于霉斑 |

挖空、叠印和陷印的术语参考 [Adobe 叠印说明](https://helpx.adobe.com/cn/illustrator/using/overprinting.html)与[陷印说明](https://helpx.adobe.com/cn/illustrator/using/trapping.html)；物影摄影的原理参考 [MoMA 的 Photogram 释义](https://www.moma.org/collection/terms/photogram)；中文断行术语参考 [W3C《中文排版需求》](https://www.w3.org/TR/clreq/)；爬移参考 [Adobe 小册子设置](https://helpx.adobe.com/cn/indesign/desktop/print/print-booklets/booklet-printing-settings.html)。

## 许可

代码（`src/`、根目录生成的页面和 `build.py`）采用 MIT 许可；文字说明和页面绘制的示例图采用 CC BY 4.0，转载或改编请注明出处。字体、引用资料和商标不在此列，详见 [LICENSE](LICENSE)。本项目与 Claude 协作完成。

## 参考资料

各页面底部列有算法、印刷特性和油墨色值的资料来源。参数根据多种设计方法整理；油墨色值与纹理均为屏幕模拟，实际印刷以印厂实物色卡和工艺要求为准。

---

## English

**Print Labs** is a set of interactive experiments with Swiss, Riso and halftone print styles. `index.html` is the hub; `print.html` is the Print Texture Lab and `layout.html` the Layout Lab; `object.html` is a lite Object Lab (imposition, bleed, safe area, folds and cuts, saddle-stitch creep, preflight); `element.html` is the Element Lab, which translates web components into the Riso / Swiss language step by step, with before/after and a sourced fit check. Sources live in `src/` (`shared.css` holds the styles every page shares, `links.js` the links between pages); run `python3 build.py` to generate the pages in the repo root for GitHub Pages and body-only versions in `dist/` for claude.ai. Do not edit the generated root html files.

**Print Texture Lab** is a browser playground for print textures: halftone screens, Riso-style overprinting, print flaws, related print processes and duotones. It is a single self-contained `print.html`; uploaded photos are processed locally and never leave the browser.

- **Screens**: AM dots (round / ellipse / diamond / square), line screen, cross-hatch, Ben-Day, ordered dither (Bayer), error diffusion (Floyd–Steinberg), FM stochastic, threshold, continuous tone
- **Processes**: screen print, letterpress, woodcut, seal stamp (zhuwen / baiwen), rubbing, photocopy with copy generations, cyanotype, photogram; a process makes its own marks. Sources include a fern (object), wood grain (surface) and a wood-type show bill. Letterpress has a type-wear setting (chipped edges, wood grain in solids, uneven inking per block, deeper impression), and the paper can be aged: yellowing, edges and foxing, one or two folds with ink cracking along them (time, not a print process)
- **Printed-on patterns**: graph paper, dot grid, ruled, ledger, security tint
- **Transitions**: one A → B change made eight ways: AM dots, FM grain, ordered dither, overlap, split fountain, tint steps, line weight, hard edge and trapping
- **Tone**: contrast, black point, white point, midtones, posterize
- **Paper**: uncoated / coated / tracing stock, 9 paper colours including kraft and black card, white ink
- **Knockout**: invert any plate on its own for knockouts and white-on-black
- **Plate view**: one black-and-white file per plate, as you would send to a print shop
- **Ink modes**: mono, two-colour, three-colour, duotone, gradient map (digital duotone); overprint or opaque coverage
- **Inks**: 12 approximate Riso ink colours, including white
- **Flaws**: misregistration, ink grain, ink starvation, roller banding, paper texture, dot gain, RGB split
- **Presets**: 28 proofs, each described by its final look, with essential / representative / optional features and where each comes from (design, process, material); switch features off one by one
- **Provenance**: every screen, process, paper stock, ink mode and dot shape carries a fact-checked origin note with links (hover a button for a summary)
- **Bilingual**: switch between 中文 and English in the top-right corner

**Layout Lab** (`layout.html`) is a parametric poster generator. Its parameters cover content; grid (format, a web-hero screen width with breakpoint folding, columns, margins, gutters, baseline); typography (pairing, type scale, hierarchy levels, title size / weight / width / leading / tracking, body measure, title treatment: solid / in ink / outline / knockout / two plates, alignment, uppercase, vertical setting, CJK typesetting with line-break rules, punctuation trimming and Chinese–Latin spacing, orphan avoidance); composition (rule-breaking, whitespace, asymmetry, rotation jitter, overlap layers, axis angle, title crop, focal point, bleed); flow and guides (Z / F / radial reading paths, guide arrow, size progression, framing, contrast ladder, numbering); shapes (vocabulary, count, size spread, fill, corner radius, stroke width, angles, grid snapping); inks (count, colours, paper, text ink, area ratio, accent count, overprint, flood and tint); whole-poster print texture (misregistration, grain, ink starvation, paper); the image (screening, size, rectangle / circle / arch / cutout, crop, repeats, knockout left as paper or filled with another ink, upload); collage and seals (cut edge, torn edge, tape, shadow, zhuwen / baiwen seal); constraint rules (everything on the grid, shapes avoid text, at most three sizes, harmonic scale, one hero, plus strictness); multi-page rhythm (1–4 pages, alternate or repeat); motion (hover misregistration, parallax, intro duration and easing); print marks; and a random seed. It reports whitespace, alignment, balance, type ratio, body contrast and orphans live, can overlay the grid, balance and reading order, gives every setting an i button with a hover note and pinnable source links, and exports PNG / SVG on GitHub Pages. Presets: Swiss, Halftone, Riso zine, Editorial, Constructivist and Wood-type poster (each line set to the full measure with optional hand-set wobble, with stars and sunbursts). Each has a style card (category, era, core idea, traits, key figures, how it differs, defining settings, sources) and can be compared side by side with another preset, with differing settings highlighted. The parameter list is a synthesis of design practice, not taken from any single book.

Open `index.html` (the hub) in a browser or host it on any static server such as GitHub Pages. The only external dependency is Google Fonts. Ink colours are on-screen approximations; check a print shop's physical swatches for real results.

**License.** Code (`src/`, the generated pages and `build.py`) is MIT; the written content and the example images the pages draw are CC BY 4.0, so credit Print Labs when you reuse or adapt them. Fonts, linked references and trademarks are excluded; see [LICENSE](LICENSE). Made in collaboration with Claude.
