from playwright.sync_api import Page, expect

def test_verify_page_url(page: Page):
    page.goto("https://demowebshop.tricentis.com/") # passing url
    # capture the url of the page
    myurl = page.url
    print("The url of the page is: ", myurl)
    expect(page).to_have_url("https://demowebshop.tricentis.com/") # expected url

def test_verify_page_title(page: Page):
    page.goto("https://demowebshop.tricentis.com/") 
    # capture the title of the page
    mytitle = page.title
    print("The title of the page is: ", mytitle)
    expect(page).to_have_title("Demo Web Shop") # expected title