import pytest
from playwright.sync_api import Page, expect

def test_radio_buttons(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    female_radio = page.locator("input[value='female']")
    expect(female_radio).to_be_visible()
    expect(female_radio).to_be_enabled()
    expect(female_radio).not_to_be_checked()
    female_radio.check()
    expect(female_radio).to_be_checked()

    page.wait_for_timeout(5000)  