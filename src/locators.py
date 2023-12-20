from selenium.webdriver.common.by import By


class SpotifyLocators:
    BTN_LOGIN = By.XPATH, "//span[text()='Log in']"
    INPUT_USERNAME = By.ID, "login-username"
    INPUT_PASSWORD = By.ID, "login-password"
