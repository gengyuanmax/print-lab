/* links.js — where the pages of Print Labs live. On GitHub Pages or from local files the pages sit side by side;
   inside claude.ai each page is its own artifact, so the links go to the published artifacts instead. */
(() => {
  const h = location.hostname;
  const local = h.endsWith('github.io') || location.protocol === 'file:' || h === 'localhost' || h === '127.0.0.1';
  const FILE = {home:'index.html', print:'print.html', layout:'layout.html', object:'object.html', element:'element.html'};
  const ART = {
    home:'@ART_HOME@',
    print:'https://claude.ai/artifact/BEBGEYAVkseDmEd78EbxS4',
    layout:'https://claude.ai/artifact/3kpSy3NxXfTr8N6h2EhqAB',
    object:'@ART_OBJECT@',
    element:'@ART_ELEMENT@',
  };
  const wire = () => document.querySelectorAll('a[data-page]').forEach(a => {
    const k = a.dataset.page;
    if (local || !ART[k] || ART[k].startsWith('@')) { a.href = FILE[k]; return; }
    a.href = ART[k]; a.target = '_blank'; a.rel = 'noopener';
  });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', wire); else wire();
})();
