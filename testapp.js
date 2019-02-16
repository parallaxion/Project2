
function run(){
    topic = document.getElementById("query").value
    console.log(topic)
url = `https://newsapi.org/v2/everything?q=${topic}&from=2019-02-01&sortBy=publishedAt&apiKey=${NEWS_KEY}`

sources= "https://newsapi.org/v2/sources?apiKey=358ac513e47b40fcbc47492633beb76c"
d3.json(sources).then(function(dat){
    console.log(dat)
});
d3.json(url).then(function(data) {
    console.log('grabbing topics')
    console.log(data);
    document.getElementById('content').innerHTML = JSON.stringify(data)
  });


//trump
//technology
//change
//console.log(API_KEY)

console.log("never gets here")
// Creating map object
var map = L.map("map", {
    center: [40.7128, -74.0059],
    zoom: 11
  });
  console.log("map")
  // Adding tile layer
  L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
  }).addTo(map);
  
  var link = "http://data.beta.nyc//dataset/0ff93d2d-90ba-457c-9f7e-39e47bf2ac5f/resource/" +
  "35dd04fb-81b3-479b-a074-a27a37888ce7/download/d085e2f8d0b54d4590b1e7d1f35594c1pediacitiesnycneighborhoods.geojson";
  
  // Grabbing our GeoJSON data..
  //d3.json(link).then(function(data) {
 d3.json('countries.geo.json').then(function(data) {
    // Creating a GeoJSON layer with the retrieved data
    console.log(data)
    L.geoJson(data).addTo(map);
  });
  console.log("hi2")
};

//https://stackoverflow.com/questions/13316925/simple-label-on-a-leaflet-geojson-polygon
// L.geoJson(geoJsonData, {
//   onEachFeature: function(feature, layer) {
//     var label = L.marker(layer.getBounds().getCenter(), {
//       icon: L.divIcon({
//         className: 'label',
//         html: feature.properties.NAME,
//         iconSize: [100, 40]
//       })
//     }).addTo(map);
//   }
// );

run()