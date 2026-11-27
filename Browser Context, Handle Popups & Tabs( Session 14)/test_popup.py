from playwright.sync_api import expect, Playwright


def test_browser_context(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")
    page.on("popup", lambda popup: popup.wait_for_load_state())  # register the event
    PopUp = page.locator("#PopUp").click()

    page.wait_for_timeout(3000)

    all_popups = context.pages
    print(f"total popups/pages: {len(all_popups)}")

    # capture the urls of pages
    print("")
    print("Titles & URLs of Pages:")
    for pop in all_popups:
        pop_title, pop_url = str(pop.title()), str(pop.url)
        print(f"* {pop_title}: {pop_url}")
        if "Playwright" in pop_title:
            pop.locator(".getStarted_Sjon").click()
            pop.wait_for_timeout(3000)
            expect(pop).to_have_title("Installation | Playwright")
            pop.close()

    page.wait_for_timeout(3000)
    context.close()
    browser.close()
    
