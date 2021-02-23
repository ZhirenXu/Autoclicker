from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Function import Login
from Function import SimpleCSV
import time
import progressbar

def loadUrlSession(session, url):
    html = session.get(url)
    return html

def installDriver():
    pass

def getWorkID():
    workID = SimpleCSV.readCSV("internal id.csv")

    return workID

def getSetID():
    fileSet = SimpleCSV.readCSV("file set.csv")

    return fileSet

def getCredit():
    browser = Login.login()
    creditCookie = browser.session.cookies.get_dict()
    keyList = list(creditCookie.keys())
    key = keyList[0]
    cookie = {'name': key, 'value': creditCookie[key]}

    return cookie

def processUrl(cookie, workUrl, thumbnailList, repMediaList):
    driver = webdriver.Firefox()
    driver.get("https://library.osu.edu/dc")
    driver.add_cookie(cookie)
    urlAmount = len(workUrl)
    k = 0
    
    for k in progressbar.progressbar(range(urlAmount), redirect_stdout=True):
        try:
            url = workUrl.pop(0)
            driver.get(url)
            #html = loadUrlSession(session, url)
            print("Current URL: ", url)
        except:
            print("Fail to open website!\n")
        try:
            driver.implicitly_wait(3)
            fileManagerUrl = driver.find_element_by_link_text('File Manager')
            fileManagerUrl.click()
        except:
            print("Fail to find File Manager Button!\n")
        try:
            driver.implicitly_wait(3)
            sortButton = driver.find_element(By.XPATH, '//button[text()="Sort alphabetically"]')
            sortButton.click()
            print("Sort clicked")
        except:
            print("Fail to sort!")
        try:
            driver.implicitly_wait(3)
            thumbnailButton = driver.find_element_by_id(thumbnailList.pop(0))
            thumbnailButton.click()
            print("Thumbnail clicked")
        except:
            print("Fail to find thumbnail button!\n")
        try:
            driver.implicitly_wait(3)
            repMediaButton = driver.find_element_by_id(repMediaList.pop(0))
            repMediaButton.click()
            print("repMedia clicked")
        except:
            print("Fail to find representative button!\n")
        try:
            saveButton = driver.find_element(By.XPATH, '//button[text()="Save"]')
            time.sleep(4)
            saveButton.click()
            time.sleep(4)
            driver.implicitly_wait(3)
        except:
            print("Fail to find save button!\n")
            continue
    driver.quit()

def createWorkUrl(workIDList):
    workUrl = []
    for workID in workIDList:
        workUrl.append(workID + "?locale=en")

    return workUrl

def createThumbnailID(fileSetList):
    thumbnailList = []
    for fileSet in fileSetList:
        thumbnailList.append("thumbnail_id_" + fileSet)

    return thumbnailList

def createRepMediaID(fileSetList):
    repMediaList = []
    for fileSet in fileSetList:
        repMediaList.append("representative_id_" + fileSet)

    return repMediaList
        
def main(*argv):
    loginCookie = getCredit()
    #loginCookie = getCredit(session)
    workIDList = getWorkID()
    fileSetList = getSetID()
    workUrlList = createWorkUrl(workIDList)
    
    thumbnailList = createThumbnailID(fileSetList)
    repMediaList = createRepMediaID(fileSetList)
    processUrl(loginCookie, workUrlList, thumbnailList, repMediaList)

    
if __name__ == "__main__":
    main()
