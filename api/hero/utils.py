from app import db
from api.hero.models import Hero, HeroRole

def add_all_ow_heroes():
    '''
        Hero Roles should be created first so we can assign them to each Hero as their instantiated.
    '''
    dps = HeroRole(title="Damage")
    tank = HeroRole(title="Tank")
    support = HeroRole(title="Support")

    db.session.add(dps)
    db.session.add(tank)
    db.session.add(support)

    ana = Hero(name='Ana', hero_role=support)
    db.session.add(ana)
    ashe = Hero(name='Ashe', hero_role=dps)
    db.session.add(ashe)
    bap = Hero(name='Baptiste', hero_role=support)
    db.session.add(bap)
    bastion = Hero(name='Bastion', hero_role=dps)
    db.session.add(bastion)
    brig = Hero(name='Brigitte', hero_role=support)
    db.session.add(brig)
    dva = Hero(name='D.Va', hero_role=tank)
    db.session.add(dva)
    doom = Hero(name='Doomfist', hero_role=dps)
    db.session.add(doom)
    echo = Hero(name='Echo', hero_role=dps)
    db.session.add(echo)
    genji = Hero(name='Genji', hero_role=dps)
    db.session.add(genji)
    hanzo = Hero(name='Hanzo', hero_role=dps)
    db.session.add(hanzo)
    junk = Hero(name='Junkrat', hero_role=dps)
    db.session.add(junk)
    lucio = Hero(name='Lucio', hero_role=support)
    db.session.add(lucio)
    mcree = Hero(name='Cassidy', hero_role=dps)
    db.session.add(mcree)
    mei = Hero(name='Mei', hero_role=dps)
    db.session.add(mei)
    mercy = Hero(name='Mercy', hero_role=support)
    db.session.add(mercy)
    moira = Hero(name='Moira', hero_role=support)
    db.session.add(moira)
    orisa = Hero(name='Orisa', hero_role=tank)
    db.session.add(orisa)
    pharah = Hero(name='Pharah', hero_role=dps)
    db.session.add(pharah)
    reaper = Hero(name='Reaper', hero_role=dps)
    db.session.add(reaper)
    rein = Hero(name='Reinhardt', hero_role=tank)
    db.session.add(rein)
    hog = Hero(name='Roadhog', hero_role=tank)
    db.session.add(hog)
    sigma = Hero(name='Sigma', hero_role=tank)
    db.session.add(sigma)
    soldier = Hero(name='Soldier:76', hero_role=dps)
    db.session.add(soldier)
    sombra = Hero(name='Sombra', hero_role=dps)
    db.session.add(sombra)
    sym = Hero(name='Symmetra', hero_role=dps)
    db.session.add(sym)
    torb = Hero(name='Torbjorn', hero_role=dps)
    db.session.add(torb)
    tracer = Hero(name='Tracer', hero_role=dps)
    db.session.add(tracer)
    widow = Hero(name='Widowmaker', hero_role=dps)
    db.session.add(widow)
    winston = Hero(name='Winston', hero_role=tank)
    db.session.add(winston)
    ball = Hero(name='Wrecking Ball', hero_role=tank)
    db.session.add(ball)
    zarya = Hero(name='Zarya', hero_role=tank)
    db.session.add(zarya)
    zen = Hero(name='Zenyatta', hero_role=support)
    db.session.add(zen)

    db.session.commit()