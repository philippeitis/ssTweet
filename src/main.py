from screenshot import save_image
from upload import upload_image

def main():
    url='https://twitter.com/lavishsaluja/status/1219836535849111552'
    mode='mobile'
    filename='sample_tweet'
    photo_list=[filename+'.jpg']
    album_title='ssTweet'
    auth_file_name=None
    # auth_file_name='client_id.json'

    save_image(url, mode, filename)
    upload_image(photo_list, album_title, auth_file_name)

if (__name__ == "__main__"):
    main()