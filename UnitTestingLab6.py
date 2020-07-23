from selenium import webdriver
import os
import unittest
import time


class LoginTest(unittest.TestRunner):
    def setUp(self):
        self.driver = webdriver.Chrome("./drivers/chromedriver.exe")
        driver = self.driver
        time.sleep(2)
        driver.maximize_window()

    def test_chrome_fn(self):
        self.driver.get("https://gnsaddy.github.io/webAutomationSelenium/")
        loginEmail = self.driver.find_element_by_xpath('//*[@id="inputEmail"]')
        #elements is recursive so use element
        loginPass = self.driver.find_element_by_xpath('//*[@id="inputPassword"]')

        time.sleep(2)
        loginEmail.send_keys("aditya@gmail.com")
        loginPass.send_keys("testing")

        btn = self.driver.find_element_by_xpath('//*[@id="btnLogin"]')
        btn.click()
        time.sleep(3)
        print("Both are valid")
        alertJS = self.driver.switch_to_alert
        print(alertJS.text)
        alertJS.accept()
        timeStr=time.strftime("%Y%m%d=%H%M%S")
        sImage="webImages"
        self.driver.save_screenshot("../screenshots/"+sImage+timeStr+".png")
        time.sleep(5)
