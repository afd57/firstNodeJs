$(document).ready(function() {

	$('#button_call').click(function(){	
		$.ajax({ 
			type: 'GET', 
			url: '/theURL', 
			data: { get_param: 'value' }, 
			dataType: 'json',
			success: function (data) {
				for(item in data){					
					$('#userTable').append('<tr class="success"><td>'+data[item]['name']+'</td>'+
															   '<td>'+data[item]['age']+'</td>'+ 
														   	   '<td>'+data[item]['city']+'</td>'+'</tr>')
				}
			}
		});
	});
	
});