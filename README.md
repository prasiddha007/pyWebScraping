## LinkedIn Profile Scraper

This Python script uses Selenium and Beautiful Soup to scrape a LinkedIn profile page for the name of the user.

### Script Explanation

1. **Imports**: The script imports necessary libraries for web automation (`webdriver` from `selenium`), managing Chrome WebDriver (`Service` from `selenium.webdriver.chrome.service` and `ChromeDriverManager` from `webdriver_manager.chrome`), selecting elements (`By` from `selenium.webdriver.common.by`), and parsing HTML (`BeautifulSoup` from `bs4`).

2. **WebDriver Setup**: It creates a Chrome WebDriver instance using `webdriver.Chrome` and `ChromeService` with `ChromeDriverManager().install()` to manage the Chrome driver.

3. **Login to LinkedIn**: The script navigates to the LinkedIn login page using `driver.get('https://www.linkedin.com/login')`, fills in the username and password fields with your LinkedIn credentials, and submits the login form.

4. **Scrape Profile**: It specifies the LinkedIn profile URL to scrape, opens the profile page, gets the page source, and parses it with Beautiful Soup to extract the name and headline of the user.

5. **Print Results**: The script prints the extracted name.

## Requirements

- [Python 3](https://www.python.org/downloads/)
- [Selenium](https://pypi.org/project/selenium/)
- [WebDriver Manager for Chrome](https://pypi.org/project/webdriver-manager/)
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)

## Installation

1. **Python**: If you don't have Python installed, download and install it from the [official Python website](https://www.python.org/downloads/). Make sure to select the appropriate installer for your operating system.

2. **Dependencies**: Install the required libraries using pip:

   ```bash
   pip install selenium webdriver_manager beautifulsoup4
   ```

## Usage

1. Enter your LinkedIn email address and password when prompted.
2. Replace `https://www.linkedin.com/in/profilelink/` with the URL of the LinkedIn profile you want to scrape.
3. Run the script:

```bash
python main.py
```

The script will open a Chrome browser, log in to LinkedIn, and scrape the specified profile for the name.
