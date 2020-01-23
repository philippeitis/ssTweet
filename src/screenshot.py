import requests
import json
import base64

def save_image(url, mode, name):
    api_url = 'https://www.googleapis.com/pagespeedonline/v4/runPagespeed?screenshot=true&strategy=' + mode + '&url=' + url
    resp = requests.request(method = 'get', url = api_url)
    data = resp.json()
    screenshot_data = data['screenshot']['data']
    decoded_screenshot_data = base64.b64decode(screenshot_data, altchars= '-_', validate=False)

    with open(name + '.jpg', 'wb') as file:
        file.write(decoded_screenshot_data)