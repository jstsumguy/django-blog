$(document).ready(function() {

	$('#create-comment-btn').on('click', function() {
		message = {};
		message.content = $('#new-comment-content').val();
		message.user_id = $('#user_id').val();
		message.post_id = $('#post_id').val();

		$.ajax({
			type: 'post',
			url: '../../create_comment/',
			data: JSON.stringify(message),
			success: function(response) {
				console.log(response);
				if(response.indexOf('success') > -1)
					location.reload();
			}
		})
	})
})