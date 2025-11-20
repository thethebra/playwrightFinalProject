import pytest
import os
from playwright.sync_api import sync_playwright

from resources.tabs import Tabs

headless_mode = os.getenv("CI") == "true"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless_mode)
        yield browser
        browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def tabs(context):
    return Tabs(context)
