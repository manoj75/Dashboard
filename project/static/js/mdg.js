$(document).ready(function(){
   $('.button-left').click(function(){
       $('.main').toggleClass('fliph');
   }); 
    $('a.collapsed').click( function(e) {
        $('.collapse').collapse('hide');
    });
    $('.sidebar li > a').click(function(e) {
        e.preventDefault();
        $('a').removeClass('active');
        $(this).addClass('active');
	$('.collapse').collapse('hide');
    });
});