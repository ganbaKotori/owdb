class MatchManager {
	constructor(match, ow_maps = [], ow_heroes = []) {
		this.match = match;
		this.ow_maps = ow_maps;
		this.ow_heroes = ow_heroes;
	}

	get_match() {
		return this.match;
	}
}
