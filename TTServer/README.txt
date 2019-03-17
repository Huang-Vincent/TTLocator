The local server is responsible for several tasks, including
	-Scraping twitter daily for posts relating to #TrashTag #TrashTagChallenge
	-Parsing collected posts for coordinates. This was done through several layers
		of parsing, starting with a raw_data.json file holding the filtered down
		twitter api returns. This allowed us to minimize API calls needed for
		testing.
	-Reparsing the raw_data file to remove escape characters and preparing for
		firebase integration
	-Passing over the data file once more with Named Entity Recognition to find
		cities, places, and landmarks from the body of a twitter post if the tweet
		geo-location metadata is not available

This data is then stored on Firebase for future map queries
The local server then listens for new firebase db queries from the front end and
triggers twillio messages to relevant users when the new user indicates an interest
in #TrashTagging in the local area. It also listens for replies to the twillio
account to remove all of a user's indicators on the map.

Start by running main.py