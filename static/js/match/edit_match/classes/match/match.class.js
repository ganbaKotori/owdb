class Match {
	constructor(friends_manager, match_round_manager, match_map_manager) {
        this.friends_manager = friends_manager;
        this.match_round_manager = match_round_manager;
        this.match_map_manager = match_map_manager;
	}

	add_friend(){
		let friend = User();
		this.friends_manager.add_friend();
	}

	// set_current_ow_map(ow_map) {
	// 	if(this.current_map_selected != null && this.current_map_selected.map_mode != ow_map.map_mode){
    //         if (confirm("Changing to a different Match Mode will reset Match Rounds. Continue?") == true) {
    //             this.remove_all_rounds();
    //             this.current_map_selected = ow_map;
    //             update_match_final_results();
    //             if (ow_map.map_mode == 'Control'){
    //                 this.show_contol_rounds();
    //             } else {
    //             }
    //         } else {

    //         }
	// 	} else {
    //         this.current_map_selected = ow_map;
    //         update_match_final_results();
    //         if (ow_map.map_mode == 'Control'){
    //             this.show_contol_rounds();
    //         } else {
    //         }

    //     }
	// }
	
	// get_friends_options() {
	// 	let friends_options_str = '';
	// 	let current_tagged_friends = [];


	// 	$(".tagged-friend-select").each(function () {
	// 		if($(this).val() != null){
	// 			current_tagged_friends.push($(this).val());
	// 		}
	// 	})

	// 	this.all_friends.forEach(friend => {
	// 		if (!current_tagged_friends.includes(friend)){
	// 			friends_options_str += `<option value="${friend}">${friend}</option>`;
	// 		}
			
	// 	})
	// 	return friends_options_str
	// }

	// add_tagged_friend() {
	// 	if(this.tagged_friend_count < MAX_TAGGED_FRIENDS){
	// 		this.tagged_friend_id_count++;
	// 		this.tagged_friend_count++;
	// 	}
	// }

	// show_contol_rounds(){
	// 	$('.match-row').hide();
	// 	$('.control-match-row').show();
	// }


	// remove_tagged_friend(tagged_friend){
	// 	tagged_friend.remove();
	// 	this.tagged_friend_count--;

	// }

	// _check_round_count(){
	// 	if (this.round_count == 0) {
	// 		console.log('no rounds!');
	// 	}
	// }

	// remove_all_rounds(){
	// 	this.round_count = 0;
    //     this.rounds = [];
	// 	$('.match-round-list').empty();
	// }

}