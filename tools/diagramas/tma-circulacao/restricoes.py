"""Restrições de altitude das cartas STAR e SID (AIRAC 2508A1 a 2610A1).

Chave: nome do procedimento como no pacote (sem a transição). Valor: fixo ->
restrição. Formato: "<FL100" no nível ou abaixo, ">FL100" no nível ou acima,
"=FL100" no nível, "8000-FL090" janela (de baixo para cima). Altitudes em pés.
Atualize junto com as cartas: o gerador só usa estes valores para estimar os
níveis nos cruzamentos.
"""

STAR = {
    # SBGR
    "MOLLE1D": {"GR071": "<FL270", "GR072": "<FL230", "GR073": "<FL270", "GR327": ">FL240", "GR074": "<FL230",
                "GR249": ">FL190", "GR076": ">FL160", "GR077": "=FL140", "GR252": "=FL140",
                "SANPA": "8000-FL090", "GR283": "<8000", "LOMEN": ">6000"},
    "MOLLE1C": {"GR071": "<FL270", "GR072": "<FL230", "GR073": "<FL270", "GR327": ">FL240", "GR074": "<FL230",
                "GR249": ">FL190", "GR076": ">FL160", "GR077": "=FL140", "GR252": "=FL140",
                "SANPA": "FL090-FL100", "UTKUG": ">6000"},
    "SANPA1A": {"VUNOX": "<FL220", "GR259": "<FL180", "GR262": "<FL160", "SANPA": "8000-FL090",
                "GR283": "<8000", "LOMEN": ">6000"},
    "VUNOX1B": {"VUNOX": "<FL220", "GR259": "<FL180", "GR262": "<FL160", "SANPA": "FL090-FL100", "UTKUG": ">6000"},
    "EDMUS1B": {"EDMUS": "<FL170", "NIBVO": "<FL150", "GR278": "8000-FL090", "GR282": "<8000", "UTKUG": ">6000",
                # mesmo nome no pacote para a chegada de SBKP pista 15
                "KP153": ">FL230", "KP213": ">FL140", "KP212": ">FL130", "KP211": ">FL120", "KP209": "<FL110",
                "KP207": ">FL090", "ITEDI": ">6000"},
    "EDMUS2A": {"EDMUS": "<FL260", "POLYP": "<FL150", "GR284": ">FL110", "GR286": "=FL110", "GR283": "=FL100",
                "GR287": "<FL090", "GR288": "7000-8000", "GR289": "=7000", "LOMEN": ">6000"},
    # SBSP
    "ORESU1A": {"ENTIT": "<FL270", "NEKIG": "<FL230", "SP031": ">FL200", "RUSTE": "FL200-FL240",
                "ORESU": "FL130-FL170", "PRUMO": ">FL120", "IROPU": "8000-FL090", "LUVDI": ">5500"},
    "ORESU1B": {"ENTIT": "<FL270", "NEKIG": "<FL230", "SP031": ">FL200", "RUSTE": "FL200-FL240",
                "ORESU": "FL130-FL170", "PRUMO": ">FL120", "KOMGU": "=FL090", "SP098": "=FL090", "OGTAL": ">6000"},
    "OGTAL2A": {"ANISE": "<FL230", "SP091": "<FL200", "MANLO": "<FL260", "OGTAL": "<FL120", "SP099": "=FL090",
                "SP101": "=FL090", "SP032": ">7000", "KOMGU": ">5500"},
    "ANISE1A": {"ANISE": "<FL170", "SP091": "<FL140", "OGTAL": ">6000"},
    "IBDAL2A": {"MANLO": "<FL190", "ESUNI": ">6000"},
    # SBKP
    "ITEDI1A": {"ENTIT": "<FL190", "KP203": "<FL110", "KP204": "<FL090", "ITEDI": ">6000",
                "KP153": ">FL230", "KP213": ">FL140", "KP212": ">FL130", "KP211": ">FL120", "KP209": "<FL110",
                "KP207": ">FL090"},
    "VERME1A": {"GNOME": "FL160-FL170", "KP219": ">FL160", "KP217": "<FL120", "KP216": ">FL100", "KP214": "<8000",
                "NILKA": ">6500"},
    "UTLOT3A": {"UTLOT": "<FL160", "NOBRE": ">6000"},
    "ENTIT1A": {"ENTIT": "<FL220", "KP204": ">FL150", "KP226": "<FL140", "KP227": ">FL090", "KP228": ">8000",
                "KP209": ">6500"},
    "EDMUS1A": {"EDMUS": "<FL300", "KP153": ">FL230", "KP154": "<FL180", "KP213": ">FL120", "KP231": ">FL100",
                "KP269": "7000-8000", "KP191": ">6500"},
    "UBKUP2A": {"KP201": "<FL170", "NILKA": ">FL120", "KP221": ">FL090", "KP222": "<7500", "UBKUP": ">6500",
                "KP224": ">FL120", "KP223": "<FL090", "KP271": "=8000"},
}

SID = {
    # SBGR
    "AMVUL6A": {"GR222": "<FL100", "GR217": ">FL100", "GR223": ">FL180", "GR224": ">FL250"},
    "REORI3A": {"GR222": "<FL100", "GR217": ">FL100", "GR223": ">FL180", "GR224": ">FL250"},
    "EKOPO1A": {"GR027": "<FL100", "EKOPO": "<FL130"},
    "NIBRU3A": {"GR209": "<6000", "EKOPO": "<FL130"},
    "UREMI3A": {"GR209": "<6000", "EKOPO": "<FL130"},
    "ORONU1A": {"GR316": "<FL100", "GR223": ">FL180", "GR224": ">FL250"},
    "ORONU1B": {"GR324": ">FL100", "GR292": ">FL110", "GR021": "<FL120", "GR022": ">FL130", "GERKA": "<FL140"},
    "ZORZA3A": {"GR027": "7000-FL090", "GR212": "<FL160", "CGO": ">FL100", "GR214": ">FL240", "GR216": ">FL270"},
    "CGO5A": {"GR319": "6000-7000", "GR212": "<FL160", "CGO": ">FL100", "GR214": ">FL240", "GR216": ">FL270"},
    "ISNAP2A": {"GR237": ">6500", "GR242": "<FL160", "ISOXO": ">FL160", "ORIMU": "<FL220"},
    "EVNEB3A": {"GR237": ">6500", "GR242": "<FL160", "ISOXO": ">FL160", "ORIMU": "<FL220"},
    "XOLUS1A": {"GR081": "FL100-FL110", "GR082": ">FL120", "GR083": ">FL130", "GR084": "<FL150",
                "GR086": "FL160-FL170", "XOLUS": "<FL190"},
    "ZORZA5B": {"GR237": ">6500", "CGO": ">FL100", "GR219": ">FL190", "UGTIX": ">FL250"},
    "CGO4B": {"GR237": ">6500", "CGO": ">FL100", "GR219": ">FL190", "UGTIX": ">FL250"},
    "AKRER3A": {"GR048": ">6000", "AKRER": "<8000", "XOGOD": "<FL100", "UMRAR": "<FL110", "UBRAM": "FL120-FL130"},
    # SBSP
    "BAIAN3A": {"SP103": ">FL140", "ISOXO": ">FL170", "ORIMU": "<FL220"},
    "BAIAN3B": {"VUNVU": ">5500", "SP103": ">FL140", "ISOXO": ">FL170", "ORIMU": "<FL220"},
    "SEDLO1A": {"SP083": "<7500"},
    "UTKOM1A": {"SP106": "<7500"},
    "UBRAM1A": {"SP081": "=6000", "SP039": ">8000", "SP038": "=FL090", "XOGOD": "<FL100", "UMRAR": "<FL110",
                "UBRAM": ">FL120", "ASETA": ">FL150"},
    "UBRAM1B": {"SP079": "6000-8000", "SP038": "=FL090", "XOGOD": "<FL100", "UMRAR": "<FL110", "UBRAM": ">FL120",
                "ASETA": ">FL150"},
    "UGTIX1B": {"SP083": "<7500", "SP084": ">FL100", "SP086": ">FL130", "UGTIX": ">FL240", "SP087": ">FL250"},
    "UGTIX2A": {"SP106": "<7500", "SP084": ">FL100", "SP086": ">FL130", "UGTIX": ">FL240", "SP087": ">FL250"},
    # SBKP
    "EGEVA1B": {"KP144": "<FL080", "KP257": "<FL100", "KP274": "<FL230"},
    "SOVSI1A": {"KP259": "7000-8000", "KP261": ">FL100", "KP136": "FL110-FL170"},
    "EGBEN1A": {"EGBEN": "<8000", "KP242": "FL090-FL130", "KP243": ">FL130", "URRAO": ">FL140", "KP244": ">FL190",
                "DEXIB": ">FL100", "GERTU": ">FL200", "KP179": ">FL160"},
    "ISMOB1A": {"EGBEN": "<8000", "DEXIB": ">FL100", "KP179": ">FL160"},
    "EGEVA1A": {"KP263": "<FL090"},
    "KONVI2B": {"KP254": ">4500", "KP267": ">5000", "KP256": "<7000", "KP243": ">FL130", "URRAO": ">FL140",
                "KP244": ">FL190"},
    "KONVI2C": {"EGBEN": "6000-8000", "KP249": "FL090-FL100", "KONVI": "<FL130"},
    "KONVI2D": {"KP254": ">4500", "KP267": ">5000", "KP256": "<7000", "KP249": "FL090-FL100", "KONVI": "<FL130"},
    "OBLUG2A": {"KP266": "<FL110", "KP268": "<FL200"},
    "OPGUN2A": {"GERTU": ">FL190", "KP179": ">FL160"},
    "OSUDO4A": {"KP238": ">FL090", "KP264": "<FL200", "KP239": ">FL140", "OPNOB": "<FL230", "KP246": ">8000",
                "KP247": ">FL110", "KP248": "<FL170"},
    "UGIKI1A": {"KP251": ">6000", "KP127": "8000-FL100", "MUDET": ">FL120", "GUABO": ">FL170"},
    "UGIKI1B": {"KP259": "7000-8000", "KP262": ">FL100", "KP127": "<FL110", "MUDET": ">FL120"},
}


def pes(txt):
    return int(txt[2:]) * 100 if txt.startswith("FL") else int(txt)


def faixa(r):
    """Restrição -> (mínimo, máximo) em pés; None quando não limita."""
    if r[0] == "<":
        return (None, pes(r[1:]))
    if r[0] == ">":
        return (pes(r[1:]), None)
    if r[0] == "=":
        v = pes(r[1:])
        return (v, v)
    lo, hi = r.split("-")
    return (pes(lo), pes(hi))
