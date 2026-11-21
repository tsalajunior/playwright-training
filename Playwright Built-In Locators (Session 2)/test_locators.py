import time
import pytest

from playwright.sync_api import Page, expect

@pytest.mark.skip
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

# get by role
def test_verify_pw_locator_role(page:Page):
    page.goto("https://demowebshop.tricentis.com/register")
    page.wait_for_timeout(5000)
    heading = page.get_by_role("heading", name="Register")
    expect(heading).to_be_visible()
    page.close()

# get by label
def test_verify_pw_locator_label(page:Page):
    page.goto("https://demowebshop.tricentis.com/register")
    page.wait_for_timeout(5000)
    first_name = page.get_by_label("First name:")
    last_name = page.get_by_label("Last name:")
    email = page.get_by_label("Email:")

    first_name.fill("Stephane")
    last_name.fill("Boska")
    email.fill("stephane.boska@example.com")

    expect(first_name).to_be_visible()
    expect(last_name).to_be_visible()
    expect(email).to_be_visible()
    page.close()

# get by placeholder
def test_verify_pw_locator_placeholder(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(5000)
    search_bar = page.get_by_placeholder("Search store")
    search_bar.fill("laptop")
    expect(search_bar).to_be_visible()
    page.close()

# get by title
def test_verify_pw_locator_title(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.wait_for_timeout(5000)
    title = page.get_by_title("Automation Testing Practice - Atom")
    # expect(title).to_have_text("Automation Testing Practice - Atom")
    page.close()


# get by test_id
def test_verify_pw_locator_test_id(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.wait_for_timeout(5000)
    email_id = page.get_by_test_id("profile-email")
    expect(email_id).to_have_text("john.doe@example.com")
    expect(email_id).to_be_visible()
    page.close()