"""Geometria comum para os diagramas de SBCY (projeção local, 17/35 na horizontal)."""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
# geometria GND_DRAW (repositório privado), baixada por ../baixar.sh
GND = os.environ.get('GND_DRAW') or os.path.join(HERE, '..', '.dados', 'SBCY')


def dms(d, m, s):
    return d + m / 60 + s / 3600


LAT0, LON0 = -dms(15, 39, 0), -dms(56, 7, 3)  # ARP
KX = math.cos(math.radians(LAT0)) * 111320.0
KY = 110540.0

# AIP AD 2.12: cabeceiras e fim de pista
THR = {
    '17': (-dms(15, 38, 37.47), -dms(56, 7, 17.69)),
    '35': (-dms(15, 39, 43.99), -dms(56, 6, 42.33)),
}
END = THR  # sem cabeceira deslocada

# PDC SBCY, folha 2: coordenadas das posições (o GND_DRAW e o OSM só têm fragmentos dos pátios)
STANDS = {
    '1': [(55.10, 15.40), (56.28, 14.80), (57.43, 14.08), (58.48, 13.49), (59.57, 13.01), (60.81, 12.32),
          (62.07, 11.62), (63.32, 10.97), (64.45, 10.27), (65.64, 9.67), (66.82, 9.08), (68.00, 8.47),
          (69.16, 7.82)],
    '2': [(70.19, 7.20), (71.16, 6.70), (72.13, 6.20), (73.10, 5.71), (74.18, 4.22), (74.50, 4.88),
          (75.65, 3.42), (76.00, 4.08), (77.17, 2.65), (77.50, 3.31)],
}  # segundos de 15°38' S e 56°07' W (60+ = 15°39')


def stand_pts(apron):
    return [(-dms(56, 7, w), -dms(15, 38, s)) for s, w in STANDS[apron]]


def proj(lon, lat):
    return ((lon - LON0) * KX, (lat - LAT0) * KY)


_a = proj(END['17'][1], END['17'][0])
_b = proj(END['35'][1], END['35'][0])
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
    """Taxiways do GND_DRAW (já vêm com ref) como [(ref, [(lon, lat), ...])].
    O arquivo também traz as linhas de posição (parking_position), que ficam de fora; 'Charlie' vira C."""
    return [(REN.get(f['properties'].get('ref'), f['properties'].get('ref')), [tuple(p[:2]) for p in ln])
            for f in load('A.TAXIWAYS') if f['properties'].get('aeroway') != 'parking_position'
            for ln in lines(f['geometry'])]


REN = {'Charlie': 'C'}


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
