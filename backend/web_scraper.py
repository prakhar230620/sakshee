from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


def scrape_content(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    # Wait for dynamic content to load
    time.sleep(5)

    page_source = driver.page_source
    driver.quit()

    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract text content from the page
    content = ' '.join([p.text for p in soup.find_all('p')])

    return content