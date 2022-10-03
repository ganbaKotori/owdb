const MAX_TAGGED_FRIENDS = 4;


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
	constructor(id, phase, score) {
		this.id = id;
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

let get_total_team_score = () => {
	console.log('GETTING TEAM SCORE')
	let total_team_score = 0;
	$(".match-round-score-attack").each(function () {
		if($(this).val() != null){
			total_team_score += parseInt($(this).val());
		}
	})
	$('#team-score-total').text(total_team_score);
	$('#team-score-total').addClass("confirm_selection");
	$('#team-score-total').on("animationend", function(){
		$(this).removeClass('confirm_selection');
	  });
	return total_team_score;
}

let get_total_enemy_score = () => {
	let total_enemy_score = 0;
	$(".match-round-score-defend").each(function () {
		if($(this).val() != null){
			total_enemy_score += parseInt($(this).val());
		}
	});
	console.log(total_enemy_score, 'DEEND')
	$('#enemy-score-total').text(total_enemy_score);
	$('#enemy-score-total').addClass("confirm_selection");
	$('#enemy-score-total').on("animationend", function(){
		$(this).removeClass('confirm_selection');
	  });
	return total_enemy_score;
}



$(document).ready(function() {
	var date = new Date();
	$('.ow-hero-check').hide();

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
		console.log(score);
		// get_total_team_score();
		update_match_final_results();
	});

	$(document).on('click', '.plus-btn', function() {
		let round_id = $(this).data('round-id');
		let score = parseInt($(`#match_rounds-${round_id}-score-obtained`).val());
		if(score + 1 <= match.current_map_selected.max_score){
			$(`#match_rounds-${round_id}-score-obtained`).val(score + 1);
		}
		console.log(score);
		// get_total_team_score();
		update_match_final_results();
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
		$(`#match_rounds-${round_id}-score-text`).text('Team Score');
		$(`#match_rounds-${round_id}-score-obtained`).removeClass('match-round-score-defend');
		$(`#match_rounds-${round_id}-score-obtained`).addClass('match-round-score-attack');
		// get_total_enemy_score();
		// get_total_team_score();
		update_match_final_results();
	});

	$(document).on('click', '.defend-btn', function() {
		let round_id = $(this).data('round-id');
		console.log(round_id, 'defend');
		$(`#match_rounds-${round_id}-score-text`).text('Enemy Score');
		$(`#match_rounds-${round_id}-score-obtained`).removeClass('match-round-score-attack');
		$(`#match_rounds-${round_id}-score-obtained`).addClass('match-round-score-defend');
		// get_total_enemy_score();
		// get_total_team_score();
		update_match_final_results();
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
		//get_total_team_score();

	});

	$(document).on('change', '.match-round-score-attack',function() {
		//get_total_team_score();
		//get_total_enemy_score();
		update_match_final_results();
	});

	$(document).on('change', '.match-round-score-defend', function() {
		console.log('match round score deend is changed')
		//get_total_enemy_score();
		update_match_final_results();
	});

	$('.tag-friends-btn').on('click', async function() {
		// const friends = await get_current_user_friends();
		// console.log(friends)

	});

	$('.today-btn').on('click', async function() {
		$('#date-match-played').val(((date.getMonth() > 8) ? (date.getMonth() + 1) : ('0' + (date.getMonth() + 1))) + '/' + ((date.getDate() > 9) ? date.getDate() : ('0' + date.getDate())) + '/' + date.getFullYear());
	});

	$(document).on('click', '.control-player-plus', function() {
		match.add_round(phase="ATTACK", score=1);
		update_match_final_results();
	})

	$(document).on('click', '.control-player-minus', function() {
		const attack_round = match.rounds.findIndex(round => {
			return round.phase === 'ATTACK';
		  });
		if (attack_round != null){
			match.remove_round_by_id(match.rounds[attack_round].id);
			update_match_final_results();
		}
	})

	$(document).on('click', '.control-enemy-plus', function() {
		match.add_round(phase="DEFEND", score=1);
		update_match_final_results();
	})

	$(document).on('click', '.control-enemy-minus', function() {
		const defend_round = match.rounds.findIndex(round => {
			return round.phase === 'DEFEND';
		  });
		if (defend_round != null){
			match.remove_round_by_id(match.rounds[defend_round].id);
			update_match_final_results();
		}
	})
	
});

let update_match_final_results = () => {
	let total_enemy_score = get_total_enemy_score();
	let total_team_score = get_total_team_score();
	if (total_team_score > total_enemy_score){
		$('#match-final-result').text('VICTORY');
	} else if(total_team_score < total_enemy_score){
		$('#match-final-result').text('DEFEAT');
	} else {
		$('#match-final-result').text('DRAW');
	}
}
