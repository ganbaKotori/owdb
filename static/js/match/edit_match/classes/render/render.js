class RenderManager {
	constructor() {
		this.round_index_count = 0;
	}

	get_round_index() {
		return this.round_index_count++;
	}

	render_match_round(round_list_selector, phase = 'ATTACK', score = 0) {
		let round_index = this.get_round_index();
		$(round_list_selector).append(`
        <li class="list-group-item" id="match-round-${round_index}">
            <div class="row ml-2">
                <div class="col-4">
                    <h6><i>Phase</i></h6>
                    <input type="radio" 
                           class="btn-check attack-btn"
                           name="match_rounds-${round_index}-phase"
                           id="match_rounds-${round_index}-phase-attack"
                           autocomplete="off"
                           value="ATTACK"
                           data-round-id="${round_index}"
                           ${phase == 'ATTACK' ? 'checked' : ''}>
                    <label class="btn btn-outline-primary" for="match_rounds-${round_index}-phase-attack">Attack</label>
    
                    <input type="radio" 
                           class="btn-check defend-btn" 
                           name="match_rounds-${round_index}-phase" 
                           id="match_rounds-${round_index}-phase-defend"
                           autocomplete="off"
                           value="DEFEND"
                           data-round-id="${round_index}"
                           ${phase == 'DEFEND' ? 'checked' : ''}>
                    <label class="btn btn-outline-primary" for="match_rounds-${round_index}-phase-defend">Defend</label>
                </div>
                <div class="col-6">
                    <h6><i><span id="match_rounds-${round_index}-score-text">${phase == 'ATTACK'
			? 'Team Score'
			: 'Enemy Score'}</span></i></h6>
                    <div class="input-group">
                        <button class="btn btn-primary minus-btn" type="button" data-round-id="${round_index}">-</button>
                        <input type="text" class="form-control match-round-score ${phase == 'ATTACK'
							? 'match-round-score-attack'
							: 'match-round-score-defend'}" id="match_rounds-${round_index}-score-obtained" name="match_rounds-${round_index}-score" value="${score}" required>
                        <button class="btn btn-primary plus-btn" type="button" data-round-id="${round_index}">+</button>
                    </div>
                </div>
                <div class="col-2">
                    <svg class="icon icon-xs me-2 mt-4 delete-match-round-btn" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                </div>
            </div>
          </li>`);
	}
}
