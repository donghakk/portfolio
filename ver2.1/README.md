# Portfolio ver2.1

Styling study of the preserved ver2 portfolio. The content, section sequence, responsive column structure, links and media remain the same. The original ver2 source and root default route remain intact.

- Preview / public route: `/ver2.1/`
- Original: `/ver2/`
- Shared media: `../ver2/assets/` and `../assets/`
- PDF: the existing, unchanged 8-page ver2 PDF
- Rebuild HTML: `PYTHONDONTWRITEBYTECODE=1 python3 ver2.1/scripts/build.py` from the repository root

Visual direction: bright editorial typography, cobalt and ink accents, a translucent sticky navigation, framed media, clearer surface hierarchy, and subtle hover/entrance motion. No new image assets, external fonts, libraries or network dependencies.

Progressive enhancement highlights the section being read. All content remains visible without JavaScript; reduced-motion preferences disable transitions and entrance motion. Native video controls and keyboard focus indicators remain available.

Validation: visible text, ordered IDs, link targets and media are compared against ver2. Local asset references and JavaScript syntax are checked. Browser visual/interaction QA was not performed for this styling study.
