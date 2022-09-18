const MAX_TAGGED_FRIENDS = 5;
class Match {
	constructor(friends) {
		this.round_count = 0;
		this.round_id_count = 0;
		this.total_player_team_score = 0;
		this.total_enemy_team_score = 0;
		this.current_map_id = null;
		this.current_map_selected = null;
		this.add_round('ATTACK', 0);

		this.tagged_friend_count = 0;
		this.tagged_friend_id_count = 0;
		//this.tagged_friends = tagged_friends;
		this.all_friends = friends;
	}

	set_current_ow_map(ow_map) {
		this.current_map_selected = ow_map;
	}
	
	get_friends_options() {
		let friends_options_str = '';
		let current_tagged_friends = [];


		$(".tagged-friend-select").each(function () {
			if($(this).val() != null){
				current_tagged_friends.push($(this).val());
			}
		})

		this.all_friends.forEach(friend => {
			if (!current_tagged_friends.includes(friend)){
				friends_options_str += `<option value="${friend}">${friend}</option>`;
			}
			
		})
		return friends_options_str
	}

	add_round(phase, score) {
		this.round_count++;
		$('.match-round-list').append(`
		<li class="list-group-item">
			<div class="row ml-2">
				<div class="col-4">
					<h6><i>Phase</i></h6>
					<input type="radio" 
						   class="btn-check attack-btn"
						   name="match_rounds-${this.round_id_count}-phase"
						   id="match_rounds-${this.round_id_count}-phase-attack"
						   autocomplete="off"
						   value="ATTACK"
						   data-round-id="${this.round_id_count}"
						   ${phase=="ATTACK" ? "checked": ""}>
					<label class="btn btn-outline-primary" for="match_rounds-${this.round_id_count}-phase-attack">Attack</label>

					<input type="radio" 
						   class="btn-check defend-btn" 
						   name="match_rounds-${this.round_id_count}-phase" 
						   id="match_rounds-${this.round_id_count}-phase-defend"
						   autocomplete="off"
						   value="DEFEND"
						   data-round-id="${this.round_id_count}"
						   ${phase=="DEFEND" ? "checked": ""}>
					<label class="btn btn-outline-primary" for="match_rounds-${this.round_id_count}-phase-defend">Defend</label>
				</div>
				<div class="col-6">
					<h6><i><span id="match_rounds-${this.round_id_count}-score-text">${phase=="ATTACK" ? "Team Score": "Enemy Score"}</span></i></h6>
					<div class="input-group">
						<button class="btn btn-primary minus-btn" type="button" data-round-id="${this.round_id_count}">-</button>
						<input type="text" class="form-control match-round-score" id="match_rounds-${this.round_id_count}-score-obtained" name="match_rounds-${this.round_id_count}-score" value="${score}" required>
						<button class="btn btn-primary plus-btn" type="button" data-round-id="${this.round_id_count}">+</button>
					</div>
				</div>
				<div class="col-2">
					<svg class="icon icon-xs me-2 mt-4 delete-match-round-btn" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
				</div>
			</div>
	  	</li>`);
		this.round_id_count++;
	}

	add_tagged_friend() {
		if(this.tagged_friend_count < MAX_TAGGED_FRIENDS){
			$('.tagged-friends-list').append(`
			<li class="list-group-item">
				<div class="row ml-2">
					<div class="col-5">
						<h6><i>Role</i></h6>
						<input
							class="btn-check"
							id="tagged_friends-${this.tagged_friend_id_count}-role-damage"
							name="tagged_friends-${this.tagged_friend_id_count}-role" 
							type="radio"
							value="DAMAGE"
							checked
						>
						<label class="btn btn-outline-danger" for="tagged_friends-${this.tagged_friend_id_count}-role-damage">Damage</label>
						<input 
							class="btn-check"
							id="tagged_friends-${this.tagged_friend_id_count}-role-tank"
							name="tagged_friends-${this.tagged_friend_id_count}-role"
							type="radio"
							value="TANK"
						>
						<label class="btn btn-outline-danger" for="tagged_friends-${this.tagged_friend_id_count}-role-tank">Tank</label>
						<input
							class="btn-check"
							id="tagged_friends-${this.tagged_friend_id_count}-role-support"
							name="tagged_friends-${this.tagged_friend_id_count}-role"
							type="radio"
							value="SUPPORT"
						>
						<label class="btn btn-outline-danger" for="tagged_friends-${this.tagged_friend_id_count}-role-support">Support</label>
					</div>
					<div class="col-5">
						<h6><i><span id="tagged_friends-${this.tagged_friend_id_count}-score-text"></span>Friend</i></h6>
						<select 
							class="form-select form-select-lg tagged-friend-select"
							id="tagged_friends-${this.tagged_friend_id_count}-username"
							name="tagged_friends-${this.tagged_friend_id_count}-username">
								${this.get_friends_options()}
						</select>
					</div>
					<div class="col-2">
						<svg class="icon icon-xs me-2 mt-4 delete-tagged-friend-btn" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
					</div>
				</div>
			  </li>`);
			this.tagged_friend_id_count++;
			this.tagged_friend_count++;
		}
	}

	remove_round(round) {
		if (this.round_count > 1) {
			this.round_count--;
			round.remove();
		}
	}

	remove_tagged_friend(tagged_friend) {
		tagged_friend.remove();
		this.tagged_friend_count--;

	}

	_check_round_count() {
		if (this.round_count == 0) {
			console.log('no rounds!');
		}
	}
}

class User {
	constructor(id) {
		this.id = id;
		this.heroes_played = [];
		this.hero_role = null;

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

class Hero {
	constructor(id){
		this.id = id;
	}
}

class MatchRound {
	constructor(phase, score) {
		this.phase = phase;
		this.score = score;
	}
}

class OverwatchMap {
	constructor(id, name, map_mode, max_score) {
		this.id = id;
		this.name = name;
		this.map_mode = map_mode;
		this.max_score = max_score;
	}
}

const match = new Match(current_user_friends);
const ow_maps = [];

ow_maps_data.forEach(ow_map => {
	let new_map = new OverwatchMap(ow_map.id, ow_map.name, ow_map.map_mode.name, ow_map.map_mode.max_score);
	ow_maps.push(new_map)
});



const map_images = {
"HOLLYWOOD" : "\\static\\assets\\img\\ow_map_img\\hollywood.jpg",
"HAVANA" : "\\static\\assets\\img\\ow_map_img\\default.jpg",
"NEPAL" : "\\static\\assets\\img\\ow_map_img\\nepal.jpg",
"NUMBANI" : "\\static\\assets\\img\\ow_map_img\\numbani.jpg",
"ILIOS" : "\\static\\assets\\img\\ow_map_img\\ilios.jpg",
"BLIZZARD WORLD" : "\\static\\assets\\img\\ow_map_img\\blizzard-world.jpg",
"VOLSKAYA INDUSTRIES" : "\\static\\assets\\img\\ow_map_img\\volskaya-industries.jpg",
"KING'S ROW" :  "\\static\\assets\\img\\ow_map_img\\kings-row.jpg",
"BUSAN"  : "\\static\\assets\\img\\ow_map_img\\busan.jpg",
"DORADO" : "\\static\\assets\\img\\ow_map_img\\dorado.jpg",
"HANAMURA" : "\\static\\assets\\img\\ow_map_img\\hanamura.jpg",
"JUNKERTOWN" : "\\static\\assets\\img\\ow_map_img\\junkertown.jpg",
"LIJIANG TOWER" : "\\static\\assets\\img\\ow_map_img\\lijiang-tower.jpg",
"OASIS" : "\\static\\assets\\img\\ow_map_img\\oasis.jpg",
"RIALTO" : "\\static\\assets\\img\\ow_map_img\\rialto.jpg",
"ROUTE 66" : "\\static\\assets\\img\\ow_map_img\\route-66.jpg",
"TEMPLE OF ANUBIS" : "\\static\\assets\\img\\ow_map_img\\temple-of-anubis.jpg",
"WATCHPOINT: GIBRALTAR" : "\\static\\assets\\img\\ow_map_img\\watchpoint-gibraltar.jpg",
"EICHENWALDE" :  "\\static\\assets\\img\\ow_map_img\\eichenwalde.jpg"
}


const get_friends_options = friends => {
	let friends_options_str = ''
	friends.forEach(friend => {
		friends_options_str += `<option value="${friend}">${friend}</option>`;
	})
	return friends_options_str
}

$(document).ready(function() {
	var date = new Date();
	$('.ow-hero-check').hide();
	$('#date-match-played').val(((date.getMonth() > 8) ? (date.getMonth() + 1) : ('0' + (date.getMonth() + 1))) + '/' + ((date.getDate() > 9) ? date.getDate() : ('0' + date.getDate())) + '/' + date.getFullYear());

	$('.ow-hero-role-radio-btn').on('change', function() {
		console.log($(this).val());
		$('.ow-hero-check').hide();
		$(`.ow-hero-check-role-${$(this).val()}`).show();
	});

	$('.add-round-btn').on('click', function() {
		match.add_round('ATTACK', 0);
	});

	$(document).on('click', '.minus-btn', function() {
		let round_id = $(this).data('round-id');
		let score = parseInt($(`#match_rounds-${round_id}-score-obtained`).val());
		if(score - 1 >= 0){
			$(`#match_rounds-${round_id}-score-obtained`).val(score - 1);
		}
		console.log(score)
	});

	$(document).on('click', '.plus-btn', function() {
		let round_id = $(this).data('round-id');
		let score = parseInt($(`#match_rounds-${round_id}-score-obtained`).val());
		if(score + 1 <= match.current_map_selected.max_score){
			$(`#match_rounds-${round_id}-score-obtained`).val(score + 1);
		}
		console.log(score)
	});

	$('.add_tagged-friend-btn').on('click', function() {
		$(".tagged-friend-select").each(function () {

			console.log($(this).val());
		
		})
		match.add_tagged_friend();
	});

	$(document).on('click', '.delete-match-round-btn', function() {
		match.remove_round($(this).parent().parent().parent());
	});

	$(document).on('click', '.delete-tagged-friend-btn', function() {
		console.log('clicked')
		match.remove_tagged_friend($(this).parent().parent().parent());
	});

	$(document).on('click', '.attack-btn', function() {
		let round_id = $(this).data('round-id');
		console.log(round_id);
		$(`#match_rounds-${round_id}-score-text`).text('Team Score')
	});

	$(document).on('click', '.defend-btn', function() {
		let round_id = $(this).data('round-id');
		console.log(round_id);
		$(`#match_rounds-${round_id}-score-text`).text('Enemy Score')
	});


	

	$('#ow_map_select').on('change', function() {
		console.log($( "#ow_map_select option:selected" ).text())
		$('#map-image').attr('src',map_images[$( "#ow_map_select option:selected" ).text()]);
		$('#map-title-text').text($( "#ow_map_select option:selected" ).text());
		let current_map_id = parseInt($('#ow_map_select').val());
		console.log(current_map_id)
		let map_selected = ow_maps.find(ow_map => ow_map.id === current_map_id);
		match.set_current_ow_map(map_selected)
		console.log(match.current_map_selected)
	});

	$('.match-round-score').on('change', function() {
		let current_max_score = match.current_map_selected.max_score;
		console.log(current_max_score);
		let current_score = $(this).val();
		console.log(current_score)
		if (current_score > current_max_score){
			$(this).val(current_max_score)
		}

	});

	$('.tag-friends-btn').on('click', async function() {
		// const friends = await get_current_user_friends();
		// console.log(friends)

	});

	$('.today-btn').on('click', async function() {
		$('#date-match-played').val(((date.getMonth() > 8) ? (date.getMonth() + 1) : ('0' + (date.getMonth() + 1))) + '/' + ((date.getDate() > 9) ? date.getDate() : ('0' + date.getDate())) + '/' + date.getFullYear());
	});
	
});
