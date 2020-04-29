# -*- coding: utf-8 -*-
import sys, getopt, datetime, codecs, os
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got
from datetime import date
import time, random

today = datetime.datetime.today()

hashtags = ['#gaming']


base = datetime.datetime(2020, 4, 28)
delta = today-base
dates = [ base + datetime.timedelta(days=x) for x in range(delta.days) ] #It doesn't include today
# Summing up days -> base + datetime.timedelta(days=1)

maxtweets = 300 
orig_stdout = sys.stdout
output = open('tweets\\output-'+str(today.date())+'.txt', 'a')
sys.stdout = output

for hashtag in hashtags:
	for date in dates:
		sleepy = random.randint(0,18)
		print("Sleeping for {:d}".format(sleepy))
		time.sleep(sleepy) #Trying to avoid being blocked by Twitter
		
		since = (base + datetime.timedelta(days=-1)).date()
		
		if hashtag[0] == '#':
			ht = hashtag[1:]
			ht = ht.replace(" ", "_")
		else:
			ht = hashtag
			ht = ht.replace(" ", "_")
		starttime = datetime.datetime.now()	
		print("Getting tweets for {:s}, saving in tweets_".format(hashtag) + ht + "_" +\
				str(date.date()) + ".csv at " + str(starttime))
		
		#You are gonna need to create a tweet folder or change the --output parameter
		os.system("python Exporter.py --toptweets --querysearch \"" + hashtag + " lang:pt\"\
			--since " + str(since) + " --until " + str(date.date()) + " --maxtweets " +\
			str(maxtweets) + " --output tweets\\tweets_" + ht + "_" + str(date.date()) + ".csv >> tweets\\output_system_" \
			+ str(today.date()) + ".txt")
		
		stoptime = datetime.datetime.now()
		deltaLittle = stoptime - starttime
		print("It took {0} seconds to get all tweets. Finished at {1}".format(str(deltaLittle), str(stoptime)))

sys.stdout = orig_stdout
output.close()