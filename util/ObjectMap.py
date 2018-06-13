#encoding = utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

def getElement(driver,locationType,locatorExpress):
    try:
        element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=locationType,value=locatorExpress))
        return element
    except Exception as e:
        raise e

def getElements(driver,locationType,locatorExpress):
    try:
        elements = WebDriverWait(driver,30).until(lambda x:x.find_elements(by=locationType,value=locatorExpress))
        return elements
    except Exception as e:
        raise e

if __name__=='__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    searchBox = getElement(driver,"id","kw")
    print(searchBox.tag_name)
    aList = getElements(driver,"tag name","a")
    print(len(aList))
    driver.quit()

