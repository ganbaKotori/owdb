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

$('.add-friend-btn').on('click', function(){
    const username = $(this).data('username');
    console.log(username);
    send_friend_request(username);
})