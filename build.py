#!/usr/bin/env python3
"""Build Print Labs.

Sources live in src/: shared.css and links.js are shared by every page; each page source has a
/*@shared*/ marker at the top of its <style> and a <script>/*@links*/</script> placeholder.

Outputs:
  index.html, print.html, layout.html  full documents for GitHub Pages (repo root)
  dist/<name>.html                     body-only versions for claude.ai artifacts (the host adds the doctype)
"""
import pathlib, re

ROOT = pathlib.Path(__file__).parent
SRC, DIST = ROOT / 'src', ROOT / 'dist'
PAGES = {'home.html': 'index.html', 'print.html': 'print.html', 'layout.html': 'layout.html', 'object.html': 'object.html'}
HOME_ARTIFACT = 'https://claude.ai/artifact/PeE1kDmTykEsa3FWtq1ujK'
OBJECT_ARTIFACT = 'https://claude.ai/artifact/MDsc8WCa1yWzZArUPnWvAo'

def inline(src: str) -> str:
    shared = (SRC / 'shared.css').read_text()
    links = (SRC / 'links.js').read_text().replace('@ART_HOME@', HOME_ARTIFACT).replace('@ART_OBJECT@', OBJECT_ARTIFACT)
    assert src.count('/*@shared*/') == 1 and src.count('/*@links*/') == 1
    return src.replace('/*@shared*/', shared).replace('/*@links*/', links)

def document(body: str) -> str:
    # move everything before the first <div class="wrap"> (title, fonts, style) into <head>
    i = body.index('<div class="wrap">')
    head, rest = body[:i], body[i:]
    head = head.replace('body{background:var(--paper)', 'body{margin:0;background:var(--paper)', 1)
    return ('<!doctype html>\n<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + head + '</head>\n<body>\n' + rest + '</body>\n</html>\n')

DIST.mkdir(exist_ok=True)
for src_name, out_name in PAGES.items():
    body = inline((SRC / src_name).read_text())
    (DIST / src_name).write_text(body)
    (ROOT / out_name).write_text(document(body))
    print(f'built {out_name} ({len(body)//1024} KB)')
