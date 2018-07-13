import re
from keys import consumer_secret,consumer_key,access_token,access_secret
import tweepy
from tweepy import OAuthHandler
import time
from time import sleep
import nltk
from nltk.corpus import *
nltk.download('stopwords')
import paralleldots
import collections
from collections import Counter
import textblob
from textblob import TextBlob
import  flag


auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tweepy.API(auth)

paralleldots.set_api_key("BJnIQFVlvmYwoWLVYltgzsV01JKT5nRsSgg36OEVey0")
paralleldots.get_api_key()


def retrieve_tweets():
    global tweets
    tweet_input = input("enter the hashtag you want to search")
    tweets = api.search(q=tweet_input)
    print(tweets)


def f_count():
    tweet_input = input("Enter the hashtag you want to search")
    tweets = api.search(q=tweet_input)
    print("UserName      Followers Count")

    for tweet in tweets:
        print(tweet.user.name + "     " + str(tweet.user.followers_count))



def update_status():
    update_status=api.update_status(status ="Hi people...!")
    print(update_status)

def tweet_location():
    tweets=input("Enter the hashtag  you want to search")
    tweet1=api.search(tweets)
    for search_results in tweet1:
        print('location',search_results.user.location)
        print('time_zone',search_results.user.time_zone)

def sentiments():
    tweet_input = input("Enter the hashtag you want to search")
    tweets = api.search(q=tweet_input)
    print(tweets)

    for tweet in tweets:
        text = tweet.text

    print("\nSentiments")
    print(paralleldots.sentiment("i'am very happy")["sentiment"])


def stwords():
    global count
    stop_words = set(stopwords.words('english'))
    x = [x.upper() for x in stop_words]
    tweets = api.user_timeline(screen_name="antman", count=20, tweet_mode="extended")
    for tweet_compare in tweets:
        fulltext = tweet_compare.full_text
        tmp = []
        tmp.append(fulltext)
        temp = tmp
        import re
        cur_tweet = re.sub(r"http\S+", "", str(temp))
        cur_tweet1 = re.split(r"\s", cur_tweet)
        cur_tweet = [w for w in cur_tweet1 if not w in stop_words]
        cur_tweet=[]
        for w in cur_tweet1:
            if w not in stop_words:
                cur_tweet.append(w)
                count = Counter(cur_tweet).most_common(10)
        print(count)

#MENU
def display_menu():
    print('''Select an option you want to perform :
    1.)To Retrieve  the Tweets..
    2.)To Count the number of Followers..
    3.)To Update the Status..
    4.)To find the Sentiments..
    5.)To Find location and time zone of tweet..
    6.) EXIT the Menu.......
    ''')
    option=int(input("Please enter the option you want to retrieve from the given  MENU: "))
    if (option==1):
        retrieve_tweets()
        display_menu()

    elif (option == 2):
        f_count()
        display_menu()

    elif (option == 3):
        update_status()
        display_menu()

    elif (option==4):
        sentiments()
        display_menu()

    elif (option==5):
        tweet_location()
        display_menu()

    elif option == 6:
        print("Good Byeeeeeee....🖐🖐")
        flag = False
    else:
        print("Please enter the valid input ")

display_menu()
