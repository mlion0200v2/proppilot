# app/services/gmail_client.py

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
import email

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_service():
    creds = None
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=8080)
    return build('gmail', 'v1', credentials=creds)

def fetch_recent_emails(max_results=5):
    service = get_service()

    # Query to fetch emails from a specific sender
    query = 'from: pinnacleinternational.ca'
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