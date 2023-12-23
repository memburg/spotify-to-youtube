from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as EC


class BrowserUtils:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)

    def click_element(self, locator: Tuple[str, str] | WebElement) -> None:
        if isinstance(locator, WebElement):
            locator.click()
        elif isinstance(locator, tuple):
            self.driver.find_element(*locator).click()
        else:
            raise ValueError(
                "Unsupported locator type. Please provide a WebElement or a Tuple."
            )

    def wait_until_element_is_clickable(
        self, locator: Tuple[str, str] | WebElement
    ) -> None:
        self.wait.until(EC.element_to_be_clickable(locator))

    def wait_until_element_is_visible(self, locator: Tuple[str, str]) -> None:
        self.wait.until(EC.visibility_of_element_located(locator))

    def send_keys(self, locator: Tuple[str, str], keys: str) -> None:
        self.driver.find_element(*locator).send_keys(keys)

    def wait_until_page_is_loaded(self) -> None:
        script = "return document.readyState;"

        while True:
            page_status = self.driver.execute_script(script=script)

            if page_status == "complete":
                return

    def get_element(self, locator: Tuple[str, str]) -> WebElement:
        return self.driver.find_element(*locator)

    def get_elements(self, locator: Tuple[str, str]) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def go_back(self) -> None:
        self.driver.execute_script("window.history.go(-1)")
