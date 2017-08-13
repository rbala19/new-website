$(document).ready(function() {
	$('.event-row').click(function() {
		 window.location.href = $(this).data('url');
	});
});
