from playwright.sync_api import expect, Page
import pytest

@pytest.mark.skip
def test_simple_dialog(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    page.wait_for_timeout(3000)

    # approach 1
    # registering an event
    def handle_dialog(dialog):
        dialog.accept() # close the alert by clicking on the OK button

    page.on("dialog", handle_dialog) 
    page.wait_for_timeout(3000)
    page.locator('#alertBtn').click()

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_simple_dialog2(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    page.wait_for_timeout(3000)

    # approach 2
    page.on("dialog", lambda dialog:dialog.accept()) 
    page.wait_for_timeout(3000)
    page.locator('#alertBtn').click()

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_confirmation_dialog(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    page.wait_for_timeout(3000)

    # page.on("dialog", lambda dialog:dialog.accept()) 
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.wait_for_timeout(3000)

    page.locator('#confirmBtn').click()
    page.wait_for_timeout(5000)

    message = page.locator("#demo").inner_text()
    print(f"message: {message}")

    # expect(page.locator("#demo")).to_have_text("You pressed OK!")
    expect(page.locator("#demo")).to_have_text("You pressed Cancel!")
    page.wait_for_timeout(3000)

def test_prompt_alert_dialog(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    value = 'Stéphane Boska'
    page.on("dialog", lambda dialog: dialog.accept(value))
    page.locator('#promptBtn').click()
    page.wait_for_timeout(3000)

    txt = page.locator('#demo').inner_text()
    print(f"message: {txt}")

    expect(page.locator('#demo')).to_have_text(f"Hello {value}! How are you today?")
    page.wait_for_timeout(3000)
