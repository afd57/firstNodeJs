$(document).ready(function() {

	$('#button_call').click(function(){	
		$.ajax({
			type: "GET",
			url: "/theURL" // modify the url according to your application logic
		}).done(function(yourData) {
			$('#return_vale').html(yourData)
		});
		
	});
	
});