# Import tweepy, time, sleep, credentials.py
import tweepy
from time import sleep
from credentials import *
import praw


# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Choose a subreddit to search for post
# In this case use r/all for most responses
subreddit = reddit.subreddit('all')

# For loop to search r/all subreddit for keyword "venezuela"
for submission in subreddit.search("venezuela"):
    # Make a new tweet from found url address
    try:
        tweet = api.update_status(submission.url)

        # Terminal output
        print('Found a new post!')

        # Wait 180 seconds before finding a new tweet
        # Prevents spam and losing developer status
        sleep(180)

    # Throw an exception for when we find a duplicate post.
    # Twitter does not allow users to make the same post
    # So there must be an exception to pass and wait
    # 180 seconds again before it finds another post
    except tweepy.TweepError as error:
        if error.api_code == 187:
            
            print('duplicate message')
            sleep(180)
        else:
            raise error
