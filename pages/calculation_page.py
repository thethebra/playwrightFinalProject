from playwright.sync_api import Page, expect
from allure import step

from pages.base_page import BasePage

class CalculationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Расчет
        self.calculation_result_locator = self.page.locator('//h1[contains(text(), "Результаты расчета")]')
        self.td_locator = lambda value: self.page.locator(f'//td[text()="{value}"]')
        self.td_value_locator = lambda value: self.page.locator(f'//td[text()="{value}"]/following-sibling::td[contains(@class, "col-2") and normalize-space()!=""]')

    def check_page_calculation(self):
        with step("Проверка перехода на страницу 'Расчет'"):
            expect(self.calculation_result_locator).to_be_visible()
            self.make_screenshot("Расчет")

    def check_parameter(self, parameter: str, value: str):
        with step(f"Проверка указанного значения '{parameter}': {value}"):
            self.go_to_element(self.td_locator(parameter))
            self.make_screenshot(parameter)
            expect(self.td_value_locator(parameter)).to_contain_text(value)
