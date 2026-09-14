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

- `assets/profile.png`: user-provided portrait added to the introductory website section and PDF page 1. Original image bytes and aspect ratio retained.

- `assets/selfad-mobile-*.jpg`: actual mobile Chrome captures from https://selfad.co.kr on 2026-09-14 (390×844 viewport override requested by the user). Existing advertiser login reused for Biz Home and navigation; public FAQ and empty influencer signup/consent captured. Screens show no names/contact/customer records, and no form entries or submissions occurred. Web includes five views; PDF uses four representative views. Current UI may include later team changes.
- `assets/irm-system-design.png` / `.svg`: system architecture diagram built from verified implementation facts. Separates local Naver/Instagram collection, AWS Fargate YouTube collection and email sending, Google Sheets review/state/history, and operational support. Rebuild with `scripts/build_irm_diagram.py` and Poppler; no simulated product UI.
- `assets/sanchaekon-deployment-concept.png`: generated explanatory mockup of personal CI/CD/infrastructure work. The repeated Nginx denotes the same component in service and release flows. Does not claim automatic rollback.
- PennyPal and Star Diary images are preserved existing repository assets. Star Diary is explicitly attributed as team UI; individual scope is member/landing/TTS frontend, not Three.js or voice-model implementation.

## Verification

All eight PDF pages rendered and visually inspected. FAQ and IRM pages rechecked after final changes. HTML IDs, anchor targets, image alt text and local file targets validated. Responsive CSS provided; interactive browser testing was not performed in this change. The earlier version's tracked files are unchanged. No public push, deployment or application upload performed.
