import pytest
from playwright.sync_api import Page, expect


def test_checkboxes(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    sunday = page.locator("input[value='sunday']")
    # sunday = page.get_by_label("Sunday")
    sunday.check()
    expect(sunday).to_be_checked()

    page.wait_for_timeout(5000)


def test_check_multiple_checkboxes(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    checkboxes = []
    # for day in days:
    #     checkbox = page.get_by_label(day)
    #     checkboxes.append(checkbox)

    checkboxes = [page.get_by_label(day) for day in days]
    print("number of checkboxes:", len(checkboxes))

    for checkbox in checkboxes:
        expect(checkbox).not_to_be_checked()
        checkbox.check()
        expect(checkbox).to_be_checked()

    page.wait_for_timeout(5000)


def test_last_three_checkboxes(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    checkboxes = [page.get_by_label(day) for day in days]
    print("number of checkboxes:", len(checkboxes))

    for checkbox in checkboxes[-3:]:
        expect(checkbox).not_to_be_checked()
        checkbox.check()
        expect(checkbox).to_be_checked()

    page.wait_for_timeout(5000)

def test_specific_checkboxes(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    checkboxes = [page.get_by_label(day) for day in days]
    print("number of checkboxes:", len(checkboxes))

    for checkbox in checkboxes:
        if checkbox.get_attribute("value") in ["saturday", "tuesday", "thursday"]:
            expect(checkbox).not_to_be_checked()
            checkbox.check()
            expect(checkbox).to_be_checked()

    page.wait_for_timeout(5000)

def test_uncheck_checkboxes(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    checkboxes = [page.get_by_label(day) for day in days]
    print("number of checkboxes:", len(checkboxes))

    for checkbox in checkboxes:
        checkbox.check()
        expect(checkbox).to_be_checked()

    for checkbox in checkboxes[-3:]:
        checkbox.uncheck()
        expect(checkbox).not_to_be_checked()

    page.wait_for_timeout(5000)

def test_toggling_checkboxes(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    checkboxes = [page.get_by_label(day) for day in days]
    print("number of checkboxes:", len(checkboxes))

    for checkbox in checkboxes:
        if checkbox.is_checked():
            checkbox.uncheck()
            expect(checkbox).not_to_be_checked()
        else:
            checkbox.check()
            expect(checkbox).to_be_checked()

    page.wait_for_timeout(5000)

def test_random_checkboxes(page: Page):
    import random
    page.goto("https://testautomationpractice.blogspot.com/")
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    checkboxes = [page.get_by_label(day) for day in days]
    print("number of checkboxes:", len(checkboxes))

    index = [1, 3, 6]

    random_days = [checkboxes[i] for i in index]
    for checkbox in random_days:
        expect(checkbox).not_to_be_checked()
        checkbox.check()
        expect(checkbox).to_be_checked()

    page.wait_for_timeout(5000)


def test_select_checkboxes_by_label_and_input_value(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    sunday = page.get_by_label("Sunday")
    monday = page.locator("input[value='monday']")

    sunday.check()
    monday.check()

    expect(sunday).to_be_checked()
    expect(monday).to_be_checked()

