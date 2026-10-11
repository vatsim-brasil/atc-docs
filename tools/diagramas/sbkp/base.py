"""Geometria comum para os diagramas de SBKP (projeção local, 15/33 na horizontal)."""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
# geometria GND_DRAW (repositório privado), baixada por ../baixar.sh
GND = os.environ.get('GND_DRAW') or os.path.join(HERE, '..', '.dados', 'SBKP')


def dms(d, m, s):
    return d + m / 60 + s / 3600


LAT0, LON0 = -dms(23, 0, 25), -dms(47, 8, 4)  # ARP
KX = math.cos(math.radians(LAT0)) * 111320.0
KY = 110540.0

# AIP AD 2.12: cabeceiras e fim de pista
THR = {
    '15': (-dms(22, 59, 54.45), -dms(47, 8, 49.21)),
    '33': (-dms(23, 0, 57.12), -dms(47, 7, 21.69)),
}
END = {'15': THR['15'], '33': (-dms(23, 0, 58.91), -dms(47, 7, 19.18))}  # cabeceira 33 deslocada 90 m


def proj(lon, lat):
    return ((lon - LON0) * KX, (lat - LAT0) * KY)


_a = proj(END['15'][1], END['15'][0])
_b = proj(END['33'][1], END['33'][0])
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
