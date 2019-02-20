// get country variable from url
var pathArray = window.location.pathname.split('/');
var country = pathArray[2]

// get keywords data for country
d3.json("/keywords/"+country).then(result => {
  var all_keywords = result.all_keywords;
  var all_values = result.all_values;
  
  // push keywords and values lists to values
  var values = []
  values.push(all_keywords)
  values.push(all_values)

  // set data for table
  var data = [{
  type: 'table',
  // header
  header: {
    values: [["Keyword"], ["Word Degree"]],
    align: "center",
    line: {width: 1, color: 'black'},
    fill: {color: "grey"},
    font: {family: "Arial", size: 20, color: "white"}
  },
  // cells
  cells: {
    values: values,
    align: "center",
    line: {color: "black", width: 1},
    font: {family: "Arial", size: 12, color: ["black"]}
  }
  }]

  // plot table
  Plotly.plot('table', data);

})