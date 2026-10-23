"""Style edition of preserved v2, with user-requested live Selfad LP embeds."""
import json
import re
from html import escape
from pathlib import Path
from terminology import normalize_html
ROOT = Path(__file__).resolve().parents[1]
source = (ROOT.parent / 'ver2/index.html').read_text()
source = source.replace('포트폴리오 · Ver.2</title>', '포트폴리오 · Ver.2.1</title>')
# Share preserved v2 assets except the renamed diagram; retain existing section anchors.
for attr in ('src', 'href', 'poster'):
    source = source.replace(f'{attr}="assets/', f'{attr}="../ver2/assets/')
source = source.replace('업무가 끝나는 곳까지.</h1>', '<span>업무가 끝나는 곳까지.</span></h1>')
data = json.loads((ROOT.parent / 'ver2/data/portfolio.json').read_text())
cards = []
for lp in data['projects'][0]['videos']:
    title, url = escape(lp['title']), escape(lp['source'])
    cards.append(f'''<figure class="lp-preview"><div class="video-heading"><h3>{title}</h3><a href="{url}" target="_blank" rel="noopener">운영 페이지 ↗</a></div><iframe class="lp-frame" data-src="{url}" title="셀프애드 {title} 실제 운영 페이지" width="390" height="720" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" sandbox="allow-scripts allow-same-origin allow-forms allow-popups allow-popups-to-escape-sandbox"></iframe><figcaption>프레임 안에서 스크롤해 LP를 살펴보세요.</figcaption></figure>''')
media = '<div class="lp-embeds">' + ''.join(cards) + '</div><p class="media-note">실제 운영 페이지를 연결했습니다. 화면 속 금액·프로젝트는 서비스 소개용 예시를 포함합니다.</p>'
source, count = re.subn(r'<div class="lp-videos">.*?<p class="media-note">.*?</p>', lambda _: media, source, count=1, flags=re.S)
assert count == 1, 'Expected the original Selfad video block'
source = source.replace('</head>', '<meta name="theme-color" content="#f7f9fc"><script src="interactions.js?v=20260915-entry" defer></script></head>')
terms = json.loads((ROOT / 'data/terminology.json').read_text())
source = normalize_html(source)
source = source.replace('../ver2/assets/irm-system-design.png', 'assets/influencer-automation-system-design.png')
source = source.replace('../downloads/kim-donghak-portfolio-v2.pdf', '../downloads/kim-donghak-portfolio-v2.1.pdf')
assert 'IRM' not in source
assert '<h2>' + terms['display_name'] + '</h2>' in source
(ROOT / 'index.html').write_text(source)
print('Built ver2.1/index.html from preserved v2 content')
