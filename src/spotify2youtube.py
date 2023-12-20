import time

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from creds import spotify
from browser_utils import BrowserUtils
from locators import SpotifyLocators

if __name__ == "__main__":
    driver: WebDriver = webdriver.Firefox()
    driver.get("https://open.spotify.com/")
    browser_utils = BrowserUtils(driver=driver)

    try:
        browser_utils.wait_until_element_is_clickable(SpotifyLocators.BTN_LOGIN)
        browser_utils.click_element(SpotifyLocators.BTN_LOGIN)

        browser_utils.wait_until_element_is_clickable(SpotifyLocators.INPUT_USERNAME)
        browser_utils.wait_until_element_is_clickable(SpotifyLocators.INPUT_PASSWORD)

        browser_utils.send_keys(SpotifyLocators.INPUT_USERNAME, spotify.get("user"))
        browser_utils.send_keys(SpotifyLocators.INPUT_PASSWORD, spotify.get("password"))

        time.sleep(10)
    except Exception as e:
        print(f"There was an unexpected error :(\n\n{e}")
    finally:
        driver.quit()
