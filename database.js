var map;
var geocoder;
var marker1;
var personLoc;
var WORLD_BOUNDS = {
  north: 85,
  south: -85,
  west: -180,
  east: 180,
};

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
  var bounds = new google.maps.LatLngBounds();
  geocoder = new google.maps.Geocoder();
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 39.828, lng: -98.579},
    zoom: 3.75,
    disableDoubleClickZoom: true,
    restriction: {
            latLngBounds: WORLD_BOUNDS,
            strictBounds: true,
    },
  });


  addMarkers();

  google.maps.event.addListener(map, 'click', function(event) {
   placeMarker(event.latLng);
   setTimeout(function() {
     var yesno = confirmPlacement();
     if (yesno) {
       $( "div.popup" ).show();
       $( "#map" ).hide();
       personLoc = event.latLng;
     }
   }, 200);
  });
}

function confirmPlacement() {
  return confirm("Do you want to start a #TrashTag here?");
}

function placeMarker(location) {
  if (marker1) {
    marker1.setPosition(location);
  } else {
    marker1 = new google.maps.Marker({
      position: location,
      icon: {
        url: "blue-dot.png"
      }
    });
    marker1.setMap(map);
  }
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

function writeUserData(lat, long, number, twitter) {
  firebase.database().ref('Clients/'+twitter+'/Coordinates').set({
    Lat: lat,
    Long: long
  });

  firebase.database().ref('Clients/'+twitter).update({
    Number: number
  });
}

function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  $( "div.popup" ).hide();
  $( "#map" ).show();
  document.getElementById("myForm").style.display = "none";
}

function submitForm() {
  writeUserData(personLoc.lat(), personLoc.lng(), $("#number").val(), $("#twitter").val());
  $( "div.popup" ).hide();
  $( "#map" ).show();
  $("#number").val('');
  $("#twitter").val('');
}
