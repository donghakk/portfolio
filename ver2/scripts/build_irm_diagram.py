"""Functional IRM architecture diagram, not a simulated application screen."""
from pathlib import Path
from html import escape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

ROOT=Path(__file__).resolve().parents[1]
TEMP=ROOT.parents[1]/'tmp/portfolio-v2-qa'
TEMP.mkdir(parents=True,exist_ok=True)
W,H=1600,900
INK='#14233b'; BLUE='#245de5'; MUTED='#50617a'; LINE='#c8d5e8'; PALE='#f2f6fc'
pdfmetrics.registerFont(TTFont('KR','/System/Library/Fonts/Supplemental/Arial Unicode.ttf'))
C=canvas.Canvas(str(TEMP/'irm-system-design.pdf'),pagesize=(W,H))
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', '<rect width="1600" height="900" fill="white"/>']

def box(x,y,w,h,fill=PALE,stroke=LINE):
    C.setFillColor(HexColor(fill));C.setStrokeColor(HexColor(stroke));C.setLineWidth(2)
    C.roundRect(x,H-y-h,w,h,12,stroke=1,fill=1)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
def text(s,x,y,size=25,color=INK):
    C.setFont('KR',size);C.setFillColor(HexColor(color));C.drawString(x,H-y-size*.82,s)
    svg.append(f'<text x="{x}" y="{y+size*.82}" font-family="Arial, Apple SD Gothic Neo, sans-serif" font-size="{size}" fill="{color}">{escape(s)}</text>')
def arrow(points,dashed=False):
    C.setStrokeColor(HexColor(BLUE));C.setFillColor(HexColor(BLUE));C.setLineWidth(3)
    C.setDash(8,6) if dashed else C.setDash()
    p=C.beginPath();p.moveTo(points[0][0],H-points[0][1])
    for x,y in points[1:]:p.lineTo(x,H-y)
    C.drawPath(p)
    import math
    x,y=points[-1];px,py=points[-2];a=math.atan2(y-py,x-px)
    corners=[(x,y),(x-14*math.cos(a-.45),y-14*math.sin(a-.45)),(x-14*math.cos(a+.45),y-14*math.sin(a+.45))]
    q=C.beginPath();q.moveTo(corners[0][0],H-corners[0][1])
    for cx,cy in corners[1:]:q.lineTo(cx,H-cy)
    q.close();C.setDash();C.drawPath(q,stroke=0,fill=1)
    dash=' stroke-dasharray="8 6"' if dashed else ''
    svg.append(f'<polyline points="{" ".join(f"{x},{y}" for x,y in points)}" fill="none" stroke="{BLUE}" stroke-width="3"{dash}/>')
    svg.append(f'<polygon points="{" ".join(f"{x},{y}" for x,y in corners)}" fill="{BLUE}"/>')

text('IRM / SYSTEM ARCHITECTURE',55,40,23,BLUE)
text('수집 데이터를 검토와 발송, 운영 기록으로 연결',55,83,39)
text('01  수집',55,160,23,BLUE)
text('02  검토 · 상태 관리',605,160,23,BLUE)
text('03  검증 · 발송',1145,160,23,BLUE)

box(55,220,370,125)
text('LOCAL',82,244,19,BLUE)
text('Naver · Instagram 수집',82,282,27)
box(55,395,370,125)
text('AWS FARGATE',82,419,19,BLUE)
text('YouTube 수집',82,457,27)

box(605,260,370,240,fill='#eaf1ff',stroke=BLUE)
text('Google Sheets',634,293,32)
text('수집 데이터 정리 · 중복 제거',634,349,23)
text('담당자 검토 · 발송 상태 관리',634,391,23)
text('발송 이력 보존',634,433,23)

box(1145,260,400,240)
text('AWS FARGATE',1174,292,19,BLUE)
text('발송 전 검증 · 한도 확인',1174,339,27)
text('메일 발송',1174,394,30)
text('수신거부 대상 반영',1174,449,22,MUTED)

arrow([(425,282),(513,282),(513,345),(605,345)])
arrow([(425,457),(513,457),(513,417),(605,417)])
arrow([(975,370),(1145,370)])
text('발송 대상',1000,328,21,MUTED)
arrow([(1345,500),(1345,568),(790,568),(790,500)],True)
text('발송 상태 · 이력 갱신',900,584,22,MUTED)

box(55,663,1490,180,fill='#ffffff')
text('수신거부 처리',83,691,25,BLUE)
text('HMAC 토큰',83,736,23)
text('Apps Script · Cloudflare Worker',83,776,23,MUTED)
text('실행 자원',629,691,25,BLUE)
text('ECR · EFS',629,736,23)
text('Secrets Manager',629,776,23,MUTED)
text('운영 확인',1149,691,25,BLUE)
text('CloudWatch 실행 로그',1149,736,23)
text('Google Sheets 발송 이력',1149,776,23,MUTED)
svg.append('</svg>')
(ROOT/'assets/irm-system-design.svg').write_text('\n'.join(svg))
C.save()
print('Built IRM system architecture SVG and intermediate PDF')
