import time

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from creds import spotify
from browser_utils import BrowserUtils
from locators import SpotifyLocators
from utils import SpotifyUtils

if __name__ == "__main__":
    driver: WebDriver = webdriver.Firefox()
    driver.get("https://open.spotify.com/")
    browser_utils = BrowserUtils(driver=driver)

    try:
        # Step I: perform Spotify login
        browser_utils.wait_until_element_is_clickable(SpotifyLocators.BTN_LOGIN)
        browser_utils.click_element(SpotifyLocators.BTN_LOGIN)

        browser_utils.wait_until_element_is_clickable(SpotifyLocators.INPUT_USERNAME)
        browser_utils.wait_until_element_is_clickable(SpotifyLocators.INPUT_PASSWORD)
        browser_utils.wait_until_element_is_clickable(SpotifyLocators.SUBMIT_LOGIN)

        browser_utils.send_keys(SpotifyLocators.INPUT_USERNAME, spotify.get("user"))
        browser_utils.send_keys(SpotifyLocators.INPUT_PASSWORD, spotify.get("password"))
        browser_utils.click_element(SpotifyLocators.SUBMIT_LOGIN)

        # Step II: go to playlists and extract the playlists
        browser_utils.wait_until_page_is_loaded()
        browser_utils.wait_until_element_is_clickable(SpotifyLocators.BTN_PLAYLISTS)
        driver.get(f"https://open.spotify.com/user/{spotify.get('user')}/playlists")
        browser_utils.wait_until_page_is_loaded()
        browser_utils.wait_until_element_is_visible(SpotifyLocators.PLAYLISTS_H2)

        SpotifyUtils.extract_playlists(
            browser_utils.get_elements(SpotifyLocators.PLAYLISTS_TITLES)
        )
    except Exception as e:
        print(f"There was an unexpected error :(\n\n{e}")
    finally:
        driver.quit()
