import pytest
from playwright.sync_api import expect, Page
from pathlib import Path

download_dir = Path(__file__).parent / "downloads"


def test_download_files(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    value = "random text"
    inputText = page.locator("#inputText")
    inputText.fill(value)

    generateTxt = page.locator("#generateTxt")
    generateTxt.click()

    with page.expect_download() as download_info:
        page.locator("#txtDownloadLink").click()
    download = download_info.value
    download.save_as(download_dir / download.suggested_filename)

    page.wait_for_timeout(3000)
