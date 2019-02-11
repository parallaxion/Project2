import datetime as dt
import pandas as pd
import pymongo
import requests

from config import API_KEY
from countries import countries, country_codes

#connect to mongodb
conn = 'mongodb://localhost:27017/top_headlines'
client = pymongo.MongoClient(conn)
# Declare the database
db = client["top_headlines"]
# Declare the collection
collection = db["countries_data"]

#get data
data = collection.find()

#set empty list for dates
dates = []
#find latest date
for article in data[0]["articles"]:
    dates.append(article["date"])
latestDate = max(dates)
print(f"Latest Date in Database: {latestDate}")

#find today's date
today = dt.datetime.strftime(dt.date.today(), "%Y-%m-%d")

#get id for raw data db
allRaw = db["raw_countries_data"]
rawID = allRaw[0]["_id"]

#if latest date is before today,
if latestDate < today:
    for i in range(len(country_codes)):
        
        #visit news api
        query_url = f"https://newsapi.org/v2/top-headlines?country={country_codes[i]}&apiKey={API_KEY}"
        #get response
        response = requests.get(query_url).json()
        
        #add raw articles data to raw countries data db
        rawCollection = db["raw_countries_data"]
        rawCollection.update_one({"_id": rawID}, {"$push": {countries[i]: response["articles"]}})

        #for each article
        for article in response["articles"]:
            #construct article dictionary
            articleDict = {"source": article["source"]["name"], 
                           "title": article["title"].split(" - ")[0], 
                           "url": article["url"], 
                           "date": article["publishedAt"][:10]}
            #add article dict to countries data db
            collection.update_one({"country": countries[i]}, {"$push": {"articles": articleDict}})
    print("Database updated.")
else:
    print("Database is up to date.")