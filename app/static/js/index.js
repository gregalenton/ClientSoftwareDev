// tooltip function 
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

// button function 
$('.reply').click(function(){
	$(this).hide();
	$('.email-content').css()
});

$('.cancel').click(function(){
	$('.reply').show(500);
});