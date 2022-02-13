import tweepy
from credintials import *
from config import create_api
from time import sleep

#function that retweets tweets containing specific hashtags
def retweet_hashtag(api, query, sleep_time):
    print("This bot retweets a tweet containing a certain hashtag and then sleeps for a specified time")
    #searches and retweets from each tweet relating to the query

    #errors i cant solve right now: i cant seem to get it to recognize that a tweet has already been retweeted/favorited
    #retweeted status and favorited status are always false even if i have retweeted/favorited them
    #will continue to expiriement at a later date with this. for rn it seems to work
    for tweet in api.search_tweets(query):
        if not tweet.user.screen_name == 'JoesTestGrounds':
            print(tweet.retweeted)
            try:
                print("Tweet by: @" + tweet.user.screen_name) #prints out username
                print(tweet.id)
                tweet.retweet()
                print("Retweeted") #prints retweeted
                tweet.favorite()
                print("Favorited") #prints favorited
                sleep(sleep_time)
            except Exception as e:
                print(e.reason)
        
def main():
    api = create_api()
    query = "# jokerrrwordle" #for determining my wordle answers from my main account
    sleep_time = 360

    retweet_hashtag(api, query, sleep_time)

if __name__ == "__main__":
    main()