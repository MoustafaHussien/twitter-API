import tweepy
import datetime

ckey = 'rTWMi8ejikhsyyBdaRbpytVEA'
csecret = "c180XPEpQTC9eu2k9xCRFvZgqUa2du9yKpnwae6f4GBbRbOcbs"
atoken = "794364093020913665-xe0uMfb4ypPAylCzcZrmumq54NTMEgg"
asecret = "lbcuN7e07kJkZxL7QzGoQVvm0JbO4vTovGDKkXa465QmS"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)


def get_all_tweets(screen_name):
    tweets = api.user_timeline(screen_name=screen_name, count=200)
    for tweet in tweets:
        x = (datetime.datetime.utcnow() - tweet.created_at)
        if (x.days < 1) and (x.seconds < (60 * 60)):
            print tweet.text.encode("utf-8")


def start():
    for friend in tweepy.Cursor(api.friends).items():
        print(str(friend.screen_name) + " " + str(friend.id))
        get_all_tweets(friend.screen_name)


if __name__ == '__main__':
    start()
