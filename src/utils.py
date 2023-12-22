from selenium.webdriver.remote.webdriver import WebElement


class SpotifyUtils:
    def extract_playlists(elements: list[WebElement]) -> list[str]:
        playlists: list[str] = []

        for e in elements:
            playlists.append(e.text)

        print(playlists)
        return playlists
