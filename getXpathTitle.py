from selenium import webdriver
from FacebookXpath import *
import xlsxwriter
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.facebook.com/public/Forhadul-Islam")

workbook = xlsxwriter.Workbook('25.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Name')
worksheet.write('B1', 'Bio')
worksheet.write('C1', "Work")
worksheet.write('D1', "Education")
worksheet.write('E1', "Profile Url")


def getdata():
    i = 2
    a = 0
    while a < 10:

        driver.implicitly_wait(10)
        element = driver.find_elements_by_xpath(publicProfile)
        ActionChains(driver).key_down(Keys.CONTROL).click(element[i]).key_up(Keys.CONTROL).perform()
        driver.switch_to.window(driver.window_handles[1])

        driver.implicitly_wait(6)
        name = driver.find_element_by_xpath(profileName).text
        worksheet.write('A' + str(i) + '', name)
        worksheet.write('E' + str(i) + '', driver.current_url)
        print("name sucessfully saved!")

        if driver.find_elements_by_xpath(workAndEducation):
            work = driver.find_elements_by_xpath(workAndEducation)
            worksheet.write('C' + str(i) + '', work[0].text)
            worksheet.write('D' + str(i) + '', work[-1].text)
            print("work and education sucessfuly saved!")
        else: print("work and education xpath not found")


        if driver.find_elements_by_xpath(profileBio):
            bio = driver.find_element_by_xpath(profileBio).text
            worksheet.write('B' + str(i) + '', bio)
            print("profile bio successfuly saved!")
        else:print("profile bio xpath not fuond")

        driver.close()
        driver.switch_to.window(driver.window_handles[-1])

        i += 1
        a += 1
try:
    getdata()
except:
    pass
workbook.close()

def getAndSaveProfileData():
    i = 1
    while i <= 10:
        driver.implicitly_wait(6)
        name = driver.find_element_by_xpath(profileName).text
        worksheet.write('A' + str(i) + '', name)
        worksheet.write('E' + str(i) + '', driver.current_url)
        print("name sucessfully saved!")

        if driver.find_elements_by_xpath(workAndEducation):
            work = driver.find_elements_by_xpath(workAndEducation)
            worksheet.write('C' + str(i) + '', work[0].text)
            worksheet.write('D' + str(i) + '', work[-1].text)
            print("work and education sucessfuly saved!")
        else:
            print("work and education xpath not found")

        if driver.find_elements_by_xpath(profileBio):
            bio = driver.find_element_by_xpath(profileBio).text
            worksheet.write('B' + str(i) + '', bio)
            print("profile bio successfuly saved!")
        else:
            print("profile bio xpath not fuond")

        driver.close()
        driver.switch_to.window(driver.window_handles[-1])



