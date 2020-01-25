import logging
import json
logging.basicConfig(format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I_%M_%S %p',
                    filename='log_file',
                    level=logging.INFO)

class Media:
    def __init__(self, session):
        self.session = session
    

    album_url = 'https://photoslibrary.googleapis.com/v1/albums'
    upload_url = 'https://photoslibrary.googleapis.com/v1/uploads'
    media_items_url = 'https://photoslibrary.googleapis.com/v1/mediaItems:batchCreate'
    

    def get_albums(self, created_by_app=False):
        params = {
                'excludeNonAppCreatedData': created_by_app
        }
        while True:
            albums = self.session.get(self.album_url, params=params).json()
            logging.debug("response: {}".format(albums))
            if 'albums' in albums:
                for album in albums["albums"]:
                    yield album
                if 'nextPageToken' in albums:
                    params["pageToken"] = albums["nextPageToken"]
                else:
                    return
            else:
                return
    

    def create_new_album_id(self, album_title):
        body = json.dumps({
            'album': {
                'title': album_title
            }
        })
        album = self.session.post(self.album_url, body).json()
        if('id' in album):
            logging.info('created album: {}'.format(album_title))
            return album['id']
        else:
            logging.error('some error occured. could not create or find an existing album. response: {}'.format(album))
            return None


    def retrieve_album_id(self, album_title):
        for album in self.get_albums():
            if(album['title'].lower() == album_title.lower()):
                logging.info("existing album: {}".format(album_title))
                return album['id']

        return self.create_new_album_id(album_title)

    
    def upload_photos(self, photo_list, album_title):
        album_id = self.retrieve_album_id(album_title)
        if(album_title and not album_id):
            logging.critical('upload interrupted. could  not verify album_id: {album_id} or album_title: {album_title}'.format(album_id=album_id, album_title=album_title))
            return None
        
        self.session.headers['Content-type']= 'application/octet-stream'
        self.session.headers['X-Goog-Upload-Protocol']= 'raw'

        for photo_name in photo_list:
            bytes = convert_image_to_bytes(photo_name)
            if(bytes == None):
                continue
            self.session.headers['X-Goog-Upload-File-Name'] = photo_name
            upload_token = self.session.post(self.upload_url, bytes)
            if(verify_upload_token(upload_token)):
                body = json.dumps({"albumId":album_id, "newMediaItems":[{"description":"","simpleMediaItem":{"uploadToken":upload_token.content.decode()}}]}, indent=4)
                new_media_items_result = self.session.post(url=self.media_items_url, data=body).json()
                log_upload_activity(new_media_items_result, photo_name)
        try:
            del(session.headers['Content-type'])
            del(session.headers['X-Goog-Upload-Protocol'])
            del(session.headers['X-Goog-Upload-File-Name'])
        except:
            pass


# helper functions for the class
def log_upload_activity(response, photo_name):
    logging.debug('response: {0}'.format(response))
    if('newMediaItemResults' in response):
        status = response['newMediaItemResults'][0]['status']
        if(status.get('code') and (status.get('code') > 0)):
            logging.error('could not add {photo_name} to the album. message: {message}'.format(photo_name=photo_name, message=status['message']))
        else:
            logging.info('Added {photo_name} to your album'.format(photo_name=photo_name))
    else:
        logging.error('could not add your photo to the album you requested')


def verify_upload_token(upload_token):
    if(upload_token.status_code==200 and upload_token.content):
        return True
    else:
        logging.error('Couldnot generate valid upload token. Check if the file has already been added. upload_token: {}'.format(upload_token))
        return False


def convert_image_to_bytes(photo_name):
    try:
        file = open(photo_name, 'rb')
        bytes = file.read()
        return bytes
    except OSError as err:
        logging.error('error: {error} reaised while reading the {photo_name} file'.format(error=err,photo_name=photo_name))
        return None