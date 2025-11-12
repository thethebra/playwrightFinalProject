from playwright.sync_api import Page, expect
from allure import attach, attachment_type, step

from pages.base_page import BasePage

class LoginPage(BasePage):
    username: str = "tester@inzhenerka.tech"
    password: str = "LetsTest!"
    url: str = "https://dev.topklik.online/"

    def __init__(self, page: Page):
        super().__init__(page)
        self.login_locator = self.page.locator('[name="login"]')
        self.password_locator = self.page.locator('[name="pass"]')
        self.enter_button_locator = self.page.locator('//button[contains(text(), "Войти")]')
        self.username_locator = self.page.locator('//h2[contains(text(), "Tester")]')

    def open(self):
        with step("Переход на страницу авторизации"):
            self.page.goto(self.url)
            self.page.wait_for_load_state("load")
            self.make_screenshot("Страница авторизации")

    def login(self):
        with step("Авторизация"):
            self.login_locator.fill(self.username)
            self.password_locator.fill(self.password)
            self.enter_button_locator.click()
            self.make_screenshot("Авторизация")

    def check_authorization(self):
        with step("Проверка авторизации"):
            expect(self.username_locator).to_be_visible(timeout=10000)
            self.make_screenshot("Авторизован")
