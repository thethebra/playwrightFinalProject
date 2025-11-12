from pages.login_page import LoginPage
from allure import parent_suite, suite, sub_suite, id, title

class TestLogin:
    @parent_suite("UI-тесты")
    @suite("Тесты на авторизацию")
    @sub_suite("Позитивные тесты")
    @title("Успешная авторизация")
    @id("1")
    def test_login(self, page):
        p = LoginPage(page)
        p.open()
        p.login()
        p.check_authorization()
