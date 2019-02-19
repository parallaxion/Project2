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
    
#route to return country's top 5 keywords for pop-up
@app.route("/keywords/<country>")
def country_keywords(country):
    #set collection
collection = db["countries_keywords"]
#find the document that matches the country
all_keywords = collection.find_one({"country": country})
#list all keywords
all_keywords_list = list(all_keywords["keywords"].keys())
#list all keyword values
all_values = []
for word in all_keywords_list:
    all_values.append(all_keywords["keywords"][word])
#take top five
top_five = [all_keywords_list[i] for i in range(5)]

keyword_dict = {}
#add top five to keyword dict
keyword_dict["top_five"] = top_five
#add all keywords and values to keyword dict
keyword_dict["all_keywords"] = all_keywords_list
keyword_dict["all_values"] = all_values
    return jsonify (keyword_dict)

console.log(all_keywords)

   ## data = collection.find({"country": "Ireland"})
    #print(DeprecationWarning)
   # for x in data:
        #print(x)

    return json.dumps(routeReturn)


if __name__ == "__main__":
    app.run(debug=True)