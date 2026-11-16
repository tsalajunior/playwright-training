from playwright.sync_api import Page, expect
import pytest


# tag id
def test_verify_css_locators_tag_id(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input#small-searchterms").fill("laptop")
    # page.locator("#small-searchterms").fill("laptop")
    page.wait_for_timeout(5000)

# tag class
def test_verify_css_locators_tag_class(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input.search-box-text.ui-autocomplete-input").fill("laptop")
    # page.locator(".search-box-text").fill("laptop")
    page.wait_for_timeout(5000)

# tag attribute
def test_verify_css_locators_tag_attribute(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input[value='Search store']").fill("laptop")
    # page.locator("[title='Search store']").fill("laptop")
    page.wait_for_timeout(5000)

# tag class attribute
def test_verify_css_locators_tag_class_attribute(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input.search-box-text.ui-autocomplete-input[name='q']").fill("laptop")
    # page.locator(".search-box-text[title='Search store']").fill("laptop")
    page.wait_for_timeout(5000)


# execises 
# 1) verify logo visibility using css locator
def test_verify_logo_visibility(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    expect(page.locator("img[alt='Tricentis Demo Web Shop']")).to_be_visible()
    page.wait_for_timeout(5000)

# 2) capture all the computer related products and verify the count
def test_verify_computer_products_count(page: Page):
    page.goto("https://demowebshop.tricentis.com/computers")
    categories = page.locator(".sub-category-item")
    expect(categories).to_have_count(3)
    page.wait_for_timeout(5000)

# 3) print the name of the first product
def test_print_first_product_name(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    first_product_name = page.locator(".product-item h2 a").first
    print("First product name:", first_product_name.inner_text())
    page.wait_for_timeout(5000)

# 4) print the name of the last product
def test_print_last_product_name(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    last_product_name = page.locator(".product-item h2 a").last
    print("Last product name:", last_product_name.inner_text())
    page.wait_for_timeout(5000)

# 5) print the name of the nth product
def test_print_nth_product_name(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    nth_product_name = page.locator(".product-item h2 a").nth(2)  
    print("Nth product name:", nth_product_name.inner_text())
    page.wait_for_timeout(5000)

# 6) print the titles of all the products
def test_print_all_product_titles(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    product_titles = page.locator(".product-item h2 a")
    for title in product_titles.all_text_contents():
        print("Product title:", title)
    page.wait_for_timeout(5000)

# 7) get the first, last and nth link from the footer and print the text of the links
def test_print_footer_links(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    footer_links = page.locator(".footer a")
    first_link_text = footer_links.first.inner_text()
    last_link_text = footer_links.last.inner_text()
    nth_link_text = footer_links.nth(2).inner_text()  

    print("First footer link text:", first_link_text)
    print("Last footer link text:", last_link_text)
    print("Nth footer link text:", nth_link_text)

    page.wait_for_timeout(5000)