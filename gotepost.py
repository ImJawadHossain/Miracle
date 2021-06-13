import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys



chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")
actions = ActionChains(driver)
driver.get('https://www.facebook.com')

def login():
    try:
        # I use environment veriable  base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
        username = str("01531180425")
        password = os.environ.get('password')

        driver.find_element_by_name("email").send_keys(username)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_name("login").click()
        print(input('Press any Key: '))
        print("Login work Successfully ")

    except:
        pass
login()

driver.get("https://www.facebook.com/groups/601242797290982")
driver.implicitly_wait(10)
actions.send_keys(Keys.TAB * 23)
time.sleep(4)
actions.perform()
print("Firast 23 tabs Working")

actions.send_keys(Keys.ENTER)
actions.perform()

def activePostAreaAndPostInPage():
    sleepTime = 4
    implicitlyWaitTime = 20
    time.sleep(sleepTime)

    active_post_area = driver.switch_to.active_element
    driver.implicitly_wait(implicitlyWaitTime)
    time.sleep(sleepTime)
    active_post_area.send_keys("'driver.switch_to.active_element' "
                               "this code is a one of important snippet for facebook automation.")

    actions.perform()
    print("Writing Post in the post area Successfully ")

    for i in range(2):
        driver.implicitly_wait(implicitlyWaitTime)
        actions.send_keys(Keys.TAB * 5)
        print(str(i) + " tabs Working")
    actions.send_keys(Keys.ENTER)
    actions.perform()

activePostAreaAndPostInPage()
driver.find