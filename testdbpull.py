import datetime as dt
import pandas as pd
import pymongo
import requests
import json
from py_translator import Translator
import csv
import sys

import logging

langByCountry = {}
with open('countrieslang.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        langByCountry[row[1]] = row[3]
        #print(row)
        #print(row[0])
        #print(row[0],row[1],row[2],)
#print(langByCountry)
try:
  s = Translator().translate(text='help my silly friend', dest='es').text
  print(s)
except json.decoder.JSONDecodeError as airOr:
  #x = sys.exc_info()
  print(airOr)

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
    print(country['country'])
    print("----------------------------------------------------")
    # print(country['country_code'])
    # print(len(country['articles']))
    f = open(country['country']+".txt", "w")
    
    countryWords[country['country']] = ''
    for article in country['articles']:
  
      #on a country basis
      countryWords[country['country']] = countryWords[country['country']] + article['title'] + ' '

      #a master list of all words NOT translated yet
      #allWords = allWords + article['title']
    
    #translate here!
    thisWords = countryWords[country['country']]
    print("BEFORE")
    print(thisWords)
    thisLang = 'en'
    if (thisLang != ''):
      #TRANSLATE TO ENGLISH en
      try:
        thisWords = Translator().translate(text=thisWords, dest='en').text
        #print("translating")
      except:
        print("failed to translate")
      print("AFTER")
      print(thisWords)
    allWords = allWords + thisWords
    #dump to country file.. for testing yo
    f.write(json.dumps(thisWords))
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
