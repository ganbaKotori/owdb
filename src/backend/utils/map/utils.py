from schema.map.MapSchema import MapSchema
from models.map.Map import Map

def get_map_json(ow_map: Map):
    map_schema = MapSchema()
    return map_schema.dump(ow_map)

def get_all_map_json():
    ow_maps_json = []
    ow_maps = Map.query.order_by(Map.name.asc()).all()
    for m in ow_maps:
        ow_maps_json.append(get_map_json(m))
    return ow_maps_json

