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
    columnwidth: [250,250],
    columnorder: [1,2],
    header: {
      values: [["Keyword"], ["Word Degree"]],
      align: "center",
      line: {width: 2, color: 'black'},
      fill: {color: ['rgb(31, 119, 180)']},
      font: {family: "Arial", size: 28, color: "white"},
      height: 40
  },
  // cells
  cells: {
    values: values,
    align: "center",
    line: {color: "black", width: 2},
    fill: {color: ['rgb(31, 119, 180)']},
    font: {family: "Arial", size: 22, color: ["white"]},
    height: 30
  }
  }]

  var layout = {
    height: 400,
    margin: {
      l: 175,
      r: 75,
      t: 25,
      b: 5
    },
    plot_bgcolor: 'rgba(202, 202, 202, 0.2)',
    paper_bgcolor: 'rgba(202, 202, 202, 0.2)'

  };
  // plot table
  Plotly.plot('table', data, layout);

})