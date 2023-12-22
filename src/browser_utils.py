from typing import Tuple
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as EC


class BrowserUtils:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    def click_element(self, locator: Tuple[str, str]) -> None:
        self.driver.find_element(*locator).click()

    def wait_until_element_is_clickable(
        self, locator: Tuple[str, str] | WebElement
    ) -> None:
        self.wait.until(EC.element_to_be_clickable(locator))

    def send_keys(self, locator: Tuple[str, str], keys: str) -> None:
        self.driver.find_element(*locator).send_keys(keys)

    def get_elements(self, locator: str) -> list[WebElement]:
        pass
