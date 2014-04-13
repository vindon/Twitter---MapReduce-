Twitter---MapReduce-
====================
country.py program: 

The pre-processing is done in Map step which checks for a tweet if it contains 
the  “place” json attribute. If it doesn't,  it skips the current tweet and goes for the next tweet
in the order.  If it contains, then the worker node wants to make sure that the tweet is not a “retweet”
and the number of retweets is equal to zero.  If the above conditions are satisfied then the mapper worker
uses a local dictionary data structure to keep track of the countries and the number of tweets for that country.
If the dictionary already contains the country name (key) it will increment the number of tweets
for that country (value). 
If it doesn’t contain, it will add the (“countryName”, 1) pair into the dictionary.
It’s worth mentioning that each worker node uses a different dictionary. The post-processing step
is done After Reduce. In this step the program simply sorts the collected dictionary (this dictionary is defined in the beginning of the program) by value (number of tweets) and prints the first 3 countries. 

hashtags.py program:

The pre-processing as well as the post-processing is very similar to the country.py program.
The pre-processing is done in Map step again using local dictionary in each worker node.
The dictionary contains the hashtag as a key and the number of occurrences of that hashtag as a value. 
The post-processing step is done After Reduce. The program sorts the final dictionary by count of hashtags 
and prints out the top 10 hashtags. 
