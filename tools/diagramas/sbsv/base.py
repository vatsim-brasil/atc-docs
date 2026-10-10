"""Geometria comum para os diagramas de SBSV (projeção local, 10/28 na horizontal)."""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
# geometria GND_DRAW (repositório privado), baixada por ../baixar.sh
GND = os.environ.get('GND_DRAW') or os.path.join(HERE, '..', '.dados', 'SBSV')


def dms(d, m, s):
    return d + m / 60 + s / 3600


LAT0, LON0 = -dms(12, 54, 31), -dms(38, 19, 21)  # ARP
KX = math.cos(math.radians(LAT0)) * 111320.0
KY = 110540.0

# AIP AD 2.12: cabeceiras e fins de pista
THR = {
    '10': (-dms(12, 54, 39.86), -dms(38, 20, 6.08)),
    '28': (-dms(12, 54, 21.84), -dms(38, 18, 36.25)),
    '17': (-dms(12, 54, 27.99), -dms(38, 20, 37.45)),
    '35': (-dms(12, 55, 7.92), -dms(38, 20, 7.71)),
}
END = {  # extremidades físicas
    '10': (-dms(12, 54, 40.64), -dms(38, 20, 9.98)),
    '28': (-dms(12, 54, 21.06), -dms(38, 18, 32.35)),
    '17': THR['17'],
    '35': THR['35'],
}


def proj(lon, lat):
    return ((lon - LON0) * KX, (lat - LAT0) * KY)


_a = proj(END['10'][1], END['10'][0])
_b = proj(END['28'][1], END['28'][0])
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
