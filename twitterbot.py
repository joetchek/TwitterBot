import tweepy
from credintials import *

#setting authorizationj and access token
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#declaring api
api = tweepy.API(auth)

#verification
try:
    api.verify_credentials()
    print("Good")
except:
    print("error")

#testing tweeting a single tweet
try:
    api.update_status("This tweet was made with a bot! :)")
    print("Tweet successful")
except:
    print("Error with tweet")