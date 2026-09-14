"""Build version 2 without changing the first portfolio version."""
import json
from pathlib import Path
from html import escape as e

ROOT = Path(__file__).resolve().parents[1]
D = json.loads((ROOT/'data/portfolio.json').read_text())

def timeline(items):
    return ''.join(f'<li><span>{e(x["date"])}</span><div><strong>{e(x["title"])}</strong><p>{e(x["detail"])}</p></div></li>' for x in items)

def picture(im):
    return f'<figure><a href="{e(im["src"])}" target="_blank" rel="noopener" aria-label="{e(im["alt"])} 크게 보기"><img src="{e(im["src"])}" alt="{e(im["alt"])}" width="{im["width"]}" height="{im["height"]}" loading="lazy"></a><figcaption>{e(im["caption"])}</figcaption></figure>'

def media(p):
    if not p.get('videos'):
        return f'<div class="gallery">{"".join(picture(i) for i in p["images"])}</div>'
    cards=[]
    for v in p['videos']:
        cards.append(f'''<figure class="lp-video"><div class="video-heading"><h3>{e(v['title'])}</h3><a href="{e(v['source'])}" target="_blank" rel="noopener">운영 페이지 ↗</a></div><video controls playsinline muted preload="none" poster="{e(v['poster'])}" width="704" height="1252" aria-label="{e(v['title'])} 스크롤 영상"><source src="{e(v['src'])}" type="video/mp4"><a href="{e(v['src'])}">영상 다운로드</a></video><figcaption>{e(v['caption'])}</figcaption><a class="full-capture" href="{e(v['full'])}" target="_blank" rel="noopener">전체 화면 크게 보기 ↗</a></figure>''')
    return '<div class="lp-videos">'+''.join(cards)+'</div><p class="media-note">실제 운영 LP의 화면 캡처를 스크롤 영상으로 구성했습니다. 화면 속 금액·프로젝트는 서비스 소개용 예시를 포함합니다.</p>'

def project(p, number):
    return f'''<article id="{p['id']}" class="case"><header class="case-heading"><span class="number">{number}</span><div><p class="eyebrow">{e(p['english'])}</p><h2>{e(p['name'])}</h2><p class="case-title">{e(p['title'])}</p></div></header>
<p class="lead">{e(p['summary'])}</p><div class="meta"><span>{e(p['period'])}</span><span>{e(p['role'])}</span><span>{e(p['team'])}</span></div><p class="small">{e(p['employment'])}</p>
{media(p)}
<div class="columns"><section><h3>문제</h3><p>{e(p['problem'])}</p></section><section><h3>선택과 구현</h3><p>{e(p['decision'])}</p></section></div>
<section class="contribution"><h3>내가 맡은 부분</h3><ul>{''.join('<li>'+e(s)+'</li>' for s in p['implementation'])}</ul></section>
<section class="result"><h3>결과와 현재 상태</h3><p>{e(p['result'])}</p><p class="small">{e(p['scope'])}</p></section>
<p class="tech">{' · '.join(e(t) for t in p['tech'])}</p><footer class="evidence"><span>{e(p['evidence'])}</span><div>{''.join(f'<a href="{e(a["url"])}" target="_blank" rel="noopener">{e(a["label"])}</a>' for a in p['links'])}</div></footer></article>'''

P=D['projects']
nav=[('intro','소개'),('index','Index'),('selfad','셀프애드'),('irm','IRM'),('sanchaekon','산책온'),('ssafy','SSAFY')]
index=''.join(f'<a href="#{pid}"><span>0{i+1}</span><div><h3>{name}</h3><p>{desc}</p></div><span class="page-no">{page}</span></a>' for i,(pid,name,desc,page) in enumerate([
('selfad','셀프애드','운영 플랫폼의 모바일 UI와 업무 흐름','03'),('irm','IRM','수집부터 발송까지 이어지는 업무 자동화','05'),('sanchaekon','산책온','지도 표시와 배포 설계 · 본인 기여','06'),('ssafy','SSAFY 프로젝트','PennyPal · 별일','07–08')]))
html=f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>김동학 포트폴리오 · Ver.2</title><meta name="description" content="김동학의 소개, 경력과 교육, 셀프애드·IRM·산책온·SSAFY 프로젝트 포트폴리오"><link rel="stylesheet" href="styles.css"></head><body>
<a class="skip" href="#intro">본문으로 건너뛰기</a><header class="top"><a class="brand" href="#intro">DH.</a><nav aria-label="포트폴리오 목차">{''.join(f'<a href="#{a}">{b}</a>' for a,b in nav)}</nav><a class="download" href="../downloads/kim-donghak-portfolio-v2.pdf" download>PDF ↓</a></header>
<main><section id="intro" class="intro"><p class="eyebrow">KIM DONGHAK / FRONTEND · PRODUCT ENGINEER</p><div class="intro-heading"><h1>화면에서 시작해,<br>업무가 끝나는 곳까지.</h1><img class="portrait" src="assets/profile.png" alt="김동학 프로필 사진" width="1086" height="1448"></div><p class="bio"><strong>안녕하세요, 김동학입니다.</strong><br>{e(D['intro'])}</p><p class="value">사용자가 일을 끝낼 수 있는 흐름을 만듭니다.<br>화면의 사용성, 데이터 연결, 운영의 제약을 함께 살핍니다.</p>
<div class="background"><section><h2>경력</h2><ol>{timeline(D['experience'][:2])}</ol></section><section><h2>교육</h2><ol>{timeline(D['experience'][2:])}</ol></section></div>
<div class="intro-footer"><span>AWS SAA · SQLD</span><a href="{D['github']}" target="_blank" rel="noopener">github.com/donghakk ↗</a></div></section>
<section id="index" class="index"><p class="eyebrow">SELECTED WORK / 2026.09</p><h2>Index<span>개요</span></h2><div>{index}</div><p class="small">오른쪽 숫자는 PDF 페이지입니다.</p></section>
{''.join(project(p,f'0{i+1}') for i,p in enumerate(P[:3]))}
<section id="ssafy" class="ssafy"><p class="eyebrow">04 / SSAFY PROJECTS</p><h2>팀 안에서 만든 두 가지 경험</h2><p>삼성 청년 SW 아카데미 10기 · 6인 팀 프로젝트<br>회원 기능과 데이터 탐색, 브라우저 음성 처리의 프론트엔드를 담당했습니다.</p><nav aria-label="SSAFY 하위 프로젝트"><a href="#pennypal">04.1 PennyPal</a><a href="#stardiary">04.2 별일</a></nav>
{''.join(project(p,f'04.{i+1}') for i,p in enumerate(P[3:]))}</section>
<footer class="end"><strong>김동학</strong><span>Frontend · Product Engineer</span><a href="#intro">처음으로 ↑</a></footer></main></body></html>'''
(ROOT/'index.html').write_text(html)
print('Built ver2/index.html')
