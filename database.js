var map;
var geocoder;
var marker;

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
    zoom: 3.75
  });
  google.maps.event.addListener(map, 'click', function(event) {
   placeMarker(event.latLng);
 });
}

function placeMarker(location) {
  if (marker) {
    marker.setPosition(location);
  } else {
    marker = new google.maps.Marker({
      position: location,
      map: map,
      animation: google.maps.Animation.DROP,
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
            title: i_title,
            icon: {
              url: "blue-dot.png"
            }
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
      if (numElements == 2) {
        codeAddress(results[0], results[1]);
      } else if (numElements == 3) {
        var marker = new google.maps.Marker({
          position: {lat: results[1], lng: results[2]},
          title: results[0],
          icon: {
            url: "blue-dot.png"
          }
        });
        marker.setMap(map);
      }
    })
  })
}

addMarkers();
