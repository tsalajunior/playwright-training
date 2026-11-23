import pytest
from playwright.sync_api import Page, expect


def test_drag_drop(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    source = page.locator("#draggable")
    target = page.locator("#droppable")

    # approach 1: manual drag using hover
    # source.hover()
    # page.mouse.down()
    # target.hover()
    # page.mouse.up()

    # approach 2: drag_to() method
    source.drag_to(target)

    page.wait_for_timeout(4000)
