import tweepy
import pandas as pd
import json


import spacy
from spacy import displacy
from collections import Counter

import requests
import time

def TwitterScraper():
	nlp = spacy.load('en_core_web_sm')

	consumer_key = 'aDioWf2uw896yNgiOjceOJLL2'
	consumer_secret = 'ZJZIGCoKpVgCAFwB8Yb06CuNdIj8lslNBJ0HHmNTCoF8LswsYP'
	access_token = '1066549932222541824-IeXGev741BeYR67otODIP4eCX8uMcs'
	access_token_secret = 'nSDJuZ3GEebX3Fo0lWgm5pdwH3UDjWFF4QpFLGbFWxKH7'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth,wait_on_rate_limit=True)


	tweetmap = {}

	df = []
	filterWords = ['trashtag', 'Trashtag', ""]
	searchTerms = ['#trashtag', '#trashchallenge']
	for term in searchTerms:
		counter = 0
		for tweet in tweepy.Cursor(api.search,q=term,count=100,lang="en", since="2018-04-03").items():
			print '\r' + tweet.user.screen_name ,
			counter+=1
			if counter > 10000: break

			if "RT" not in tweet.text:
				if tweet.coordinates != None:
					values = ['@' + tweet.user.screen_name, tweet.coordinates['coordinates'][1], tweet.coordinates['coordinates'][0]]
					df.append(values)

				else:
					doc = nlp(unicode(tweet.text))
					for obj in doc.ents:
						if (obj.label_ == "LOC" or obj.label_ == "GPE") and obj.label_ != None and obj.text.strip() not in filterWords:
							df.append(['@' + tweet.user.screen_name, obj.text.strip()])
							break

	dfJSON = pd.DataFrame(df).to_json(orient='values')
	outFile = open('raw_data.json', 'w')
	json.dump(dfJSON, outFile)
	outFile.close()


def ReformatRawData():
	reformattedFile = open('raw_data.json')
	
	text = reformattedFile.readline()
	text = text[1:-1]
	
	text = text.replace('\\','')
	text = text.replace(',null', '')

	newRawData = open('pretty_raw_data.json','w')
	newRawData.write(text)
	newRawData.close()
	reformattedFile.close()

def Reparse():
	url = "https://maps.googleapis.com/maps/api/geocode/json"
	newDataSet = []

	with open('pretty_raw_data.json', 'r') as data_file:
		data = json.load(data_file)

		for line in data:
			if len(line) == 2:
				parameters = {'sensor': 'false', 'address': line[1] ,'key' : 'AIzaSyB8ZxDD4j3d2heRl1bMt10Ni4xjvk9adAU'}
				r = requests.get(url, params=parameters)

				if r.json()['status'] == 'ZERO_RESULTS':
					time.sleep(1)
					continue

				results = r.json()['results']
				location = results[0]['geometry']['location']

				newDataSet.append([line[0], location['lat'], location['lng']])
			else:
				newDataSet.append(line)

	newFile = open('MapPoints.json', 'w')
	json.dump(newDataSet, newFile)
	newFile.close()