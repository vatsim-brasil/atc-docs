"""Geometria comum para os diagramas de SBSP (projeção local, pistas 17/35 na horizontal)."""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
# geometria GND_DRAW (repositório privado), baixada por ../baixar.sh
GND = os.environ.get('GND_DRAW') or os.path.join(HERE, '..', '.dados', 'SBSP')


def dms(d, m, s):
    return d + m / 60 + s / 3600


LAT0, LON0 = -dms(23, 37, 34), -dms(46, 39, 23)  # ARP
KX = math.cos(math.radians(LAT0)) * 111320.0
KY = 110540.0

# AIP AD 2.12: cabeceiras e fim de pista
THR = {
    '17R': (-dms(23, 37, 15.42), -dms(46, 39, 37.53)),
    '35L': (-dms(23, 38, 3.49), -dms(46, 39, 4.27)),
    '17L': (-dms(23, 37, 14.83), -dms(46, 39, 28.80)),
    '35R': (-dms(23, 37, 52.55), -dms(46, 39, 2.72)),
}
END = {  # extremidades físicas (todas as cabeceiras são deslocadas)
    '17R': (-dms(23, 37, 12.60), -dms(46, 39, 39.48)), '35L': (-dms(23, 38, 4.23), -dms(46, 39, 3.76)),
    '17L': (-dms(23, 37, 13.16), -dms(46, 39, 29.95)), '35R': (-dms(23, 37, 54.20), -dms(46, 39, 1.56)),
}


def proj(lon, lat):
    return ((lon - LON0) * KX, (lat - LAT0) * KY)


_a = proj(END['17R'][1], END['17R'][0])
_b = proj(END['35L'][1], END['35L'][0])
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
    with open(os.path.join(GND, name + '.geojson')) as f:
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
