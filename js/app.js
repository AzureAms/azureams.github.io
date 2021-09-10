$(document).ready(function(){
	$("#mobile-menu-button").click(() => {
		$("#mobile-menu").slideToggle()
		$("#mobile-menu").css("display","flex")
	})
})
$(window).on("scroll", function() {
	if($(window).scrollTop() < 800) {
		$(".navbar").addClass("nav-active");
	} else {
		//remove the background property so it comes transparent again (defined in your css)
		$(".navbar").removeClass("nav-active");
	}
});
