import time
import tweepy
import honestAbeBotKeys as keys
import keyTerms as terms
import csv, json, sys
import requests

from textblob import TextBlob

# KeyTerm Class handles list from ketTerms.py
class KeyTerm():
    def __init__(self, list_):
        self.term      = list_[0]
        self.industry  = list_[1]
        self.sentiment = list_[2]

# Donor class handles information about a politician's donor
class Donor():
    def __init__(self, industry='', code='', ammount=0):
        self.industry = industry
        self.code     = code
        self.ammount  = ammount
    def __eq__(self, other):
        return self.industry == other.industry and self.ammount == other.ammount
    def __ne__(self, other):
        return not self == other

# Politician class handles information about an individual politician
class Politician():
    def __init__(self, list_):
        self.handle    = list_[0][0]
        self.firstName = list_[0][1]
        self.lastName  = list_[0][2]
        self.fullName  = list_[0][3]
        self.party     = self.getParty(list_[0][3])
        self.id        = list_[0][4]
        self.year      = list_[0][5]
        self.donors    = self.getDonors(list_)
    def getParty(self, fullName):
        letter = fullName[-2]
        if letter == 'D' or letter == 'R' or letter == 'I':
            return letter
        else:
            return ''
    def getDonors(self, list_):
        donors = []
        for item in list_:
            donors.append(Donor(item[6], item[7], int(item[8])))
        return donors

# Analysis class handles all information necessary to judge whether or not a tweet is biased
class Analysis():
    def __init__(self, tweet):
        self.tweet = tweet
        self.id = tweet.id
        self.text = tweet._json['full_text'].encode(sys.stdout.encoding, errors='replace')
        self.handle = tweet.user.screen_name
        self.politician = self.getPolitician(self.handle)
        self.firstName = self.politician.firstName
        self.lastName  = self.politician.lastName
        self.fullName  = self.politician.fullName
        self.party     = self.politician.party
        self.donors    = self.politician.donors
        self.keyTerms  = self.getKeyTerms(self.text)
        self.sentiment = self.getSentiment(self.text)
        self.topDonor  = self.crossReference(self.donors, self.keyTerms, self.sentiment)
        self.valid     = self.validate(self.topDonor)
    # Returns whether or not a relevant top donor for the tweet subject exists
    #   if True, the tweet is reply-worthy
    def validate(self, topDonor):
        return topDonor != Donor()
    # Returns a Politician object based on the Twitter handle (username) of the tweet
    def getPolitician(self, handle):
        with open('./data.csv', 'r') as myfile:
            politicians = list(csv.reader(myfile))
            list_ = []
            for politician in politicians:
                if handle == politician[0]:
                    list_.append(politician)
        if len(list_) > 0:
            return Politician(list_)
        else:
            raise ValueError('list_ object has length 0 [Twitter handle not found][@{}]'.format(handle))
    # General information about the Analysis object (debug info)
    def details(self, showText=False):
        print '----------------------------------'
        print 'handle:   ', self.handle
        print 'id:       ', self.id
        if showText: print 'text:     ', self.text
        print 'name:     ', self.firstName, self.lastName
        print 'party:    ', self.party
        print 'sentiment:', self.sentiment
        print 'topDonor: ', self.topDonor.industry, str(self.topDonor.ammount)
        print 'valid:    ', str(self.valid)
        print '----------------------------------'
    # Returns the first and last name of Tweet-er based off the Twitter handle (Deprecated)
    def getName(self, handle):
        firstName = ''
        lastName  = ''
        with open('./data.csv', 'r') as myfile:
            senators = list(csv.reader(myfile))
            for senator in senators:
                if senator[0] == handle:
                    firstName = senator[1]
                    lastName  = senator[2]
        return firstName, lastName
    # Returns the sentiment of the Tweet based off the Tweet text
    def getSentiment(self, text):
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
    # Returns list of donors objects--a list of all top 10 industries that pays a particular politician
    def getDonors(self, name):
        donors = []
        with open('./data.csv', 'r') as myfile:
            senators = list(csv.reader(myfile))
            for senator in senators:
                if senator[0] == name:
                    donors.append([senator[6], senator[8]])
        return donors
    # Returns a list of KeyTerm objects that were mentioned in the Tweet text
    def getKeyTerms(self, text):
        str = text.lower()
        results = []
        for term in terms.getKeyTerms():
            if term[0] in str:
                results.append(KeyTerm(term))
        return results
    # Returns a top donor (if one exists) by cross referencing relevant KeyTerms and
    #   the list of a politicians top donors
    def crossReference(self, donors, keyTerms, sentiment):
        industry = ''
        code = ''
        ammount = 0
        for keyTerm in keyTerms:
            for donor in donors:
                if (donor.industry == keyTerm.industry) and (sentiment == keyTerm.sentiment):
                    if donor.ammount > ammount:
                        industry = donor.industry
                        code = donor.code
                        ammount = donor.ammount
        return Donor(industry, code, ammount)

# Returns authenticated Tweepy API
def twitterAuth():
    auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
    auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)
    return tweepy.API(auth)

# Returns String of formated reply
def formatReply(industry, ammount, lastName):
    possesiveName = ''
    if lastName[-1] == 's':
        possesiveName = lastName + "'"
    else:
        possesiveName = lastName + "'s"
    reply = 'Senator ' + possesiveName + ' views and motives may be biased by the $' + "{:,}".format(ammount) + ' they have recieved from the ' + industry + ' industry'
    return reply

# Actually sends reply (also checks to make sure that it is not a duplicate)
def replyToTweet(api, name, reply, id):
    try:
        api.update_status('@' + name + ' ' + reply, id)
    except:
        print 'ERROR: Duplicate Status'

if __name__ == '__main__':
    api = twitterAuth() # Get authenticated Tweepy API object
    recentID = 0        # recentID holds the most recent Tweet ID (to make sure not to look at old Tweets)
    while(1):
        print '\n##### RUNNING #####\n'
        tweets = api.home_timeline(include_rts=False, tweet_mode='extended')
        for tweet in tweets:
            valid = False # valid holds whether or not info on a politician is logged
            # Checks to make sure data.csv holds info on a politician
            with open('./data.csv', 'r') as myfile:
                senators = list(csv.reader(myfile))
                for senator in senators:
                    if senator[0] == tweet.user.screen_name:
                        valid = True
            # If valid Tweet, run an analysis on it
            if valid:
                a = Analysis(tweet)
                if a.valid: # If the Analysis is valid (reply-worthy), then tweet back
                    a.details(showText=True) # Show Analysis info
                    reply = formatReply(a.topDonor.industry, a.topDonor.ammount, a.lastName) # Format
                    replyToTweet(api, a.handle, reply, a.id) # Reply
        recentID = tweets[0].id # Update most recent ID
        time.sleep(5 * 60) # Wait 5 minutes because Tweepy API only allows so many requests
