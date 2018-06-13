#encoding = utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class WaitUtil(object):
    def __init__(self,driver):
        self.locationTypeDict={
            "xpath":By.XPATH,
            "id":By.ID,
            "name":By.NAME,
            "class_name":By.CLASS_NAME,
            "tag_name":By.TAG_NAME,
            "link_text":By.LINK_TEXT,
            "partial_link_text":By.PARTIAL_LINK_TEXT
        }
        self.driver = driver
        self.wait = WebDriverWait(self.driver,30)

    def presenceOfElementLocated(self,locatorMethod,locatorExpression,*arg):
        try:
            if self.locationTypeDict.has_key(locatorMethod.lower()):
                self.wait.until(
                    EC.presence_of_all_elements_located((
                        self.locationTypeDict[locatorMethod.lower()],
                        locatorExpression)))
            else:
                raise TypeError("未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e


    def frameToBeAvailableAndSwitchToIt(self,locationType,locatorExpression):
        try:
            self.wait.until(
                EC.frame_to_be_available_and_switch_to_it((
                    self.locationTypeDict[locationType.lower()],
                    locatorExpression)))
        except Exception as e:
            raise e

    def visibilityOfElementLocated(self,locationType,locatorExpression):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((
                    self.locationTypeDict[locationType.lower()],
                    locatorExpression)))
            return element
        except Exception as e:
            raise e

if __name__=='__main__':
    driver = webdriver.Chrome()
    driver.get("http://mail.126.com")
    waitUtil = WaitUtil(driver)
    waitUtil.frame_available_and_switch_to_it("id","x-URS-iframe")
    e = waitUtil.visibility_element_located("xpath","//input[@name='email']")
    e.send_keys("success")
    driver.quit()

