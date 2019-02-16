import datetime as dt
import pandas as pd
import pymongo
import requests
import json
#import update from updateDB
from config import API_KEY
#from countries import countries, country_codes

from flask import Flask, jsonify, render_template
app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)