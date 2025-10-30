from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/tasks"]

def createTask(task : dict):
    
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request()) 
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("tasks", "v1", credentials=creds)

    result = service.tasks().insert(tasklist="@default", body=task).execute()
    print(f"[Task created] : {result['title']}")
# createTask({
#     "title" : "Message freelancer on LinkedIn",
#     "notes" : "Follow up on collaboration post found by scraper."

# })