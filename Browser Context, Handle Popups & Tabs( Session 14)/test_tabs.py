from playwright.sync_api import expect, Playwright


def test_tabs(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    parent_page = context.new_page()

    parent_page.goto("https://testautomationpractice.blogspot.com/")

    # register event for handling tabs
    parent_page.on("page", lambda page: page.wait_for_load_state())
    # btn = parent_page.locator('button[onclick="myFunction()"]').click()
    btn = parent_page.locator('button:has-text("New Tab")').click()
    parent_page.wait_for_timeout(3000)

    all_pages = context.pages
    print(f"Number of pages/tabs: {len(all_pages)}")
    print('')

    # for tab in all_pages:
    #     title_, url_ = str(tab.title()), str(tab.url)
    #     print(f"* {title_}: {url_}")

    print(f"Parent page infos: {str(all_pages[0].title())}, {str(all_pages[0].url)}")
    print(f"Child page infos: {str(all_pages[1].title())}, {str(all_pages[1].url)}")


