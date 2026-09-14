"""Encode smooth scrolling from real, fully revealed LP page captures.

Usage: python build_lp_videos.py /path/to/captures /path/to/ffmpeg
Inputs: marketer-final.jpg and influencer-final.jpg. No UI simulation.
"""
import json
import subprocess
import sys
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
captures=Path(sys.argv[1]);ffmpeg=sys.argv[2]
out=ROOT/'assets/lp';out.mkdir(parents=True,exist_ok=True)
fps=30;duration=26;hold=2;width=704;height=1252
manifest=[]
for role in ['marketer','influencer']:
    source=Image.open(captures/f'{role}-final.jpg').convert('RGB')
    assert source.width>=width and source.height>height
    # One pixel trimmed at the edge solely for the codec's even-width requirement.
    poster=source.crop((0,0,width,height))
    poster.save(out/f'{role}-poster.png',optimize=True)
    detail_y=round((source.height-height)*0.28)
    source.crop((0,detail_y,width,detail_y+height)).save(out/f'{role}-detail.png',optimize=True)
    source.save(out/f'{role}-full.jpg',quality=96,subsampling=0)
    target=out/f'{role}-scroll.mp4'
    cmd=[ffmpeg,'-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{width}x{height}','-r',str(fps),'-i','pipe:0','-an','-c:v','libx264','-preset','fast','-crf','16','-pix_fmt','yuv420p','-movflags','+faststart',str(target)]
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    for f in range(duration*fps):
        t=f/fps
        progress=max(0,min(1,(t-hold)/(duration-2*hold)))
        # Smooth acceleration/deceleration, constant direction, no rescaling.
        progress=progress*progress*(3-2*progress)
        y=round((source.height-height)*progress)
        proc.stdin.write(source.crop((0,y,width,y+height)).tobytes())
    proc.stdin.close()
    assert proc.wait()==0
    manifest.append({'role':role,'width':width,'height':height,'fps':fps,'duration':duration,'bytes':target.stat().st_size,'captureSize':source.size,'source':f'https://selfad.co.kr/lp/{role}','captured':'2026-09-15','method':'Actual full-page browser screenshot, vertically panned; not a recording of live interactions.'})
(out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(manifest,ensure_ascii=False))
