import MapReduce
import sys

"""
Author: Tigran Hakobyan & Qian Ding 

# Determines the 3 countries with the most tweets that were not retweeted
# using a simple Python MapReduce Framework. Assumes json input file.

"""

AllCountries = {}

#use and create an instance of MapReduce

mr = MapReduce.MapReduce()

def mapper(record):

	value = record
	p = {}
	p = None
	d = {}
	if not 'place' in value:
		pass
	else:
		retweeted  = value['retweeted']
		retweetCount = value['retweet_count']
		if retweeted == False and retweetCount == 0:
			p = value ['place']
			if p != None:
				country  = p['country']
				if country not in d:		
					d[country] = 1
				else:
					tempValue = d.get(country)
					tempValue = tempValue + 1
					d[country] = tempValue
					
		else:
			pass
		
	for key, value in d.iteritems():
		mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
	total = 0
	for v in list_of_values:
		total += v
		
	AllCountries[key] = total
	

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
  
  topTree  = sorted(AllCountries.iteritems(), key = lambda x : x[1], reverse = True)
  print ("These are the 3 countries with the most tweets that were not retweeted: ")
  print
  print ("1. " + topTree[0][0] + " : " + str(topTree[0][1]) + " tweets" )
  print ("2. " + topTree[1][0] + " : " + str(topTree[1][1]) + " tweets" )
  print ("3. " + topTree[2][0] + " : " + str(topTree[2][1]) + " tweets" )

