from pages.login_page import LoginPage

class LoginPageSteps(LoginPage):
    def open_login_page(self):
        LoginPage.goto()
