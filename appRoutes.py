import datetime as dt
import pandas as pd
import pymongo
import requests
import json
from bson.json_util import dumps
#import update from updateDB
from config import API_KEY
from countries import countries, country_codes

from flask import Flask, jsonify, render_template
app = Flask(__name__)

conn = 'mongodb://localhost:27017/top_headlines'
# print(conn)
client = pymongo.MongoClient(conn)
# print(client)
# Declare the database
db = client["top_headlines"]

@app.route("/")
def index():
    #update()
    return render_template('index.html')

@app.route("/blob")
def blob():
    collection = db["countries_wordblob"]
    data = collection.find()
#     #get data
#     #countries =  db.collection.find().distinct("country")
#     routeReturn = {}
#     for country in collection.find().distinct('country'):
#      #   print(country)
#         myWords = collection.find_one({"country": country})
#         routeReturn[country] = myWords['keywords']
#     #    print(myWords['keywords'])
#     print(routeReturn)
    
#    ## data = collection.find({"country": "Ireland"})
#     #print(DeprecationWarning)
#    # for x in data:
#         #print(x)
    duece = dumps(data)
    doubleduece = json.loads(duece)
    return json.dumps(doubleduece)


@app.route("/geojson")
def geo():
    #filename = "hello.txt"
    with open('countries.geo.json') as f:
        data = json.load(f)

        formatted_countries= []
        for country in countries:
            if country == "Serbia":
                country = "Republic of Serbia"
                formatted_countries.append(country)
            else:
                formatted_countries.append(country)
        
        goodData = []
        for entry in data["features"]:
            if entry["properties"]["name"] in formatted_countries:
                goodData.append(entry)
                print(entry["properties"]["name"])
            else:
                pass


    return json.dumps(goodData)

@app.route("/keywords/")
def keywords():
    #connect to mongo
    {{"Country": "Argentina", "Top": ["Trump", "Resigns", "Woman", "Worry", "Markel"]}, {{"Country": "Canada", "Top": ["Hockey", "Kim", "Scared", "Snow", "Oil"]}}}

### FILTER BY KEYWORD!!

@app.route("/world")
def test():   #connect to mongodb
    # conn = 'mongodb://localhost:27017/top_headlines'
    # print(conn)
    # client = pymongo.MongoClient(conn)
    # print(client)
    # # Declare the database
    # db = client["top_headlines"]
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
    # print(routeReturn)
    
   ## data = collection.find({"country": "Ireland"})
    #print(DeprecationWarning)
   # for x in data:
        #print(x)

    return json.dumps(routeReturn)


if __name__ == "__main__":
    app.run(debug=True)