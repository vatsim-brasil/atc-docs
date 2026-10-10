"""Geometria comum para os diagramas de SBGL (projeção local, 10/28 na horizontal)."""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
# geometria GND_DRAW (repositório privado), baixada por ../baixar.sh
GND = os.environ.get('GND_DRAW') or os.path.join(HERE, '..', '.dados', 'SBGL')


def dms(d, m, s):
    return d + m / 60 + s / 3600


LAT0, LON0 = -dms(22, 48, 36), -dms(43, 15, 2)  # ARP
KX = math.cos(math.radians(LAT0)) * 111320.0
KY = 110540.0

# AIP AD 2.12: cabeceiras e fins de pista
THR = {
    '10': (-dms(22, 48, 6.66), -dms(43, 15, 18.62)),
    '28': (-dms(22, 47, 31.84), -dms(43, 13, 3.50)),
    '15': (-dms(22, 48, 47.20), -dms(43, 15, 45.61)),
    '33': (-dms(22, 49, 42.55), -dms(43, 14, 21.99)),
}
END = {  # extremidades físicas da 15/33
    '15': (-dms(22, 48, 44.74), -dms(43, 15, 49.32)),
    '33': (-dms(22, 49, 44.82), -dms(43, 14, 18.57)),
}


def proj(lon, lat):
    return ((lon - LON0) * KX, (lat - LAT0) * KY)


_a = proj(THR['10'][1], THR['10'][0])
_b = proj(THR['28'][1], THR['28'][0])
THETA = math.atan2(_b[1] - _a[1], _b[0] - _a[0])
COS, SIN = math.cos(-THETA), math.sin(-THETA)


def xy(lon, lat):
    x, y = proj(lon, lat)
    return (x * COS - y * SIN, -(x * SIN + y * COS))


def thr(n):
    return xy(THR[n][1], THR[n][0])


def end(n):
    return xy(END[n][1], END[n][0])


def load(name):
    path = os.path.join(GND, name + '.geojson')
    if not os.path.exists(path):  # no GND_DRAW os arquivos de SBGL têm o prefixo SBGL_
        path = os.path.join(GND, 'SBGL_' + name + '.geojson')
    with open(path) as f:
        return [x for x in json.load(f)['features'] if x['geometry']]


def osm():
    with open(os.path.join(HERE, 'osm.json')) as f:
        return json.load(f)['elements']


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
