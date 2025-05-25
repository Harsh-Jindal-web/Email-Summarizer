# Email Summarizer

A Python application that listens for new unread Gmail emails, summarizes their content using Groq’s Gemini API, and logs the summary along with email details to a Google Sheet.

---

## Features

- Authenticate with Gmail and Google Sheets APIs  
- Fetch unread emails from Gmail  
- Extract sender, subject, and email body  
- Summarize email content using Groq Gemini API  
- Log email details and summaries to Google Sheets  
- Mark processed emails as read  
- Runs continuously, polling every 10 seconds  

---

## Prerequisites

- Python 3.7+  
- Google Cloud Platform (GCP) project with Gmail and Sheets APIs enabled  
- OAuth 2.0 Client Credentials JSON (`credentials.json`)  
- A Google Sheet to log summaries (Spreadsheet ID)  
- Groq API key with access to Gemini model  
- `.env` file for environment variables  

---

## Setup Instructions

### 1. Clone repository

```bash
git clone https://github.com/Harsh-Jindal-web/Email-Summarizer.git
cd email_summarizer
```

### 2. Create & activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate      # Linux/macOS
# On Windows:
# venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Enable Gmail and Sheets APIs in Google Cloud Console

- Enable **Gmail API** and **Google Sheets API** in your Google Cloud project.  
- Create **OAuth 2.0 Client IDs** credentials for a **Desktop app**.  
- Download the `credentials.json` file and place it in the project root directory.  


### 5. Configure OAuth Consent Screen and Add Test Users

- Go to **APIs & Services > OAuth consent screen** in Google Cloud Console.  
- Set **Publishing status** to **Testing**.  
- Add test user emails — these are the Google accounts that will be authorized to use your app.  
- Save the changes.  

> Note: Only test users can authenticate while the app is in testing mode.


### 6. Set up Google Sheet

- Create a Google Sheet to log email summaries.  
- Note the **Spreadsheet ID** from the URL (the long string between `/d/` and `/edit`).  
    ```
    https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit
    ```
- Add the following headers to the first row:
  ```
  Sender | Subject | Summary | Action Items | Timestamp
  ```
- Share the Google Sheet with your Google account email if required for access.  



### 7. Get Groq API Key

- Sign up or log in at [Groq Console](https://console.groq.com).  
- Navigate to **Settings > API Keys**.  
- Create a new API key and copy it.  
- Ensure your API key has access to the Gemini model (`gemma2-9b-it` or your chosen model).  

---

### 8. Create .env file

- Add the following environment variables in a .env file at your project root:
   ```
   SPREDSHEET_ID=your_google_sheet_id_here
   GROQ_API_KEY=your_groq_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
- Replace with your actual Google Sheet ID and Groq API key.

## Usage

1. Run the application:
```
python main.py
```

- On first run, a browser window will open for Google OAuth authentication (for test users).
- If it doesn’t open automatically, copy-paste the provided URL into a browser manually.

2. Authenticate via the browser popup (for Gmail and Sheets access)

3. The script will:
   - Fetch unread emails every 10 seconds
   - Summarize them using **Gemma2-9b-it**
   - Log results into your Google Sheet

## 🤔 How to contribute

- Fork this repository;
- Create a branch with your feature: `git checkout -b my-feature`;
- Commit your changes: `git commit -m "feat: my new feature"`;
- Push to your branch: `git push origin my-feature`.

Once your pull request has been merged, you can delete your branch.

## 📜 License
This project is licensed under the MIT License.