import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import *
s=[]; allp=[]
P=lambda pts:'M'+' L'.join(f'{x:.0f},{y:.0f}' for x,y in pts)
for f in load('4_PATIO'):
    for p in polys(f['geometry']): s.append(f'<path d="{path_d(p)}" fill="#ccd"/>')
for f in load('6_PRÉDIOS'):
    for p in polys(f['geometry']): s.append(f'<path d="{path_d(p)}" fill="#445"/>')
for n in ('8_PISTAS',):
    for f in load(n):
        for p in polys(f['geometry']): s.append(f'<path d="{path_d(p)}" fill="#222"/>')
for i,e in enumerate(osm()):
    if e['tags'].get('aeroway') not in ('taxiway','holding_position'): continue
    pts=[xy(g['lon'],g['lat']) for g in e['geometry']]; allp+=pts
    s.append(f'<path d="{P(pts)}" fill="none" stroke="#e80" stroke-width="6"/>')
    m=pts[len(pts)//2]; s.append(f'<text x="{m[0]:.0f}" y="{m[1]:.0f}" font-size="{sys.argv[2] if len(sys.argv)>2 else 30}" fill="blue">{i}:{e["tags"].get("ref","")}</text>')
for nm,c in ():
    for f in load(nm):
        for ln in lines(f['geometry']): s.append(f'<path d="{P([xy(*q[:2]) for q in ln])}" fill="none" stroke="{c}" stroke-width="3"/>')
for n in list(THR):
    x,y=thr(n); s.append(f'<circle cx="{x}" cy="{y}" r="20" fill="lime"/><text x="{x}" y="{y}" font-size="60" fill="green">{n}</text>')
xs=[p[0] for p in allp]; ys=[p[1] for p in allp]
X0,X1,Y0,Y1=min(xs)-200,max(xs)+200,min(ys)-200,max(ys)+200
print(X0,X1,Y0,Y1)
vb=sys.argv[3] if len(sys.argv)>3 else f'{X0:.0f} {Y0:.0f} {X1-X0:.0f} {Y1-Y0:.0f}'
w,h=[float(v) for v in vb.split()[2:]]
open(sys.argv[1],'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="2400" height="{2400*h/w:.0f}"><rect x="-99999" y="-99999" width="199999" height="199999" fill="#fff"/>'+''.join(s)+'</svg>')
