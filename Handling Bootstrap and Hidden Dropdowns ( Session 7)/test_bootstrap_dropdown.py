import pytest
from playwright.sync_api import Page, expect


def test_bootstrapdropdown(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # login steps
    page.locator('input[name="username"]').fill("Admin")
    page.locator('input[name="password"]').fill("admin123")
    page.locator('button[type="submit"]').click()

    page.wait_for_timeout(3000)

    # click on PIM
    page.get_by_text("PIM").click()

    # click on job title dropdown and open all options
    page.locator("form i").nth(2).click()
    page.wait_for_timeout(5000)

    # capture all the options
    # use: selector hub > devtools > settings > ignore list > uncheck 'content scripts'
    options = page.locator('div[role="listbox"] span')

    # count number of options
    count = options.count()
    print(f"number of options: {count}")

    expect(options).to_have_count(count) # assertion for counting options

    page.wait_for_timeout(3000)

    # print all the options 
    print(options.all_text_contents())

    # print all the options text using loop
    for i in range(options):
        print(options.nth(i).text_content())

    # select/click on specific option
    for i in range(options):
        text = options.nth(i).inner_text()
        if text == 'Automation Tester':
            print(text)
            options.nth(i).click()
            break 
    
    page.wait_for_timeout(5000)
