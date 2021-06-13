from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")
chrome_options.add_argument('--profile-directory=Default')
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
actions = ActionChains(driver)


driver.get("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp")
print(input("pass key: "))
driver.implicitly_wait(10)


def checkUssername():
    i = 0
    driver.find_element_by_xpath("//input[@id='username']").send_keys("mdjawad")
    while True:
        driver.find_element_by_xpath("//input[@id='username']").send_keys(i)
        driver.find_element_by_xpath("//input[@name='Passwd']").click()
        driver.implicitly_wait(10)
        time.sleep(1)
        driver.find_element_by_xpath("//input[@name='Passwd']").click()
        try:
            a = driver.find_element_by_xpath("//div[@class='o6cuMc']").text
            print(a,'--',i)
        except:
            pass
            print("Ussername abileable")
        bs = len(str(i))
        driver.find_element_by_xpath("//input[@id='username']").click()
        driver.find_element_by_xpath("//input[@id='username']").send_keys(Keys.BACK_SPACE * bs)
        i += 1








def gmailCheckLetter():
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    cba = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



    a = 0
    b = 0

    driver.find_element_by_xpath("//input[@id='username']").send_keys("Jawad")

    while True:
        if a < 26 and b < 26:
            print(abc[a] + cba[b])

            l = abc[a] + cba[b]

            driver.find_element_by_xpath("//input[@id='username']").send_keys(l)
            driver.find_element_by_xpath("//input[@name='Passwd']").click()
            driver.implicitly_wait(10)
            time.sleep(1)
            driver.find_element_by_xpath("//input[@name='Passwd']").click()
            try:
                a = driver.find_element_by_xpath("//div[@class='o6cuMc']").text
                print(a, '--', l)
            except:
                pass
                print("Ussername abileable")
            bs = len(str(l))
            driver.find_element_by_xpath("//input[@id='username']").click()
            driver.find_element_by_xpath("//input[@id='username']").send_keys(Keys.BACK_SPACE * bs)


            a += 1

        if a == 26:
            a = 0
            b += 1
            if b < 26:
                print(abc[a] + cba[b])

                y = abc[a] + cba[b]

                driver.find_element_by_xpath("//input[@id='username']").send_keys(y)
                driver.find_element_by_xpath("//input[@name='Passwd']").click()
                driver.implicitly_wait(10)
                time.sleep(1)
                driver.find_element_by_xpath("//input[@name='Passwd']").click()
                try:
                    a = driver.find_element_by_xpath("//div[@class='o6cuMc']").text
                    print(a, '--', y)
                except:
                    pass
                    print("Ussername abileable")
                bs = len(y)
                driver.find_element_by_xpath("//input[@id='username']").click()
                driver.find_element_by_xpath("//input[@id='username']").send_keys(Keys.BACK_SPACE * bs)


            a += 1


gmailCheckLetter()