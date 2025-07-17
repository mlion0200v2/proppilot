# test_email_todo.py

from app.services.gmail_client import fetch_recent_emails
from app.services.todo_generator import generate_todo_from_email
from app.services.todo_storage import load_todos_for_today

emails = fetch_recent_emails(max_results=1)

if emails:
    email = emails[0]
    print("📬 Email Subject:", email['subject'])
    print("📨 From:", email['from'])
    print("📝 Generated ToDo:")
    print(generate_todo_from_email(email['body']))
else:
    print("⚠️ No recent emails found.")

today_todos = load_todos_for_today()
print("\n📅 Today's ToDos:")
for todo in today_todos:
    print(f"- {todo['task']} (Due: {todo['due']})")