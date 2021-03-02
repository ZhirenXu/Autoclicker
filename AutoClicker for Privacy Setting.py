from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Function import Login
from Function import SimpleCSV
import time
import progressbar
import sys
import subprocess
import os.path

def loadUrlSession(session, url):
    html = session.get(url)
    return html

def installDriver():
    print(os.getcwd())
    subprocess.call("firefoxdriver.exe")
    print("Once finish installation, press enter to continue.")
    input()

def getCredit():
    browser = Login.login()
    creditCookie = browser.session.cookies.get_dict()
    keyList = list(creditCookie.keys())
    key = keyList[0]
    cookie = {'name': key, 'value': creditCookie[key]}

    return cookie

def readWorkUrl():
    print("Please enter input CSV file name which contains internal URL for each record (with .csv): \n")
    fileName = input()
    urlList = SimpleCSV.readCSV(fileName)
    workUrl = []
    for workID in urlList:
        workUrl.append(workID + "?locale=en")

    return workUrl

def processUrl(cookie, workUrl):
    driver = webdriver.Firefox()
    driver.get("https://library.osu.edu/dc")
    driver.add_cookie(cookie)
    urlAmount = len(workUrl)
    k = 0
    
    for k in progressbar.progressbar(range(urlAmount), redirect_stdout=True):
        try:
            url = workUrl.pop(0)
            driver.implicitly_wait(3)
            driver.get(url)
            print("Current URL: ", url)
        except:
            print("Fail to open website!\n")
        try:
            driver.implicitly_wait(4)
            fileManagerUrl = driver.find_element_by_link_text('Edit')
            fileManagerUrl.click()
        except:
            print("Fail to find Edit Button!\n")
        try:
            driver.implicitly_wait(4)
            privateButton = driver.find_element_by_id("generic_work_visibility_restricted")
            privateButton.click()
            print("Private button clicked")
        except:
            print("Fail to find Private button!\n")
        try:
            saveButton = driver.find_element_by_id("with_files_submit")
            saveButton.click()
            driver.implicitly_wait(3)
            time.sleep(3)
        except:
            print("Fail to find save button!\n")
        try:
            driver.implicitly_wait(3)
            applyChangeToContent = driver.find_element_by_xpath("//input[@value='Yes please.'][@type='submit']")
            applyChangeToContent.click()
            time.sleep(4)
        except:
            print("No need to apply for contents or Fail to find 'Yes Please.' button!\n")
            continue
    driver.quit()
        
def main(*argv):
    loginCookie = getCredit()
    #installDriver()
    workUrlList = readWorkUrl()
    #workUrlList = ["https://library.osu.edu/dc/concern/generic_works/m326m316g"]
    processUrl(loginCookie, workUrlList)

    print("Process finished. Hit enter to exit.")
    input()
    sys.exit()

    
if __name__ == "__main__":
    main()
