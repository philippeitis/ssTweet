from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import AuthorizedSession
from google.oauth2.credentials import Credentials
import json
import logging
logging.basicConfig(format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I_%M_%S %p',
                    filename='log_file',
                    level=logging.INFO)


class Authorization:
    def __init__(self, scopes):
        self.scopes = scopes


    def prompt_user_for_credentials(self, scopes):
        flow = InstalledAppFlow.from_client_secrets_file(
            '/Users/lavishsaluja/credentials/photos_cred.json',
            scopes=scopes)
        logging.info('Prompting user to login to get their credentials for the defined scopes')
        cred = flow.run_local_server(host='localhost', port=8080, 
                                        authorization_prompt_message='', 
                                        success_message="Thank you for verification. You may close this window now.\n\n\n\n\nIf you're curious to know what happened: The authentication has been completed and we have got your credentials, if we get them right, we'll be uploading the screenshots of your tweets to your Photos account as a next step. Try refreshing your Photos app.", 
                                        open_browser=True)
        return cred
    

    def get_credentials(self, auth_file):
        cred = None
        if(auth_file):
            try:
                cred = Credentials.from_authorized_user_file(auth_file, self.scopes)
                return cred
            except ValueError as err:
                logging.error('the info (auth file) is not in the expected format: {}'.format(err))
                return None
        if(cred==None):
            cred = self.prompt_user_for_credentials(self.scopes)
            return cred


    def get_auth_session(self, cred):
        session = AuthorizedSession(cred)
        return session