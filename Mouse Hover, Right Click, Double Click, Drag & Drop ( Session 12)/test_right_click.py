import pytest
from playwright.sync_api import Page, expect


def test_right_click(page:Page):
    page.goto('https://swisnl.github.io/jQuery-contextMenu/demo.html')

    right_btn = page.locator('.context-menu-one.btn.btn-neutral')
    right_btn.click(button="right")
    

    page.wait_for_timeout(4000)