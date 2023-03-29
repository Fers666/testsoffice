import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest-playwright


def test_open_page(page):
    page.goto("www.yandex.ru")



