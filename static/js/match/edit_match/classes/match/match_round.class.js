class MatchRound {
	constructor(phase="ATTACK", score=0, id=null) {
		this.id = id;
		this.phase = phase;
		this.score = score;
	}

    add_round(phase, score) {
		this.round_count++;
		this.rounds.push(new MatchRound(this.round_id_count,phase,score));
		this.round_id_count++;
		console.log(this.rounds)
	}
}