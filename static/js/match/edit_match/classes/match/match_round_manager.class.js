class MatchRoundManager {
	_match_round_iteration = 0;

	constructor(match_rounds = [ new MatchRound(MatchRoundPhase.Attack, 0, this.get_next_match_round_iteration()) ]) {
		this.match_rounds = match_rounds;
	}

	get_rounds() {
		return this.match_rounds;
	}

	add_round(phase = MatchRoundPhase.Attack, score = 0) {
		this.match_rounds.push(new MatchRound(phase, score, this.get_next_match_round_iteration()));
	}

	remove_round_by_id(match_round_id) {
		let match_round_index = this.match_rounds.findIndex((mr) => {
			return mr.id === match_round_id;
		});

		console.log('removing round', match_round_index);
		this.match_users.splice(match_round_index, 1);
	}

	get_next_match_round_iteration() {
		let current_iteration = this._match_round_iteration;
		this._match_round_iteration++;
		return current_iteration;
	}

	get_total_team_score() {
		let total = 0;
		this.match_rounds.forEach((mr) => {
			if (mr.get_phase == MatchRoundPhase.Attack) total += mr.get_score();
		});
		return total;
	}

	get_total_enemy_score() {
		let total = 0;
		this.match_rounds.forEach((mr) => {
			if (mr.get_phase == MatchRoundPhase.Defend) total += mr.get_score();
		});
		return total;
	}
}
