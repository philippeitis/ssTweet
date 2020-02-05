import tweepy
import sys
sys.path.insert(1, '/Users/lavishsaluja/credentials')
from twitter_credentials import consumer_key,consumer_secret,access_key,access_secret

def get_api():
    auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def get_tweet(url):
    tweet_id = url.split('/')[-1]
    api = get_api()
    tweet = api.get_status(tweet_id)
    return tweet

def get_twitter_url(user_name, status_id):
    return "https://twitter.com/" + str(user_name) + "/status/" + str(status_id)

def update_urls(tweet, api, urls):
    tweet_id = tweet.id
    user_name = tweet.user.screen_name
    max_id = None
    replies = tweepy.Cursor(api.search, q='to:{}'.format(user_name),
                                since_id=tweet_id, max_id=max_id, tweet_mode='extended').items()
    
    for reply in replies:
        if(reply.in_reply_to_status_id == tweet_id):
            urls.append(get_twitter_url(user_name, reply.id))
            try:
                for reply_to_reply in update_urls(reply, api, urls):
                    pass
            except Exception:
                pass
        max_id = reply.id
    return urls