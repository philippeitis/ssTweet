import logging

class Media:
    def __init__(self, session):
        self.session = session
    
    album_url = 'https://photoslibrary.googleapis.com/v1/albums'
    upload_url = 'https://photoslibrary.googleapis.com/v1/uploads'
    media_items_url = 'https://photoslibrary.googleapis.com/v1/mediaItems:batchCreate'

    def get_albums(self, created_by_app = False):
        params = {
            'excludNonAppCreatedData': created_by_app
        }
        while True: 
            albums = self.session.get(self.album_url,params=params).json()
            # albums = self.session.request('GET','https://photoslibrary.googleapis.com/v1/albums').json()
            # albums = {'albums': [{'id': 'AJ8vYPyyd6apDnQRxe6F_OStKDwA_5jYpI5J6Rc9-EQYeSAKo8l6y1BLbSw-hZSgnXJxGvw4TIz2', 'title': 'ssTweet', 'productUrl': 'https://photos.google.com/lr/album/AJ8vYPyyd6apDnQRxe6F_OStKDwA_5jYpI5J6Rc9-EQYeSAKo8l6y1BLbSw-hZSgnXJxGvw4TIz2', 'isWriteable': True, 'coverPhotoBaseUrl': 'https://lh3.googleusercontent.com/lr/AGWb-e6yGsCfr5YaqQ0vhuJMz7yK_5K89EMLBZzFZxI-vBbFpjRfJdjfke0c1cVToeRpMaoBfqWr2owTb59u1gj94SgQ9W8KY6zJ2XGgORnNGeJUssq9dx8kLREaFgFip-_l2Q3pJ9OCZAJEVi0dL50gksJ3jUdNBAX5TSjZGeyvALz-aQNtjxmmnD3Mm6kgTVh7rSwaYPuA7AG2qN8oGioDO2wL6qgbFKx4rhKDvGzySdST6fo1BV7r2UA76yYHeUJ5flEUSiFmYxcsiQkHTExfWzVsG5jERlCqpWmzZb1ZIVV26QVV4aux1EZtUwveePIuY8hntKNLSBi3PTi27ahXGMm8VW8tL5B67NC7vY7YHJCxaPKg8bA2mlNA_hdRM315UqMsOHnrPq78NiLxuWMlGUcRVe8EoOuof9AIQAo9TDaJmzFliSjMDAFPWGfBsUJeQ5SWCfSQ-NcJH5J0x3ag-7NRPJ3j7Bru_O3eo7RkwvBtvM3_fu5nswHYQZeanCVgvv1qv1nMKYul1q6FI0lnvYXLXeZLHhXryhLN3xlwT0DaAj0XqVQEhrUdnJCtiXbN0aMy62n2lQYsXAkuTxzJpc_TbmqiLQ4C2ep4H0ajMhLwGGwR_WV9xgLyzMOFAQlg7usBmxx8QUJ_jWzEPpSh-l6NmAg8nBUTUwc2vzDrUBa6AwpvqsDwh3oHiT1ll2HeWDqPYFFj_p0SFvcXK0dHnd27M8-Xr4Yp3JflFuQq0DL6mESGlwq7XL_4gmPgzYqDathAJn61yEyHTN0lcPWBo03dgs5QLlMnQVqiHRhrGLH_XGP1cmtLdgw'}]} 
            logging.debug("response: {}".format(albums))
            if('albums' in albums):
                for album in albums['albums']:
                    yield album
                if('nextPageToken' in albums):
                    params['page_token'] = albums['nextPageToken']
                else:
                    return
            else:
                return
    
    def create_new_album_id(self, album_title):
        body = {
            'album': {
                'title': album_title
            }
        }
        album = self.session.post(self.album_url, body).json()
        if('id' in album):
            logging.info('created album: {}'.format(album_title))
            return album['id']
        else:
            logging.error('some error occured. could not create or find an existing album. response: {}'.format(album))
            return None

    def retrieve_album_id(self, album_title):
        for album in self.get_albums(True):
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
                body = {
                    'albumId': album_id,
                    'newMediaItms': [
                        {
                            'description':'automatically generated screenshot by your twitter bot',
                            'simpleMediaItem': {
                                'uploadToken': upload_token
                            }
                        }
                    ]
                }
                new_media_items_result = self.session.post(url=self.media_items_url, data=body)
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
            logging.info('Added {photo_name} to your album'.format(photo_name))
    else:
        logging.error('could not add your photo {photo_name} to the album. Here is the error message {message}'.format(photo_name=photo_name, message=response))


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