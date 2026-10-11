"""Geometria comum para os diagramas de SBFL (projeção local, 14/32 na horizontal)."""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
# geometria GND_DRAW (repositório privado), baixada por ../baixar.sh
GND = os.environ.get('GND_DRAW') or os.path.join(HERE, '..', '.dados', 'SBFL')


def dms(d, m, s):
    return d + m / 60 + s / 3600


LAT0, LON0 = -dms(27, 40, 13), -dms(48, 33, 9)  # ARP
KX = math.cos(math.radians(LAT0)) * 111320.0
KY = 110540.0

# AIP AD 2.12: cabeceiras e fim de pista
THR = {
    '14': (-dms(27, 39, 56.59), -dms(48, 33, 4.35)),
    '32': (-dms(27, 40, 36.98), -dms(48, 31, 49.44)),
    '03': (-dms(27, 40, 30.57), -dms(48, 33, 15.04)),
    '21': (-dms(27, 39, 53.01), -dms(48, 33, 6.36)),
}
END = dict(THR, **{'21': (-dms(27, 39, 48.56), -dms(48, 33, 5.33))})  # cabeceira 21 deslocada 140 m


def proj(lon, lat):
    return ((lon - LON0) * KX, (lat - LAT0) * KY)


_a = proj(END['14'][1], END['14'][0])
_b = proj(END['32'][1], END['32'][0])
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
