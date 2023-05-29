class User {
	constructor(id, username, hero_manager = null, user_id) {
		this.id = id;
		this.username = username;
		this.hero_manager = hero_manager;
		this.user_id = user_id;
	}

	// constructor(id, heroes_played, hero_role) {
	// 	this.id = id;
	// 	this.heroes_played = heroes_played;
	// 	this.hero_role = hero_role;
	// }
	add_hero(hero_id) {
		this.heroes_played.push(hero_id);
	}
}
