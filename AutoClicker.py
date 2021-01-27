from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Function import Login
from selenium.webdriver.common.by import By

def installDriver():
    pass
def demo():
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()

def test():
    #browser = Login.login()
    #creditCookie = browser.session.cookies.get_dict()
    #keyList = list(creditCookie.keys())
    #key = keyList[0]
    #print(creditCookie)
    #get website
    driver = webdriver.Firefox()
    #cookie = {'name': key, 'value': creditCookie[key]}
    #driver.add_cookie(cookie)
    driver.get("https://library.osu.edu/dc/concern/generic_works/s1784n301?locale=en")
    driver.find_element_by_xpath('//button[@type="button"]/span["Login"]').click()
    #driver.find_element_by_link_text("https://library.osu.edu/dc/users/auth/shibboleth?locale=en").click()
    #driver.find_element_by_id("File Manager").click()
def main(*argv):
    test()
    
if __name__ == "__main__":
    main()
