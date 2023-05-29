const get_current_user_friends = async () => {
    const response = await fetch(`/api/user/friendship`, {
        method: 'GET',
    });
    return response.json();
}

const send_friend_request = async username => {
    const response = await fetch(`/api/user/${username}/send_friend_request`, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
    });
    return response.json();
}

const accept_friend_request = async friendship_id => {
    const response = await fetch(`/api/user/friendship/${friendship_id}/accept`, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
    });
    return response.json();
}

const decline_friend_request = async friendship_id => {
    const response = await fetch(`/api/user/friendship/${friendship_id}/decline`, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
    });
    return response.json();
}

$('.add-friend-btn').on('click', function(){
    const username = $(this).data('username');
    console.log(username);
    send_friend_request(username);
})

$('.accept-friend-btn').on('click', async function(){
    let friendship_id = $(this).data("friendship-id")
    let results = await accept_friend_request(friendship_id);
})

$('.decline-friend-btn').on('click', function(){
    const username = $(this).data('username');
    console.log(username, 'declined');
    //send_friend_request(username);
})