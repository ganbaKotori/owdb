class FriendsManager {
	constructor(friends=[]) {
        this.friends = friends;
	}

    add_friend(User){
        this.friends.push(User);
    }

    remove_friend(round_id){
        let friends_index = this.friends.findIndex(round => {
			return round.id === round_id;
		  });

        console.log('removing friend', friends_index);
        this.rounds.splice(friends_index, 1);
    }
}