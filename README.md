# 김동학 · Developer Portfolio

제품 프론트엔드, 업무 자동화, 서비스 통합의 개인 구현 사례를 소개하는 정적 웹 포트폴리오입니다.

- 기존 공개 주소: https://donghakk.github.io/portfolio/
- 웹: `index.html` / `styles.css`
- 웹·PDF 공통 원고: `data/portfolio.json`
- PDF: `downloads/kim-donghak-portfolio.pdf` (9쪽)
- 기존 `assets/` 원본은 보존했습니다.

## 원고 수정과 빌드

Python 3.10 이상으로 웹을 생성합니다. 외부 패키지는 필요하지 않습니다.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/build.py
PYTHONDONTWRITEBYTECODE=1 python3 -m http.server 4317 --bind 127.0.0.1
```

PDF 생성에는 `reportlab`, `pypdf`와 한국어 글꼴이 필요합니다. 생성 스크립트의 글꼴 경로는 macOS Arial Unicode를 사용합니다. 다른 환경에서는 해당 글꼴 경로를 바꿔야 합니다.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_pdf.py
```

PDF는 명시적인 페이지 구성을 사용하므로 원고를 늘린 뒤에는 페이지 하단 검사와 전 페이지 렌더링 검토를 함께 수행해야 합니다. 생성물은 GitHub Pages에서 별도 서버 없이 제공됩니다.

## 콘텐츠 원칙

- 개인 기여와 팀 성과, 유급 경력과 프로젝트 참여를 구분합니다.
- 구현, 당시 검증 기록, 현재 운영 상태를 구분합니다.
- 사내 자료와 미검증 성과 수치를 공개하지 않습니다.
- 프로젝트 기술 전체를 개인 보유 기술로 옮기지 않습니다.
- 공통 원고를 변경한 뒤 웹과 PDF를 함께 다시 생성합니다.

## 이미지

PennyPal 화면은 기존 공개 포트폴리오의 이미지를 재사용했습니다. 회원가입 UI·검증과 금융 탐색 데이터 연결의 기여를 설명하며, 서비스의 팀 디자인과 개인 구현 범위를 구분합니다. 다른 프로젝트의 기존 이미지도 `assets/`에 보존되어 있습니다.

## 배포

기존 GitHub Pages 설정을 유지합니다. 검토한 변경을 공개 브랜치에 반영하면 기존 Pages 배포 흐름을 따릅니다. 공개 사이트 갱신 전 본문·자료 공개 범위와 PDF를 검토합니다.
