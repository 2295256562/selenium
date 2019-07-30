from cases.login_case import Mytest
from page.LoginPage import LoginPage

class TestMOkeInde(Mytest):

    def test_Logincase(self):
        moke = LoginPage(self.dr)

        username = '18758127481'
        password = 'a1234567890'

        moke.login_success(username, password)