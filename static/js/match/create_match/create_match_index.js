class Match {
	constructor() {
		this.round_count = 0;
		this.add_round();
	}

	add_round() {
		this.round_count++;
		$('.match-round-list').append(`
		<li class="list-group-item">
			<div class="row ml-2">
				<div class="col">
					<h6><i> Round Phase</i></h6>
					<input type="radio" class="btn-check" name="options-outlined" id="success-outlined" autocomplete="off" checked>
					<label class="btn btn-outline-danger" for="success-outlined">ATTACK</label>

					<input type="radio" class="btn-check" name="options-outlined" id="danger-outlined" autocomplete="off">
					<label class="btn btn-outline-info" for="danger-outlined">DEFEND</label>
				</div>
				<div class="col">
					<h6><i>Round Result</i></h6>
					<input type="radio" class="btn-check" name="options-outlined" id="success-outlined" autocomplete="off" checked>
					<label class="btn btn-outline-danger" for="success-outlined">All Objectives Cleared</label>

					<input type="radio" class="btn-check" name="options-outlined" id="danger-outlined" autocomplete="off">
					<label class="btn btn-outline-info" for="danger-outlined">Out of Time</label>
				</div>
			</div>
	  	</li>`);
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

class MatchRound {
	constructor(phase, result) {
		this.phase = phase;
		this.result = result;
	}
}

const match = new Match();

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
});
