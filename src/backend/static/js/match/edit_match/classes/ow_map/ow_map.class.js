class OverwatchMap {
	constructor(id, name, ow_map_mode, image_location) {
		this.id = id;
		this.name = name;
		this.ow_map_mode = ow_map_mode;
		this.image_location = image_location;
	}

	get_map_mode() {
		return this.ow_map_mode.id;
	}

	get_image_location() {
		return this.image_location;
	}
}
