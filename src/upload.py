from authorization_class import Authorization
from media_class import Media
import logging

logging.basicConfig(
	format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
	datefmt='%m/%d/%Y %I_%M_%S %p',
	filename='log_file',
	level=logging.INFO
)


def upload_image(photo_list, album_title, auth_file_name):
	scopes = ['https://www.googleapis.com/auth/photoslibrary', 'https://www.googleapis.com/auth/photoslibrary.sharing']
	auth_object = Authorization(scopes)
	cred = auth_object.get_credentials(auth_file_name)

	session = auth_object.get_auth_session(cred)
	media_object = Media(session)
	media_object.upload_photos(photo_list, album_title)
