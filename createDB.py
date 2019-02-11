import requests
import pymongo
from config import API_KEY

countries = ["Argentina", "Australia", "Austria", 
"Belgium", "Brazil", "Bulgaria", "Canada", "China", 
"Colombia", "Cuba", "Czech Republic", "Egypt", "France", 
"Germany", "Greece", "Hong Kong", "Hungary", "India", "Indonesia", 
"Ireland", "Israel", "Italy", "Japan", "Latvia", "Lithuania", 
"Malaysia", "Mexico", "Morocco", "Netherlands", "New Zealand", 
"Nigeria", "Norway", "Philippines", "Poland", "Portugal", 
"Romania", "Russia", "Saudi Arabia", "Serbia", "Singapore", 
"Slovakia", "Slovenia", "South Africa", "South Korea", "Sweden", 
"Switzerland", "Taiwan", "Thailand", "Turkey", "United Arab Emirates", 
"Ukraine", "United Kingdom", "United States of America", "Venezuela"]

country_codes = ["ar", "au", "at", "be", "br", "bg", "ca", "cn", 
"co", "cu", "cz", "eg", "fr", "de", "gr", "hk", "hu", "in", "id", 
"ie", "il", "it", "jp", "lv", "lt", "my", "mx", "ma", "nl", "nz", 
"ng", "no", "ph", "pl", "pt", "ro", "ru", "sa", "rs", "sg", "sk", 
"si", "za", "kr", "se", "ch", "tw", "th", "tr", "ae", "ua", "gb", 
"us", "ve"]

rawData = {}
countriesData = []
for i in range(len(country_codes)):
    #visit news api
    query_url = f"https://newsapi.org/v2/top-headlines?country={country_codes[i]}&apiKey={API_KEY}"
    #get response
    response = requests.get(query_url).json()
    #add raw articles data to rawData dict
    rawData[countries[i]] = response["articles"]
    
    #set empty articles list
    articlesList = []
    #for each article
    for article in response["articles"]:
        #construct article dictionary
        articleDict = {"source": article["source"]["name"], 
                       "title": article["title"].split(" - ")[0], 
                       "url": article["url"], 
                       "date": article["publishedAt"][:10]}
        #add dict to articles list
        articlesList.append(articleDict)
    
    #construct country dictionary
    countryDict = {
        "country": countries[i],
        "country_code": country_codes[i],
        "articles": articlesList
    }
    #add dict to countries data
    countriesData.append(countryDict)

#connect to mongo
conn = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(conn)

#declare the database
db = client["top_headlines"]

#drop if exists for initial db creation
db["countries_data"].drop()
db["raw_countries_data"].drop()

#declare the collection
rawCollection = db["raw_countries_data"]
collection = db["countries_data"]

#insert data into dbs
rawCollection.insert_one(rawData)
collection.insert_many(countriesData)