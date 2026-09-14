# 김동학 · Developer Portfolio

제품 프론트엔드, 업무 자동화, 서비스 통합의 개인 구현 사례를 소개하는 정적 포트폴리오입니다.

- 공개 사이트: https://donghakk.github.io/portfolio/ (현재 `/ver2/`로 이동)
- 현재 웹·공통 원고: `ver2/index.html`, `ver2/data/portfolio.json`
- 읽기용 원고: `ver2/manuscript.md`
- 현재 PDF: `downloads/kim-donghak-portfolio-v2.pdf` (8쪽)
- 구성: 소개·사진·경력·교육 → Index → 셀프애드 → IRM → 산책온 → SSAFY(PennyPal·별일)

## 빌드

저장소 루트에서 실행합니다. 웹에는 Python 3.10 이상, PDF에는 ReportLab·pypdf와 macOS Arial Unicode 글꼴이 필요합니다.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 ver2/scripts/build.py
PYTHONDONTWRITEBYTECODE=1 python3 ver2/scripts/build_pdf.py
PYTHONDONTWRITEBYTECODE=1 python3 -m http.server 4317 --bind 127.0.0.1
```

기존 루트 `scripts/`와 `data/`는 이전 버전입니다. 현재 사이트를 수정할 때는 `ver2/`를 사용합니다. 원고 변경 후 웹·PDF를 함께 생성하고 PDF를 렌더링해 확인합니다.

## 미디어와 배포

셀프애드 광고주·인플루언서 운영 LP의 실제 모바일 캡처를 각각 26초 MP4로 구성했습니다. 재생은 사용자가 시작하며 전체 페이지 이미지도 열 수 있습니다. 출처와 생성 방법은 `ver2/README.md`에 있습니다.

GitHub Pages는 `main` 브랜치의 루트를 배포합니다. 개인 기여와 팀 성과, 유급 경력과 무급 참여를 구분하며 미검증 성과 수치는 제시하지 않습니다.
