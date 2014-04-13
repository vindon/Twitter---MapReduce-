import MapReduce
import sys
import sys
import json
import codecs

"""
Author: Tigran Hakobyan & Qian Ding 

# Determines the top 10 hashtags.
# using a simple Python MapReduce Framework. Assumes json input file.

"""

AllHashtags = {}

#use and create an instance of MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
	tweet = record
	p = {}
	p = None
	d = {}
	# If tweet doesn't contain 'entities' field
	# we ignore the tweet and go to the next tweet.
	if not 'entities' in tweet:
		pass
	else:
		entities  = tweet['entities']
		# 'hashtags' is list a in 'entities' field of
		# tweet.
		if not 'hashtags' in entities:
			pass	
		else:
			hashtags = entities['hashtags']
			# If hashtags is empty we can ignore the current tweet.
			if not hashtags:
				pass
			else:
				# Tweet can contain multiple hashtags.
				for hsh in hashtags:
					# In this program we assume that 
					# hashtags are not case sensitive. 
					txt = hsh['text'].lower()
					if txt not in d:
						d[txt] = 1
					else:
						tempValue = d.get(txt)
						tempValue = tempValue + 1
						d[txt] = tempValue
		
	for key, value in d.iteritems():
		mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
	total = 0
	for v in list_of_values:
		total += v
		
	AllHashtags[key] = total
	

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
  # Sorts the dictionary items by value (value is the hashtag's count) in reversed order.
  topTenHashtags  = sorted(AllHashtags.iteritems(), key = lambda x : x[1], reverse = True)
  print ("These are the top ten hashtags: ")
  print
  i = 1;
  for e in topTenHashtags[:10]:
	  print (str(i) + ". " + e[0])
	  i = i + 1
  print
