from allure import parent_suite, suite, sub_suite, id, title

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.calculation_page import CalculationPage

class TestE2E:
    @parent_suite("UI-тесты")
    @suite("E2E-тесты")
    @sub_suite("Позитивные тесты")
    @title("Заказ: П-образная столешница")
    @id("4")
    def test_u_shaped_countertop(self, page, tabs):
        p = LoginPage(page)
        p.open()
        p.login()
        p.check_authorization()
        p = MainPage(page)
        p.show_countertop()
        p.check_countertop_is_active()
        p.switch_to_u_shaped_countertop()
        p.select_thickness(4)
        p.delete_plinth()
        p.select_island()
        p.select_water_passages()
        p.select_color("N-103 Gray Onix")
        p.calculate()
        p.get_calculation(tabs)
        page = tabs.active
        p = CalculationPage(page)
        p.check_page_calculation()
        p.check_parameter("Материал", "acryl:Neomarm:N-103 Gray Onix")
        p.check_parameter("Тип столешницы", "П-образная")
        p.check_parameter("Опции", "Проточки для стока воды")
        p.check_parameter("Стоимость итоговая", "412500.00")
