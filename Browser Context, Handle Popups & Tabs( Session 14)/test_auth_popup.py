from playwright.sync_api import expect, Playwright


def test_auth_popup(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(http_credentials={"username":"admin", "password":"admin"})
    page =  context.new_page()
    page.goto('https://the-internet.herokuapp.com/basic_auth')

    page.wait_for_load_state()
    expect(page.locator('p')).to_be_visible()
    page.wait_for_timeout(3000)