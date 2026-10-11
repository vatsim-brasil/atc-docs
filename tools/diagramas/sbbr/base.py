"""Geometria comum para os diagramas de SBBR (projeção local, pistas 11/29 na horizontal)."""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
# geometria GND_DRAW (repositório privado), baixada por ../baixar.sh
GND = os.environ.get('GND_DRAW') or os.path.join(HERE, '..', '.dados', 'SBBR')


def dms(d, m, s):
    return d + m / 60 + s / 3600


LAT0, LON0 = -dms(15, 52, 16), -dms(47, 55, 7)  # ARP
KX = math.cos(math.radians(LAT0)) * 111320.0
KY = 110540.0

# AIP AD 2.12: cabeceiras e fim de pista
THR = {
    '11L': (-dms(15, 51, 48.86), -dms(47, 55, 39.22)),
    '29R': (-dms(15, 51, 42.26), -dms(47, 53, 56.94)),
    '11R': (-dms(15, 52, 50.41), -dms(47, 56, 23.96)),
    '29L': (-dms(15, 52, 43.62), -dms(47, 54, 38.33)),
}
END = {  # extremidades físicas: as cabeceiras 29R e 29L são deslocadas 150 m
    '11L': THR['11L'], '29R': (-dms(15, 51, 41.94), -dms(47, 53, 51.91)),
    '11R': THR['11R'], '29L': (-dms(15, 52, 43.29), -dms(47, 54, 33.30)),
}


def proj(lon, lat):
    return ((lon - LON0) * KX, (lat - LAT0) * KY)


_a = proj(END['11L'][1], END['11L'][0])
_b = proj(END['29R'][1], END['29R'][0])
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
