from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
from schema import *
from agent import LLMagent as agent
from Prompt import ExtractTaskLlm

def scrape_linkedin_posts(query):
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir="./linkedin_session", headless=False
        )
        page = browser.new_page()

        url = f"https://www.linkedin.com/search/results/content/?keywords={query.replace(' ', '%20')}"
        page.goto(url)

        page.wait_for_selector("div.occludable-update", timeout=20000)
        for i in range(6):
            page.mouse.wheel(0, 3000)
            time.sleep(2)

        html = page.content()
        soup = BeautifulSoup(html, "html.parser")

        for post in soup.find_all("div", class_="feed-shared-update-v2"):
            # Extract data-urn
            data_urn = post.get("data-urn")
            post_url = f"https://www.linkedin.com/feed/update/{data_urn}" if data_urn else "URL not found"

            # Extract text
            text_div = post.find("div", class_="update-components-text")
            text = text_div.get_text(separator="\n", strip=True) if text_div else "No text found"

            # Extract author
            author_tag = post.find("span", class_="update-components-actor__title")
            author_name = author_tag.get_text(strip=True) if author_tag else "Author not found"
            print(agent(ExtractTaskLlm(url=post_url, text=text)))
            # Filter for job/freelance keywords
            # if any(k in text.lower() for k in ["hire", "freelance", "project", "looking for", "remote"]):
            #     print(f"Author: {author_name}")
            #     print(f"URL: {post_url}")
            #     print(f"Text: {text[:300]}...\n")

        input("Press Enter to close the browser...")
        browser.close()

# Example usage
scrape_linkedin_posts("freelance developer")
