import pytest
from playwright.sync_api import expect, Page
from pathlib import Path

file = Path(__file__).parent / "uploads" / "Stephane_Resume.pdf"
files = [
    Path(__file__).parent / "uploads" / "Stephane_Resume.pdf",
    Path(__file__).parent / "uploads" / "TechnicalTrainingAgenda.pdf"
]

@pytest.mark.skip
def test_single_file(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    singleFileInput = page.locator('#singleFileInput').set_input_files(str(file))
    btnSingleFile = page.locator("button:has-text('Upload Single File')")
    btnSingleFile.click()
    singleFileStatus = page.locator('#singleFileStatus')

    expect(singleFileStatus).to_contain_text(file.name)
    print("File uploaded successfully!")

    page.wait_for_timeout(3000)

def test_multiple_files(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator('#multipleFilesInput').set_input_files([str(path) for path in files])
    btnMultipleFiles = page.locator("button:has-text('Upload Multiple Files')")
    btnMultipleFiles.click()
    multipleFileStatus = page.locator('#multipleFilesStatus')

    for uploaded_file in files:
        expect(multipleFileStatus).to_contain_text(uploaded_file.name)
    print("Files uploaded successfully!")

    page.wait_for_timeout(3000)