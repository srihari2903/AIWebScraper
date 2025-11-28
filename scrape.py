from selenium.webdriver.safari.webdriver import WebDriver as Safari
from selenium.webdriver.safari.options import Options
import time

def scrape_website(website):
    print("Launching safari browser...")

    '''chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service = Service(chrome_driver_path), options= options)'''

    options = Options()
    options.use_technology_preview = False

    driver = Safari(options = options)

    try:
        driver.get(website)
        print("Page Loaded...")
        html = driver.page_source
        time.sleep(5)

        return html
    finally:
        driver.quit()