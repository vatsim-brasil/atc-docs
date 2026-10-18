"""Geometria comum para os diagramas de SBNF (projeção local, 08/26 na horizontal)."""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
# geometria GND_DRAW (repositório privado), baixada por ../baixar.sh
GND = os.environ.get('GND_DRAW') or os.path.join(HERE, '..', '.dados', 'SBNF')


def dms(d, m, s):
    return d + m / 60 + s / 3600


LAT0, LON0 = -dms(26, 52, 43), -dms(48, 39, 3)  # ARP
KX = math.cos(math.radians(LAT0)) * 111320.0
KY = 110540.0

# AIP AD 2.12: cabeceiras e fim de pista
THR = {
    '08': (-dms(26, 53, 0.86), -dms(48, 39, 27.98)),
    '26': (-dms(26, 52, 27.99), -dms(48, 38, 34.06)),
}
END = THR  # sem cabeceira deslocada


def proj(lon, lat):
    return ((lon - LON0) * KX, (lat - LAT0) * KY)


_a = proj(END['08'][1], END['08'][0])
_b = proj(END['26'][1], END['26'][0])
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


def taxiways():
    """Taxiways do GND_DRAW (já vêm com ref) como [(ref, [(lon, lat), ...])]."""
    return [(f['properties'].get('ref'), [tuple(p[:2]) for p in ln])
            for f in load('9A_TAXIWAY') for ln in lines(f['geometry'])]


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
