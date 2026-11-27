from playwright.sync_api import expect, Playwright


def test_browser_context(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)  # create browser
    try:
        context = browser.new_context()  # create context
        page1 = context.new_page()  # create page 1
        page2 = context.new_page()  # create page 2

        page1.goto("https://www.selenium.dev/")
        expect(page1).to_have_title("Selenium")

        page2.goto("https://practice.expandtesting.com/")
        expect(page2).to_have_title(
            "Automation Testing Practice Website for QA and Developers | UI and API"
        )
    finally:
        browser.close()
