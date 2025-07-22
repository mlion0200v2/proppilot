# app/services/gmail_client.py

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
import email
from pathlib import Path

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
CREDENTIALS_FILE = Path("credentials.json")
TOKEN_FILE = Path("token.json")

def get_service():
    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
        creds = flow.run_local_server(
            port=8080,
            access_type='offline',
            include_granted_scopes='true'
        )
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def fetch_recent_emails(max_results=5):
    service = get_service()

    # Query to fetch emails from a specific sender
    query = 'list: Luxmore'
    # query = 'from: luxmoreacct@gmail.com'
    results = service.users().messages().list(
        userId='me', 
        labelIds=['INBOX'], 
        q=query,
        maxResults=max_results
    ).execute()
    messages = results.get('messages', [])

    emails = []
    for msg in messages:
        txt = service.users().messages().get(userId='me', id=msg['id'], format='raw').execute()
        raw_data = base64.urlsafe_b64decode(txt['raw'].encode('ASCII'))
        mime_msg = email.message_from_bytes(raw_data)

        emails.append({
            'subject': mime_msg['Subject'],
            'from': mime_msg['From'],
            'date': mime_msg['Date'],
            'body': get_body(mime_msg)
        })
    return emails

def get_body(mime_msg):
    if mime_msg.is_multipart():
        for part in mime_msg.walk():
            if part.get_content_type() == 'text/plain':
                return part.get_payload(decode=True).decode()
    else:
        return mime_msg.get_payload(decode=True).decode()