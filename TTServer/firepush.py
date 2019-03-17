import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

import math

import twilioSender

cred = credentials.Certificate('credentials.json')
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://hackrpi2019-41699.firebaseio.com/'})
ref = db.reference("Clients")

client_dictionary = []
user_group = []

isInitial = True

def listener(event):
	users = ref.get()

	global isInitial
	if isInitial:
		print "Listening: "
		isInitial = False
	else:
		allClients = ref.get()

		Lat = 0
		Long = 0
		name = ''
		number = 0

		for name, val in allClients.items():
			if event.path[1:] == name:
				handle = name
				Lat = val['Coordinates']['Lat']
				Long = val['Coordinates']['Long']
				Number = val['Number']
				break


		for client_name, client_val in allClients.items():
			if client_name == name: continue
			lat_square = (client_val['Coordinates']['Lat'] - Lat) ** 2
			long_square = (client_val['Coordinates']['Long'] - Long) ** 2
			distance = (lat_square + long_square) ** .5
			if distance < 3:
				print "Sending Message:", handle, "and", client_name, "are close to each other."
				twilioSender.create_message(name, str(client_val['Number']))
				twilioSender.create_message(client_name, str(Number))		

def begin():
	firebase_admin.db.reference('Clients').listen(listener)