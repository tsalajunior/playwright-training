from playwright.sync_api import Page, expect


def select_checkin_date(page, year, month, day):
    # selecting year and month
    while True:
        checkin_month_year = (
            page.locator("h3[aria-live='polite']").nth(0).inner_text()
        )
        current_month, current_year = checkin_month_year.split(" ")

        if current_month == month and current_year == year:
            break
        else:
            page.locator("button[aria-label='Next month']").click()  # go to next month

    # selecting date
    all_dates = page.locator("table.b8fcb0c66a tbody").nth(0).locator("td").all()
    for dt in all_dates:
        if dt.inner_text() == day:
            dt.click()
            break


def select_checkout_date(page, year, month, day):
    # selecting year and month
    while True:
        checkout_month_year = (
            page.locator("h3[aria-live='polite']").nth(1).inner_text()
        )
        current_month, current_year = checkout_month_year.split(" ")

        if current_month == month and current_year == year:
            break
        else:
            page.locator("button[aria-label='Next month']").click()  # go to next month

    # selecting date
    all_dates = page.locator("table.b8fcb0c66a tbody").nth(1).locator("td").all()
    for dt in all_dates:
        if dt.inner_text() == day:
            dt.click()
            break


def test_datepickers(page: Page):
    page.goto("https://www.booking.com/")
    page.get_by_test_id("searchbox-dates-container").click()

    select_checkin_date(page, "2026", "November", "30")
    select_checkout_date(page, "2026", "December", "3")

    checkin_text = page.locator(
        "span[data-testid='date-display-field-start']"
    ).inner_text()
    checkout_text = page.locator(
        "span[data-testid='date-display-field-end']"
    ).inner_text()

    print(f"trip info: {checkin_text} - {checkout_text}")
    expect(page.locator("span[data-testid='date-display-field-start']")).to_contain_text(checkin_text)
    expect(page.locator("span[data-testid='date-display-field-end']")).to_contain_text(checkout_text)

    page.wait_for_timeout(3000)
