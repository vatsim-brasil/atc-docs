"""Geometria comum para os diagramas de SBVT (projeção local, norte para cima)."""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
# geometria GND_DRAW (repositório privado), baixada por ../baixar.sh
GND = os.environ.get('GND_DRAW') or os.path.join(HERE, '..', '.dados', 'SBVT')


def dms(d, m, s):
    return d + m / 60 + s / 3600


LAT0, LON0 = -dms(20, 15, 29), -dms(40, 17, 11)  # ARP
KX = math.cos(math.radians(LAT0)) * 111320.0
KY = 110540.0

# AIP AD 2.12: cabeceiras (sem cabeceira deslocada)
THR = {
    '02': (-dms(20, 15, 58.03), -dms(40, 16, 42.43)),
    '20': (-dms(20, 14, 51.68), -dms(40, 16, 52.23)),
    '06': (-dms(20, 15, 52.34), -dms(40, 17, 28.16)),
    '24': (-dms(20, 15, 3.99), -dms(40, 16, 56.32)),
}
END = THR


def proj(lon, lat):
    return ((lon - LON0) * KX, (lat - LAT0) * KY)


THETA = 0.0
COS, SIN = 1.0, 0.0


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
