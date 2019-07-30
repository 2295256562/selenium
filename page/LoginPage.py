from page.BasePage import BasePage
from selenium.webdriver.common.by import By
from page.indexPage import IndexPage

class LoginPage(BasePage):

    def login_btn(self):
        """登录按钮"""
        return self.click('js-signin-btn')


    def usernameInput(self, username):
        return self.input('name=>email', username)

    def passwordInput(self, password):
        return self.input('name=>password', password)

    def loginBtn(self):
        return self.click('css=>.moco-btn-lg')



    def login_success(self, username, password):

        self.login_btn()
        self.sleep(2)
        self.usernameInput(username)
        self.sleep(1)
        self.passwordInput(password)
        self.loginBtn()