from GetOldTweets3.manager.TweetManager import TweetManager
from GetOldTweets3.manager.TweetCriteria import *
import os.path as op
import pandas as pd
file_name = './corona/2020-06.csv'

def save_partial_result(tweets):
    global file_name
    df = pd.DataFrame(t.__dict__ for t in tweets)

    if not op.isfile(file_name):
        df.to_csv(file_name)
    else:
        df.to_csv(file_name, mode='a', header=False)

def scrap_tweets():
    query = '(covid-19 OR sars-cov-2 OR coronavirus OR 2019-ncov OR pandemia OR quarentena)'
    tweetCriteria = TweetCriteria().setQuerySearch(query)\
                                            .setSince("2020-06-01")\
                                            .setUntil("2020-06-30")\
                                            .setLang("pt")
    TweetManager.getTweets(tweetCriteria, bufferLength=50, receiveBuffer=save_partial_result)

scrap_tweets()