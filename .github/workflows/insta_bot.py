from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

USERNAME = 'selenium.bot.demo1'  # Use a dummy account
PASSWORD = 'Selenium@12345'
TARGET_USER = 'cbitosc'

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Initialize driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def login():
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)

    user_input = driver.find_element(By.NAME, "username")
    pass_input = driver.find_element(By.NAME, "password")

    user_input.send_keys(USERNAME)
    pass_input.send_keys(PASSWORD)
    pass_input.send_keys(Keys.ENTER)
    time.sleep(8)

    # Dismiss "Save Info" popup
    try:
        not_now = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
        not_now.click()
        time.sleep(3)
    except:
        pass

def search_and_follow():
    driver.get(f"https://www.instagram.com/{TARGET_USER}/")
    time.sleep(6)

    try:
        follow_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Follow')]")
        follow_button.click()
        print("Followed the user.")
        time.sleep(3)
    except:
        print("Already following or button not found.")

def extract_data():
    time.sleep(3)
    
    # Bio text is inside the header section
    try:
        bio = driver.find_element(By.XPATH, "//div[@class='_aa_c']//div[@class='_aacl _aaco _aacw _aacx _aad7 _aade']").text
    except:
        bio = "Bio not found"

    # Stats: posts, followers, following
    try:
        stats = driver.find_elements(By.XPATH, "//ul[@class='_aa_7']/li/div/span")
        posts = stats[0].text
        followers = stats[1].get_attribute("title") or stats[1].text
        following = stats[2].text
    except:
        posts, followers, following = "N/A", "N/A", "N/A"

    with open("profile_info.txt", "w", encoding="utf-8") as f:
        f.write(f"Username: {TARGET_USER}\n")
        f.write(f"Bio: {bio}\n")
        f.write(f"Posts: {posts}\n")
        f.write(f"Followers: {followers}\n")
        f.write(f"Following: {following}\n")

    print("Profile data saved to profile_info.txt")

if __name__ == "__main__":
    login()
    search_and_follow()
    extract_data()
    driver.quit()
