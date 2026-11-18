import pytest
from playwright.sync_api import Page, expect


def test_sorted_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # dropdown_options = page.locator('#animals option') # sorted dropdown
    dropdown_options = page.locator("#colors option") # unsorted dropdown

    options_text = [text.strip() for text in dropdown_options.all_text_contents()]
    original_list = options_text.copy()
    sorted_list = sorted(options_text, reverse=True)

    print("")
    print("Original List:", original_list)
    print("Sorted List:", sorted_list)

    if original_list == sorted_list:
        print("The dropdown is sorted.")
    else:
        print("The dropdown is not sorted.")

    page.wait_for_timeout(5000)