import tweepy
import json

ckey = 'rTWMi8ejikhsyyBdaRbpytVEA'
csecret = "c180XPEpQTC9eu2k9xCRFvZgqUa2du9yKpnwae6f4GBbRbOcbs"
atoken = "794364093020913665-xe0uMfb4ypPAylCzcZrmumq54NTMEgg"
asecret = "lbcuN7e07kJkZxL7QzGoQVvm0JbO4vTovGDKkXa465QmS"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)


class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        data_json = json.loads(data)
        if "lang" in data_json and data_json["lang"] == "en" and "text" in data_json:
            text = data_json["text"].encode("utf-8")
            print(str(text))
        return True


def on_error(self, status):
    print(status)


if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    stream = tweepy.Stream(auth, l)

stream.filter(track=['egypt'])
