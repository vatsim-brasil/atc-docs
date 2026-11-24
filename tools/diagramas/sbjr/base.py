"""Geometria comum para os diagramas de SBJR (projeção local, 03/21 na horizontal)."""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
# geometria GND_DRAW (repositório privado), baixada por ../baixar.sh
GND = os.environ.get('GND_DRAW') or os.path.join(HERE, '..', '.dados', 'SBJR')


def dms(d, m, s):
    return d + m / 60 + s / 3600


LAT0, LON0 = -dms(22, 59, 15), -dms(43, 22, 12)  # ARP
KX = math.cos(math.radians(LAT0)) * 111320.0
KY = 110540.0

# extremidades da pista: pontos médios das cabeceiras do polígono 9.PISTA do GND_DRAW
# (o ROTAER só dá as coordenadas ao segundo: S22 59 27 W043 22 21 e S22 58 58 W043 22 19)
THR = {
    '03': (-22.9908204, -43.3724414),
    '21': (-22.9827103, -43.3719605),
}
END = THR  # sem cabeceira deslocada


def proj(lon, lat):
    return ((lon - LON0) * KX, (lat - LAT0) * KY)


_a = proj(END['03'][1], END['03'][0])
_b = proj(END['21'][1], END['21'][0])
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
    return [(f['properties'].get('ref_2'), [tuple(p[:2]) for p in ln])
            for f in load('A.TAXIWAYS') for ln in lines(f['geometry'])]


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
