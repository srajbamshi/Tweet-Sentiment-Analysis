#Import the libraries
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import sys
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

ACCESS_TOKEN = "3294900861-8vMK9Y2pUB7tWAUkzv3XM7yX9HKvY1kKvyE8gUC"
ACCESS_TOKEN_SECRET = "R8X52w4nNlbSBUlp0KSEQYVT6h0V8zse6AwAR947OME26"
CONSUMER_KEY = "fpwWvMuOVI0xHbacBwMaSCHqV"
CONSUMER_SECRET = "OQoH53rEeXYZD62lcRpN85oSIVWjj8GIZ44HQkUYuX9oLLw3e5"

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# Creation of the actual interface, using authentication
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

searchTerm = '#Stocks'
tweetAmount = 200

tweets = tweepy.Cursor(api.search, q = searchTerm, lang = 'en').items(tweetAmount)

# Print the last 5 tweets from the account
print("Show tweets \n")
for tweet in tweets:
  print(tweet.text)

# Print tweets
print("Show tweets \n")
for tweet in tweets:
    clean_text = tweet.text
    print(clean_text)

