function activate(item){
    $(item).addClass("active");
}

function contact(form){
    $.ajax({
        type: "POST",
        url: 'contact/',
        data: form.serialize(),
        success : function(json) {
            console.log("success"); // another sanity check
            alert("Thank You for your contact, we will keep in touch soon!");
        },
    });
}

$().ready(function() {

    $(".send").on("click", function(event){
        event.preventDefault();
        contact($(".form-contact"));
    });

  $('select').material_select();

    $(window).scroll(function() {
       if($(window).scrollTop() + $(window).height() == $(document).height()) {
            $("nav li").removeClass("active");
            $("nav .nav-contact").addClass("active");
       }
       if($(window).scrollTop() == 0) {
            $("nav li").removeClass("active");
            $("nav .nav-home").addClass("active");
       }
    });

    $("nav ul li a").on("click",function(){       
            var id = $(this).attr("href");
            $('html,body').animate({scrollTop:$(id).offset().top-110},1000);
            var li = $(this).parent("li");        
            setTimeout(function(){
                $("nav li").removeClass("active");
                li.addClass("active");
            }, 500);  
            return false;     
        });

    $('#home').waypoint(function(direction) {
        $("nav li").removeClass("active");
        $("nav .nav-home").addClass("active");
    },{
        offset:'110px'
    });

    $('#works').waypoint(function(direction) {
        $("nav li").removeClass("active");
        $("nav .nav-works").addClass("active");
    },{
        offset:'110px'
    });

    $('#testimonials').waypoint(function(direction) {
        $("nav li").removeClass("active");
        $("nav .nav-testimonials").addClass("active");
    },{
        offset:'110px'
    });

    $('#contact').waypoint(function(direction) {
        $("nav li").removeClass("active");
        $("nav .nav-contact").addClass("active");
    },{
        offset:'110px'
    });
    

    $('.parallax').parallax();
    $(".button-collapse").sideNav();
    $('.navbar').pushpin({ top: $('.navbar').offset().top });

    var options = [ 
    {selector: '.step', offset: 0, callback: 'activate(".step")' },
    ];
    Materialize.scrollFire(options); 

    $(".testimonials").owlCarousel({
     
          navigation : true, // Show next and prev buttons
          slideSpeed : 300,
          paginationSpeed : 400,
          singleItem:true,
          navigationText: ["<",">"],
          autoPlay: 10000,
          navigation: false,
     
          // "singleItem:true" is a shortcut for:
          // items : 1, 
          // itemsDesktop : false,
          // itemsDesktopSmall : false,
          // itemsTablet: false,
          // itemsMobile : false
     
    });
});