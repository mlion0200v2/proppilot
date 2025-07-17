# 🏠 PropPilot: AI Assistant for Landlords & Property Managers

**PropPilot** is an AI-powered assistant that helps landlords and property managers automate daily tasks like parsing emails, generating to-do lists, and sending reminders — freeing up time for what truly matters.

---

## 🚀 Features (MVP)

| Category       | Feature                         | Description |
| -------------- | ------------------------------- | ----------- |
| 📬 Email Parser | ✅ Parse Gmail threads to extract tenant requests into to-do tasks | Auto-summarize emails and detect actionable items using GPT |
| 📋 Task Manager | ✅ Save & edit todos via Streamlit dashboard | Todos are saved locally in JSON, easy to review or check off |
| 📧 Reminder     | ✅ Email daily task summaries at 8 AM | Email reminders keep you on top of your property management |

---

## 🔧 Tech Stack

- Python 3.10+
- OpenAI GPT-4o API
- Google Gmail API (OAuth)
- Streamlit
- Miniconda (for environment isolation)

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/PropPilot.git
cd PropPilot
```

### 2. Create a Conda environment

```bash
conda create -n proppilot python=3.10
conda activate proppilot
```

### 3. Install required Python packages
```bash
pip install -r requirements.txt
```

### 4. Set up Gmail API credentials
1. Visit the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project and enable **Gmail API**.
3. Configure an **OAuth 2.0 Client ID**:
   - Set the application type to **Desktop App**.
   - Under **OAuth Consent Screen**, add your Gmail address as a **Test User**.
4. Download the `credentials.json` file and place it in the root directory of your project.

> 💡 On first run, your script will open a browser to complete the OAuth authentication and generate a `token.json`.

---

### 🛠 Troubleshooting

#### ❌ `redirect_uri_mismatch`
Make sure you selected **Desktop App** as the OAuth Client type. This automatically uses the correct redirect URI:  
`http://localhost:8080/`

#### ❌ `access_denied`
Ensure the Gmail address you're logging in with is **listed under Test Users** in the OAuth consent screen.

#### ❌ `403 - Gmail API has not been used...`
Enable the Gmail API in your project and wait 1–2 minutes before retrying:  
[Enable Gmail API](https://console.developers.google.com/apis/api/gmail.googleapis.com/overview)

---