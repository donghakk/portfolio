"""Build the static portfolio from the same content used by the PDF exporter."""
import json
from html import escape as esc
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'data/portfolio.json').read_text())
def e(value):
    return esc(str(value), quote=True)
def links(project):
    return ''.join(f'<a href="{e(x["url"])}" target="_blank" rel="noopener noreferrer">{e(x["label"])} <span aria-hidden="true">↗</span></a>' for x in project['links'])
def flow(project):
    return '<figure class="diagram"><ol>' + ''.join(f'<li><span class="step">0{i+1}</span><span>{e(s)}</span></li>' for i,s in enumerate(project['flow'])) + f'</ol><figcaption>{e(project["diagramCaption"])}</figcaption></figure>'
def project_html(p, i):
    images = ''.join(f'<figure><a href="{e(im["src"])}" target="_blank" rel="noopener noreferrer" aria-label="{e(im["alt"])} 크게 보기"><img src="{e(im["src"])}" alt="{e(im["alt"])}" width="1000" height="{474 if "signup" in im["src"] else 513}" loading="lazy"></a><figcaption>{e(im["caption"])}</figcaption></figure>' for im in p['images'])
    return f'''<article class="project" id="{e(p['id'])}" aria-labelledby="title-{e(p['id'])}">
<header class="project-header"><span class="project-index">{i+1:02}</span><div><p class="eyebrow">{e(p['english'])} <span>/ {e(p['category'])}</span></p><h2 id="title-{e(p['id'])}">{e(p['name'])}</h2><p class="project-title">{e(p['title'])}</p></div></header>
<p class="summary">{e(p['summary'])}</p>
<dl class="metadata"><div><dt>기간</dt><dd>{e(p['period'])}</dd></div><div><dt>역할</dt><dd>{e(p['role'])}</dd></div><div><dt>팀 / 상태</dt><dd>{e(p['team'])}<br>{e(p['status'])}</dd></div></dl>
<p class="employment">{e(p['employment'])}</p><ul class="tags" aria-label="사용 기술">{''.join(f'<li>{e(t)}</li>' for t in p['tech'])}</ul>
<div class="case-grid"><section><h3>문제와 제약</h3><p>{e(p['problem'])}</p></section><section><h3>선택과 이유</h3><p>{e(p['decision'])}</p></section></div>
{flow(p)}<section class="implementation"><h3>내가 구현한 부분</h3><ul>{''.join(f'<li>{e(s)}</li>' for s in p['implementation'])}</ul></section>
{f'<div class="gallery">{images}</div>' if images else ''}
<section class="result"><h3>결과와 확인 범위</h3><p>{e(p['result'])}</p><p class="scope">{e(p['scope'])}</p></section>
<footer class="project-footer"><p>{e(p['evidence'])}</p><div class="source-links">{links(p)}</div></footer></article>'''

nav = ''.join(f'<a href="#{e(p["id"])}"><span>{i+1:02}</span>{e(p["name"])}</a>' for i,p in enumerate(data['projects']))
cards = ''.join(f'<a class="project-link" href="#{e(p["id"])}"><span class="card-number">{i+1:02}</span><div><strong>{e(p["name"])}</strong><p>{e(p["category"])}</p></div><span aria-hidden="true">↗</span></a>' for i,p in enumerate(data['projects'][:3]))
skills = ''.join(f'<div><h3>{e(s["title"])}</h3><p>{e(s["tools"])}</p><span>{e(s["detail"])}</span></div>' for s in data['skills'])
timeline = ''.join(f'<li><span>{e(x["date"])}</span><div><h3>{e(x["title"])}</h3><p>{e(x["detail"])}</p></div></li>' for x in data['experience'])
html = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light dark"><title>김동학 | Frontend · Product Engineer</title><meta name="description" content="김동학의 개발 포트폴리오. Selfad 제품 화면, IRM 업무 자동화, 산책온 지도·배포와 React 기반 프로젝트의 개인 기여를 소개합니다."><link rel="stylesheet" href="styles.css"></head>
<body><a class="skip-link" href="#main">본문으로 건너뛰기</a><header class="topbar"><a href="#top" class="brand">DH<span>.</span></a><span>김동학 <span class="muted">/ Developer Portfolio</span></span><a class="github" href="{e(data['github'])}" target="_blank" rel="noopener noreferrer">GitHub ↗</a></header>
<div class="layout" id="top"><aside class="sidebar"><p class="eyebrow">SELECTED WORK</p><nav aria-label="프로젝트 목차">{nav}<a href="#background"><span>+</span>경력 · 교육</a></nav><a class="pdf-link" href="downloads/kim-donghak-portfolio.pdf" download>포트폴리오 PDF ↓</a><p class="updated">UPDATED {e(data['updated'])}</p></aside>
<main id="main"><section class="hero" aria-labelledby="intro-title"><p class="eyebrow">{e(data['role'])}</p><h1 id="intro-title">{e(data['headline']).replace(chr(10),'<br>')}</h1><p class="intro">{e(data['intro'])}</p><div class="project-directory">{cards}</div></section>
<section class="skills" aria-label="기술과 구현 경험">{skills}</section>
{''.join(project_html(p,i) for i,p in enumerate(data['projects']))}
<section class="background" id="background"><p class="eyebrow">BACKGROUND</p><h2>경력과 배움</h2><ol class="timeline">{timeline}</ol><div class="certificates"><h3>자격</h3>{''.join(f'<p>{e(c)}</p>' for c in data['certificates'])}</div><section class="working-style"><h3>함께 일하는 방식</h3><p>{e(data['workingStyle'])}</p></section></section>
<footer class="page-footer"><strong>김동학</strong><p>제품 화면 · 데이터 · 운영</p><a href="{e(data['github'])}" target="_blank" rel="noopener noreferrer">github.com/donghakk ↗</a><a href="#top">맨 위로 ↑</a></footer></main></div></body></html>'''
(ROOT / 'index.html').write_text(html, encoding='utf-8')
print('Built index.html from data/portfolio.json')
