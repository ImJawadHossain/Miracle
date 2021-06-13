from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pyperclip
import os
import pathlib

chrome_options = Options()
scriptDirectory = pathlib.Path().absolute()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument('--profile-directory=Default')
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("user-data-dir=chrome-data")
chrome_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")

driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
driver.get("https://google.com")

print(input("After sing-in your google account Type anything and press Enter: "))

driver.get("https://docs.google.com/spreadsheets/u/0/")
driver.implicitly_wait(10)
driver.find_element_by_id(":1g").click()

pageurl = driver.current_url

pyperclip.copy(pageurl)

paste = pyperclip.paste()

def paste_keys():
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="t-formula-bar-input"]/div').send_keys(paste)

paste_keys()


