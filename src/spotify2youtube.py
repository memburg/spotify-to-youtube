from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from creds import spotify

if __name__ == "__main__":
    driver: WebDriver = webdriver.Firefox()
    wait = WebDriverWait(driver, timeout=10)
    driver.get("https://open.spotify.com/")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Log in']")))
    driver.find_element(By.XPATH, "//span[text()='Log in']").click()
    input("type something")
    driver.quit()
