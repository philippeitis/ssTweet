from screenshot import save_images
from upload import upload_image
import os
import logging
logging.basicConfig(format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I_%M_%S %p',
                    filename='log_file',
                    level=logging.INFO)


def main():
    url='https://twitter.com/neilkakkar/status/1224738075940675584'
    photo_list = save_images(url)
    album_title = 'TweetBot'
    auth_file_name = None
    # auth_file_name='/Users/lavishsaluja/credentials/photos_cred.json'
    upload_image(photo_list, album_title, auth_file_name)
    # os.remove(filename+'.jpg')
    


if (__name__ == "__main__"):
    main()