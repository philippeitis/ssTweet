from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import AuthorizedSession
from google.oauth2.credentials import Credentials
import logging


class Authorization:
    def __init__(self, scopes):
        self.scopes = scopes
    