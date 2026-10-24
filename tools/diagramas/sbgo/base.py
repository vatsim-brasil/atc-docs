"""Geometria comum para os diagramas de SBGO (projeção local, 14/32 na horizontal)."""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
# geometria GND_DRAW (repositório privado), baixada por ../baixar.sh
GND = os.environ.get('GND_DRAW') or os.path.join(HERE, '..', '.dados', 'SBGO')


def dms(d, m, s):
    return d + m / 60 + s / 3600


LAT0, LON0 = -dms(16, 37, 57), -dms(49, 13, 16)  # ARP
KX = math.cos(math.radians(LAT0)) * 111320.0
KY = 110540.0

# AIP AD 2.12: cabeceiras e fim de pista
THR = {
    '14': (-dms(16, 37, 38.02), -dms(49, 13, 46.16)),
    '32': (-dms(16, 38, 15.46), -dms(49, 12, 39.52)),
}
END = THR  # sem cabeceira deslocada


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


def taxiways():
    """Taxiways do GND_DRAW (já vêm com ref) como [(ref, [(lon, lat), ...])]."""
    return [(f['properties'].get('ref'), [tuple(p[:2]) for p in ln])
            for f in load('9A TAXIWAY') for ln in lines(f['geometry'])]


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
