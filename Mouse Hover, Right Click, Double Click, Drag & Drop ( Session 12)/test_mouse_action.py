import pytest
from playwright.sync_api import Page, expect


def test_mouse_action(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    btn_drop = page.locator('button[class="dropbtn"]')
    btn_drop.hover()

    phone_element = page.locator('.dropdown-content a').nth(0)
    # page.locator('dropdown-content a:nth-child(1)')
    phone_element.hover()

    page.wait_for_timeout(4000)
