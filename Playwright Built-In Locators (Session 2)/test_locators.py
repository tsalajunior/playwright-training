import time

from playwright.sync_api import Page, expect

# get by all text
def test_verify_pw_locator(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    time.sleep(5)
    page.wait_for_timeout(5000)
    logo = page.get_by_text("Tricentis Demo Web Shop")
    expect(logo).to_be_visible()
    page.close()

# get by text 
def test_verify_pw_locator_text(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    time.sleep(5)
    page.wait_for_timeout(5000)
    feat_products = page.get_by_text("Featured products")
    expect(feat_products).to_be_visible()
    page.close()