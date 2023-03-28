class MatchMapManager {
	constructor(ow_map = null) {
		this.ow_map = ow_map;
	}

	set_ow_map(ow_map) {
		this.ow_map = ow_map;
	}

	get_ow_map() {
		return this.ow_map;
	}

	static is_map_mode_different(new_map) {
		let new_map_mode_id = new_map.get_map_mode().get_id();
		let current_map_mode_id = this.get_ow_map().get_map_mode().get_id();

		if (new_map_mode_id == current_map_mode_id) return false;
		else return true;
	}
}
