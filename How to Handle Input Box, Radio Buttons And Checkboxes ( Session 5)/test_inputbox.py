import pytest
from playwright.sync_api import Page, expect


def test_input_box(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    inputbox = page.locator("#name")
    expect(inputbox).to_be_visible()
    expect(inputbox).to_be_enabled()
    expect(inputbox).to_have_attribute("maxlength", "15")
    maxlength = inputbox.get_attribute("maxlength")
    print(f"Max length of input box is: {maxlength}")
    inputbox.fill("Stephane")
    value = inputbox.input_value()
    print(f"Value in input box is: {value}")

    page.wait_for_timeout(5000)