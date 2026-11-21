from playwright.sync_api import Page, expect

def test_verify_chrome_cpu_load(page:Page):
    page.goto('https://practice.expandtesting.com/dynamic-table')

    table = page.locator('table[class="table table-striped"] tbody')
    rows  = table.locator('tr').all() # to get data in list format

    cpu = ""
    for row in rows:
        browser_name = row.locator('td').nth(0).inner_text()
        if browser_name == "Chrome":
            cpu = row.locator('td:has-text("%")').inner_text()
            print(f"CPU of Chrome: {cpu}") 
            break

    expect(page.locator('#chrome-cpu')).to_contain_text(cpu)

    page.wait_for_timeout(5000)