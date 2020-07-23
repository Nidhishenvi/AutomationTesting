import time
import unittest
from selenium import webdriver
class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./drivers/chromedriver.exe')
        time.sleep(2)
        self.driver.maximize_window()
    def test_chrome_fn(self):
        self.driver.get("https://gnsaddy.github.io/webAutomationSelenium/")
        email = self.driver.find_element_by_xpath('//*[@id="inputEmail"]')
        password = self.driver.find_element_by_xpath('//*[@id="inputPassword"]')
        email.send_keys("aditya@gmail.com")
        password.send_keys("testing")
        submitbtn = self.driver.find_element_by_xpath('//*[@id="btnLogin"]')
        submitbtn.click()
        time.sleep(5)
        print("Valid Email and Password")
        alertJS = self.driver.switch_to.alert
        print(alertJS.text)
        alertJS.accept()
        timeer = time.strftime("%Y%m%d = %H%M%S")
        picture = "webImages"
    # taking screenshots
        self.driver.save_screenshot("../screenShots/" + picture + timeer + ".png")
        time.sleep(5)
    def test_chrome_fn1(self):
        self.driver.get("https://gnsaddy.github.io/webAutomationSelenium/")
        email = self.driver.find_element_by_xpath('//*[@id="inputEmail"]')
        password = self.driver.find_element_by_xpath('//*[@id="inputPassword"]')
        email.send_keys("abs@gmail.com")
        password.send_keys("testing")
        submitbtn = self.driver.find_element_by_xpath('//*[@id="btnLogin"]')
        submitbtn.click()
        time.sleep(5)
        print("Invalid Email with valid Password")
        alertJS = self.driver.switch_to.alert
        print(alertJS.text)
        alertJS.accept()
        timeer = time.strftime("%Y%m%d = %H%M%S")
        picture = "webImages"
    # taking screenshots
        self.driver.save_screenshot("../screenShots/" + picture + timeer + ".png")
        time.sleep(5)
    def test_chrome_fn2(self):
        self.driver.get("https://gnsaddy.github.io/webAutomationSelenium/")
        email = self.driver.find_element_by_xpath('//*[@id="inputEmail"]')
        password = self.driver.find_element_by_xpath('//*[@id="inputPassword"]')
        email.send_keys("aditya@gmail.com")
        password.send_keys("xyz")
        submitbtn = self.driver.find_element_by_xpath('//*[@id="btnLogin"]')
        submitbtn.click()
        time.sleep(5)
        print("Valid Email with invalid Password")
        alertJS = self.driver.switch_to.alert
        print(alertJS.text)
        alertJS.accept()
        timeer = time.strftime("%Y%m%d = %H%M%S")
        picture = "webImages"
    # taking screenshots
        self.driver.save_screenshot("../screenShots/" + picture + timeer + ".png")
        time.sleep(5)
    def test_chrome_fn3(self):
        self.driver.get("https://gnsaddy.github.io/webAutomationSelenium/")
        email = self.driver.find_element_by_xpath('//*[@id="inputEmail"]')
        password = self.driver.find_element_by_xpath('//*[@id="inputPassword"]')
        email.send_keys("abc@gmail.com")
        password.send_keys("xyz")
        submitbtn = self.driver.find_element_by_xpath('//*[@id="btnLogin"]')
        submitbtn.click()
        time.sleep(5)
        print("Invalid Email and Password")
        alertJS = self.driver.switch_to.alert
        print(alertJS.text)
        alertJS.accept()
        timeer = time.strftime("%Y%m%d = %H%M%S")
        picture = "webImages"
    # taking screenshots
        self.driver.save_screenshot("../screenShots/" + picture + timeer + ".png")
        time.sleep(5)
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
     unittest.main()
