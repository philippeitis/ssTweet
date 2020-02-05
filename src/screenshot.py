import requests
import json
import base64
import os
import logging
from fetch_thread import get_api, get_tweet, update_urls
logging.basicConfig(format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I_%M_%S %p',
                    filename='log_file',
                    level=logging.INFO)

def save_images(url):
    api = get_api()
    tweet = get_tweet(url)
    urls = [url]
    urls = update_urls(tweet, api, urls)
    count = 0
    for url in urls:
        save_image(url, "mobile", tweet.user.screen_name + str(count))
        count += 1
    photo_list = []
    for _count in range(count):
        photo_list.append(os.path.join(os.path.expanduser('~'),'ssTweet','images',tweet.user.screen_name+str(_count)+'.jpg'))
    return photo_list


def save_image(url, mode, name):
    api_url = 'https://www.googleapis.com/pagespeedonline/v4/runPagespeed?screenshot=true&strategy=' + mode + '&url=' + url
    data = requests.request(method = 'get', url = api_url).json()
    screenshot_data = data['screenshot']['data']
    decoded_screenshot_data = base64.b64decode(screenshot_data, altchars= '-_', validate=False)
    
    with open(os.path.join(os.path.expanduser('~'),'ssTweet','images',name+'.jpg'), "wb") as file:
        file.write(decoded_screenshot_data)
