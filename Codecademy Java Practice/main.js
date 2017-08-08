function main() {
	//When loaded, have the rest of the skillsets hidden and slowly fade in
	//lower fadeIn's number to speed up the fade, or increase to slow down
  $('.skillset').hide();
  $('.skillset').fadeIn(1000);
  
	//Hide the projects by default
  $('.projects').hide();
  
	//On press, have the next items slide in with the 400ms delay
	//delay is changeable; lower to speed up, increase to slow down
  $('.projects-button').on('click', function() {
		$(this).next().slideToggle(400);
    //$(this).next().toggle();
    $(this).toggleClass('active');
    $(this).text('Projects Viewed');
	});
}

$(document).ready(main);