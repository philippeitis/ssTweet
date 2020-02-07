from screenshot import save_images, delete_images
from upload import upload_image
import logging

logging.basicConfig(
    format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I_%M_%S %p',
    filename='log_file',
    level=logging.INFO
)


def main():
    url = 'https://twitter.com/lavishsaluja/status/1225356209915453440'
    photo_list = save_images(url)
    album_title = 'Safemaps'
    auth_file_name = None
    upload_image(photo_list, album_title, auth_file_name)
    delete_images(photo_list)


if __name__ == "__main__":
    main()
