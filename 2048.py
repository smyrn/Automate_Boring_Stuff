#! Python3
# 2048.py - Automate the 2048 game.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element_by_tag_name('html')

while True:
    try:
        gameOver = browser.find_element_by_css_selector('div.game-message.game-over')
        break
    except:
        htmlElem.send_keys(Keys.UP)
    try:
        gameOver = browser.find_element_by_css_selector('div.game-message.game-over')
        break
    except:
        htmlElem.send_keys(Keys.RIGHT)
    try:
        gameOver = browser.find_element_by_css_selector('div.game-message.game-over')
        break
    except:
        htmlElem.send_keys(Keys.DOWN)
    try:
        gameOver = browser.find_element_by_css_selector('div.game-message.game-over')
        break
    except:
        htmlElem.send_keys(Keys.LEFT)

