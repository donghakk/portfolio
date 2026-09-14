"""Style-only edition of the preserved v2 document. Run after changing v2.1 CSS/JS."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
source = (ROOT.parent / 'ver2/index.html').read_text()
source = source.replace('포트폴리오 · Ver.2</title>', '포트폴리오 · Ver.2.1</title>')
# Share the original assets/PDF; preserve original text, order, anchors and layout.
for attr in ('src', 'href', 'poster'):
    source = source.replace(f'{attr}="assets/', f'{attr}="../ver2/assets/')
source = source.replace('업무가 끝나는 곳까지.</h1>', '<span>업무가 끝나는 곳까지.</span></h1>')
source = source.replace('</head>', '<meta name="theme-color" content="#f7f9fc"><script src="interactions.js" defer></script></head>')
(ROOT / 'index.html').write_text(source)
print('Built ver2.1/index.html from preserved v2 content')
