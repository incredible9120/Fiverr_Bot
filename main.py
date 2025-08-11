from seleniumwire import webdriver  # type: ignore
from selenium.webdriver.chrome.service import Service  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore
from selenium.webdriver.chrome.options import Options  # type: ignore
from selenium.webdriver.support import expected_conditions as EC  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
import time
import os
from dotenv import load_dotenv  # type: ignore


def main():
    load_dotenv()
    username = os.getenv("PROXY_USERNAME")
    password = os.getenv("PROXY_PASSWORD")
    host = os.getenv("PROXY_HOST")
    port = os.getenv("PROXY_PORT")

    proxy_url = f"http://{username}:{password}@{host}:{port}"
    # set selenium-wire options to use the proxy
    # seleniumwire_options = {"proxy": {"http": proxy_url, "https": proxy_url}}

    # set Chrome options to run in headless mode
    options = Options()
    options.add_argument("--window-size=1920,1080")

    # initialize the Chrome driver with service, selenium-wire options, and chrome options
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        # seleniumwire_options=seleniumwire_options,
        options=options,
    )

    try:
        driver.get("https://www.fiverr.com")

        # Take screenshot of initial page

        print("Waiting for button element...")
        element = WebDriverWait(driver, 45).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "display-from-sm"))
        )
        element.click()

        time.sleep(20000)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
