$().ready(function() {

  	var mainHeight = $("main").height();
  	$("#sidebar").height(mainHeight);

  	$('select').material_select();

	$(".button-collapse").sideNav();

});