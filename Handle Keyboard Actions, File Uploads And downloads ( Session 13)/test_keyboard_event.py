import pytest
from playwright.sync_api import expect, Page


def test_keyboard_event(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    input1 = page.locator('#input1')
    input1.focus()

    page.keyboard.insert_text("random text")
    page.keyboard.press("Control+A")
    page.keyboard.press("Control+C")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Control+V")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Control+V")

    input2 = page.locator('#input2')
    input3 = page.locator('#input3')

    expect(input2).to_have_value("random text")
    expect(input3).to_have_value("random text")

    page.wait_for_timeout(3000)
