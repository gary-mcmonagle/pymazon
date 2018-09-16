from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import json
import os

def create_service():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.OAuth2WebServerFlow(client_id=os.environ['gmail_client_id'],
                                   client_secret=os.environ['gmail_client_secret'],
                                   scope='https://mail.google.com/',
                                   redirect_uri="http://localhost")
        creds = tools.run_flow(flow, store)
    return build('gmail', 'v1', http=creds.authorize(Http()))