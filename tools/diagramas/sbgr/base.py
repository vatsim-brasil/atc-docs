"""Geometria comum para os diagramas de SBGR (projeção local girada)."""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
# geometria GND_DRAW (repositório privado), baixada por ../baixar.sh
GND = os.environ.get('GND_DRAW') or os.path.join(HERE, '..', '.dados', 'SBGR')

LAT0, LON0 = -23.4356, -46.4731  # ARP aproximado
KX = math.cos(math.radians(LAT0)) * 111320.0
KY = 110540.0


def dms(d, m, s):
    return d + m / 60 + s / 3600


# Cabeceiras (AIP AD 2.13 / ADC)
THR = {
    '10L': (-dms(23, 26, 3), -dms(46, 28, 57)),
    '28R': (-dms(23, 25, 30), -dms(46, 26, 57)),
    '10R': (-dms(23, 26, 20), -dms(46, 29, 13)),
    '28L': (-dms(23, 25, 52), -dms(46, 27, 32)),
}


def proj(lon, lat):
    return ((lon - LON0) * KX, (lat - LAT0) * KY)


_a = proj(THR['10L'][1], THR['10L'][0])
_b = proj(THR['28R'][1], THR['28R'][0])
THETA = math.atan2(_b[1] - _a[1], _b[0] - _a[0])  # ângulo da pista em relação ao leste
COS, SIN = math.cos(-THETA), math.sin(-THETA)


def xy(lon, lat):
    """lon/lat -> coordenadas SVG (m), pistas na horizontal, y para baixo."""
    x, y = proj(lon, lat)
    xr = x * COS - y * SIN
    yr = x * SIN + y * COS
    return (xr, -yr)


def load(name):
    with open(os.path.join(GND, name + '.geojson')) as f:
        return json.load(f)['features']


def lines(geom):
    t, c = geom['type'], geom['coordinates']
    if t == 'LineString':
        return [c]
    if t == 'MultiLineString':
        return c
    if t == 'Polygon':
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


def runway_ends(a, b, ext_a=0.0, ext_b=0.0):
    """Extremidades da pista em coordenadas SVG, estendendo cabeceiras deslocadas."""
    ax, ay = xy(THR[a][1], THR[a][0])
    bx, by = xy(THR[b][1], THR[b][0])
    L = math.hypot(bx - ax, by - ay)
    ux, uy = (bx - ax) / L, (by - ay) / L
    return (ax - ux * ext_a, ay - uy * ext_a), (bx + ux * ext_b, by + uy * ext_b)
