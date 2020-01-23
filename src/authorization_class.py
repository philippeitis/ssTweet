from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import AuthorizedSession
from google.oauth2.credentials import Credentials
import logging

class Authorization:
    def __init__(self, scopes):
        self.scopes = scopes

    def prompt_user_for_credentials(self, scopes):
        flow = InstalledAppFlow.from_client_secrets_file('client_id.json', scopes)
        cred = flow.run_local_server(host='localhost', port=8080, 
                                        authorization_prompt_message='Please visit this URL to authorize this application: {url}', 
                                        success_message='The authentication flow has completed. You may close this window.', 
                                        open_browser=True)
        return cred
    
    def get_credentials(self, auth_file):
        cred = None
        if(auth_file):
            try:
                cred = Credentials.from_authorized_user_info(auth_file, self.scopes)
                return cred
            except ValueError as err:
                logging.error('the info (auth file) is not in the expected format: {}'.format(err))
                return None
        if(cred==None):
            cred = self.prompt_user_for_credentials(self.scopes)

    def get_auth_session(self, cred):
        session = AuthorizedSession(cred)
        return session