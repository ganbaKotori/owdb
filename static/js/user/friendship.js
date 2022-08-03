const get_current_user_friends = async () => {
    const response = await fetch(`/api/user/friendship`, {
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
    });
    return response.json();
}