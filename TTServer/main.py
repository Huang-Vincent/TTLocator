import finder
import firepush

print "TTServer v1.0:"

while(True):
	command = str(raw_input('>').strip())

	if command in ['-S', '-s']:
		print "Scraping Twitter for #TrashTags"
		finder.TwitterScraper()

	elif command in ['-R', '-r']:
		print "Reformatting data"
		finder.ReformatRawData()
		print "Geocoding location data"
		finder.Reparse()

	elif command in ['-C', '-c']:
		print "Listening for new new Users..."
		firepush.begin()

	elif command in ['help', '-h', '-help']:
		print '''-S/-s: Scrape Twitter for tags and generate dataset
-R/-r/-G/-g: Reformat and geocode data for Firebase
-C/-c: Listen for front-end user input'''
	elif command in ['all','-a']:
		print "Scraping Twitter for #TrashTags"
		finder.TwitterScraper()

		print "Reformatting data"
		finder.ReformatRawData()
		print "Geocoding location data"
		finder.Reparse()
		print "Listening for new new Users..."
		firepush.begin()
	else:
		break