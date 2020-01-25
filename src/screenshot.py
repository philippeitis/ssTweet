import requests
import json
import base64
import logging
logging.basicConfig(format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I_%M_%S %p',
                    filename='log_file',
                    level=logging.INFO)


def save_image(url, mode, name):
    api_url = 'https://www.googleapis.com/pagespeedonline/v4/runPagespeed?screenshot=true&strategy=' + mode + '&url=' + url
    data = requests.request(method = 'get', url = api_url).json()
    screenshot_data = data['screenshot']['data']
    decoded_screenshot_data = base64.b64decode(screenshot_data, altchars= '-_', validate=False)

    with open(name + '.jpg', 'wb') as file:
        file.write(decoded_screenshot_data)