from django.conf import settings

import datetime
from googleapiclient.discovery import build
from google.oauth2 import service_account

import pytz
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = ['https://www.googleapis.com/auth/calendar']


credentials = pickle.load(open('token.pkl','rb'))



def calenderEvent(email, required_speciality, start_time, end_time):
    service = build("calendar", "v3", credentials=credentials)
    timezone = 'Asia/Kathmandu'
    print(start_time.isoformat())
    print(end_time.isoformat())
    
    event ={
        "summary": required_speciality,
        "start": {
            "dateTime":start_time.isoformat(),
            "timeZone": timezone,
            },
        "end": {
            "dateTime":end_time.isoformat(),
            "timeZone":timezone,
            },
        "attendees":[{"email":email}],
    }

    service.events().insert(calendarId='primary', body=event).execute()