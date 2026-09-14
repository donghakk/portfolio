"""Nine-page portfolio, sourced from data/portfolio.json. No external uploads."""
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
OUT=ROOT/'downloads/kim-donghak-portfolio.pdf'
OUT.parent.mkdir(exist_ok=True)
pdfmetrics.registerFont(TTFont('KR','/System/Library/Fonts/Supplemental/Arial Unicode.ttf'))
W,H=595.276,841.89
INK='#132238'; BLUE='#215cdf'; MUTED='#4c5b70'; LINE='#dbe2ed'; PALE='#f3f6fb'; NAVY='#112642'
C=canvas.Canvas(str(OUT),pagesize=(W,H))
C.setTitle('김동학 | Frontend · Product Engineer Portfolio')
C.setAuthor('김동학')
L=43; CW=W-2*L
def norm(s): return s.replace('–','-').replace('—','-')
def para(s,x,y,w,size=10.2,leading=16,color=INK):
    st=ParagraphStyle('p',fontName='KR',fontSize=size,leading=leading,textColor=colors.HexColor(color),wordWrap='CJK')
    p=Paragraph(escape(norm(s)).replace('\n','<br/>'),st)
    aw,h=p.wrap(w,H)
    p.drawOn(C,x,y-h)
    return y-h
def line(x,y,w,color=LINE):
    C.setStrokeColor(colors.HexColor(color)); C.setLineWidth(.65); C.line(x,y,x+w,y)
def box(x,y,w,h,color=PALE):
    C.setFillColor(colors.HexColor(color));C.rect(x,y-h,w,h,stroke=0,fill=1)
def page(n, label):
    para('DH. / KIM DONGHAK',L,H-22,300,8,12,BLUE)
    para(label,W-235,H-22,192,8,12,MUTED)
    line(L,H-41,CW)
    line(L,39,CW)
    para('PORTFOLIO · 2026.09',L,30,330,8,11,MUTED)
    para(f'{n:02} / 09',W-84,30,60,8,11,MUTED)
def section(title,text,x,y,w):
    y=para(title,x,y,w,10.7,16,BLUE)-7
    return para(text,x,y,w,10.2,16,MUTED)
def flow(p,y):
    box(L,y,CW,64,NAVY)
    col=CW/4
    for i,t in enumerate(p['flow']):
        para(f'0{i+1}',L+13+i*col,y-10,col-18,8,11,'#a7bfff')
        para(t,L+13+i*col,y-28,col-22,10,14,'#ffffff')
        if i<3: para('>',L+(i+1)*col-12,y-29,10,10,14,'#a7bfff')
    return para(p['diagramCaption'],L,y-71,CW,8.1,12,MUTED)-16
def source(p,y):
    y=para(p['evidence'],L,y,CW,8.2,12,MUTED)-7
    for a in p['links']:
        h=14
        para(a['label']+'  ↗',L,y,CW,9,14,BLUE)
        C.linkURL(a['url'],(L,y-h,W-L,y),relative=0,thickness=0)
        y-=18
    return y

page(1,'FRONTEND · PRODUCT ENGINEER')
para('김동학',L,758,CW,18,27,BLUE)
y=para('화면에서 시작해,\n업무가 끝나는 곳까지.',L,708,CW,33,46)-23
y=para(D['intro'],L,y,CW,12,20,MUTED)-32
line(L,y,CW);y-=24
y=para('SELECTED WORK',L,y,CW,9,14,BLUE)-15
for i,p in enumerate(D['projects'][:5]):
    para(f'0{i+1}',L,y,36,13,19,BLUE)
    para(p['name'],L+43,y,120,13,19)
    y2=para(p['title'],L+165,y,CW-165,10.2,17,MUTED)
    y=min(y-34,y2-15)
y-=9
line(L,y,CW);y-=20
for s in D['skills']:
    para(s['title'],L,y,90,10.2,16,BLUE)
    y=para(s['tools'],L+100,y,CW-100,10.2,16,MUTED)-12
y-=11
para('github.com/donghakk',L,y,CW,11,17,BLUE)
C.linkURL(D['github'],(L,y-17,L+190,y),relative=0,thickness=0)
assert y>70,('cover',y)
C.showPage()

for idx,p in enumerate(D['projects'][:5],2):
    page(idx,p['english'])
    para(f'{idx-1:02}',L,776,42,26,35,BLUE)
    para(p['name'],L+53,778,CW-53,24,34)
    y=para(p['title'],L+53,741,CW-53,14,21)-16
    y=para(p['summary'],L,y,CW,10.8,17,MUTED)-17
    meta=f"{p['period']}  |  {p['role']}\n{p['team']}  ·  {p['status']}"
    box(L,y,CW,48)
    para(meta,L+12,y-8,CW-24,9.2,15)
    y-=57
    y=para(p['employment'],L,y,CW,8.5,13,MUTED)-10
    y=para(' / '.join(p['tech']),L,y,CW,8.8,13,BLUE)-19
    w=(CW-25)/2
    ya=section('문제와 제약',p['problem'],L,y,w)
    yb=section('선택과 이유',p['decision'],L+w+25,y,w)
    y=min(ya,yb)-20
    y=flow(p,y)
    y=para('내가 구현한 부분',L,y,CW,10.7,16,BLUE)-6
    for item in p['implementation']:
        y=para('• '+item,L,y,CW,9.8,15,MUTED)-4
    y-=11
    y=section('결과와 확인 범위',p['result'],L,y,CW)-9
    y=para(p['scope'],L,y,CW,8.4,13,MUTED)-13
    y=source(p,y)
    assert y>=50,(p['id'],y)
    C.showPage()

page(7,'PRODUCT SCREENS')
y=para('PennyPal · 구현 화면',L,776,CW,23,33)-15
y=para('가입 기능과 금융 탐색 화면에서 맡은 UI·검증·상태·API 연결을 소개합니다.',L,y,CW,10.2,16,MUTED)-22
for imeta in D['projects'][3]['images']:
    im=ImageReader(str(ROOT/imeta['src'])); iw,ih=im.getSize()
    width=CW;height=width*ih/iw
    C.drawImage(im,L,y-height,width,height,mask='auto')
    y-=height+10
    y=para(imeta['caption'],L,y,CW,9,14,MUTED)-30
assert y>50,('screens',y)
C.showPage()

page(8,'MORE WORK')
y=para('서비스를 연결하는 다른 경험',L,776,CW,23,33)-26
for p in D['projects'][5:]:
    y=para(p['name'],L,y,CW,18,25,BLUE)-8
    y=para(f"{p['period']}  |  {p['role']}",L,y,CW,9,14,MUTED)-10
    y=para(p['summary'],L,y,CW,10.2,16)-12
    y=para(p['decision'],L,y,CW,10,16,MUTED)-10
    for item in p['implementation']:
        y=para('• '+item,L,y,CW,9.5,15,MUTED)-3
    y=para(p['result'],L,y-7,CW,9.4,15,MUTED)-9
    # One primary public source for each supporting case keeps the page focused.
    a=p['links'][0]
    para(a['label']+' ↗',L,y,CW,9,14,BLUE)
    C.linkURL(a['url'],(L,y-14,W-L,y),relative=0,thickness=0)
    y-=35
    if p['id']=='mentor': line(L,y+9,CW)
assert y>47,('more-work',y)
C.showPage()

page(9,'BACKGROUND & CONTACT')
y=para('경력과 배움',L,776,CW,25,35)-27
for ex in D['experience']:
    para(ex['date'],L,y,120,9,15,BLUE)
    yy=para(ex['title'],L+130,y,CW-130,11.3,17)-7
    yy=para(ex['detail'],L+130,yy,CW-130,9.8,15,MUTED)
    y=yy-20
    line(L,y+8,CW)
y=para('자격',L,y-4,CW,12,18,BLUE)-9
for text in D['certificates']:
    y=para(text,L,y,CW,10,16,MUTED)-5
y-=22
y=section('함께 일하는 방식',D['workingStyle'],L,y,CW)-28
y=para('김동학  /  Frontend · Product Engineer',L,y,CW,13,20)-10
para('github.com/donghakk',L,y,CW,11,17,BLUE)
C.linkURL(D['github'],(L,y-17,L+190,y),relative=0,thickness=0)
assert y>55,('background',y)
C.save()
reader=PdfReader(OUT)
assert len(reader.pages)==9
assert all((p.extract_text() or '').strip() for p in reader.pages)
assert OUT.stat().st_size<50*1024*1024
print({'pages':len(reader.pages),'bytes':OUT.stat().st_size,'output':OUT.name})
