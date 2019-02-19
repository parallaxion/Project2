var values = [
    [for (words in keywords; console.log(words)];
    [1400000, 20000, 90000, 2000, 14102000]]

var data = [{
type: 'table',
header: {
  values: [["Countries"], ["Key Word 1"],
               ["Key Word 2"], ["Key Word 3"], ["Key Word 4"]["Key Word 5"]["Key Word 6"]["Key Word 7"][
                 "Key Word 8"]["Key Word 9"]["Key Word 10"]],
  align: "center",
  line: {width: 1, color: 'black'},
  fill: {color: "grey"},
  font: {family: "Arial", size: 12, color: "white"}
},
cells: {
  values: values,
  align: "center",
  line: {color: "black", width: 1},
  font: {family: "Arial", size: 11, color: ["black"]}
}
}]

Plotly.plot('graph', data);

Styled Table
var values = [
    [1200000, 20000, 80000, 2000, 12120000],
    [1300000, 20000, 70000, 2000, 130902000],
    [1300000, 20000, 120000, 2000, 131222000],
    [1400000, 20000, 90000, 2000, 14102000]]

var data = [{
type: 'table',
header: {
  values: [["Countries"], ["Key Word 1"],
  ["Key Word 2"], ["Key Word 3"], ["Key Word 4"]["Key Word 5"]["Key Word 6"]["Key Word 7"][
    "Key Word 8"]["Key Word 9"]["Key Word 10"]],
  align: ["left", "center"],
  line: {width: 1, color: '#506784'},
  fill: {color: '#119DFF'},
  font: {family: "Arial", size: 12, color: "white"}
},
cells: {
  values: values,
  align: ["left", "center"],
  line: {color: "#506784", width: 1},
   fill: {color: ['#25FEFD', 'white']},
  font: {family: "Arial", size: 11, color: ["#506784"]}
}
}]

Plotly.plot('graph', data);