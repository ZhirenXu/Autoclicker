from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Function import Login

def installDriver():
    pass
def get 
def test():
    browser = Login.login()
    creditCookie = browser.session.cookies.get_dict()
    keyList = list(creditCookie.keys())
    key = keyList[0]
    #print(creditCookie)
    #get website
    driver = webdriver.Firefox()
    cookie = {'name': key, 'value': creditCookie[key]}
    driver.get("https://library.osu.edu/dc")
    driver.add_cookie(cookie)
#    driver.close()
    driver.get("https://library.osu.edu/dc/concern/generic_works/s1784n301?locale=en")
    fileManagerUrl = driver.find_element_by_link_text('File Manager')
    fileManagerUrl.click()
    thumbnailButton = driver.find_element_by_id('thumbnail_id_kh04dr675')
    thumbnailButton.click()
    repMediaButton = driver.find_element_by_id('representative_id_kh04dr675')
    repMediaButton.click()
    saveButton = driver.find_element(By.XPATH, '//button[text()="Save"]')
    saveButton.click()
    driver.quit()

def getCredit():
    browser = Login.login()
    creditCookie = browser.session.cookies.get_dict()
    keyList = list(creditCookie.keys())
    key = keyList[0]
    cookie = {'name': key, 'value': creditCookie[key]}

    return cookie

def processUrl(cookie, workUrl, thumbnailID, repMediaID):
    driver.get("https://library.osu.edu/dc")
    driver.add_cookie(cookie)
    for url in workUrl:
        try:
            driver.get(workUrl)
        except:
            print("Fail to open website!\n")
        try:
            fileManagerUrl = driver.find_element_by_link_text('File Manager')
            fileManagerUrl.click()
        except:
            print("Fail to find File Manager Button!\n")
        try:
            thumbnailButton = driver.find_element_by_id('thumbnailID')
            thumbnailButton.click()
        except:
            print("Fail to find thumbnail button!\n")
        try:
            repMediaButton = driver.find_element_by_id('repMediaID')
            repMediaButton.click()
        except:
            print("Fail to find representative button!\n")
        try:
            saveButton = driver.find_element(By.XPATH, '//button[text()="Save"]')
            saveButton.click()
        except:
            print("Fail to find save button!\n")

def createWorkUrl(workID):
    workUrl = "https://library.osu.edu/dc/concern/generic_works/" + workID + "?locale=en"

    return workUrl

def createThumbnailID(fileSetID):
    thumbnailID = "thumbnail_id_" + fileSetID

    return thumbnailID

def createRepMediaID(fileSetID):
    repMediaID = "representative_id_" + fileSetID

    return repMediaID
    
def main(*argv):
    loginCookie = getCredit()
    workUrlList = getWorkID()
    fileSetList = getSetID()
    createWorkUrl()
    createThumbnailID(fileSetID)
    createRepMediaID(fileSetID)
    processUrl(cookie, workUrl, thumbnailID, repMediaID)
    driver.quit()

    
if __name__ == "__main__":
    main()
