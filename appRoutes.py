import datetime as dt
import pandas as pd
import pymongo
import requests
import json
from bson.json_util import dumps
from jinja2 import TemplateNotFound

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
    return render_template('index.html')

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


@app.route("/charts/<country>")
def makeChart(country):   #connect to mongodb
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
    # return jsonify({"country": country, "keywords": list(top5keywords), "quantity": list(top5scores)})

if __name__ == "__main__":
    app.run(port=9007, debug=True)