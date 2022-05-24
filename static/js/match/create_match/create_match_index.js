class Match {
	constructor() {
		this.round_count = 0;
		this.round_id_count = 0;
		this.total_player_team_score = 0;
		this.total_enemy_team_score = 0;
		this.current_map_id = null;
		this.current_map_selected = null;
		this.add_round();
	}

	set_current_ow_map(ow_map) {
		this.current_map_selected = ow_map;
	}

	add_round() {
		this.round_count++;
		$('.match-round-list').append(`
		<li class="list-group-item">
			<div class="row ml-2">
				<div class="col-4">
					<h6><i>Phase</i></h6>
					<input type="radio" 
						   class="btn-check"
						   name="match_rounds-${this.round_id_count}-phase"
						   id="match_rounds-${this.round_id_count}-phase-attack"
						   autocomplete="off"
						   value="ATTACK"
						   checked>
					<label class="btn btn-outline-danger" for="match_rounds-${this.round_id_count}-phase-attack">Attack</label>

					<input type="radio" 
						   class="btn-check" 
						   name="match_rounds-${this.round_id_count}-phase" 
						   id="match_rounds-${this.round_id_count}-phase-defend"
						   autocomplete="off"
						   value="DEFEND"  
						   >
					<label class="btn btn-outline-info" for="match_rounds-${this.round_id_count}-phase-defend">Defend</label>
				</div>
				<div class="col-6">
					<h6><i><span id="match_rounds-${this.round_id_count}-score-text"></span> Score</i></h6>
					<div class="input-group">
						<button class="btn btn-primary" type="button" id="button-addon1">-</button>
						<input type="text" class="form-control match-round-score" id="match_rounds-${this.round_id_count}-score-obtained" name="match_rounds-${this.round_id_count}-score">
						<button class="btn btn-primary" type="button" id="button-addon1">+</button>
					</div>
				</div>
				<div class="col-2">
					<svg class="icon icon-xs me-2 mt-4 delete-match-round-btn" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
				</div>
			</div>
	  	</li>`);
		this.round_id_count++;
	}

	remove_round(round) {
		if (this.round_count > 1) {
			this.round_count--;
			round.remove();
		}
	}

	_check_round_count() {
		if (this.round_count == 0) {
			console.log('no rounds!');
		}
	}
}

/*
				<div class="col-3">
					<h6><i>Result</i></h6>
					<input type="radio" 
						   class="btn-check"
						   name="match_rounds-${this.round_id_count}-result"
						   id="match_rounds-${this.round_id_count}-result-captured"
						   autocomplete="off"
						   value=1
						   checked>
					<label class="btn btn-outline-success btn-sm" for="match_rounds-${this.round_id_count}-result-captured">
						Objectives Captured
						<svg class="icon icon-xs" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
					</label>

					<input type="radio"
						   class="btn-check"
						   name="match_rounds-${this.round_id_count}-result"
						   id="match_rounds-${this.round_id_count}-result-lost"
						   autocomplete="off"
						   value=0>
					<label class="btn btn-outline-danger btn-sm" for="match_rounds-${this.round_id_count}-result-lost">
						Objectives Lost
						<svg class="icon icon-xs" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
					</label>
				</div>
*/

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

const match = new Match();
const ow_maps = [];

ow_maps_data.forEach(ow_map => {
	let new_map = new OverwatchMap(ow_map.id, ow_map.name, ow_map.map_mode.name, ow_map.map_mode.max_score);
	ow_maps.push(new_map)
});

console.log(ow_maps)



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

$(document).ready(function() {
	$('.ow-hero-check').hide();
	console.log('starting');

	$('.ow-hero-role-radio-btn').on('change', function() {
		console.log($(this).val());
		$('.ow-hero-check').hide();
		$(`.ow-hero-check-role-${$(this).val()}`).show();
	});

	$('.add-round-btn').on('click', function() {
		match.add_round();
	});

	$(document).on('click', '.delete-match-round-btn', function() {
		match.remove_round($(this).parent().parent().parent());
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
	
});
