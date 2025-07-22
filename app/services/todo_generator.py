# app/services/todo_generator.py

from openai import OpenAI
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def generate_todo_from_email(email_body: str) -> str:
    prompt = f"""
Summerize the following email thread and extract any actionable tasks.
You are a property management assistant. Read the email content below and determine if any tasks need to be performed.
If there are tasks, output the ToDo content and deadline (if determinable)
in the following format:
- Email Subject: xxx
- From: xxx
- Todo: xxx
- Deadline: yyyy-mm-dd

Email content：
{email_body}
"""

    response = client.chat.completions.create(
        # model="gpt-3.5-turbo",
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates actionable tasks from emails."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return {
        "task": response.choices[0].message.content.strip(),
        "due": (datetime.now() + timedelta(days=2)).date().isoformat(),
        "done": False
    }