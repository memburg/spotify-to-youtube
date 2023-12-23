<h1 align="center">Spotify to YouTube</h1>

<p align="center">
    <a href="https://www.python.org/"><img alt="Language: Python" src="https://img.shields.io/badge/language-python-3572A5.svg"></a>
    <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-black.svg"></a>
    <a href="https://www.selenium.dev/"><img alt="Automation Tool: Selenium" src="https://img.shields.io/badge/browser%20automation-selenium-43b02a.svg"></a>
    <a href="https://opensource.org/licenses/MIT"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg"></a>
</p>

> "Why not?"

This little project is to take all my music from Spotify to YouTube, I'm thinking about not paying Spotify anymore ¯\_(ツ)_/¯.

- [ ] Extract all the playlists data from Spotify (scrap it, don't use its API, there are legal implications).
- [ ] Store all this data in CSV (?).
- [ ] Use the YouTube API (?) [maybe Selenium] to create the playlists based on the collected data.

## Observations

I'm kinda an idiot and I got blocked by Spotify, I didn't know I could retrieve public playlists without loging in.

I will proceed to scrap the data without login in.

## Install

Make sure you activated the virtual environment.

`pip install -r requirements.txt`
