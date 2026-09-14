# Portfolio ver2.1

Styling study of the preserved ver2 portfolio. The content, section sequence and responsive column structure remain the same. At the user’s request, the Selfad media section embeds the two live LPs instead of the ver2 video players. The original ver2 source and root default route remain intact.

- Preview / public route: `/ver2.1/`
- Original: `/ver2/`
- Shared media: `../ver2/assets/` and `../assets/`
- PDF: the existing, unchanged 8-page ver2 PDF
- Rebuild HTML: `PYTHONDONTWRITEBYTECODE=1 python3 ver2.1/scripts/build.py` from the repository root

Visual direction: bright editorial typography, cobalt and ink accents, a translucent sticky navigation, framed media, clearer surface hierarchy, and subtle hover/entrance motion. No new image assets, external fonts, libraries or network dependencies.

Progressive enhancement highlights the section being read. All content remains visible without JavaScript; reduced-motion preferences disable transitions and entrance motion. Keyboard focus indicators remain available. The two lazy-loaded iframes have descriptive titles and adjacent links to open the operating pages separately.

Validation: visible text, ordered IDs, link targets and media are compared against ver2. Local asset references and JavaScript syntax are checked. Browser visual/interaction QA was not performed for this styling study.

## Live Selfad LPs

- Advertiser: https://selfad.co.kr/lp/marketer
- Influencer: https://selfad.co.kr/lp/influencer
- HTTP headers and the HTML entrypoint were checked on 2026-09-15: neither X-Frame-Options nor CSP frame-ancestors restrictions were present. Live availability and content follow the source site. No copied product HTML or login session is bundled.
