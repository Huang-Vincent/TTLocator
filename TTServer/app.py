import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

from flask import Flask, request, redirect
from twilio import twiml

def deleteUser(handle, telephone):
	cred = credentials.Certificate('credentials.json')
	firebase_admin.initialize_app(cred, {'databaseURL' : 'https://hackrpi2019-41699.firebaseio.com/'})
	ref = db.reference("Clients")

	removed = False
	users = ref.get()
	
	for key, values in users.items():
		if values['Number'] == telephone and key == handle:
			print "DELETE:", key
			ref.child(key).delete()
			removed = True

	return removed

app = Flask(__name__)


@app.route("/")
def check_app():
    # returns a simple string stating the app is working
    return Response("It works!"), 200


@app.route("/twilio", methods=["POST"])
def inbound_sms():
    response = twiml.Response()
    # we get the SMS message from the request. we could also get the 
    # "To" and the "From" phone number as well
    inbound_message = request.form.get("Body")
    # we can now use the incoming message text in our Python application
    if inbound_message == "Hello":
        response.message("Hello back to you!")
    else:
        response.message("Hi! Not quite sure what you meant, but okay.")
    # we return back the mimetype because Twilio needs an XML response
    return Response(str(response), mimetype="application/xml"), 200


if __name__ == "__main__":
    app.run(debug=True)

