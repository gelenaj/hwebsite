$(document).ready(function() {    
$("#allDescriptions").click(function () {
        $('.accordion-group p, a.buttons').toggle('slow');
    }); 

$("#jump1990").click(function(){
    $('html, body').animate({
        scrollTop: $("#collapse4").offset().top
}, 2000);
});

$("#jump1950").click(function(){
    $('html, body').animate({
        scrollTop: $("#collapse5").offset().top
}, 2000);
});

$("#jump2000").click(function(){
    $('html, body').animate({
        scrollTop: $("#collapse6").offset().top
}, 2000);
});

});

