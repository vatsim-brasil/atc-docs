import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import *
s=[]
allp=[]
def P(pts): return 'M'+' L'.join(f'{x:.0f},{y:.0f}' for x,y in pts)
for f in load('3_PATIO'):
    for p in polys(f['geometry']): s.append(f'<path d="{path_d(p)}" fill="#ccd" fill-rule="evenodd"/>')
for f in load('4_PRÉDIOS'):
    for p in polys(f['geometry']): s.append(f'<path d="{path_d(p)}" fill="#445"/>')
for f in load('5_PISTA'):
    for p in polys(f['geometry']): s.append(f'<path d="{path_d(p)}" fill="#222"/>')
for f in load('9A2_TAXIWAY_PONTILHADA'):
    for ln in lines(f['geometry']): s.append(f'<path d="{P([xy(*q[:2]) for q in ln])}" fill="none" stroke="#9a9" stroke-width="2"/>')
for i,f in enumerate(load('9A_TAXIWAY')):
    pr=f['properties']; 
    if pr.get('aeroway')!='taxiway': continue
    for ln in lines(f['geometry']):
        pts=[xy(*q[:2]) for q in ln]; allp+=pts
        s.append(f'<path d="{P(pts)}" fill="none" stroke="#e80" stroke-width="5"/>')
        m=pts[len(pts)//2]
        s.append(f'<text x="{m[0]:.0f}" y="{m[1]:.0f}" font-size="30" fill="blue">{i}:{pr.get("ref") or ""}</text>')
for nm,c in (('9A4_HOLDING','red'),('9A3_HOLDINGS_TAXIWAY','magenta'),('9A5_RED_LINE','darkred')):
    for f in load(nm):
        for ln in lines(f['geometry']): s.append(f'<path d="{P([xy(*q[:2]) for q in ln])}" fill="none" stroke="{c}" stroke-width="8"/>')
for f in load('9B_GATES'):
    x,y=xy(*f['geometry']['coordinates'][:2]); s.append(f'<text x="{x:.0f}" y="{y:.0f}" font-size="20" fill="green">{f["properties"]["ref"]}</text>')
for n in THR:
    x,y=thr(n); s.append(f'<circle cx="{x}" cy="{y}" r="15" fill="lime"/><text x="{x}" y="{y}" font-size="50" fill="green">{n}</text>')
xs=[p[0] for p in allp]; ys=[p[1] for p in allp]
X0,X1,Y0,Y1=min(xs)-300,max(xs)+300,min(ys)-300,max(ys)+300
print(X0,X1,Y0,Y1)
open(sys.argv[1],'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{X0} {Y0} {X1-X0} {Y1-Y0}" width="{(X1-X0)/1.2:.0f}" height="{(Y1-Y0)/1.2:.0f}"><rect x="{X0}" y="{Y0}" width="100%" height="100%" fill="#fff"/>'+''.join(s)+'</svg>')
