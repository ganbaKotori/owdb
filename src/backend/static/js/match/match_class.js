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

class Match {
	constructor(friends) {
		this.round_count = 0;
		this.round_id_count = 0;
		this.total_player_team_score = 0;
		this.total_enemy_team_score = 0;
		this.current_map_id = null;
		this.current_map_selected = null;
		this.current_map_mode = null;
		this.rounds = [];
		this.add_round('ATTACK', 0);

		this.tagged_friend_count = 0;
		this.tagged_friend_id_count = 0;
		this.all_friends = friends;
	
	}

	set_current_ow_map(ow_map) {
		if(this.current_map_selected != null && this.current_map_selected.map_mode != ow_map.map_mode){
            if (confirm("Changing to a different Match Mode will reset Match Rounds. Continue?") == true) {
                this.remove_all_rounds();
                this.current_map_selected = ow_map;
                update_match_final_results();
                if (ow_map.map_mode == 'Control'){
                    this.show_contol_rounds();
                } else {
                }
            } else {

            }
		} else {
            this.current_map_selected = ow_map;
            update_match_final_results();
            if (ow_map.map_mode == 'Control'){
                this.show_contol_rounds();
            } else {
            }

        }
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
		<li class="list-group-item" id="match-round-${this.round_id_count}">
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
						<input type="text" class="form-control match-round-score ${phase=="ATTACK" ? "match-round-score-attack": "match-round-score-defend"}" id="match_rounds-${this.round_id_count}-score-obtained" name="match_rounds-${this.round_id_count}-score" value="${score}" required>
						<button class="btn btn-primary plus-btn" type="button" data-round-id="${this.round_id_count}">+</button>
					</div>
				</div>
				<div class="col-2">
					<svg class="icon icon-xs me-2 mt-4 delete-match-round-btn" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
				</div>
			</div>
	  	</li>`);
		this.rounds.push(new MatchRound(this.round_id_count,phase,score));
		this.round_id_count++;

		
		console.log(this.rounds)
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
								<option value="">Select Friend</option>
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

	show_contol_rounds(){
		$('.match-row').hide();
		$('.control-match-row').show();
	}

	remove_round(round){
		if (this.round_count > 1) {
			this.round_count--;
			round.remove();
		}
	}

    remove_round_by_id(round_id){
        let match_round_index = this.rounds.findIndex(round => {
			return round.id === round_id;
		  });

        console.log('removing', match_round_index);
        this.rounds.splice(match_round_index, 1);
        $(`#match-round-${round_id}`).remove();
    }

	remove_tagged_friend(tagged_friend){
		tagged_friend.remove();
		this.tagged_friend_count--;

	}

	_check_round_count(){
		if (this.round_count == 0) {
			console.log('no rounds!');
		}
	}

	remove_all_rounds(){
		this.round_count = 0;
        this.rounds = [];
		$('.match-round-list').empty();
	}

}