class User {
	constructor(id, hero_manager=null) {
		this.id = id;
        this.hero_manager = hero_manager;
	}

	// constructor(id, heroes_played, hero_role) {
	// 	this.id = id;
	// 	this.heroes_played = heroes_played;
	// 	this.hero_role = hero_role;
	// }
	add_hero(hero_id){
		this.heroes_played.push(hero_id);
	}
}
