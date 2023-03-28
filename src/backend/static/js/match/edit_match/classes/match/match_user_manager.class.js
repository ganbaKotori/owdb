class MatchUserManager {
	constructor(match_users = [], current_user_id) {
		this.match_users = match_users;
		this.current_user_id = current_user_id;
	}

	get_tagged_friends() {
		let current_match_user = this.match_users.find((match_user) => {
			return match_user.user_id !== current_user_id;
		});
		//console.log(current_match_user);

		return current_match_user;
	}

	get_current_match_user() {
		let current_match_user = this.match_users.find((match_user) => {
			return match_user.user_id === current_user_id;
		});
		console.log(current_match_user);

		return current_match_user;
	}

	add_friend(User) {
		this.match_users.push(User);
	}

	remove_friend_by_id(match_user_id) {
		if (match_user_id == this.get_current_match_user().id) {
			alert('Cannot remove Match creator!');
			return;
		}
		let match_users_index = this.match_users.findIndex((mu) => {
			return mu.id === match_user_id;
		});

		console.log('removing friend', match_users_index);
		this.match_users.splice(match_users_index, 1);
	}
}
