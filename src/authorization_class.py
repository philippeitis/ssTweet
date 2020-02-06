from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import AuthorizedSession
from google.oauth2.credentials import Credentials
import logging

logging.basicConfig(
    format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I_%M_%S %p',
    filename='log_file',
    level=logging.INFO
)


class Authorization:
    def __init__(self, scopes):
        self.scopes = scopes

    def prompt_user_for_credentials(self):
        flow = InstalledAppFlow.from_client_secrets_file(
            '/Users/lavishsaluja/credentials/photos_cred.json',
            scopes=self.scopes
        )

        logging.info('Prompting user to login to get their credentials for the defined scopes')

        return flow.run_local_server(
            host='localhost',
            port=8080,
            authorization_prompt_message='',
            success_message="Thank you for verification. You may close this window now.\n\n\n\n\n"
                            "If you're curious to know what happened: The authentication has been completed"
                            " and we have got your credentials, if we get them right, we'll be uploading"
                            " the screenshots of your tweets to your Photos account as a next step. Try"
                            " refreshing your Photos app.",
            open_browser=True
        )

    def get_credentials(self, auth_file):
        if auth_file:
            try:
                return Credentials.from_authorized_user_file(auth_file)
            except ValueError as err:
                logging.error('the info (auth file) is not in the expected format: {}'.format(err))
                raise err
        return self.prompt_user_for_credentials()

    def get_auth_session(self, cred):
        return AuthorizedSession(cred)
