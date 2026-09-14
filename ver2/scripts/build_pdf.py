"""Eight-page v2 portfolio. Shared content with the v2 website."""
from pathlib import Path
from html import escape
import json
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
D=json.loads((ROOT/'data/portfolio.json').read_text())
OUT=ROOT.parent/'downloads/kim-donghak-portfolio-v2.pdf'
pdfmetrics.registerFont(TTFont('KR','/System/Library/Fonts/Supplemental/Arial Unicode.ttf'))
W,H=595.276,841.89; L=42; CW=W-2*L
INK='#14233b'; BLUE='#245de5'; MUTED='#50617a'; LINE='#dbe3ee'; PALE='#f2f6fc'
C=canvas.Canvas(str(OUT),pagesize=(W,H))
C.setTitle('김동학 포트폴리오 · Ver.2'); C.setAuthor('김동학')

def para(s,x,y,w,size=10.2,leading=16,color=INK):
    s=s.replace('–','-').replace('—','-')
    p=Paragraph(escape(s).replace('\n','<br/>'),ParagraphStyle('p',fontName='KR',fontSize=size,leading=leading,textColor=colors.HexColor(color),wordWrap='CJK'))
    _,h=p.wrap(w,H);p.drawOn(C,x,y-h);return y-h
def line(y):
    C.setStrokeColor(colors.HexColor(LINE));C.setLineWidth(.7);C.line(L,y,W-L,y)
def page(n,label):
    C.bookmarkPage(str(n))
    para('DH. / KIM DONGHAK',L,H-22,280,8,12,BLUE)
    para(label,W-247,H-22,205,8,12,MUTED);line(H-42);line(39)
    para('PORTFOLIO V2 · 2026.09',L,30,300,8,11,MUTED)
    para(f'{n:02} / 08',W-82,30,45,8,11,MUTED)
def section(title,body,y):
    y=para(title,L,y,CW,11,17,BLUE)-6
    return para(body,L,y,CW,10.2,16)-15
def shot(im,y,maxh=245):
    image=ImageReader(str(ROOT/im['src']));iw,ih=image.getSize()
    scale=min(CW/iw,maxh/ih);w=iw*scale;h=ih*scale
    C.setFillColor(colors.HexColor(PALE));C.rect(L,y-h,CW,h,stroke=0,fill=1)
    C.drawImage(image,L+(CW-w)/2,y-h,w,h,mask='auto')
    return para(im['caption'],L,y-h-8,CW,8.2,12,MUTED)-18
def bullets(items,y,size=10):
    for s in items:y=para('• '+s,L,y,CW,size,15,MUTED)-5
    return y-8
def evidence(p,y):
    y=para(p['evidence'],L,y,CW,8,12,MUTED)-7
    x=L
    for a in p['links']:
        para(a['label'],x,y,220,9,14,BLUE)
        C.linkURL(a['url'],(x,y-14,x+200,y),relative=0,thickness=0);x+=220
    return y-15
def finish(y,name):
    assert y>48,(name,y)
    C.showPage()
def header(p,n,number,label=None):
    page(n,label or p['english'])
    para(number,L,775,70,22,30,BLUE)
    para(p['name'],L+78,778,CW-78,26,36)
    y=para(p['title'],L+78,739,CW-78,13,20)-15
    y=para(p['summary'],L,y,CW,10.3,16,MUTED)-12
    y=para(p['period']+'  |  '+p['role'],L,y,CW,9,14,BLUE)-6
    return y

page(1,'INTRODUCTION / BACKGROUND')
para('김동학',L,770,CW,17,25,BLUE)
y=para('화면에서 시작해,\n업무가 끝나는 곳까지.',L,723,CW,31,43)-19
y=para(D['intro'],L,y,CW,11,18,MUTED)-18
y=para('사용자가 일을 끝낼 수 있는 흐름을 만듭니다.\n화면의 사용성, 데이터 연결, 운영의 제약을 함께 살핍니다.',L,y,CW,11,18)-24
line(y);y-=20
for title,items in [('경력',D['experience'][:2]),('교육',D['experience'][2:])]:
    y=para(title,L,y,CW,12,18,BLUE)-10
    for x in items:
        para(x['date'],L,y,105,8.8,14,MUTED)
        yy=para(x['title'],L+115,y,CW-115,10,15)-3
        yy=para(x['detail'],L+115,yy,CW-115,9,14,MUTED)
        y=yy-13
    y-=5
y=para('AWS SAA · 2026.05 취득   /   SQLD · 2023.12 합격, 갱신 완료',L,y,CW,8.6,14,MUTED)-12
para('github.com/donghakk',L,y,CW,10,16,BLUE)
C.linkURL(D['github'],(L,y-16,L+220,y),relative=0,thickness=0)
finish(y-16,'intro')

page(2,'INDEX / SELECTED WORK')
para('Index',L,760,CW,38,48)
para('제품 화면에서 운영까지, 직접 맡은 다섯 가지 사례',L,697,CW,12,19,MUTED)
y=621
entries=[('01','셀프애드','모바일 UI와 광고 업무 흐름','실제 운영 UI · 2 pages',3),('02','IRM','수집·검토·발송을 잇는 업무 자동화','설명용 UI 목업',5),('03','산책온','지도 표시와 CI/CD·배포 설계','본인 담당 범위 · 설명용 배포 목업',6),('04','SSAFY 프로젝트','04.1 PennyPal — 가입·검증·금융 탐색\n04.2 별일 — 회원·TTS 프론트엔드','실제 프로젝트 UI',7)]
for num,name,desc,meta,dest in entries:
    line(y+14);para(num,L,y,50,17,24,BLUE)
    para(name,L+64,y,CW-110,21,29)
    para(f'{dest:02}',W-78,y,36,12,20,MUTED)
    yy=para(desc,L+64,y-38,CW-64,11,18,MUTED)-6
    para(meta,L+64,yy,CW-64,9,14,BLUE)
    C.linkRect('',str(dest),(L,y-95,W-L,y+14),relative=0,thickness=0)
    y-=123
finish(y,'index')

p=D['projects'][0]
y=header(p,3,'01')
y=para(p['employment'],L,y,CW,8.4,13,MUTED)-17
y=shot(p['images'][0],y,247)
y=section('문제와 선택',p['problem']+' '+p['decision'],y)
y=section('본인 기여', 'React 기반 활동 홈, 마이비즈의 URL 기반 이동, 공통 모달·모바일 바텀시트와 FAQ를 구현했습니다. 기존 API를 화면 흐름에 맞게 조합하고 모바일 노출 문제를 정비했습니다.',y)
y=para('다음 페이지에서 실제 FAQ 화면과 구현 범위를 이어서 소개합니다.',L,y,CW,9,14,BLUE)
finish(y,'selfad-main')

page(4,'01 / SELFAD · IMPLEMENTATION')
y=para('셀프애드 · 화면과 구현 범위',L,777,CW,22,32)-17
y=shot(p['images'][1],y,285)
y=section('내가 구현한 부분','활동 홈·이동·공통 모달을 하나의 사용 흐름으로 정비했습니다.',y)
y=bullets(p['implementation'],y)
y=section('결과',p['result'],y)
y=para(p['scope'],L,y,CW,8.5,13,MUTED)-18
y=evidence(p,y)
finish(y,'selfad-detail')

p=D['projects'][1]
y=header(p,5,'02')
y=para(p['employment'],L,y,CW,8.4,13,MUTED)-16
y=shot(p['images'][0],y,217)
y=section('선택과 구현',p['decision'],y)
y=bullets(['수집·정제 결과를 중복 관리, 검토, 발송 상태와 이력에 연결','발송 전 검증·한도·수신거부 처리와 실행 로그 구성','관리자 권한 요청을 철회하고 실행 역할·한정된 역할 전달 권한으로 요청 축소'],y)
y=section('결과',p['result'],y)
y=para(p['scope'],L,y,CW,8.4,13,MUTED)-12
y=evidence(p,y)
finish(y,'irm')

p=D['projects'][2]
y=header(p,6,'03')
y=shot(p['images'][0],y-7,224)
y=section('CI/CD · 배포 설계', 'Terraform으로 AWS PoC 인프라를 구성하고 GitHub Actions OIDC로 배포를 연결했습니다. Nginx의 웹/API 경로를 통합하고, 버전별 웹 release와 readiness 확인 후 전환·이전 release 복구 경계를 구성했습니다.',y)
y=section('지도 프론트엔드', '정적 타일 → Web Worker 계산 → revision 확인 → Canvas 표시로 건물 그림자를 구현했습니다. viewport 변경·OFF·dispose 시 취소하고, 오래된 결과와 네트워크·Worker 타임아웃을 처리했습니다.',y)
y=para(p['result'],L,y,CW,9.4,15,MUTED)-9
y=para(p['scope'],L,y,CW,8.4,13,MUTED)-12
y=evidence(p,y)
finish(y,'sanchaekon')

p=D['projects'][3]
y=header(p,7,'04.1','SSAFY PROJECTS / PENNYPAL')
y=para(p['employment'],L,y,CW,8.4,13,MUTED)-15
y=shot(p['images'][0],y,225)
y=section('선택과 구현',p['decision'],y)
y=bullets(p['implementation'],y)
y=para(p['scope'],L,y,CW,8.5,13,MUTED)-14
y=evidence(p,y)
finish(y,'pennypal')

p=D['projects'][4]
y=header(p,8,'04.2','SSAFY PROJECTS / STAR DIARY')
y=para(p['employment'],L,y,CW,8.4,13,MUTED)-15
y=shot(p['images'][0],y,220)
y=section('문제와 해결',p['problem']+' '+p['decision'],y)
y=bullets(['회원가입·회원정보·랜딩 및 TTS 화면의 UI·API 연결','Blob → object URL → 브라우저 오디오 재생·생성 음성 재전송','화면 상태와 요청 오류 처리'],y)
y=evidence(p,y)
finish(y,'stardiary')
C.save()
reader=PdfReader(OUT)
assert len(reader.pages)==8
assert all((p.extract_text() or '').strip() for p in reader.pages)
print({'pages':8,'bytes':OUT.stat().st_size,'output':str(OUT)})
