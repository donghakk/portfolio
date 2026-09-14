# Portfolio version 2

Current public portfolio: https://donghakk.github.io/portfolio/ver2/
The repository root redirects here.

- Content: `data/portfolio.json`
- Readable manuscript: `manuscript.md`
- PDF: `../downloads/kim-donghak-portfolio-v2.pdf` (8 pages)
- Build web from repository root: `PYTHONDONTWRITEBYTECODE=1 python3 ver2/scripts/build.py`
- Build PDF: `ver2/scripts/build_pdf.py`; requires ReportLab, pypdf and macOS Arial Unicode font.

Order: introduction/photo/career/education, Index, Selfad, IRM, Sanchaekon, SSAFY (PennyPal, Star Diary).

## Media provenance

- `assets/profile.png`: user-provided portrait. Original bytes and aspect ratio retained.
- `assets/lp/`: actual public advertiser and influencer LP captures from https://selfad.co.kr/lp/marketer and https://selfad.co.kr/lp/influencer on 2026-09-15. Chrome viewport 720×1280; all scroll-reveal sections were revealed before capturing. Actual full-page captures are 705 pixels wide. Promotional example data and later team changes may appear; these are not individual performance claims.
- `marketer-scroll.mp4` and `influencer-scroll.mp4`: vertical pans of those real captures, not recordings of live interactions. H.264, 704×1252, 30fps, 26 seconds, no audio, fast-start. One pixel trimmed for even codec width; no upscaling. Web players have native controls, posters and no autoplay. PDF uses four representative stills and links to the web videos.
- Rebuild videos with `python3 ver2/scripts/build_lp_videos.py CAPTURE_DIR FFMPEG_PATH`; requires Pillow and ffmpeg. Input names: `marketer-final.jpg`, `influencer-final.jpg`. Capture provenance and sizes are in `assets/lp/manifest.json`.
- Earlier `assets/selfad-mobile-*.jpg` captures are retained as previous assets and are no longer shown in the current gallery.
- `assets/irm-system-design.png` / `.svg`: verified system architecture, separating local Naver/Instagram collection, AWS Fargate YouTube collection and email sending, Google Sheets state/history and operational support. Rebuild with `scripts/build_irm_diagram.py` and Poppler.
- `assets/sanchaekon-deployment-concept.png`: explanatory mockup of personal CI/CD/infrastructure work. Repeated Nginx denotes the same component in service and release flows. Does not claim automatic rollback.
- PennyPal and Star Diary use existing repository images; team UI and individual frontend contributions are distinguished.

## Verification

All eight PDF pages were rendered and inspected during version 2 work; changed LP pages 3–4 were re-rendered and inspected after the video update. Both MP4s passed complete ffmpeg decoding; start/middle/end frames were reviewed. Native browser playback and local media references were checked before publication.
