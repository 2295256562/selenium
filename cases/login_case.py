import unittest
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from page import *
from page.BasePage import BasePage
from page.LoginPage import LoginPage


class Mytest(unittest.TestCase):

    def setUp(self) -> None:
        self.dr = BasePage('firefox')
        self.dr.max_windows()
        self.dr.navigate('https://www.imooc.com/')







    def tearDown(self) -> None:
        self.dr.quit()
if __name__ == '__main__':
    unittest.main()