import pytest
import pytest_playwright

def test_1(page):
    page.goto("https://10.32.0.22/")