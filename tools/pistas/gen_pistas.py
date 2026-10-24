# Gera docs/javascripts/pistas.json: declinação magnética (WMM) e rumo verdadeiro
# de cada cabeceira dos aeródromos com painel de meteorologia. Fonte: OurAirports.
import csv, json, math, re, sys, glob
from pygeomag import GeoMag
repo, oa = sys.argv[1], sys.argv[2]
# As cabeceiras valem as da tabela de pistas da página (AIP/ROTAER); o OurAirports só dá o rumo
icaos, page_rwys = set(), {}
for f in glob.glob(f'{repo}/docs/**/*.pt.md', recursive=True):
    t = open(f).read()
    for icao in re.findall(r'data-airport="([A-Z0-9]{4})"', t):
        icaos.add(icao)
        sec = re.search(r'## :material-routes:.*?\n(.*?)\n## ', t, re.S)
        if sec: page_rwys[icao] = re.findall(r'^\|\s*\*\*(\d{2}[LCR]?)\*\*', sec.group(1), re.M)
apts = {}
for r in csv.DictReader(open(f'{oa}/airports.csv')):
    for code in (r['ident'], r['icao_code'], r['gps_code']):
        if code in icaos and code not in apts: apts[code] = r
ref2icao = {a['id']: i for i, a in apts.items()}
rwys = {}
for r in csv.DictReader(open(f'{oa}/runways.csv')):
    if r['airport_ref'] in ref2icao and r['closed'] != '1':
        rwys.setdefault(ref2icao[r['airport_ref']], []).append(r)
def bearing(la1, lo1, la2, lo2):
    la1, lo1, la2, lo2 = map(math.radians, (la1, lo1, la2, lo2))
    y = math.sin(lo2 - lo1) * math.cos(la2)
    x = math.cos(la1) * math.sin(la2) - math.sin(la1) * math.cos(la2) * math.cos(lo2 - lo1)
    return (math.degrees(math.atan2(y, x)) + 360) % 360
gm = GeoMag()
out, report = {}, []
for icao in sorted(icaos):
    a = apts.get(icao)
    if not a:
        report.append(f'{icao}: sem aeroporto no OurAirports'); continue
    dec = gm.calculate(glat=float(a['latitude_deg']), glon=float(a['longitude_deg']), alt=0, time=2026.8).d
    ends = []
    for r in rwys.get(icao, []):
        le, he = r['le_ident'].strip(), r['he_ident'].strip()
        if not re.match(r'^\d{1,2}[LCR]?$', le): continue
        try:
            hdg = bearing(float(r['le_latitude_deg']), float(r['le_longitude_deg']), float(r['he_latitude_deg']), float(r['he_longitude_deg'])); src = 'coord'
        except ValueError:
            if r['le_heading_degT']:
                hdg = float(r['le_heading_degT']); src = 'hdgT'
            else:
                hdg = (int(re.match(r'\d+', le).group()) * 10 + dec) % 360; src = 'desig'
        # confere o rumo contra o designador (magnético) para pegar dado errado
        mag = (hdg - dec) % 360
        diff = abs((mag - int(re.match(r'\d+', le).group()) * 10 + 180) % 360 - 180)
        if diff > 15:
            report.append(f'{icao} {le}: rumo mag {mag:.0f} ≠ designador ({src}), usando designador')
            hdg = (int(re.match(r'\d+', le).group()) * 10 + dec) % 360
        ends += [[le.zfill(2) if le[0].isdigit() and len(re.match(r'\d+', le).group()) == 1 else le, round(hdg)], [he.zfill(2) if he and len(re.match(r'\d+', he).group()) == 1 else he, round((hdg + 180) % 360)]]
    known = dict(ends)
    final = []
    for ident in page_rwys.get(icao, []):
        if ident in known: final.append([ident, known[ident]])
        else:
            final.append([ident, round((int(ident[:2]) * 10 + dec) % 360)])
            report.append(f'{icao} {ident}: fora do OurAirports, rumo pelo designador')
    if not final: report.append(f'{icao}: sem pistas')
    out[icao] = {'dec': round(dec, 1), 'rwy': final}
json.dump(out, open(f'{repo}/docs/javascripts/pistas.json', 'w'), separators=(',', ':'))
print(len(out), 'aeródromos'); print('\n'.join(report))
