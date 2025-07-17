import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.todo_storage import load_todos_for_today
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

todos = load_todos_for_today()

summary_text = "Today's ToDos:\n\n"
if todos:
    for todo in todos:
        summary_text += f"- {todo['task']} (Due: {todo['due']})\n"
else:
    summary_text += "✅ No tasks due today!"

def send_email_reminder(subject, body, to_email):
    from_email = "birchwoodrealestategroup@gmail.com"  # ⚠️ 你的 Gmail 地址
    app_password = "uftqvmiisojakcwv"  # ⚠️ 你的 Gmail 应用密码
    # app_password = "xmhm gmsq xcbm chni"  # vancouver.simoneliu@gmail.com

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_email, app_password)
        server.send_message(msg)

send_email_reminder(
    subject=f"📋 Your PropPilot ToDos for {datetime.today().date()}",
    body=summary_text,
    to_email="vancouver.simoneliu@gmail.com"  # 可发自己，也可发他人
)

def generate_summary():
    todos = load_todos_for_today()
    if not todos:
        return "✅ No tasks due today. You're all caught up!"

    summary_lines = ["📋 Today's Tasks:"]
    for i, todo in enumerate(todos, 1):
        summary_lines.append(f"{i}. {todo['task']} (Due: {todo['due']})")
    return "\n".join(summary_lines)

if __name__ == "__main__":
    print(generate_summary())