"""Geometria comum para os diagramas de SBSL (projeção local, 06/24 na horizontal)."""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
# geometria GND_DRAW (repositório privado), baixada por ../baixar.sh
GND = os.environ.get('GND_DRAW') or os.path.join(HERE, '..', '.dados', 'SBSL')


def dms(d, m, s):
    return d + m / 60 + s / 3600


LAT0, LON0 = -dms(2, 35, 13), -dms(44, 14, 10)  # ARP
KX = math.cos(math.radians(LAT0)) * 111320.0
KY = 110540.0

# AIP AD 2.12: cabeceiras (sem deslocamento)
THR = {
    '06': (-dms(2, 35, 49.48), -dms(44, 14, 36.47)),
    '24': (-dms(2, 34, 49.13), -dms(44, 13, 47.82)),
}
END = dict(THR)
# antiga pista 09/27, fechada (marcada com X na ADC): extremidades do OSM, way 22732774
OLD = ((-2.5886664, -44.2425077), (-2.5839687, -44.2296524))


def proj(lon, lat):
    return ((lon - LON0) * KX, (lat - LAT0) * KY)


_a = proj(END['06'][1], END['06'][0])
_b = proj(END['24'][1], END['24'][0])
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


def taxiways():
    """(índice, ref do OSM, linhas) das taxiways do GND_DRAW; as feições de parking_position ficam de fora."""
    out = []
    for i, f in enumerate(load('9A_TAXIWAY')):
        if f['properties'].get('aeroway') != 'taxiway':
            continue
        for ln in lines(f['geometry']):
            out.append((i, f['properties'].get('ref'), [xy(*p[:2]) for p in ln]))
    return out
