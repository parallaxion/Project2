import datetime as dt
import pandas as pd
import pymongo
import requests
import json

from config import API_KEY
#from countries import countries, country_codes
conn = 'mongodb://localhost:27017/top_headlines'
print(conn)
client = pymongo.MongoClient(conn)
print(client)
# Declare the database
db = client["top_headlines"]
# Declare the collection
collection = db["countries_data"]

articleList = {}
#get data
data = collection.find()
#print(data[0])

countryWords = {}
clouds = {}
for country in data:
    print(country['country'])
    print(len(country['articles']))
    f = open(country['country']+".txt", "w")

    countryWords[country['country']] = ''
    for article in country['articles']:
    
      countryWords[country['country']] = countryWords[country['country']] + article['title'] + ' '
    thisWords = countryWords[country['country']]
    f.write(json.dumps(countryWords[country['country']]))
    thisList = {}
    for x in thisWords.split():
      print(x)
      #clouds[(country['country']] 
      if x in thisList:
        thisList[x] = thisList[x] + 1

      else: 
        thisList[x] = 1
      #print(thisList)
      clouds[country['country']] = thisList

    #end of loop

     # print(article)
  #  print(article)
  #articleList.append(article)

#print(len(articleList))

#print(countryWords)
f = open("clouds.txt", "w")
f.write(json.dumps(clouds))
#print(clouds)