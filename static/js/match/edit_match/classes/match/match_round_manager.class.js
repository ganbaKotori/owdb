class MatchRoundManager {
	_match_round_iteration = 0;
	total_player_team_score = 0;
	total_enemy_team_score = 0;

	constructor(match_rounds=[new MatchRound(MatchRoundPhase.Attack, 0,this.get_next_match_round_iteration())]) {
		this.match_rounds = match_rounds;
	}

    add_round(match_round) {
		this.match_rounds.push(match_round);
	}

	get_next_match_round_iteration(){
		let current_iteration = this._match_round_iteration;
		this._match_round_iteration++;
		return current_iteration;
	}
}