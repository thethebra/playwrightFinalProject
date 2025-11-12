from allure import attach, attachment_type

class BasePage(object):
    def __init__(self, page):
        self.page = page

    def make_screenshot(self, comment: str):
        screenshot = self.page.screenshot()
        attach(screenshot, comment, attachment_type.PNG)