from rake_nltk import Rake, Metric
from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import random

app = Flask(__name__)

#connect to mongo and retrieve data
mongo = PyMongo(app, uri="mongodb://localhost:27017/top_headlines")
countriesData = mongo.db.countries_data.find()

#clean data
cleanCountriesdata = []
for data in countriesData:
  data.pop('_id')
  cleanCountriesdata.append(data)

titlesString = ""
for headline in cleanCountriesdata[6]["articles"]:
  print(headline["title"])
  titlesString += " " + headline["title"]

r = Rake(max_length=2, ranking_metric=Metric.WORD_DEGREE) # Uses stopwords for english from NLTK, and all puntuation characters.
# language="Spanish"
mytext = "Manchester United vs PSG, Champions League last 16, first leg: live score and goal updates Professor Green rushed to hospital after fracturing neck in seizure England in West Indies: Tourists claim consolation 232-run victory as hosts win series 2-1 Daniel Radcliffe thinks the Harry Potter franchise will get a REBOOT Brexit: PM could delay final vote on Brexit Official Samsung Galaxy S10 cases leak as the phone nears release El Chapo found gulity: Prosecutors say there will be 'no escape' for Mexican drug lord Rapper 21 Savage released on bond after nine days in custody Unborn baby receives surgery inside womb six weeks before birth Family of NHS nurse who died after missed cervical cancer want inquiry Worcester acid attack: Man 'forced to squirt boy' Solskjaer names his XI to face PSG | Official Manchester United Website CCTV shows last known movements of missing Libby Squire Exclusive: UK chief Brexit negotiator Olly Robbins warns MPs the choice is May's deal or extension BBC asks White House for security review after Trump rally attack Vinicius Junior: Real Madrid teenager set to start against Ajax A40 police pursuit crash couple 'were newlyweds' EU and US work on new Russia sanctions in response to capture of Ukrainian sailors Protests and tight security as Catalan separatists face hefty jail terms in Spain\u2019s \u2018trial of the century\u2019 Two men found with 'acid attack' injuries in King's Cross"


r.extract_keywords_from_text(titlesString)

phrases = r.get_ranked_phrases() # To get keyword phrases ranked highest to lowest.
# print(phrases)
phraseScores = r.get_ranked_phrases_with_scores()
print(phraseScores)
print(phraseScores[0])