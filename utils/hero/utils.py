from models.map.Map import Map
from models.hero.Hero import Hero
from schema.hero.HeroSchema import HeroSchema

def get_hero_json(ow_map: Map):
    hero_schema = HeroSchema()
    return hero_schema.dump(ow_map)

def get_all_heroes_json():
    ow_heroes_json = []
    ow_heroes = Hero.query.order_by(Hero.name.asc()).all()
    
    for h in ow_heroes:
        ow_heroes_json.append(get_hero_json(h))
    return ow_heroes_json