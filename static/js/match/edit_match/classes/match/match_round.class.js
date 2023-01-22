class MatchRound {
	constructor(phase = MatchRoundPhase.Attack, score = 0, id) {
		this.id = id;
		this.phase = phase;
		this.score = score;
	}

	get_score() {
		return this.score;
	}

	get_phase() {
		return this.phase;
	}
}
