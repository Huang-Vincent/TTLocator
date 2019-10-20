# TrashTag Locator

[Website can be found here](http://ttlocator.com/) and was made for HackRPI 2019.

## Inspiration
We noticed that connection to SMS (mobile text messaging) is far more reliable and widespread than connection to the internet. However, reliable connection to the internet is a near-necessity nowadays; we sought to resolve this difference by using SMS network to provide primitive internet functionality, thereby acting as a portal to the internet for those without direct connection. In particular, this project greatly increases accessibility in developing areas which do not have the necessary expensive internet infrastructure established, but do have more widespread access to text (or even people without smartphones).

## What it does
All communication happens through text: the user sends input by texting our Twilio-registered number, and receives outputs through texts from that same number. The user enters various one of 6 different commands, which correspond to some of the most important basic uses of the internet, including:
* Search
* Directions/maps
* News
* Translation
* Image recognition & search
* E-banking Once the backend of our program receives SMS inputs, it then runs our code hosted on GCP Compute Engine, querying various APIs to fulfill the user’s queries. It fetches the data requested and then texts it back to the user.

Throughout the process, the program’s chatbot makes engaging conversation for a more entertaining user experience. In many cases the bot even suggests its own topics to the user (for search, restaurant recommendations, popular news, etc). The chatbot operates using regular-expression based keyword detection to pick up conversational cues and construct a coherent response relevant to the user’s input. The goal of creating a full-fledged conversational chatbot with personality, rather than simply a bland endpoint for predetermined user input, was to make the user experience a compelling and enjoyable one (also, it was just a fun challenge!).

## How we built it
We used Python with Flask to host our backend server for communication with Twilio. We used a unique API for each functionality: GCP’s custom search, maps, news, AutoML translate, and computer vision APIs for uses 1-5, respectively; and Capital One’s Nessie API for 6.

## Challenges we ran into
1) We had difficulty integrating our python HTTP server, Twilio, and Google Cloud Platform. Specifically, we had trouble with:
* Combining the APIs to cohesively communicate with the user
* Communicating the HTTP Get and Post requests between our HTTP server and Twilio
* Creating an effective image recognition with Google’s Cloud Vision

2) We struggled displaying the information in a user-friendly and readable SMS format. Majority of the information that was parsed had to be modified in order to be accessible and easy to read (ie removing HTML flags, removing unwanted formatting character, etc.)

3) Creating a chatbot that would pick up on conversational cues and respond accordingly was difficult--regular expressions saved the day here

## Accomplishments that we're proud of
* Getting so many basic functionalities working was incredibly gratifying.
* We managed to utilize the full power of Google Cloud Platform through using 5 of its various APIs, from the AI/ML to Compute to Search categories.
## What we learned
* How to weave together several different APIs under one cohesive project!
* How to use a bunch of Google cloud APIs--as it turns out, GCP is incredibly powerful!
* We’re Vim power users now
* GCP’s compute engine virtual machine environment
* Extensive use of regex
## What's next for SMS.net
More functionalities are always nice (email, social media…)
Moving to a Natural Language Processing-based approach for the chatbot would undoubtedly make it more powerful (but that’s a nontrivial problem, definitely not suited to an overnight hackathon)

## Authors

* **Joheen Chakraborty** - [joheenc](https://github.com/joheenc)
* **Vincent Huang** - [Huang-Vincent](https://github.com/Huang-Vincent)
* **Gaurav Aggarwal** - [Gauravity-23](https://github.com/Gauravity-23)
* **Calvin Li** - [licalvinf ](https://github.com/licalvinf )

