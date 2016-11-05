import tweepy, datetime



auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)


def get_all_tweets(screen_name):
    tweets = api.user_timeline(screen_name=screen_name, count=200)
    for tweet in tweets:
        if (datetime.datetime.utcnow() - tweet.created_at).seconds < (60 * 60):
            print tweet.text.encode("utf-8")


def start():
    for friend in tweepy.Cursor(api.friends).items():
        print(str(friend.screen_name) + " " + str(friend.id))
        get_all_tweets(friend.screen_name)


if __name__ == '__main__':
    start()
