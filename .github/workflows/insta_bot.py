from playwright.sync_api import sync_playwright
import time

USERNAME = "selenium.bot.demo1"
PASSWORD = "Selenium@12345"
TARGET_USER = "cbitosc"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.instagram.com/accounts/login/")
    page.wait_for_timeout(5000)
    page.fill("input[name='username']", USERNAME)
    page.fill("input[name='password']", PASSWORD)
    page.press("input[name='password']", "Enter")
    page.wait_for_timeout(8000)
    try:
        page.click("text=Not Now")
        page.wait_for_timeout(2000)
    except:
        pass
    page.goto(f"https://www.instagram.com/{TARGET_USER}/")
    page.wait_for_timeout(5000)
    try:
        btn = page.locator("button", has_text="Follow")
        if btn.count():
            btn.first.click()
            print("✅ Followed")
            time.sleep(2)
    except:
        print("⚠️ Already following/not found")
    stats = page.locator("header ul li")
    posts = stats.nth(0).text_content().split()[0] if stats.count() > 0 else "N/A"
    followers = stats.nth(1).text_content().split()[0] if stats.count() > 1 else "N/A"
    following = stats.nth(2).text_content().split()[0] if stats.count() > 2 else "N/A"
    try:
        bio = page.locator("header section div:nth-child(2)").text_content()
    except:
        bio = "Bio not found"
    with open("profile_info.txt", "w", encoding="utf-8") as f:
        f.write(f"Username: {TARGET_USER}\nBio: {bio}\nPosts: {posts}\nFollowers: {followers}\nFollowing: {following}\n")
    print("✅ Saved profile_info.txt")
    browser.close()
