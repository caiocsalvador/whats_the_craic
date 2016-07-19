function vizualized_message(form){
	$.ajax({
	  	type: "POST",
	  	url: 'view/',
	  	data: form.serialize(),
	  	success : function(json) {
            console.log("success"); // another sanity check
    	},
	});
}

$().ready(function() {

  	var mainHeight = $("main").height();
  	$("#sidebar").height(mainHeight);

  	$('select').material_select();

	$(".button-collapse").sideNav();

	$(".input-edit-picture span").on("click", function(){
		$("#id_picture").click();
	});

	$("#id_picture").on("change", function(){
		var filename = $('#id_picture').val().split('\\').pop();
		console.log(filename);
		$(".profile-photo").css("background-image","");
		$(".profile-photo").append("<h5>New Image</h5><p>"+filename+"</p>");
	});

	$(".messages .resume").on("click", function(){
		var resume = $(this);
		var index = $(this).index();
		index = index+2;
		if($(".messages table tr").eq(index).hasClass("active")){
			$(".messages table tr").eq(index).removeClass("active");
		}
		else{
			$(".messages table tr").eq(index).addClass("active");
			if($(".messages").hasClass("inbox")){
				vizualized_message($(".messages table tr").eq(index).children("td").children("form"));
				resume.removeClass("not-visualized");
			}			
		}
		
	});

});