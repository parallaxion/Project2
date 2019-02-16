//alert("JS LOADS!")

var myMap = L.map("map", {
  center: [0, 0],
  zoom: 2
});
  
  // Add a tile layer
  L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 5,
    id: "mapbox.streets",
    accessToken: API_KEY
  }).addTo(myMap);
  
  // An array containing each city's name, location, and population
var results = [{"Country": "Argentina", "Top": ["Trump", "Resigns", "Woman", "Worry", "Markel"]},  {"Country": "Canada", "Top": ["Hockey", "Kim", "Scared", "Snow", "Oil"]}]
coords = {"Argentina": [-38.4161, -63.6167], "Canada": [56.1304, -106.3468]}

d3.json("/world").then(function(data){  //http://localhost:5000/world //, { mode: 'cors'}
  console.log("funk")
  console.log(data)
})

console.log(coords)
var locationLabels = []
for (x in results) {
    console.log(results[x]['Country'])
    console.log(results[x]['Top'][0])
    //console.log(coords[results[x]['Country']])
    my = { "location": coords[results[x]['Country']], "name": results[x]['Country'], "label": results[x]['Top'][0]  } 
    locationLabels.push(my)
};
for (var i = 0; i < locationLabels.length; i++) {
    var here = locationLabels[i];
    console.log(here.location)
    L.marker(here.location)
      .bindPopup("<h1>" + here.name + "</h1> <hr> <h3>Population " + here.label + "</h3>")
      .addTo(myMap);
}
d3.json('/geojson').then(function(data) {
  // Creating a GeoJSON layer with the retrieved data
  console.log(data)
  L.geoJson(data).addTo(myMap);
});
console.log("hi2")