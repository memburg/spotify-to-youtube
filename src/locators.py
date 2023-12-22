from selenium.webdriver.common.by import By


class SpotifyLocators:
    BTN_LOGIN = By.XPATH, "//span[text()='Log in']"
    INPUT_USERNAME = By.ID, "login-username"
    INPUT_PASSWORD = By.ID, "login-password"
    SUBMIT_LOGIN = By.ID, "login-button"
    BTN_PLAYLISTS = By.XPATH, "//button[span[text()='Playlists']]"
    PLAYLISTS_TITLES = By.XPATH, "//span[contains(@class, 'ListRowTitle')]"
