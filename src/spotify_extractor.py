import sys
import csv
import traceback
from unidecode import unidecode

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement

from browser_utils import BrowserUtils
from locators import SpotifyLocators
from utils import SpotifyUtils

if __name__ == "__main__":
    driver: WebDriver = webdriver.Firefox()
    print(driver.get_window_size())
    browser_utils = BrowserUtils(driver=driver)
    username = sys.argv[1]

    try:
        driver.maximize_window()
        driver.get(f"https://open.spotify.com/user/{username}/playlists")
        browser_utils.wait_until_page_is_loaded()
        browser_utils.wait_until_element_is_present(SpotifyLocators.PLAYLISTS_H2)

        playlists: list[str] = SpotifyUtils.extract_playlists(
            browser_utils.get_elements(SpotifyLocators.PLAYLISTS_TITLES)
        )

        for playlist in playlists:
            SpotifyLocators.DYNAMIC_PLAYLIST[1] = f"//a[@title='{playlist}']"
            dynamic_locator = tuple(SpotifyLocators.DYNAMIC_PLAYLIST)
            browser_utils.wait_until_element_is_clickable(dynamic_locator)
            browser_utils.click_element(dynamic_locator)
            browser_utils.wait_until_element_is_present(SpotifyLocators.PLAYLIST_TITLE)

            csv_title = unidecode(playlist).lower().strip().replace(" ", "_")

            # do all the magic to extract the data here...
            with open(f"playlists/{csv_title}.csv", "w", newline="\n") as file:
                writer = csv.writer(file)

                browser_utils.wait_until_element_is_present(
                    SpotifyLocators.NUMBER_OF_SONGS
                )
                number_of_songs_element = browser_utils.get_element(
                    SpotifyLocators.NUMBER_OF_SONGS
                )
                number_of_songs = int(number_of_songs_element.text.split(" ")[0])
                saved_songs = set()

                while len(saved_songs) != number_of_songs:
                    browser_utils.wait_until_element_is_present(
                        SpotifyLocators.TRACK_LIST_ROW
                    )
                    track_row = browser_utils.get_element(
                        SpotifyLocators.TRACK_LIST_ROW
                    )
                    all_tracks = browser_utils.get_elements(
                        SpotifyLocators.TRACK_LIST_ROW
                    )

                    for track in all_tracks:
                        track_title = driver.execute_script(
                            "return arguments[0].querySelectorAll('.standalone-ellipsis-one-line')[0].innerText",
                            track,
                        )
                        artist = driver.execute_script(
                            "return arguments[0].querySelectorAll('.standalone-ellipsis-one-line')[1].innerText",
                            track,
                        )
                        album = driver.execute_script(
                            "return arguments[0].querySelectorAll('.standalone-ellipsis-one-line')[2].innerText",
                            track,
                        )
                        driver.execute_script(
                            "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'start' })",
                            all_tracks[len(all_tracks) - 1],
                        )
                        saved_songs.add("|".join([track_title, artist, album]))
                        # print(saved_songs)
                        # print(f"{track_title}|{artist}|{album}")

                saved_songs = list(saved_songs)
                for saved_song in saved_songs:
                    writer.writerow([saved_song])

            browser_utils.go_back()
            browser_utils.wait_until_element_is_present(SpotifyLocators.PLAYLISTS_H2)
    except Exception as e:
        print(traceback.format_exc())
    finally:
        print("Closing webdriver...")
        driver.quit()
