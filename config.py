#creating a function that creates the api and logs errors/if successful
import tweepy
from credintials import *
import logging

#setting up the logging system
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = logging.FileHandler("logs\\config.log")
logger.addHandler(handler)

def create_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API")
        raise e
    logger.info("API created")
    return api