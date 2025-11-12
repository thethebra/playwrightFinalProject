from allure import parent_suite, suite, sub_suite, id, title

from pages.login_page import LoginPage
from pages.main_page import MainPage

class TestMainPage:
    @parent_suite("UI-тесты")
    @suite("Тесты главной страницы")
    @sub_suite("Позитивные тесты")
    @title("Проверка работы переключателя \"Скрыть столешницу\"")
    @id("2")
    def test_check_hide_countertop(self, page):
        p = LoginPage(page)
        p.open()
        p.login()
        p.check_authorization()
        p = MainPage(page)
        p.show_countertop()
        p.check_countertop_is_active()
        p.hide_countertop()
        p.check_countertop_is_hidden()