"""Mapa de depuração de SBSL: cada taxiway do GND_DRAW com o índice da feição e o ref.

Uso: python3 -I debug.py dbg.svg [tamanho_da_fonte] ["viewBox"]
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import *
s = []; allp = []
P = lambda pts: 'M' + ' L'.join(f'{x:.0f},{y:.0f}' for x, y in pts)
for n, c in (('3_PÁTIOS', '#ccd'), ('4_PRÉDIOS', '#445')):
    for f in load(n):
        for p in polys(f['geometry']): s.append(f'<path d="{path_d(p)}" fill="{c}"/>')
for f in load('9B_GATES'):
    x, y = xy(*f['geometry']['coordinates'][:2])
    s.append(f'<text x="{x:.0f}" y="{y:.0f}" font-size="24" fill="purple">{f["properties"].get("ref")}</text>')
for i, ref, pts in taxiways():
    allp += pts
    s.append(f'<path d="{P(pts)}" fill="none" stroke="#e80" stroke-width="6"/>')
    m = pts[len(pts) // 2]
    s.append(f'<text x="{m[0]:.0f}" y="{m[1]:.0f}" font-size="{sys.argv[2] if len(sys.argv) > 2 else 30}" fill="blue">{i}:{ref or ""}</text>')
a, b = (xy(p[1], p[0]) for p in OLD)
s.append(f'<line x1="{a[0]:.0f}" y1="{a[1]:.0f}" x2="{b[0]:.0f}" y2="{b[1]:.0f}" stroke="#999" stroke-width="40"/>')
a, b = thr('06'), thr('24')
s.append(f'<line x1="{a[0]:.0f}" y1="{a[1]:.0f}" x2="{b[0]:.0f}" y2="{b[1]:.0f}" stroke="#222" stroke-width="40"/>')
for n in list(THR):
    x, y = thr(n); allp.append((x, y))
    s.append(f'<circle cx="{x}" cy="{y}" r="20" fill="lime"/><text x="{x}" y="{y}" font-size="60" fill="green">{n}</text>')
xs = [p[0] for p in allp]; ys = [p[1] for p in allp]
X0, X1, Y0, Y1 = min(xs) - 200, max(xs) + 200, min(ys) - 200, max(ys) + 200
print(X0, X1, Y0, Y1)
vb = sys.argv[3] if len(sys.argv) > 3 else f'{X0:.0f} {Y0:.0f} {X1-X0:.0f} {Y1-Y0:.0f}'
w, h = [float(v) for v in vb.split()[2:]]
open(sys.argv[1], 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="2400" height="{2400*h/w:.0f}"><rect x="-99999" y="-99999" width="199999" height="199999" fill="#fff"/>' + ''.join(s) + '</svg>')
