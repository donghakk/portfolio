# Portfolio ver2.1

Current public edition based on the preserved ver2 portfolio. The content, section sequence and responsive column structure remain the same. At the user’s request, the Selfad media section embeds the two live LPs instead of the ver2 video players. The original ver2 source is preserved. The root portfolio address now redirects to this version, as requested by the user.

- Preview / public route: `/ver2.1/`
- Original: `/ver2/`
- Shared media: `../ver2/assets/` and `../assets/`
- PDF: current 8-page `../downloads/kim-donghak-portfolio-v2.1.pdf`; original ver2 PDF preserved.
- Rebuild HTML: `PYTHONDONTWRITEBYTECODE=1 python3 ver2.1/scripts/build.py` from the repository root

Visual direction: bright editorial typography, cobalt and ink accents, a translucent sticky navigation, framed media, clearer surface hierarchy, and subtle hover/entrance motion. No new image assets, external fonts, libraries or network dependencies.

Progressive enhancement highlights the section being read. All content remains visible without JavaScript; reduced-motion preferences disable transitions and entrance motion. Keyboard focus indicators remain available. The two lazy-loaded iframes have descriptive titles and adjacent links to open the operating pages separately.

Validation: text and section order outside the requested LP media replacement are compared against ver2. Local references and JavaScript syntax are checked. Entry and section-navigation behavior were subsequently tested in the browser for the iframe scroll correction.

## Live Selfad LPs

- Advertiser: https://selfad.co.kr/lp/marketer
- Influencer: https://selfad.co.kr/lp/influencer
- HTTP headers and the HTML entrypoint were checked on 2026-09-15: neither X-Frame-Options nor CSP frame-ancestors restrictions were present. Live availability and content follow the source site. No copied product HTML or login session is bundled.

## Entry behavior

The root address redirects explicitly to `/ver2.1/#intro`. Remote LP frames receive their `src` only when they intersect the viewport; native lazy loading alone can start offscreen frames early enough to take focus and scroll the parent away from the introduction. Direct section links still work. Without JavaScript, the adjacent operating-page links remain available.


## Public project terminology (2026-09-30)

At the user's request, the former internal project label is now “인플루언서 발굴·메일 발송 자동화 도구”; compact navigation uses “영업 자동화”. `data/terminology.json` supplies the web heading, PDF, and architecture diagram. Existing `#irm` fragment links continue to work. Original ver2 content and PDF remain unchanged.

Build the diagram with `scripts/build_automation_diagram.py`, render its intermediate PDF from `/private/tmp/career-portfolio-v21-qa/` to `assets/influencer-automation-system-design.png` at 1600×900 with pdftoppm, then run `scripts/build_pdf.py` and `scripts/build.py`. Python requires reportlab and pypdf; use PYTHONDONTWRITEBYTECODE=1.
