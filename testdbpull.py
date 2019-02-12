import datetime as dt
import pandas as pd
import pymongo
import requests
import json
from py_translator import Translator
import csv

langByCountry = {}
with open('countrieslang.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        langByCountry[row[1]] = row[3]
        #print(row)
        #print(row[0])
        #print(row[0],row[1],row[2],)
#print(langByCountry)

s = Translator().translate(text='help my silly friend', dest='es').text
print(s)

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
# print("example")
# print(data[0])

countryWords = {}
clouds = {}
allWords = ''

def removeSymbols(word):
  for char in word:
    if char in " ?.!/;:~!@#$%^&*()<>'|\\":
        #print(word)
        word = word.replace(char,'')
        #print(word)
  return word

for country in data:
    # print(country['country'])
    # print(country['country_code'])
    # print(len(country['articles']))
    f = open(country['country']+".txt", "w")
    thisLang = ''
    def setLang(lang):
      global thisLang
      thisLang = lang
      
    (setLang(langByCountry[country['country_code']]) if (langByCountry[country['country_code']] != '' ) else (print("no"))) if (country['country_code'] in langByCountry) else print('country code not found!!!!!!')
    
    
    countryWords[country['country']] = ''
    for article in country['articles']:
      if (thisLang != ''):
        
        #print(article['title'])
        try:
          article['title'] = Translator().translate(text=article['title'], dest='en').text
          print("translating")
        except:
          print("failed to translate")
          article['title'] = article['title']
        print(article['title'])
      countryWords[country['country']] = countryWords[country['country']] + article['title'] + ' '
      allWords = allWords + article['title']
    thisWords = countryWords[country['country']]
    f.write(json.dumps(countryWords[country['country']]))
    thisList = {}
    #words per country
    for x in thisWords.split():
      #print(x)
      #clouds[(country['country']]
      x = removeSymbols(x)
      if x in thisList:
        thisList[x] = thisList[x] + 1

      else: 
        thisList[x] = 1
      #print(thisList)
      clouds[country['country']] = thisList
      allList = {}
#global word list
for x in allWords.split():
  x = removeSymbols(x)
  if x in allList:
    allList[x] = allList[x] + 1
  else: 
    allList[x] = 1     
    #end of loop

     # print(article)
  #  print(article)
  #articleList.append(article)

#print(len(articleList))

#print(countryWords)
f = open("countryWordCounts.txt", "w")
f.write(json.dumps(clouds))
# f = open("countryWordsRaw", "w")
# f.write(json.dumps(clouds))

f = open("allWordsRAW.txt", "w")
f.write(json.dumps(allWords))
f = open("allWordsCount.txt", "w")
f.write(json.dumps(sorted(allList.items(), key=lambda x: x[1])))
#print(allList)
#print(sorted(allList, key=allList.__getitem__))

#print(sorted(allList.items(), key=lambda x: x[1]))
