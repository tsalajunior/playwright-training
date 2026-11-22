from playwright.sync_api import Page, expect
from datetime import datetime


target_date = datetime(2025, 1, 22)
def select_date(page, target_year, target_month, target_date):
    # function to select the month and the year from the datepicker
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December",
    ]
    target = (int(target_year), month_names.index(target_month))
    navigation_count = 0

    while True:
        current_month = page.locator(".ui-datepicker-month").text_content()
        current_year = page.locator(".ui-datepicker-year").text_content()
        current = (int(current_year), month_names.index(current_month))

        if current == target:
            break

        navigation_count += 1
        if navigation_count > 240:
            raise AssertionError(
                f"Could not navigate to {target_month} {target_year}"
            )

        if current < target:
            page.locator(".ui-datepicker-next.ui-corner-all").click()
        else:
            page.locator(".ui-datepicker-prev.ui-corner-all").click()

    # Loop through the days instead of selecting the whole calendar text
    date_links = page.locator(
        ".ui-datepicker-calendar td:not(.ui-datepicker-other-month) a"
    ).all()

    for date_link in date_links:
        if date_link.inner_text().strip() == target_date:
            date_link.click()
            break
    else:
        raise AssertionError(
            f"Date {target_date} not found in {target_month} {target_year}"
        )


def test_date_pickers(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    date_input = page.locator("#datepicker")

    # approach 1
    # value = "11/22/2026"
    # date_input.fill(value) #mm/dd/yyyy
    # expect(date_input).to_have_value(value)

    # approach 2
    year = str(target_date.year)
    month = target_date.strftime("%B")
    date = str(target_date.day)
    value = target_date.strftime("%m/%d/%Y")

    date_input.click() # to open datepicker
    select_date(page, year, month, date)
    print("Selected date: ", date_input.input_value())
    expect(date_input).to_have_value(value)

    page.wait_for_timeout(3000)
