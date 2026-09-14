# Portfolio version 2

Separate review version; the repository root remains version 1.

- Preview: `/ver2/`
- Content: `data/portfolio.json`
- Readable manuscript: `manuscript.md`
- PDF: `../downloads/kim-donghak-portfolio-v2.pdf` (8 pages)
- Build web: `PYTHONDONTWRITEBYTECODE=1 python3 ver2/scripts/build.py` from the repository root.
- Build PDF: run `ver2/scripts/build_pdf.py` with Python containing ReportLab and pypdf. Requires macOS Arial Unicode font.

Order: introduction/career/education, Index, Selfad, IRM, Sanchaekon, SSAFY projects (PennyPal, Star Diary).

## Image provenance

- `assets/selfad-home.jpg`, `assets/selfad-faq.jpg`: Chrome captures of the public operating site https://selfad.co.kr on 2026-09-14. FAQ is a direct screenshot region. No account login or customer records used. Home contains the service's own illustrative promotional data; the complete home page is not claimed as personal implementation.
- `assets/irm-concept.png`: generated explanatory UI mockup, not the internal production UI. Illustrative channel icons and sample data; actual work uses Google Sheets, YouTube/Naver/Instagram collection, and the documented sending workflow.
- `assets/sanchaekon-deployment-concept.png`: generated explanatory mockup of personal CI/CD/infrastructure work. The repeated Nginx denotes the same component in service and release flows. Does not claim automatic rollback.
- PennyPal and Star Diary images are preserved existing repository assets. Star Diary is explicitly attributed as team UI; individual scope is member/landing/TTS frontend, not Three.js or voice-model implementation.

## Verification

All eight PDF pages rendered and visually inspected. FAQ and IRM pages rechecked after final changes. HTML IDs, anchor targets, image alt text and local file targets validated. Responsive CSS provided; interactive browser testing was not performed in this change. The earlier version's tracked files are unchanged. No public push, deployment or application upload performed.
