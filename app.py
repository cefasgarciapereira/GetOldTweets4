from GetOldTweets3.manager.TweetManager import TweetManager
from GetOldTweets3.manager.TweetCriteria import TweetCriteria
import os.path as op
import os
import pandas as pd
import time

month = '2020-06'
file_name = './corona/'+month+'.csv'
total = 0

def save_partial_result(tweets):
    global file_name
    global total
    global start_time

    df = pd.DataFrame(t.__dict__ for t in tweets)

    if not op.isfile(file_name):
        df.to_csv(file_name)
    else:
        df.to_csv(file_name, mode='a', header=False)
    total += 50
    os.system('clear')
    print(month+': '+str(total)+' collected...')
    print(str((start_time - time.time())/60)' minutes.')

def scrap_tweets():
    query = '(covid-19 OR sars-cov-2 OR coronavirus OR 2019-ncov OR pandemia OR quarentena)'
    tweetCriteria = TweetCriteria().setQuerySearch(query)\
                                            .setSince(month+'-01')\
                                            .setUntil(month+'-24')\
                                            .setLang("pt")
    TweetManager.getTweets(tweetCriteria, bufferLength=50, receiveBuffer=save_partial_result)

start_time = time.time()
scrap_tweets()