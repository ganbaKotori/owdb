class MatchRoundManager {
	constructor(match_rounds=[]) {
		this.match_rounds = match_rounds;

		this.total_player_team_score = 0;
		this.total_enemy_team_score = 0;
	}

    add_round(match_round) {
		this.match_rounds.push(match_round);
	}
}