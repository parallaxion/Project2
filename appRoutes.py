#master
import datetime as dt
import pandas as pd
import pymongo
import requests
import json
import requests
import pandas as pd
import operator
import pandas as pd
import matplotlib.pyplot as plt

from bson.json_util import dumps
#import update from updateDB
from config import API_KEY
from countries import countries, country_codes
#print(countries + country_codes)

from flask import Flask, jsonify, render_template
app = Flask(__name__)

dataGEOJSON = {}
with open('countries.geo.json') as f:
    dataGEOJSON = json.load(f)

conn = 'mongodb://localhost:27017/top_headlines'
print(conn)
client = pymongo.MongoClient(conn)
print(client)
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


#route that determines which country's boundaries get drawn
@app.route("/geojson")
def geo():
    #print("attempting to load the countries json file from disk")
    #open geojson file and load  
    # with open('countries.geo.json') as f:
    #     data = json.load(f)
         #formatting to account for Serbia
    formatted_countries= []
    for country in countries:
        if country == "Serbia":
            country = "Republic of Serbia"
            formatted_countries.append(country)
        else:
            formatted_countries.append(country)
    
    #set empty list for good geojson data
    goodData = []
    #for country in data's features,
    for entry in dataGEOJSON["features"]:
        #if country is in our country list,
        if entry["properties"]["name"] in formatted_countries:
            #add to good data list
            goodData.append(entry)
        #else, skip
        else:
            pass
    #pass good data into geojson format
    goodData = {'type': 'FeatureCollection',
        'features': goodData}
    #dump geojson data into json
    return json.dumps(goodData)
   

#route that returns info to display on map and tooltip
@app.route("/map_info")
def map_info():
    #open center coordinates file and load
    with open('centroids.json') as centers:
        data = json.load(centers)
        #find center coordinates data
        center_coords = data["center_coords"]

        #set collection
        collection = db["countries_keywords"]
        #get keywords data
        data = collection.find()

        #set empty map dictionary
        mapDict = {"map_info": []}
        #for country in countries_keywords,
        for entry in data:
            #set empty keyword dictionary
            kw_dict = {"country": "", "coords": {}}

            #set country variable and add to keyword dict
            country = entry["country"]
            kw_dict["country"] = country
            
            #find center coordinates for country
            for coords in center_coords:
                #if country = country, get lat and lon
                if coords["country"] == country:
                    lat = coords["coords"][1]
                    lon = coords["coords"][0]
                #else, pass
                else:
                    pass
            #add lat and lon to keyword dict
            kw_dict["coords"]["lat"] = lat
            kw_dict["coords"]["lon"] = lon

            #get top keyword and add to keyword dict
            keyword = list(entry["keywords"].keys())[0]
            kw_dict["keyword"] = keyword

            #append country's keyword dict to map dict
            mapDict["map_info"].append(kw_dict)
    return jsonify(mapDict)

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

@app.route("/country/<country>")
def country_dash(country):
    #this page that is linked in the country's tooltip
    #big merge here

    ### Jacobs simple count ###
    print(country)
    collection = db["countries_wordblob"]

    myDat = {}
    #print(routeReturn)
    for x in collection.find({"country":country}):
        myDat[x["country"]] = x["words"]
    #print(myDat)
    xxyy = {}
    for word in myDat[country]: #wish i could use arrays
        #print(word) 
        if word in xxyy:
            xxyy[word] = xxyy[word] + 1
        elif word not in xxyy:
            xxyy[word] = 1
    #print(xxyy)
    pdict= {}
    pdict['x'] = []
    pdict['y'] = []
    
    for key,val in xxyy.items():
        #print( key, "=>", val )
        pdict['x'].append(key)
        pdict['y'].append(val)
    print(pdict)
    df = pd.DataFrame.from_dict(pdict) #always in brackets, why? WHY!? okay, now it doesnt want brackets
    print(df)
    #df = pd.DataFrame.from_dict(dat)
    df.sort_values(by='y', ascending=False)
    df = df.head(20).sort_values(by='y', ascending=False)
    df.plot(kind='bar', x='x',y='y')
    #dhtml = df.to_html()
    plt.savefig('static/'+country+'.png', bbox_inches="tight", facecolor=(0, 0.79, 0.79), transparent=True)
    cnt = country +".png"
    return render_template('indexb.html',country=cnt, title=country)
    #return render_template('mycountry.html',country=cnt)

@app.route("/charts/<country>")
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

@app.route("/keywords")
def keywords():
    #dummy data test route
    {{"Country": "Argentina", "Top": ["Trump", "Resigns", "Woman", "Worry", "Markel"]}, {{"Country": "Canada", "Top": ["Hockey", "Kim", "Scared", "Snow", "Oil"]}}}

### FILTER BY KEYWORD!!

@app.route("/world")
def test(): 
  
    routeReturn = getKeywords()
    return json.dumps(routeReturn)

@app.route("/nodes")
def nodes():
    
    flaskJSON= getKeywords()
    print(flaskJSON)
    x = flaskJSON
    for z in x:
        x[z] = sorted(x[z].items(), key=operator.itemgetter(1))
    print(x)    
    return render_template('nodes.html', flaskJSON=x )

def getKeywords():
        collection = db["countries_keywords"]

        data = collection.find()

        routeReturn = {}
        for country in collection.find().distinct('country'):

            myWords = collection.find_one({"country": country})
            routeReturn[country] = myWords['keywords']

        print(routeReturn)
        return(routeReturn)

if __name__ == "__main__":
    app.run(debug=True)
# if __name__ == "__main__":
#     app.run(port=7075, debug=True)