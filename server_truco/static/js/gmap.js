var initialLocation;
var siberia = new google.maps.LatLng(60, 105);
var newyork = new google.maps.LatLng(40.69847032728747, -73.9514422416687);
var browserSupportFlag =  new Boolean();

function addMapMarkers(shopsArray,map){

    for (var i=0;i<shopsArray.length;i++){

        // set marker
        var marker = new google.maps.Marker({
            position: shopsArray[i].location,
            map: map,
            animation: google.maps.Animation.DROP,
            title: shopsArray[i].name
        });

        addListener(shopsArray[i],marker,map);
    }
}

function addListener(shop,marker,map){
    var contentString = '<div id="content">'+'<p>'+ shop.name +'</p>'
    '</div>';
    var infowindow = new google.maps.InfoWindow({
        content: contentString
    });

    google.maps.event.addListener(marker, 'click', function() {
        infowindow.open(map,marker);
    });
}

function initialize() {
    var myOptions = {
        zoom: 6,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true
    };
    var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

    // Try W3C Geolocation (Preferred)
    if(navigator.geolocation) {
        browserSupportFlag = true;
        navigator.geolocation.getCurrentPosition(function(position) {
            initialLocation = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
            map.setCenter(initialLocation);
            map.setZoom(12);

        }, function() {
            handleNoGeolocation(browserSupportFlag);
        });
    }
    // Browser doesn't support Geolocation
    else {
        browserSupportFlag = false;
        handleNoGeolocation(browserSupportFlag);
    }

    function handleNoGeolocation(errorFlag) {
        if (errorFlag == true) {
            alert("Geolocation service failed.");
            initialLocation = newyork;
        } else {
            alert("Your browser doesn't support geolocation. We've placed you in Siberia.");
            initialLocation = siberia;
        }
        map.setCenter(initialLocation);
    }

    // add Shops markers
    var testArray = new Array();

    // Test Pins
    var shop1=new Object();
    shop1.name = "tienda 1"
    shop1.location = new google.maps.LatLng(37.178646,-3.609381);

    var shop2=new Object();
    shop2.name = "tienda 2"
    shop2.location = new google.maps.LatLng(37.191775,-3.598909);

    var shop3=new Object();
    shop3.name = "tienda 3"
    shop3.location = new google.maps.LatLng(37.174817,-3.589811);

    testArray[0]= shop1;
    testArray[1]= shop2;
    testArray[2]= shop3;

    addMapMarkers(testArray,map);
}
