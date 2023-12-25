from selenium.webdriver.common.by import By


class SpotifyLocators:
    BTN_LOGIN = By.XPATH, "//span[text()='Log in']"
    INPUT_USERNAME = By.ID, "login-username"
    INPUT_PASSWORD = By.ID, "login-password"
    SUBMIT_LOGIN = By.ID, "login-button"
    BTN_PLAYLISTS = By.XPATH, "//button[span[text()='Playlists']]"
    PLAYLISTS_TITLES = By.XPATH, "//a[contains(@href, 'playlist') and @title]"
    BTN_PLAYLISTS_CHECKED = (
        By.XPATH,
        "//button[span[text()='Playlists'] and @aria-checked='true']",
    )
    PLAYLISTS_H2 = By.XPATH, "//h2[text()='Public Playlists']"
    PLAYLIST_TITLE = By.XPATH, "//h1[@dir='auto']"
    DYNAMIC_PLAYLIST = [By.XPATH, ""]
    TRACKS = By.XPATH, "//a[contains(@href, 'track')]"
    NUMBER_OF_SONGS = By.XPATH, "//span[contains(text(), 'songs')]"
    ARTISTS = (
        By.XPATH,
        "//a[contains(@href, 'artist/') and not(preceding-sibling::a[contains(@href, 'artist')])]",
    )
    TRACK_LIST_ROW = By.XPATH, "//div[@data-testid='tracklist-row']"
