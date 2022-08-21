import datetime
import tweepy
import os

creds = {"consumer_key": os.environ.get("TWITTER_API_KEY"),
         "consumer_secret": os.environ.get("TWITTER_API_SECRET"),
         "access_token": os.environ.get("TWITTER_ACCESS_TOKEN"),
         "access_token_secret": os.environ.get("TWITTER_ACCESS_TOKEN_SECRET"), }

client = tweepy.Client(
    **creds
)


def twitter_action():
    # code example
    now = datetime.datetime.now()
    thousandDaysFromNow = now + datetime.timedelta(days=1000)
    formattedDate = datetime.datetime.strftime(thousandDaysFromNow, "%m/%d/%Y")
    tweet = "today + 1000 days = {}".format(formattedDate)
    client.create_tweet(text=tweet)


if __name__ == "__main__":
    twitter_action()
