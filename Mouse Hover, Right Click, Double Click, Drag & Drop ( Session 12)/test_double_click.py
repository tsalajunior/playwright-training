import pytest
from playwright.sync_api import Page, expect


def test_double_click(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    double_click_btn = page.locator('button[ondblclick="myFunction1()"]')
    double_click_btn.dblclick()

    inputbox2 = page.locator('#field2')
    expect(inputbox2).to_have_value("Hello World!")
    
    page.wait_for_timeout(4000)