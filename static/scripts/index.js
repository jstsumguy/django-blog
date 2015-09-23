$(document).ready(function() {

	var edit_post_id = null;

	$('span.edit').on('click', function() {
		edit_post_id = $(this).attr('id');
		parent = $(this).parent().parent().parent();
		post_content = parent.find('div.post-content article');
		post_title = parent.find('div.post-heading h2.post-title');

		$('#edit-title').text(post_title.html());
		$('#edit-content').text(post_content.html());
		$('#edit-modal').modal('toggle');
	})

	$('#edit-submit').on('click', function() {
		message = {};
		message['content'] = $('#edit-content').val();
		message['id'] = edit_post_id; 
		console.log(JSON.stringify(message));

		$.ajax({
			type: 'post',
			url: '/edit_post/',
			data: JSON.stringify(message),
			success: function(response) {
				console.log(response);
				if(response.indexOf('success') > -1) 
					location.reload();
			}
		})
	})


})