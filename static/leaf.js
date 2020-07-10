var mymap = L.map('mapid').setView([12.9791198,77.5912997], 13);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
maxZoom: 18,
id: 'mapbox/streets-v11',
tileSize: 512,
zoomOffset: -1,
accessToken: 'pk.eyJ1Ijoic2hhbmtoYTExNyIsImEiOiJja2NmdW5uZWkwbHdzMnhwY2VpeGQybXBsIn0.yRa9ivhduFYLLZOO1RXO-Q'
}).addTo(mymap);

//mapMarkers1 = [];
//mapMarkers2 = [];
//mapMarkers3 = [];
//
//var source = new EventSource('/topic/testBusdatac'); //ENTER YOUR TOPICNAME HERE
//source.addEventListener('message', function(e){
//
//  console.log('Message');
//  obj = JSON.parse(e.data);
//  console.log(obj);
//
//  if(obj.busline == '00001') {
//    for (var i = 0; i < mapMarkers1.length; i++) {
//      mymap.removeLayer(mapMarkers1[i]);
//    }
//    marker1 = L.marker([obj.latitude, obj.longitude]).addTo(mymap);
//    mapMarkers1.push(marker1);
//  }
//
//  if(obj.busline == '00002') {
//    for (var i = 0; i < mapMarkers2.length; i++) {
//      mymap.removeLayer(mapMarkers2[i]);
//    }
//    marker2 = L.marker([obj.latitude, obj.longitude]).addTo(mymap);
//    mapMarkers2.push(marker2);
//  }
//
//  if(obj.busline == '00003') {
//    for (var i = 0; i < mapMarkers3.length; i++) {
//      mymap.removeLayer(mapMarkers3[i]);
//    }
//    marker3 = L.marker([obj.latitude, obj.longitude]).addTo(mymap);
//    mapMarkers3.push(marker3);
//  }
//}, false);
