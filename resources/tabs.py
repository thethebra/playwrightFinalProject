class Tabs:
    def __init__(self, context):
        self.context = context

    @property
    def all(self):
        return self.context.pages

    @property
    def active(self):
        return self.context.pages[-1]

    def wait_new(self, click_action):
        with self.context.expect_page() as new_page_info:
            click_action()
        return new_page_info.value
