from playwright.sync_api import expect, Page

def test_filter_rows(page:Page):
    page.goto('https://datatables.net/examples/core/basic_init/zero_configuration.html')

    dropdown = page.locator('#dt-length-0')
    dropdown.select_option(label='25')

    rows = page.locator("#example tbody tr")
    number_rows = rows.count()
    print(f"number of rows: {number_rows}")
    expect(rows).to_have_count(number_rows)

    page.wait_for_timeout(3000)