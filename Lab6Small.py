import unittest
import time
timestr = time.strftime("%y%m%d-%H%M%S")
from selenium import webdriver
class TestLaunch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("./drivers/chromedriver.exe") #Store the webdriver in a particular path and call it within the program
        self.driver.get("D:\stp\loginpage.html")
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.save_screenshot('C:\Screenshots\initial-login.png')
        self.driver.save_screenshot("loginScreenBeforeEnteringTheDetails"+timestr+".png")
    def test_FindClass(self):

        self.driver.find_element_by_id('User').send_keys('admin') #Enter User Name
        self.driver.find_element_by_id('Pass').send_keys('root123') #Enter Password
        self.driver.save_screenshot('C:\Screenshots\logincredentials.png')
        self.driver.save_screenshot("logincredentials"+timestr+".png")
        self.driver.find_element_by_css_selector('form#frmlog>input:nth-of-type(2)').click()  #clicking login
        self.driver.save_screenshot('C:/drivers/Screenshots/success-screen.png')
        self.driver.get("D:\stp\loginpage.html")
        self.driver.find_element_by_id('User').send_keys('administrator') #Enter wrongUser Name
        self.driver.find_element_by_id('Pass').send_keys('root123') #Enter Password
        self.driver.save_screenshot('C:Screenshots/wrong-credentials.png')
        self.driver.find_element_by_css_selector('form#frmlog>input:nth-of-type(1)').click()  #clicking reset
        self.driver.save_screenshot('C:\Screenshots\reset.png')
        self.assertTrue(self.driver.find_element_by_xpath(".//label"), "Username")

    def tearDown(self):
            self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

