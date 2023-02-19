from app import db
from models.map.Map import Map
from models.map.MapMode import MapMode



def add_all_ow_maps():
    control = MapMode(name='Control', max_score=1)
    hybrid = MapMode(name='Hybrid', max_score = 3)
    escort = MapMode(name='Escort', max_score = 3)
    assault = MapMode(name='Assault', max_score = 2)
    push = MapMode(name='Assault', max_score = 1)

    db.session.add(control)
    db.session.add(hybrid)
    db.session.add(escort)
    db.session.add(assault)
    db.session.add(push)

    hollywood = Map(name="HOLLYWOOD", map_mode=hybrid)
    db.session.add(hollywood)
    havana = Map(name="HAVANA", map_mode=escort)
    db.session.add(havana)
    nepal = Map(name="NEPAL", map_mode=control)
    db.session.add(nepal)
    numbani = Map(name="NUMBANI", map_mode=hybrid)
    db.session.add(numbani)
    ilios = Map(name="ILIOS", map_mode=control)
    db.session.add(ilios)
    blizzard_world = Map(name="BLIZZARD WORLD", map_mode=hybrid)
    db.session.add(blizzard_world)
    volskaya_industries = Map(name="VOLSKAYA INDUSTRIES", map_mode=assault)
    db.session.add(volskaya_industries)
    kings_row = Map(name="KING'S ROW", map_mode=hybrid)
    db.session.add(kings_row)
    busan = Map(name='BUSAN', map_mode=control)
    db.session.add(busan)
    dorado = Map(name='DORADO', map_mode=escort)
    db.session.add(dorado)
    hanamura = Map(name='HANAMURA', map_mode=assault)
    db.session.add(hanamura)
    junkertown = Map(name='JUNKERTOWN', map_mode=escort)
    db.session.add(junkertown)
    lijiang = Map(name='LIJIANG TOWER', map_mode=control)
    db.session.add(lijiang)
    oasis = Map(name='OASIS', map_mode=control)
    db.session.add(oasis)
    rialto = Map(name='RIALTO', map_mode=escort)
    db.session.add(rialto)
    route_66 = Map(name='ROUTE 66', map_mode=escort)
    db.session.add(route_66)
    temple_anubis = Map(name='TEMPLE OF ANUBIS', map_mode=assault)
    db.session.add(temple_anubis)
    gibraltar = Map(name='WATCHPOINT: GIBRALTAR', map_mode=escort)
    db.session.add(gibraltar)
    eichenwalde = Map(name='EICHENWALDE', map_mode=hybrid)
    db.session.add(eichenwalde)

    colosseo = Map(name='COLOSSEO', map_mode=push)
    db.session.add(colosseo)
    new_queen_street = Map(name='NEW QUEEN STREET', map_mode=push)
    db.session.add(new_queen_street)

    circuit_royal = Map(name='CIRCUIT ROYAL', map_mode=escort)
    db.session.add(circuit_royal)

    midtown = Map(name='MIDTOWN', map_mode=hybrid)
    db.session.add(midtown)

    paraiso = Map(name='PARAISO', map_mode=hybrid)
    db.session.add(paraiso)

    db.session.commit()