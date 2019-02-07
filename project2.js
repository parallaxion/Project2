url = "https://newsapi.org/v2/top-headlines?sources=reuters&apiKey=67f5bff9abe2411fbf1dd4f61e9c670c"

d3.json(url, function(response) {

  console.log(response);
});