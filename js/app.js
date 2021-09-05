$(document).ready(function(){
    $("#mobile-menu-button").click(() => {
        $("#mobile-menu").slideToggle()
        $("#mobile-menu").css("display","flex")
    })
})