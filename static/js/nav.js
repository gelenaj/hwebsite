function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "navbar-custom") {
        x.className += " responsive";
    } else {
        x.className = "navbar-custom";
    }
}