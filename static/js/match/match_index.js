$('.delete-match-btn').on('click', async function() {
	console.log('deleting match!');
	let match_id = $(this).data('match-id');
	let delete_match_response = await delete_match(match_id);
	if (delete_match_response.status == 200) {
		$(`#match-${match_id}-tr`).slideUp();
	}
	console.log(delete_match_response.status);
});

const delete_match = async (match_id) => {
	const response = await fetch(`/api/match/${match_id}`, {
		method: 'DELETE'
	});
	return response;
};
