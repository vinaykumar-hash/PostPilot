# LinkedIn Post Scraper

Automatically scrape **freelancing and job opportunity posts** from LinkedIn and **add them to Google Tasks** — complete with a next step to apply — using **Google’s Gemini AI** for intelligent task descriptions.

---

## Features

-  Scrapes freelancing / hiring posts from LinkedIn  
-  Uses Gemini AI to summarize and extract key details  
-  Automatically creates Google Tasks with apply instructions  
-  Runs in Chromium via Playwright  
-  Secure authentication using OAuth tokens  

---

## ⚙️ Setup

### 1️⃣ Clone the project

```bash
git clone https://github.com/vinaykumar-hash/LinkedIn-Post-Scraper-.git
cd LinkedIn_Posttool
```

---

### 2️⃣ Install dependencies using **uv**

> 🧠 Note: You need to have [uv](https://docs.astral.sh/uv/) installed.

```bash
uv sync
uv add google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

---

### 3️⃣ Set up Google credentials

1. Go to the **Google Cloud Console** → create a new project  
2. Enable the **Google Tasks API**  
3. Create **OAuth 2.0 credentials**  
4. Download your `credentials.json` and place it in the **root directory** of the project  

---

### 4️⃣ Authenticate with Google Cloud CLI

```bash
gcloud auth application-default login
```

---

### 5️⃣ Add your environment variables

Create a `.env` file in the root directory and add:

```bash
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
```

---

### 6️⃣ Start the program

```bash
python main.py
```

✅ The script will:
- Open a Chromium browser window  
- Ask you to log in to LinkedIn (only once)  
- Scrape freelancing posts  
- Use Gemini AI to extract key info  
- Add the details automatically to your Google Tasks  

---

## 🧠 Customize your search

You can modify the search query in `main.py`:

```python
scrape_linkedin_posts('"freelance project" OR "looking for freelancer" OR "hiring remote"')
```

---

## 📦 Folder Structure

```
LinkedIn_Posttool/
│
├── main.py
├── agent.py
├── schema.py
├── Prompt.py
├── Googletask.py
├── credentials.json       # (your OAuth credentials)
├── token.json             # (auto-generated)
├── .env
└── .gitignore
```

---

## 🧰 Tech Stack

- **Python** 🐍  
- **Playwright** → for LinkedIn scraping  
- **BeautifulSoup4** → for HTML parsing  
- **LangChain + Gemini** → for AI-based data extraction  
- **Google Tasks API** → for automation  

---

## ⚠️ Notes

- Do **not commit** your `credentials.json` or `token.json` files to GitHub.  
- They contain sensitive OAuth credentials.  
- `.gitignore` already includes them by default.

---

## ✨ Example Output

```
[Task created] : LinkedIn Application -> Freelance UI/UX Designer
```

---

## 💡 Made With

❤️ by [Vinay Kumar](https://github.com/vinaykumar-hash)  
🧠 Powered by **Gemini AI**, **Playwright**, and **Google Tasks API**
