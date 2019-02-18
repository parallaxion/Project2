// Add a tile layer
var liteTiles = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 10,
  id: "mapbox.light",
  accessToken: API_KEY
});

var layers = {
  COUNTRY_NAMES: new L.LayerGroup(),
  COUNTRY_KEYWORDS: new L.LayerGroup()
}

var myMap = L.map("map", {
  center: [0, 0],
  zoom: 2,
  layers: [
    layers.COUNTRY_KEYWORDS,
    // layers.COUNTRY_NAMES
  ]
});
  
liteTiles.addTo(myMap)

d3.json('/geojson').then(function(data) {
  // Creating a GeoJSON layer with the retrieved data
  // console.log(data)
  L.geoJson(data).addTo(myMap);
});

var overlays = {
  "Keywords": layers.COUNTRY_KEYWORDS,
  "Names": layers.COUNTRY_NAMES
}
  
L.control.layers(overlays, null).addTo(myMap);



d3.json("/map_info").then(function(map_info) {
  countries_info = map_info.map_info
  // for each country,
  countries_info.forEach(info => {
    // set name, coords, and top keyword
    var country_name = info.country;
    var lat = info.coords.lat
    var lon = info.coords.lon
    var keyword = info.keyword

    // get top 5 keywords data from endpoint
    d3.json("/keywords/"+country_name).then(function(country_keywords) {
      top_five = country_keywords.top_five
      // set empty list of keyword list items
      var kw_list_items = []
      var keyword_html = ""
      // for each keyword, format and push to kw list items
      top_five.forEach(keyword => {
        kw_list_items.push("<li>"+keyword+"</li>")
      });
      // combine keyword list items into one html string
      kw_list_items.forEach(item => {
        keyword_html += item
      })
      console.log(keyword_html)

      // name and keyword icons
      name_icon = L.divIcon({className: "country_name_icon", html: "<h4>"+country_name+"</h4>"})
      kw_icon = L.divIcon({className: "country_keyword_icon", html: "<h4>"+keyword+"</h4>"})

      // name and keyword markers
      nameMarker = L.marker([lat, lon], {
        icon: name_icon
      })
      keywordMarker = L.marker([lat, lon], {
        icon: kw_icon
      })

      // add name and keyword markers to names and keywords layers
      nameMarker.addTo(layers["COUNTRY_NAMES"])
      keywordMarker.addTo(layers["COUNTRY_KEYWORDS"])

      nameMarker.bindPopup("<ul>"+keyword_html+"</ul></br><a href='/country/"+country_name+"'>Find out more...</a>");
      keywordMarker.bindPopup("<ul>"+keyword_html+"</ul></br><a href='/country/"+country_name+"'>Find out more...</a>");
      
    }); // end of country keywords
  }); // end for each country
}) // end map_info