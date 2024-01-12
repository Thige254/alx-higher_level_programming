$(document).ready(function () {
	$('#btn_translate').click(function () {
	  const languageCode = $('#language_code').val();
	  
	  /*Make a GET request to the API */
	  $.ajax({
		url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
		type: 'GET',
		success: function (response) {
		  /* Display the translation in the DIV#hello */
		  $('#hello').text(response.hello);
		},
		error: function () {
		  /* Display an error message if the request fails */
		  $('#hello').text('Error: Translation not available');
		}
	  });
	});
  });
