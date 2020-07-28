from GetOldTweets3.manager.TweetManager import TweetManager
from GetOldTweets3.manager.TweetCriteria import TweetCriteria
import os.path as op
import os
import pandas as pd
import time

month = '2020-06'
day = 21
file_name = './corona/'+month+'.csv'
total = 0

def save_partial_result(tweets):
    global file_name
    global total
    global start_time
    global day

    df = pd.DataFrame(t.__dict__ for t in tweets)

    if not op.isfile(file_name):
        df.to_csv(file_name)
    else:
        df.to_csv(file_name, mode='a', header=False)
    total += 50
    os.system('clear')
    print(month+'-'+str(day)+': '+str(total)+' collected...')
    print(str((time.time() - start_time)/60)+' minutes.')

def scrap_tweets():
    global day
    log_file = open("./corona/log.txt","a") 
    query = '(covid-19 OR sars-cov-2 OR coronavirus OR 2019-ncov OR pandemia OR quarentena)'
    while day > 1:
        print('Starting '+str(day))
        log_file.write('\nStarting'+str(day))
        tweetCriteria = TweetCriteria().setQuerySearch(query)\
                                                .setSince(month+'-'+str(day - 1))\
                                                .setUntil(month+'-'+str(day))\
                                                .setLang("pt")
        TweetManager.getTweets(tweetCriteria, bufferLength=50, receiveBuffer=save_partial_result)
        log_file.write('\nFinished'+str(day)+'\n')
        print('Finished '+str(day))
        day = day - 1

start_time = time.time()
scrap_tweets()