class MapManager {
	constructor(ow_maps = []) {
		this.ow_maps = ow_maps;
	}

	// set_ow_map(ow_map) {
	// 	this.ow_map = ow_map;
	// }

	// get_ow_map() {}

	// is_map_mode_different(new_map) {
	// 	let new_map_mode = new_map.get_map_mode();
	// 	let new_map_mode_id = new_map_mode.id;

	// 	let current_map_mode = this.get_current_ow_map().get_map_mode();
	// 	let current_map_mode_id = current_map_mode.id;
	// 	if (new_map_mode_id == current_map_mode_id) return false;
	// 	else return true;
	// }

	get_map_by_id(ow_map_id) {
		let ow_map = this.ow_maps.find((pw_map) => {
			return ow_map.id === ow_map_id;
		});

		return ow_map;
	}
}
