from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to the LinkedIn login page
driver.get('https://www.linkedin.com/login')

# Enter your email address and password
driver.find_element(By.ID, 'username').send_keys('#insert linkedin email address for login')
driver.find_element(By.ID,'password').send_keys('#insert linkedin password for login!')
# Submit the login form
driver.find_element(By.CSS_SELECTOR,'.login__form_action_container button').click()

# Enter desired linkedin profile url for scraping
profile_url = 'https://www.linkedin.com/in/profilelink/'
driver.get(profile_url)

# Get the page source
page_source = driver.page_source
# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(page_source, 'html.parser')
# Extract the name and headline
name = soup.find('h1', {'class': 'text-heading-xlarge inline t-24 v-align-middle break-words'}).text.strip()
# Print the extracted data
print('Name:', name)