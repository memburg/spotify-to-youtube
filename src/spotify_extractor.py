import sys
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement

from creds import spotify
from browser_utils import BrowserUtils
from locators import SpotifyLocators
from utils import SpotifyUtils

if __name__ == "__main__":
    driver: WebDriver = webdriver.Firefox()
    browser_utils = BrowserUtils(driver=driver)
    username = sys.argv[1]

    try:
        driver.get(f"https://open.spotify.com/user/{username}/playlists")
        browser_utils.wait_until_page_is_loaded()
        browser_utils.wait_until_element_is_visible(SpotifyLocators.PLAYLISTS_H2)

        playlists: list[str] = SpotifyUtils.extract_playlists(
            browser_utils.get_elements(SpotifyLocators.PLAYLISTS_TITLES)
        )

        for playlist in playlists:
            SpotifyLocators.DYNAMIC_PLAYLIST[1] = f"//a[@title='{playlist}']"
            dynamic_locator = tuple(SpotifyLocators.DYNAMIC_PLAYLIST)
            browser_utils.wait_until_element_is_clickable(dynamic_locator)
            browser_utils.click_element(dynamic_locator)
            browser_utils.wait_until_element_is_visible(SpotifyLocators.PLAYLIST_TITLE)

            # do all the magic to extract the data here...

            browser_utils.go_back()
            browser_utils.wait_until_element_is_visible(SpotifyLocators.PLAYLISTS_H2)

    except Exception as e:
        print(f"There was an unexpected error :(\n\n{e}")
    finally:
        driver.quit()
