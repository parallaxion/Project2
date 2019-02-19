//h chart code for individual countries using Plotly
//svg starter code below

//issues/questions: 
//chart page/location
//defining country variable to country clicked on map or separate country page?

//country variable defined for testing purposes
// var country = "Argentina"

var pathArray = window.location.pathname.split('/');
var secondLevelLocation = pathArray[2]

function makeChart(country) {
  var countryurl = `/charts/${country}`;
  // var countryurl = `http://127.0.0.1:9014/{country}/Argentina`
  // var req = new XMLHttpRequest();
  // req.open('GET', countryurl, true);
  var chartData = d3.json(countryurl).then((data) => {
    // var chartData = load(countryurl).then((data) => {
    var name = data.country;
    var x = data.quantity;
    var y = data.keywords;

    var trace1 = {
      x: x,
      y: y, 
      // function(d, i) {
      //       return i * 60;
      //     },
      // text: "",
      type: "bar",
      orientation: "h"
    };
      var layout1 = {
        height: 500,
        width: 800,
        // function(d) {
        //       return d * 10;
        //     },
        xaxis: {
          title: `Top 5 Keywords for ${name}`,
          automargin: true
        }
      };
      var data1 = [trace1];
      // Render the plot to the div tag with id "chart"
      Plotly.newPlot("chart", data1, layout1);
  });
  console.log("hi5")
};      

// function handleSubmit() {
//   // Prevent the page from refreshing
//   d3.event.preventDefault();

  // Build the plot with the new stock
makeChart(secondLevelLocation);
// }

// // Add event listener for submit button
// d3.select("#submit").on("click", handleSubmit);

//starter code for svg alternative?
// var svgHeight = 600;
// var svgWeight = 400;

// // Append an SVG wrapper to the page and set a variable equal to a reference to it
// var svg = d3.select("#chart)
//   .append("svg")
//     .attr("height", svgHeight)
//     .attr("width", svgWeight);

// d3.select(".chart").selectAll("div")
// // svg.select(".chart").selectAll("div")
//   .data(chartData)
//   .enter() // creates placeholder for new data
//   .append("div") // appends a div to placeholder
//   .classed("bar", true) // sets the class of the new div
//   .attr("width", function(d) {
//     return d * 10;
//   })
//   .attr("height", 50)
//   .attr("x", 0)
//   .attr("y", function(d, i) {
//     return i * 60;
//   });