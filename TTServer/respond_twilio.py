
from flask import Flask, Response, request
from twilio.twiml.messaging_response import Message, MessagingResponse

import firebase_admin
from firebase_admin import db
from firebase_admin import credentials


def deleteUser(handle, telephone):
	cred = credentials.Certificate('credentials.json')
	firebase_admin.initialize_app(cred, {'databaseURL' : 'https://hackrpi2019-41699.firebaseio.com/'})
	ref = db.reference("Clients")

	removed = False
	users = ref.get()
	
	for key, values in users.items():
		if values['Number'] == telephone and key == handle:
			print ("DELETE:", key)
			ref.child(key).delete()
			removed = True

	return removed

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms():
    # Start our response
    response = MessagingResponse()

    inbound_message = request.form['Body']
    number = request.form['From'][2:]
    handle = inbound_message.replace('Remove', '').strip()
    # we can now use the incoming message text in our Python application
    if "Remove" in inbound_message:
        response.message("Removing " + handle + "!")
        if deleteUser(handle, number):
            response.message("Successfully removed " + handle + "!")
        else:
            response.message("Error removing " + handle + ", please try again.")


    else:
        response.message("Hi! Not quite sure what you meant, but okay.")
    # we return back the mimetype because Twilio needs an XML response
    return Response(str(response), mimetype="application/xml"), 200

if __name__ == "__main__":
    app.run(debug=True)
 
