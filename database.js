var map;
var geocoder;
var marker1;

var config = {
  apiKey: "AIzaSyANUg5_izXIuY6hhdrUPWy9v4m_7SoJ5SY",
  authDomain: "hackrpi2019-41699.firebaseapp.com",
  databaseURL: "https://hackrpi2019-41699.firebaseio.com",
  projectId: "hackrpi2019-41699",
  storageBucket: "hackrpi2019-41699.appspot.com",
  messagingSenderId: "273813608241"
};
firebase.initializeApp(config);
var database = firebase.database();
var peopleRef = database.ref().child('MapPoints');

function initMap() {
  geocoder = new google.maps.Geocoder();
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 39.828, lng: -98.579},
    zoom: 3.75,
    minZoom: 2.5,
    disableDoubleClickZoom: true
  });


  google.maps.event.addListener(map, 'click', function(event) {
   placeMarker(event.latLng);
   var yesno;
   setTimeout(function() {
     yesno = confirm("Do you want to start a #trashtag here?");
   }, 300);
   if (yesno) {
     var contentString = '<div id="content">'+
            '<div id="siteNotice">'+
            '</div>'+
            '<h1 id="firstHeading" class="firstHeading">Uluru</h1>'+
            '<div id="bodyContent">'+
            '<p><b>Uluru</b>, also referred to as <b>Ayers Rock</b>, is a large ' +
            'sandstone rock formation in the southern part of the '+
            'Northern Territory, central Australia. It lies 335&#160;km (208&#160;mi) '+
            'south west of the nearest large town, Alice Springs; 450&#160;km '+
            '(280&#160;mi) by road. Kata Tjuta and Uluru are the two major '+
            'features of the Uluru - Kata Tjuta National Park. Uluru is '+
            'sacred to the Pitjantjatjara and Yankunytjatjara, the '+
            'Aboriginal people of the area. It has many springs, waterholes, '+
            'rock caves and ancient paintings. Uluru is listed as a World '+
            'Heritage Site.</p>'+
            '<p>Attribution: Uluru, <a href="https://en.wikipedia.org/w/index.php?title=Uluru&oldid=297882194">'+
            'https://en.wikipedia.org/w/index.php?title=Uluru</a> '+
            '(last visited June 22, 2009).</p>'+
            '</div>'+
            '</div>';

        var infowindow = new google.maps.InfoWindow({
          content: contentString
        });

        infowindow.open(map, popup);

   }
  });
}

function placeMarker(location) {
  if (marker1) {
    marker1.setPosition(location);
  } else {
    marker1 = new google.maps.Marker({
      position: location,
      map: map,
      icon: {
        url: "blue-dot.png"
      }
    });
  }
}

function codeAddress(i_title, address) {
    geocoder.geocode( { 'address': address}, function(results, status) {
      console.log(status);
      if (status == 'OK') {
        var marker = new google.maps.Marker({
            map: map,
            position: results[0].geometry.location,
            title: i_title
        });
      }
    });
  }

function addMarkers() {
  peopleRef.once('value')
  .then(function(snapshot) {
    snapshot.forEach(function(childSnapshot) {
      var results = [];
      var numElements = 0;
      childSnapshot.forEach(function(anotherSnapshot) {
        var key = anotherSnapshot.key;
        var childData = anotherSnapshot.val();
        results.push(childData);
        numElements++;
      })
        var marker = new google.maps.Marker({
          position: {lat: results[1], lng: results[2]},
          title: results[0]
        });
        marker.setMap(map);

    })
  })
}

addMarkers();
