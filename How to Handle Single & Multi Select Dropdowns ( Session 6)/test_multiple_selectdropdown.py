import pytest
from playwright.sync_api import Page, expect

def test_multiple_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # Select multiple options from the dropdown - 3 ways

    # page.locator("#colors").select_option(label=["Red", "Green", "Blue"])  # Select by label
    # page.locator("#colors").select_option(["Red", "Green", "Blue"])

    # # page.locator("#colors").select_option(value=["red", "green", "blue", "white"]) # Select by value
    # page.locator("#colors").select_option(["red", "green", "blue", "white"])

    page.locator("#colors").select_option(index=[0, 3, 5]) # Select by index

    # count the number of selected options
    dropdown_options = page.locator("#colors option")
    expect(dropdown_options).to_have_count(7)  # Total options in the dropdown

    page.wait_for_timeout(5000)

