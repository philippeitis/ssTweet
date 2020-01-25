from screenshot import save_image
from upload import upload_image
import os
import logging
logging.basicConfig(format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I_%M_%S %p',
                    filename='log_file',
                    level=logging.INFO)


def main():
    logging.info('\n\n')
    url='https://twitter.com/j_asminewang/status/1220822304231493633'
    mode='mobile'
    filename='sample_tweet'
    photo_list=[filename+'.jpg']
    album_title='TweetBot'
    # auth_file_name=None
    auth_file_name='/Users/lavishsaluja/client_id.json'
    save_image(url, mode, filename)
    upload_image(photo_list, album_title, auth_file_name)


if (__name__ == "__main__"):
    main()