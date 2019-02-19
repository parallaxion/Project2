import datetime as dt
import pandas as pd
import pymongo
import requests

from config import API_KEY
#from countries import countries, country_codes

from flask import Flask, jsonify, render_template
app = Flask(__name__)


@app.route("/")
def index():

 
   # return render_template('index.html')
   return render_template('bargraph.html')



@app.route("/line")
def test():   #connect to mongodb
    conn = 'mongodb://localhost:27017/top_headlines'
    print(conn)
    client = pymongo.MongoClient(conn)
    print(client)
    # Declare the database
    db = client["top_headlines"]
    # Declare the collection
    collection = db["countries_data"]

    #get data
    data = collection.find()

    return data


if __name__ == "__main__":
    app.run(debug=True)