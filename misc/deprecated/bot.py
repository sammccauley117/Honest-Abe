import time
import tweepy
import honestAbeBotKeys as keys
import keyTerms as terms
import csv, json, sys
import requests

from textblob import TextBlob

class Analysis():
    def __init__(self, tweet):
        self


# Returns authenticated Tweepy API
def twitterAuth():
    auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
    auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)
    return tweepy.API(auth)





def formatReply(industry, ammount, lastName):
    possesiveName = ''
    if lastName[-1] == 's':
        possesiveName = lastName + "'"
    else:
        possesiveName = lastName + "'s"
    reply = 'Senator ' + possesiveName + ' views and motives may be biased by the $' + "{:,}".format(ammount) + ' they have recieved from the ' + industry + ' industry'
    return reply





# Returns a politician's top 10 donors
def getDonors(name):
    donors = []
    with open('./data.csv', 'r') as myfile:
        senators = list(csv.reader(myfile))
        for senator in senators:
            if senator[0] == name:
                donors.append([senator[6], senator[8]])
    return donors





# Returns list of key industries to check for
def getIndustries(tweet):
    str = tweet.lower()
    results = []
    for term in terms.getKeyTerms():
        if term[0] in str:
            results.append(term[1])
    return list(set(results))

def validateSentiment():





def getSentiment(tweet):
    analysis = TextBlob(tweet.text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'





def getNameFromTwitter(name):
    firstName = ''
    lastName  = ''
    with open('./data.csv', 'r') as myfile:
        senators = list(csv.reader(myfile))
        for senator in senators:
            if senator[0] == name:
                firstName = senator[1]
                lastName  = senator[2]
    return firstName, lastName





def checkIndustries(industries, donors):
    topIndustry = ''
    ammount = 0
    for industry in industries:
        for donor in donors:
            if industry == donor[0]:
                if int(donor[1]) > ammount:
                    topIndustry = industry
                    ammount = int(donor[1])
    return topIndustry, ammount





def checkTweet(tweet, name):
    industries = getIndustries(tweet) # Returns a list of industries that were mentioned in tweet
    donors = getDonors(name)          # Returns top donors for politician
    print 'Relevant Industries: ' + str(industries)
    print 'Top Donors: ' + str(donors)
    topIndustry, ammount = checkIndustries(industries, donors)  # Checks if any industries in tweet are top donors
    firstName, lastName = getNameFromTwitter(name)              # Returns first and last name from Twitter handle
    sentiment = getSentiment(tweet)
    return topIndustry, ammount, lastName





def replyToTweet(api, name, reply, id):
    api.update_status('@' + name + ' ' + reply, id)





if __name__ == '__main__':
    api = twitterAuth()
    recentID = 0
    while(1):
        print '\n##### RUNNING #####\n'
        tweets = api.home_timeline(include_rts=False, tweet_mode='extended')
        for tweet in tweets:
            name = tweet.user.screen_name
            text = tweet._json['full_text'].encode(sys.stdout.encoding, errors='replace')
            industry, ammount, lastName, sentiment = checkTweet(text, name)
            print 'Name:      ' + name
            print 'Tweet:     ' + text
            print 'Sentiment: ' + sentiment
            print 'Industry:  ' + industry
            if industry != '' and ammount != 0 and lastName != '':
                if tweet.id > recentID:
                    print 'REPLY: ' + formatReply(industry, ammount, lastName)
                    # replyToTweet(api, name, formatReply(industry, ammount, lastName), tweet.id)
                else:
                    print 'REPLY: [ERROR - invalid ID]'
            print '###################################################################################################################################################'
        recentID = tweets[0].id
        time.sleep(5 * 60)
