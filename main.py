from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Replace with your LinkedIn account credentials
USERNAME=input("Enter your linkedin email address: ")
PASSWORD=input("Enter your linkedin password: ")
profile_url=input("Enter the desired linkedin profile url for scraping: ")

# URL of the LinkedIn login page
LOGIN_URL = 'https://www.linkedin.com/login'

# Function to log in to LinkedIn
def login(driver):


    driver.get(LOGIN_URL)
    time.sleep(1)

    driver.find_element(By.ID, 'username').send_keys(USERNAME)
    driver.find_element(By.ID,'password').send_keys(PASSWORD)

    driver.find_element(By.CSS_SELECTOR,'.login__form_action_container button').click()

    time.sleep(1)

    # desired linkedin profile url for scraping
    driver.get(profile_url)

    # Get the page source
    page_source = driver.page_source

    # Parse the HTML using Beautiful Soup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract the name and headline
    name = soup.find('h1', {'class': 'text-heading-xlarge inline t-24 v-align-middle break-words'}).text.strip()
    time.sleep(2)

    # Print the extracted data
    print('Name:', name)

# Main script
if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')  # Maximize the browser window
    driver = webdriver.Chrome(options=options)

    try:
        login(driver)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the browser window
        driver.quit()