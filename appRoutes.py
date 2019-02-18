import datetime as dt
import pandas as pd
import pymongo
import requests
import json
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from bson.json_util import dumps
from jinja2 import TemplateNotFound
plotly.tools.set_credentials_file(username='ordna', api_key='sk586EuSjwMs2XuhKAV5')

#import update from updateDB
from config import API_KEY
#from countries import countries, country_codes

from flask import Flask, jsonify, render_template
app = Flask(__name__)

# app.config['MONGO_DBNAME'] = 'top_headlines'
# app.config['MONGO_URI'] = 'mongodb://mongodb0.top_headlines.com:27017/admin'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/top_headlines'
# mongo = pymongo(app)

@app.route("/")
def index():
    #update()
    return render_template('indexb.html')

@app.route("/geojson")
def geo():
    #filename = "hello.txt"
    with open('countries.geo.json') as f:
        data = json.load(f)
    return json.dumps(data)

@app.route("/keywords/")
def keywords():
    #connect to mongo
    {{"Country": "Argentina", "Top": ["Trump", "Resigns", "Woman", "Worry", "Markel"]}, {{"Country": "Canada", "Top": ["Hockey", "Kim", "Scared", "Snow", "Oil"]}}}

@app.route("/world")
def test():   #connect to mongodb
    conn = 'mongodb://localhost:27017/top_headlines'
    print(conn)
    client = pymongo.MongoClient(conn)
    print(client)
    # Declare the database
    db = client["top_headlines"]
    # Declare the collection
    collection = db["countries_keywords"]

    data = collection.find()

    #get data
    #countries =  db.collection.find().distinct("country")
    routeReturn = {}
    for country in collection.find().distinct('country'):
     #   print(country)
        myWords = collection.find_one({"country": country})
        routeReturn[country] = myWords['keywords']
    #    print(myWords['keywords'])
    print(routeReturn)
    
   ## data = collection.find({"country": "Ireland"})
    #print(DeprecationWarning)
   # for x in data:
        #print(x)

    return json.dumps(routeReturn)


@app.route("/country/<country>")
def chartData(country):   #connect to mongodb
    conn = 'mongodb://localhost:27017/top_headlines'
    print(conn)
    client = pymongo.MongoClient(conn)
    print(client)
    # Declare the database
    db = client["top_headlines"]
    # Declare the collection
    collection = db["countries_keywords"]
    # country = request.args.get('country')
    data = dumps(collection.find({"country": country}))
    data = json.loads(data)
    keywords = data[0]["keywords"]
    chart_df = pd.DataFrame.from_dict(keywords, orient="index")
    chart_df = chart_df.reset_index()
    chart_df = chart_df.head(5)
    top5keywords = chart_df["index"]
    top5scores = chart_df[0]
    return jsonify({"country": country, "keywords": list(top5keywords), "quantity": list(top5scores)})

@app.route("/charts/<country>")
def makeChart(country):
    # python plotly code attempt to run via flask
    # countryurl = "/country/${country}"
    # chartData =  d3.json(countryurl).
    # countryurl = "http://127.0.0.1:9014/country/{country}"
    # # countryurl = "/country/${country}"
    # # chart_data = chart_df.to_dict(orient='records')
    # # chart_data = json.dumps(chart_data, indent=2)
    # data2 = {'chart_data': chart_data}
    # name = {"data": "{country}"}
    # x = {"data": "{quantity}"}
    # y = {"data": "{keywords}"}
    # print(keywords)
    # trace1 = go.Bar(
    #   x = [x],
    #   y = [y], 
    # #   'type': 'bar'
    # #   orientation = "h"
    # )

    # trace1 = {
    #   'x': {x},
    #   'y': {y}, 
    # #   'type': "bar",
    # #   'orientation': "h"
    # }

    # layout1 = go.Layout(
    #   height = 500,
    #   width = 800,
    # )
    # data1 = [trace1]
    # fig = go.Figure(data=data1, layout=layout1)
    # py.iplot(fig, filename="chart")
    # # console.warn(xhr.responseText)
    return render_template("indexb.html")

if __name__ == "__main__":
    app.run(port=9000, debug=True)