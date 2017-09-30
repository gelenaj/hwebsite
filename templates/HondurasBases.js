<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=YOUR_KEY&sensor=true"></script>

//Function

//Function to initialize the google map api
function initialize() {
   var reqlat = '14.656934'; //Lattitude
   var reqlong = '-86.556886'; //Longittude
   var mapOptions = {
   center: new google.maps.LatLng(reqlat,reqlong),
   zoom: 7,
   mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map = new google.maps.Map(document.getElementById("map_canvas"),mapOptions);
  //Add marker
  var marker1 = new google.maps.Marker({
     position: new google.maps.LatLng(15.5149,-87.9923),
     map: map
  });
}