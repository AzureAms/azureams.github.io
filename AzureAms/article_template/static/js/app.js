$(document).ready(function(){
	$("#mobile-menu-button").click(() => {
		$("#mobile-menu").slideToggle()
		$("#mobile-menu").css("display","flex")
	})
	$("#read-more-button").click(() => {
		window.location.href = "./html/news.html"
	})
	$("#changeButton").load("../html/DarkLightButton.html"); 
})
