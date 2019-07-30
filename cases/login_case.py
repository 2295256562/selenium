import unittest
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from page import *
from page.BasePage import BasePage
from page.LoginPage import LoginPage


class LoginCase(unittest.TestCase):
    def setUp(self):
        self.dr = BasePage()

    def test_login_success(self):
        username = '17671105406'
        password = 'yuanman99'
        login_page = LoginPage(self.dr, '/signin?next=%2F')

        index_Page = login_page.login_success(username=username, password=password)
        self.assertTrue(username in index_Page)