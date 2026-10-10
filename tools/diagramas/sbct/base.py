"""Geometria comum para os diagramas de SBCT (projeção local, norte para cima)."""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
# geometria GND_DRAW (repositório privado), baixada por ../baixar.sh
GND = os.environ.get('GND_DRAW') or os.path.join(HERE, '..', '.dados', 'SBCT')

def dms(d, m, s):
    return d + m / 60 + s / 3600

LAT0, LON0 = -dms(25, 31, 54), -dms(49, 10, 34)  # ARP
KX = math.cos(math.radians(LAT0)) * 111320.0
KY = 110540.0

# Cabeceiras (AIP AD 2.12)
THR = {
    '11': (-dms(25, 31, 41.83), -dms(49, 10, 48.62)),
    '29': (-dms(25, 31, 43.62), -dms(49, 9, 44.22)),
    '15': (-dms(25, 31, 19.53), -dms(49, 10, 58.49)),
    '33': (-dms(25, 32, 10.10), -dms(49, 10, 1.87)),
}

def proj(lon, lat):
    return ((lon - LON0) * KX, (lat - LAT0) * KY)

_a = proj(THR['15'][1], THR['15'][0])
_b = proj(THR['33'][1], THR['33'][0])
THETA = math.atan2(_b[1] - _a[1], _b[0] - _a[0])  # 15/33 na horizontal
COS, SIN = math.cos(-THETA), math.sin(-THETA)

def xy(lon, lat):
    x, y = proj(lon, lat)
    return (x * COS - y * SIN, -(x * SIN + y * COS))

def thr(n):
    return xy(THR[n][1], THR[n][0])

def load(name):
    with open(os.path.join(GND, name + '.geojson')) as f:
        return [x for x in json.load(f)['features'] if x['geometry']]

def lines(geom):
    t, c = geom['type'], geom['coordinates']
    if t == 'LineString':
        return [c]
    if t in ('MultiLineString', 'Polygon'):
        return c
    if t == 'MultiPolygon':
        return [r for p in c for r in p]
    return []

def polys(geom):
    t, c = geom['type'], geom['coordinates']
    if t == 'Polygon':
        return [c]
    if t == 'MultiPolygon':
        return c
    return []

def path_d(rings, close=True):
    out = []
    for ring in rings:
        pts = [xy(*p[:2]) for p in ring]
        out.append('M' + ' L'.join(f'{x:.0f},{y:.0f}' for x, y in pts) + (' Z' if close else ''))
    return ' '.join(out)
