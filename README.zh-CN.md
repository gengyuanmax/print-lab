# 印刷实验室

[English](README.md) · **简体中文**

[打开实验室 ↗](https://gengyuanmax.github.io/print-lab/) · [GitHub 源码 ↗](https://github.com/gengyuanmax/print-lab)

一个边动手、边学习印刷与视觉设计的交互实验室。调整网点、油墨、字体、构图和纸张形式，观察它们如何改变画面。

这也是一份与 AI 一起学习设计的记录：了解设计的基本元素，尝试自己做选择，再把想要的视觉效果表达清楚。

## 四个实验室，分别玩什么？

| 实验室 | 可以尝试的内容 |
| --- | --- |
| [01 · 印痕实验室](https://gengyuanmax.github.io/print-lab/print.html) | 把图像变成网点与油墨，比较加网方式、印刷工艺、叠印和纸张质感。 |
| [02 · 版式实验室](https://gengyuanmax.github.io/print-lab/layout.html) | 调整网格、字体、配色与拼贴，生成海报、比较风格并导出作品。 |
| [03 · 实物实验室](https://gengyuanmax.github.io/print-lab/object.html) | 看一张纸如何变成小志、折页或小册子，了解页序、折线、出血和安全区。 |
| [04 · 元素实验室](https://gengyuanmax.github.io/print-lab/element.html) | 改造网页组件、处理照片，再用叠印、挖空和蒙版等方式组合形状、文字与图像。 |

**第一次来，可以这样开始：** 打开印痕实验室，选择 Riso 预设，改一改网点大小和油墨颜色；再到版式实验室，看看这些视觉元素如何组成一张海报。

各页右上角可切换中文和英文，浏览器会记住所选语言。上传的图片只在浏览器本地处理。

<details>
<summary><strong>观看 26 秒功能演示（英文字幕）</strong></summary>

[![印刷实验室演示：印刷质感、海报版式、纸张折叠与图形组合，配有英文字幕](assets/social/print-lab-demo-en.gif)](https://gengyuanmax.github.io/print-lab/)

</details>

## 进一步了解功能

<details>
<summary><strong>01 · 印痕实验室：网点、油墨与纸张</strong></summary>

- **加网与影调：** 比较 AM 调幅网、线条网、交叉排线、Ben-Day 网点、Bayer 有序抖动、Floyd–Steinberg 误差扩散、FM 调频网、阈值位图和连续调；调整对比度、明暗范围及网点形状；网点还可沿同心圆、放射线或螺旋排列，并只印在圆、星、心或几个字的外形里。
- **印刷工艺：** 模拟丝网、凸版、木刻、印章、拓印、复印、蓝晒和物影摄影，尝试木活字磨损、多次翻印与纸张做旧。
- **油墨与质感：** 搭配一至三色油墨、双色调或渐变映射，比较透明叠印与不透明遮盖；加入套色错位、颗粒、缺墨、墨辊条纹和网点扩大。
- **比较与学习：** 从 30 张预设样张出发，逐项关闭效果，比较影调过渡，并查看黑白分色稿。控件附有原理说明和参考资料。

</details>

<details>
<summary><strong>02 · 版式实验室：网格、字体与构图</strong></summary>

- **六种起点：** 瑞士风格、半色调海报、Riso 小志、杂志版式、构成主义和木活字海报。点击“换一张”，保留当前设计规则，生成新的构图。
- **编排参数：** 调整网格、页边距、字号层级、字距、对齐、留白、阅读路径、形状和配色；中文排版包含断行禁则与中西文间距处理。
- **印刷与拼贴：** 加入网点、剪纸、撕边、胶带、印章和整页纹理，也可探索多页编排、印刷标记及动效。
- **比较与导出：** 并排比较预设，叠加网格和阅读顺序，在网站中导出 PNG 或 SVG。版式指标是简化估算，用于比较实验方案。
- **描述这张海报：** 一键生成给人和 AI 看的设计说明（风格、网格、字体、颜色、构图、质感和全部参数）、给图像生成模型的英文提示词、CSS 设计 tokens，以及带随机种子的 JSON 配置；配置可在本工具或分享链接里还原同一张海报。

</details>

<details>
<summary><strong>03 · 实物实验室：从一张纸到一本小册子</strong></summary>

- 探索单张海报、8 页折页小志、对折页、三折页和骑马钉小册子。
- 在拼版图与阅读视图之间切换，理解印刷页序和阅读页序的区别。
- 调整纸张尺寸、出血、安全距离、克重和印刷方式，查看折线、裁切线及小册子的爬移估算。
- 这是用于学习的简化模型；其中的印前提示不能替代印厂的生产要求。

</details>

<details>
<summary><strong>04 · 元素实验室：组件、照片与组合</strong></summary>

- **改造常见元素：** 尝试导航、按钮、卡片、图标和标签等，对比原始样式与瑞士风格、Riso 色块或纸品造型。
- **处理图像：** 裁切、镜像、按颜色去底、生成剪影或线稿，加入网点、错位复制和扫描拖影。
- **组合一至两个元素：** 在画布上直接摆放形状、文字、照片、手绘或实物，比较叠印、挖空、陷印、交织和剪切蒙版。
- **理解处理效果：** 说明附有来源，并区分印刷建议与视觉设计方法。去底、浅色模拟及适配提示均为简化演示。

</details>

## 本地运行

无需安装依赖包或配置应用后端。下载项目后，可以启动本地静态服务器：

```sh
git clone https://github.com/gengyuanmax/print-lab.git
cd print-lab
python3 -m http.server 8000 --bind 127.0.0.1
```

在浏览器中打开 [localhost:8000](http://localhost:8000)。也可以直接打开 `index.html`。

字体从 Google Fonts 加载；版式导出会按需加载 `html-to-image`。上传的照片始终在浏览器中处理。

## 修改与构建

修改 `src/` 中的源文件，然后运行：

```sh
python3 build.py
```

| 位置 | 用途 |
| --- | --- |
| `src/home.html` | 首页内容与分享预览信息 |
| `src/print.html`、`src/layout.html`、`src/object.html`、`src/element.html` | 各实验室的内容与交互逻辑 |
| `src/shared.css` | 共用的配色、字体、布局和控件样式 |
| `src/links.js` | 本地页面、GitHub Pages 与 Claude artifacts 的导航链接 |
| `assets/social/` | 演示 GIF 与社交分享图片 |
| 根目录的 HTML | 构建生成的 GitHub Pages 页面，请勿直接编辑 |
| `dist/` | 构建生成的 Claude artifacts 内容版本，不纳入版本管理 |

更新文档时，请同时维护本文件和[英文 README](README.md)。

<details>
<summary><strong>在领英等平台分享网站</strong></summary>

首页提供英文 Open Graph 标题、简介、演示 GIF 和备用静态图。横版分享素材为 `assets/social/print-lab-share-en.gif` 与 `.jpg`，尺寸为 1200 × 630，两侧留边，保留完整界面和字幕。原比例演示位于 `assets/social/print-lab-demo-en.gif`，两份 GIF 均小于 5 MB。

裁切方式、图片选择和动画播放由分享平台决定。部署后可用 [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/) 检查或刷新链接预览；如果希望以媒体帖展示演示，可以直接上传 GIF 或视频，并在正文附上网站链接。

</details>

## 资料来源与使用边界

各实验室提供原理说明与参考链接。参数结合了多种印刷和视觉设计方法，并非照搬某一本书或某套设计系统。欢迎通过 [GitHub issues](https://github.com/gengyuanmax/print-lab/issues) 纠错或补充资料。

油墨颜色、纹理和印前检查均为屏幕模拟。实际生产请以印厂实物色卡和工艺要求为准。

<details>
<summary><strong>常用术语</strong></summary>

| 术语 | 本项目中的含义 |
| --- | --- |
| 半色调（halftone） | 用网点表现明暗层次；AM 改变网点大小，FM 改变网点分布。 |
| 挖空（knockout） | 移除下层油墨，让纸色或另一种颜色显露。 |
| 反白 | 在深色背景中留出图文，呈现纸色。 |
| 印版反相 | 交换单块印版的着墨与留白区域；其他色版仍可能在此处着墨。 |
| 陷印（trapping） | 让相邻颜色的边缘略微重叠，减少套印不准造成的白缝。 |
| 网点扩大（dot gain） | 印刷后网点覆盖面积增大的现象。 |
| 物影摄影（photogram） | 将物体放在感光材料上曝光，无需相机即可成像。 |
| 爬移（creep） | 折叠套入的内层纸张因厚度而向外突出。 |
| 逐行满排（set to measure） | 调整一行文字，使其排满设定行宽；本页用于模拟木活字海报。 |
| 褐斑（foxing） | 纸张老化时出现的褐色或红褐色斑点，不等同于霉斑。 |

部分参考资料：[Adobe 叠印说明](https://helpx.adobe.com/cn/illustrator/using/overprinting.html)、[Adobe 陷印说明](https://helpx.adobe.com/cn/illustrator/using/trapping.html)、[MoMA 物影摄影释义](https://www.moma.org/collection/terms/photogram)、[W3C《中文排版需求》](https://www.w3.org/TR/clreq/)与 [Adobe 小册子印刷说明](https://helpx.adobe.com/cn/indesign/desktop/print/print-booklets/booklet-printing-settings.html)。

</details>

## 许可与致谢

- **代码：** MIT 许可。
- **文字说明与页面绘制的示例图：** CC BY 4.0，转载或改编请注明 Print Labs。
- 字体、引用资料和商标适用各自权利人的条款。

完整范围见 [LICENSE](LICENSE)。由 [Gengyuan Zhang](https://gengyuanmax.github.io/) 与 Claude 协作完成。
