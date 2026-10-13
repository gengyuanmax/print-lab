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

Open `index.html` in a browser or host it on any static server such as GitHub Pages. The only external dependency is Google Fonts. Ink colours are on-screen approximations; check a print shop's physical swatches for real results.
