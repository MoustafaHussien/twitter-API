import tweepy
import datetime
import csv

ckey = 'rTWMi8ejikhsyyBdaRbpytVEA'
csecret = "c180XPEpQTC9eu2k9xCRFvZgqUa2du9yKpnwae6f4GBbRbOcbs"
atoken = "794364093020913665-xe0uMfb4ypPAylCzcZrmumq54NTMEgg"
asecret = "lbcuN7e07kJkZxL7QzGoQVvm0JbO4vTovGDKkXa465QmS"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)


def get_all_tweets(friend, csv_writer):
    tweets = api.user_timeline(screen_name=friend.screen_name, count=200)
    for tweet in tweets:
        x = (datetime.datetime.utcnow() - tweet.created_at)
        if (x.days < 1) and (x.seconds < (60 * 60)):
            if hasattr(tweet, 'retweeted_status'):
                csv_writer.writerow([friend.id, friend.screen_name, tweet.id, tweet.created_at, tweet.retweeted_status.text.encode('utf-8')])
            else:
                csv_writer.writerow([friend.id, friend.screen_name, tweet.id, tweet.created_at, tweet.text.encode('utf-8')])


def start():
    csv_file = open('result ' + str(datetime.datetime.now()) + '.csv', 'a')
    csv_writer = csv.writer(csv_file)
    for friend in tweepy.Cursor(api.friends).items():
        get_all_tweets(friend, csv_writer)
    csv_file.close()


if __name__ == '__main__':
    start()
