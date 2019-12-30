from __future__ import print_function
import pickle
import os.path
import yaml
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from os import path

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def calendar_config():
    '''
    Open a configuration file and read iframe,
    file with credentials for Calendar API and
    calendarID
    :return: List with iframe, api_credentials, calendarID strings
    :rtype: List
    '''
    if(path.exists("../config.yml")):
        with open('../config.yml', 'r') as file_config:
            content = yaml.load(file_config)
        if 'calendar' in content:
            iframe = content['calendar'].get('iframe', None)
            api_credentials = content['calendar'].get('api_credentials', None)
            calendarID = content['calendar'].get('calendarID', None)
            desks = content['calendar'].get('desks', None)
            api_credentials_path = os.path.join('../', api_credentials)
            return iframe, api_credentials_path, calendarID, desks
        else:
            return 4*[None]
    else:
        return 4*[None]


def initializeCalendar():
    """Initialize a Google Calendar API
    :return: Connection to Calendar
    :rtype: googleapiclient.discovery.Resource
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('../token.pickle'):
        with open('../token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            result = calendar_config()
            flow = InstalledAppFlow.from_client_secrets_file(
                result[1], SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('../token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    CAL = build('calendar', 'v3', credentials=creds)
    return CAL
