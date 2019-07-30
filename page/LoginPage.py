from page.BasePage import BasePage
from selenium.webdriver.common.by import By
from page.indexPage import IndexPage

class LoginPage(BasePage):

    def username_field(self):
        """username 输入框"""
        return self.getElenment(By.NAME, 'username')

    def password_field(self):
        """password 输入框"""
        return self.getElenment(By.NAME, 'password')

    def login_btn(self):
        return self.getElenment(By.NAME, 'submit')

    def login_success(self, username, password):
        self.username_field().send_keys(username)
        self.password_field().send_keys(password)
        self.login_btn().click()

        ## 返回登录成功的页面,首页
        return IndexPage(self.driver)