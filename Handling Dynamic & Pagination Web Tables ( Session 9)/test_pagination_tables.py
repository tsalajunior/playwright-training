from playwright.sync_api import expect, Page

def test_pagination_tables(page:Page):
    page.goto('https://datatables.net/examples/core/basic_init/zero_configuration.html')

    has_more_pages = True

    while has_more_pages:
        rows = page.locator('#example tbody tr').all() 
        for row in rows:
            print(row.inner_text())
        print('-----------------------------------------------------------------')
        page.wait_for_timeout(2000)
            
        next_btn = page.locator("button[aria-label$='Next']")
        is_disabled = next_btn.get_attribute('class') # extract the value of class attribute

        if "disabled" in is_disabled:
            has_more_pages = False
        else:
            next_btn.click()