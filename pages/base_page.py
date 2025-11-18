from allure import attach, attachment_type
from playwright.sync_api import Locator

from resources.tabs import Tabs

class BasePage(object):
    def __init__(self, page):
        self.page = page

    def make_screenshot(self, comment: str):
        screenshot = self.page.screenshot()
        attach(screenshot, comment, attachment_type.PNG)

    def go_to_element(self, locator: Locator):
        locator.scroll_into_view_if_needed()

    def get_new_tab_after_click(self, tabs: Tabs, locator: Locator):
        return tabs.wait_new(lambda: locator.click())
