from twilio.rest import Client

def create_message(name, phone):
	account_sid = 'AC72bd88879377efdfd4313aca2c76c239'
	auth_token = '98b20b882795f4ce953a1d53a6e2cbf1'
	client = Client(account_sid, auth_token)
	phone = "+1" + phone
	textbody = "Hello, it seems that you are close to " + name + ", who has also participated in #trashtag! Wild!\nTo remove yourself from the map, please reply 'Remove @<Twitter-Handle>'."
	message = client.messages.create(body= textbody, from_= '+19549474781',to = phone)
	print "\tMessage sent succesfully"