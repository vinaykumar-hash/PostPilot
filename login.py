from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    user_data_dir = "./linkedin_session" 
    browser = p.chromium.launch_persistent_context(user_data_dir, headless=False)
    page = browser.new_page()
    page.goto("https://www.linkedin.com/login")

    print("🔐 Please log in to LinkedIn manually in the opened browser window.")
    input("✅ Press Enter after you’ve successfully logged in and can see your feed...")

    browser.close()
    print("🎉 Session saved. You won’t need to log in again next time!")
