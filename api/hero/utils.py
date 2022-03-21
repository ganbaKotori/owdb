from app import db
from api.hero.models import Hero

def add_all_ow_heroes():
    winston = Hero(name="Winston")
    db.session.add(winston)
    reinhardt = Hero(name="Reinhardt")
    db.session.add(reinhardt)
    zarya = Hero(name="Zarya")
    db.session.add(zarya)
    dva = Hero(name="D.Va")
    db.session.add(dva)
    sigma = Hero(name="Sigma")
    db.session.add(sigma)
    roadhog = Hero(name="Roadhog")
    db.session.add(roadhog)
    wrecking_ball = Hero(name="Wrecking Ball")
    db.session.add(wrecking_ball)
    orisa = Hero(name="Orisa")
    db.session.add(orisa)
    db.session.commit()