import os.path
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def main():
    creds = None
    if os.path.exists('token.json'):
        flow = InstalledAppFlow.from_client_secrets_file("token.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
        return Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        print('Credentials not present')
        sys.exit(1)

def get_creds():
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        return creds

# main()

    
