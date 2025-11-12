from re import compile
from playwright.sync_api import Page, expect
from allure import step

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.toggle_hide_counter_locator = self.page.locator('[alt="toggle"]')
        self.counter_locator = self.page.locator('//div[@data-testid="countertop"]/img')

    def show_countertop(self):
        with step("Переключатель 'Скрыть столешницу' - включен"):
            if "active" not in self.toggle_hide_counter_locator.get_attribute("src"):
                self.toggle_hide_counter_locator.click()
            expect(self.toggle_hide_counter_locator).to_have_attribute("src", compile("active"))
            self.make_screenshot("Переключатель включен")

    def hide_countertop(self):
        with step("Переключатель 'Скрыть столешницу' - выключен"):
            if "inactive" not in self.toggle_hide_counter_locator.get_attribute("src"):
                self.toggle_hide_counter_locator.click()
            expect(self.toggle_hide_counter_locator).to_have_attribute("src", compile("inactive"))
            self.make_screenshot("Переключатель выключен")

    def check_countertop_is_hidden(self):
        expect(self.counter_locator).not_to_have_attribute("src", compile("countertop"))

    def check_countertop_is_active(self):
        expect(self.counter_locator).to_have_attribute("src", compile("countertop"))
