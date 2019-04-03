# Import tweepy, time, sleep, credentials.py
import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# For loop with hashtags to retweet
for tweet in tweepy.Cursor(api.search,
q=('#Maduro OR #Caracas OR #VenezuelaResiste OR #Venezuela -filter:retweets'),
lang='en').items():
# After .items( there can be set number of retweets
# But in our case we lease it blank to run indefinitely

    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')

        # Wait 180 seconds before finding a new tweet
        # Prevents spam and losing developer status
        sleep(180)

    # If an error arises, print it out
    except tweepy.TweepError as e:
        print(e.reason)

    # Else break the program
    except StopIteration:
        break

#The default implementation returns False for all error code, but here
#we can override it to allow Tweepy to reconnect for some or all codes,
#using backoff strategies.
class MyStreamListener(tweepy.StreamListener):

    def on_error(self, status_code):
        if status_code == 420:
            # Returning False in on_error disconnects the stream
            return False
