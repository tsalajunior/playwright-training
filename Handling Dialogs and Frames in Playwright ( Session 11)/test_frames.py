import pytest
from playwright.sync_api import expect, Page


def test_frames(page:Page):
    page.goto('https://ui.vision/demo/webtest/frames/')

    all_frames = page.frames
    print("number of frames: ", len(all_frames))

    # frame 1
    # frame_1 = page.frame_locator("frame[src$='frame_1.html']")
    # frame_1 = page.frame("name of the frame in case")
    frame_1 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_1")
    input_1 = frame_1.locator("input[name$='mytext1']")
    input_1.fill("Hello there!")

    expect(input_1).to_have_value("Hello there!")

    page.wait_for_timeout(3000)