#👤 Author
Shivam Kumar
Final Year, IIIT Allahabad

---

# 🧠 Reddit-Based User Persona Generator

This project builds a user persona by analyzing Reddit user activity (posts and comments) using LLMs like OpenAI GPT. The generated persona includes motivations, frustrations, habits, goals, and inferred traits — **with proper citations**.

---

## 📌 Features

- ✅ Scrapes Reddit user data via PRAW (posts + comments)
- ✅ Cleans and organizes content
- ✅ Uses LLM (OpenAI GPT) to generate user personas
- ✅ Adds citation icons (🔗) for each insight from Reddit source
- ✅ Simple interface using Streamlit
- ✅ Supports any Reddit user profile link
- ✅ Sample personas provided

## Tech Stack
-Python,
Streamlit,
Langchain + LLM,
PRAW (Python Reddit API Wrapper),
dotenv

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/BeyondChats-Assignment.git
cd BeyondChats-Assignment

```
### 2.Create & Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate

```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
---
## 4. Add API Secrets
OPENAI_API_KEY = "your-openai-api-key"
REDDIT_CLIENT_ID = "your-reddit-client-id"
REDDIT_CLIENT_SECRET = "your-reddit-client-secret"
REDDIT_USER_AGENT = "your-app-name"
---

### Run the Application
```bash
streamlit run app.py
```
---
### Enter a Reddit user profile URL like:
https://www.reddit.com/user/kojied/
---

