from re import compile
from playwright.sync_api import Page, expect
from allure import step

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Выбор типа локатора
        self.toggle_hide_counter_locator = self.page.locator('[alt="toggle"]')
        self.counter_locator = self.page.locator('//div[@data-testid="countertop"]/img')
        self.button_switch_q_locator = self.page.locator('[data-testid="countertop-type-q"]')
        self.button_switch_u_locator = self.page.locator('[data-testid="countertop-type-u"]')
        self.counter_line_locator = self.page.locator('//div[contains(@class, "line")]')

        # Выбор толщины
        self.thickness_select_locator = self.page.locator('//label[text()="Толщина"]/following-sibling::button')
        self.thickness_option_locator = lambda name: self.page.locator(f'//span[contains(@class, "selectTitle styles_optionNumber") and contains(text(), "{name}")]/ancestor::button')
        self.thickness_selected_option_locator = self.page.locator('//label[text()="Толщина"]/following-sibling::button/div[contains(@class, "inputDigital styles_number")]')

        # Выбор плинтуса
        self.plinth_locator = self.page.locator('//div[text()="Плинтус"]/parent::button')
        self.plinth_switch_locator = self.page.locator('//div[contains(@class, "plinthSwitch")]')

        # Выбор острова
        self.island_locator = self.page.locator('//h4[text()="Остров"]/ancestor::div[@data-testid="product-item"]')
        self.island_active_locator = self.page.locator('//h4[text()="Остров"]/ancestor::div[contains(@class, "style_productItem")]')

        # Выбор проточки
        self.water_passages_locator = self.page.locator('//h4[text()="Проточки для стока воды"]/ancestor::div[@data-testid="options-item"]')
        self.water_passages_active_locator = self.page.locator('//h4[text()="Проточки для стока воды"]/ancestor::div[contains(@class, "style_optionsItem")]')

        # Выбор цвета
        self.color_locator = lambda option: self.page.locator(f'//div[text()="{option}"]')
        self.color_is_selected_locator = lambda option: self.page.locator(f'//div[text()="{option}"]/preceding-sibling::div/img[@alt="ok-blue"]')

        # Рассчет
        self.calculate_button_locator = self.page.locator('//button[@data-testid="calc-button"]')
        self.calculation_button_locator = self.page.locator('//button[@data-testid="open-report-button"]')
        self.handlers_title_locator = self.page.locator('//h1[text()="Обработчики"]')

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

    def switch_to_straight_countertop(self):
        with step("Смена типа основной части: прямая"):
            if "active" not in self.button_switch_q_locator.get_attribute("class"):
                self.button_switch_q_locator.click()
            self.make_screenshot("Прямая столешница")
            expect(self.counter_line_locator.first).to_have_attribute("class", compile("c-Q"))

    def switch_to_u_shaped_countertop(self):
        with step("Смена типа основной части: П-образная"):
            if "active" not in self.button_switch_u_locator.get_attribute("class"):
                self.button_switch_u_locator.click()
            self.make_screenshot("П-образная столешница")
            expect(self.counter_line_locator.first).to_have_attribute("class", compile("c-U"))

    def select_thickness(self, thickness_option: int):
        with step(f"Выбор толщины: {thickness_option}"):
            self.thickness_select_locator.click()
            self.thickness_option_locator(thickness_option).click()
            expect(self.thickness_selected_option_locator).to_have_text("4")
            self.make_screenshot(f"Выбрана толщина: {thickness_option}")

    def delete_plinth(self):
        with step("Удаление плинтусов"):
            self.plinth_locator.click()
            expect(self.plinth_switch_locator).to_have_count(0)
            self.make_screenshot("Удалены плинтусы")

    def select_island(self):
        with step("Добавление острова"):
            self.island_locator.click()
            self.make_screenshot("Остров добавлен")
            expect(self.island_active_locator).to_have_attribute("class", compile("active"))

    def select_water_passages(self):
        with step("Добавление проточки для стока воды"):
            self.water_passages_locator.click()
            self.make_screenshot("Проточки добавлены")
            expect(self.water_passages_active_locator).to_have_attribute("class", compile("active"))

    def select_color(self, color_option: str):
        with step(f"Выбор цвета: {color_option}"):
            self.color_locator(color_option).click()
            self.make_screenshot(f"Цвет {color_option} выбран")
            expect(self.color_is_selected_locator(color_option)).to_be_visible()

    def calculate(self):
        with step("Рассчитать заказ"):
            self.calculate_button_locator.click()
            expect(self.handlers_title_locator).to_be_visible()
            self.make_screenshot("Заказ рассчитан")

    def get_calculation(self, tabs):
        with step("Получить расчет"):
            self.get_new_tab_after_click(tabs, self.calculation_button_locator)
            self.make_screenshot("Переход на расчет")
