import pytest
from playwright.sync_api import Page, expect


def test_single_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # 3 ways to select an option from a dropdown

    # page.locator('#country').select_option(label='Canada')  # Select by label
    # page.locator('#country').select_option(value='canada') # Select by value
    page.locator('#country').select_option(index=2)  # Select by index

    # check number of options in the dropdown and print all the options in the dropdown
    options = page.locator('#country option')
    expect(options).to_have_count(10)

    options_text = [text.strip() for text in options.all_text_contents()]
    print(f"Options in the dropdown: {options_text}")

    for option in options_text:
        print(f"Option: {option}")

    page.wait_for_timeout(5000)
    