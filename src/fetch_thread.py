import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET


def get_api():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    return tweepy.API(auth, wait_on_rate_limit=True)


def get_tweet(url):
    tweet_id = url.split('/')[-1]
    api = get_api()
    return api.get_status(tweet_id)


def get_twitter_url(user_name, status_id):
    return "https://twitter.com/" + str(user_name) + "/status/" + str(status_id)


def update_urls(tweet, api):
    tweet_id = tweet.id
    user_name = tweet.user.screen_name
    max_id = None
    replies = tweepy.Cursor(
        api.search,
        q='to:{}'.format(user_name),
        since_id=tweet_id,
        max_id=max_id,
        tweet_mode='extended'
    ).items()

    urls = []
    for reply in replies:
        if reply.in_reply_to_status_id == tweet_id:
            urls.append(get_twitter_url(user_name, reply.id))
            try:
                urls.extend(update_urls(reply, api))
            except tweepy.TweepError:
                pass
    return urls
