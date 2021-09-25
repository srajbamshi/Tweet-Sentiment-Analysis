# Import packages

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

# Loading Twitter API Credentials
mykeys = open('twitterkeys.txt', 'r').read().splitlines()
consumerKey = mykeys[0]
consumerSecret = mykeys[1]
accessToken = mykeys[2]
accessTokenSecret = mykeys[3]

# Create the authentication object
authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)

# Set the access token and access token secret
authenticate.set_access_token(accessToken, accessTokenSecret)

# Create the API object while passing in the auth information
# Creation of the actual interface, using authentication
api = tweepy.API(authenticate, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# collect tweets on     #MRT
for tweet in tweepy.Cursor(api.search,q="MRT",count=100, lang="en",rpp=100).items():
    print(tweet.created_at, tweet.text)



