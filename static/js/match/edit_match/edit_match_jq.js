$(document).ready(function() {
	let jq2 = () => {
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
			if (score - 1 >= 0) {
				$(`#match_rounds-${round_id}-score-obtained`).val(score - 1);
			}
			console.log(score);
			// get_total_team_score();
			update_match_final_results();
		});

		$(document).on('click', '.plus-btn', function() {
			let round_id = $(this).data('round-id');
			let score = parseInt($(`#match_rounds-${round_id}-score-obtained`).val());
			if (score + 1 <= match.current_map_selected.max_score) {
				$(`#match_rounds-${round_id}-score-obtained`).val(score + 1);
			}
			console.log(score);
			// get_total_team_score();
			update_match_final_results();
		});

		$('.add_tagged-friend-btn').on('click', function() {
			$('.tagged-friend-select').each(function() {
				console.log($(this).val());
			});
			match.add_tagged_friend();
		});

		$(document).on('click', '.delete-match-round-btn', function() {
			match.remove_round($(this).parent().parent().parent());
		});

		$(document).on('click', '.delete-tagged-friend-btn', function() {
			console.log('clicked');
			match.remove_tagged_friend($(this).parent().parent().parent());
		});

		$(document).on('click', '.attack-btn', function() {
			let round_id = $(this).data('round-id');
			console.log(round_id);
			$(`#match_rounds-${round_id}-score-text`).text('Team Score');
			$(`#match_rounds-${round_id}-score-obtained`).removeClass('match-round-score-defend');
			$(`#match_rounds-${round_id}-score-obtained`).addClass('match-round-score-attack');
			update_match_final_results();
		});

		$(document).on('click', '.defend-btn', function() {
			let round_id = $(this).data('round-id');
			console.log(round_id, 'defend');
			$(`#match_rounds-${round_id}-score-text`).text('Enemy Score');
			$(`#match_rounds-${round_id}-score-obtained`).removeClass('match-round-score-attack');
			$(`#match_rounds-${round_id}-score-obtained`).addClass('match-round-score-defend');
			update_match_final_results();
		});

		$('#ow_map_select').on('change', function() {
			console.log($('#ow_map_select option:selected').text());
			$('#map-image').attr('src', map_images[$('#ow_map_select option:selected').text()]);
			$('#map-title-text').text($('#ow_map_select option:selected').text());
			let current_map_id = parseInt($('#ow_map_select').val());
			console.log(current_map_id);
			let map_selected = ow_maps.find((ow_map) => ow_map.id === current_map_id);
			match.set_current_ow_map(map_selected);
			console.log(match.current_map_selected);
		});

		$('.match-round-score').on('change', function() {
			let current_max_score = match.current_map_selected.max_score;
			console.log(current_max_score);
			let current_score = $(this).val();
			console.log(current_score);
			if (current_score > current_max_score) {
				$(this).val(current_max_score);
			}
			//get_total_team_score();
		});

		$(document).on('click', '.control-enemy-plus', function() {
			match.add_round((phase = 'DEFEND'), (score = 1));
			update_match_final_results();
		});

		$(document).on('click', '.control-enemy-minus', function() {
			const defend_round = match.rounds.findIndex((round) => {
				return round.phase === 'DEFEND';
			});
			if (defend_round != null) {
				match.remove_round_by_id(match.rounds[defend_round].id);
				update_match_final_results();
			}
		});

		$(document).on('click', '.control-player-plus', function() {
			match.add_round((phase = 'ATTACK'), (score = 1));
			update_match_final_results();
		});

		$(document).on('click', '.control-player-minus', function() {
			const attack_round = match.rounds.findIndex((round) => {
				return round.phase === 'ATTACK';
			});
			if (attack_round != null) {
				match.remove_round_by_id(match.rounds[attack_round].id);
				update_match_final_results();
			}
		});

		$(document).on('change', '.match-round-score-attack', function() {
			//get_total_team_score();
			//get_total_enemy_score();
			update_match_final_results();
		});

		$(document).on('change', '.match-round-score-defend', function() {
			console.log('match round score deend is changed');
			//get_total_enemy_score();
			update_match_final_results();
		});

		$('.tag-friends-btn').on('click', async function() {
			// const friends = await get_current_user_friends();
			// console.log(friends)
		});

		$('.today-btn').on('click', async function() {
			fp.setDate(new Date());
		});

		$('.delete-match-btn').on('click', async function() {
			if (confirm('Are you sure you want to delete this match?') == true) {
				let match_id = $(this).data('match-id');
				let delete_match_response = await delete_match(match_id);
				if (delete_match_response.status == 200) {
					alert('Match Deleted!');
					$(`#match-${match_id}-tr`).slideUp();
				}
				console.log(delete_match_response.status);
			} else {
			}
		});
	};
});

const render_all = (match_manager, render_manager) => {
	console.log('renderinggg');
	match_manager.get_match().get_rounds().forEach((m, index) => {
		render_manager.render_match_round(MATCH_ROUND_LIST_CLASSNAME, m.get_phase(), m.get_score(), index);
	});
};

const jq = (match_manager, render_manager) => {
	$('.add-round-btn').on('click', render_all, function() {
		console.log('render');
		match_manager.get_match().get_match_round_manager().add_round();
		//render_manager.render_match_round(MATCH_ROUND_LIST_CLASSNAME);
		render_all(match_manager, render_manager);
	});
};
