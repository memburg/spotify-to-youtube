from unidecode import unidecode
from selenium.webdriver.remote.webdriver import WebElement


class SpotifyUtils:
    def extract_playlists(elements: list[WebElement]) -> list[str]:
        playlists: list[str] = []

        for e in elements:
            # normalized_name = unidecode(e.text).lower().strip().replace(" ", "_")
            # print(f"{e.text} - {normalized_name}")
            # playlists.append(normalized_name)
            playlists.append(e.text)

        return playlists
