
function run(){
    topic = document.getElementById("query").value
    console.log(topic)
url = `https://newsapi.org/v2/everything?q=${topic}&from=2019-01-07&sortBy=publishedAt&apiKey=358ac513e47b40fcbc47492633beb76c`

d3.json(url).then(function(data) {
    console.log('hi')
    console.log(data);
    document.getElementById('content').innerHTML = JSON.stringify(data)
  });

};
//trump
//technology
//change
run()