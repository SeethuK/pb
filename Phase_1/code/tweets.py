import tweepy
import csv
import json
import pandas as pd
####input your credentials here
consumer_key = "pu0xhtpjnt6bipf9gwuwinIKW"
consumer_secret = "Jf8333O2yIpq6YJSykpWpnc3bQpYTLFOb5HkhGchUarJpjeSuE"
access_token = "1098025614953582592-tncLOpKFFjrvbcCs9ctH9AMN3HMqbI"
access_token_secret = "XWlaw0D0qaML1jPmDljqTLsjgMoBfiifffAvzlmhliVaD"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('tweetsdata.csv', 'a')
# Use csv Writer
csvWriter = csv.writer(csvFile)
track=['PulwamaAttack','love']
for t in track:
    print "Tracking "+t
    for tweet in tweepy.Cursor(api.search,q=t,count=100000000,lang="en",since="2000-01-01",include_entities=True).items():
	print "Tracking ..."+t
	csvWriter.writerow([tweet.created_at,tweet.entities, tweet.text.encode('utf-8')])
	print tweet.created_at
    print "Finished "+t+"\n"
csvFile.close()
