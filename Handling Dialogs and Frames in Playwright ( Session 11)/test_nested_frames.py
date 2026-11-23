import pytest
from playwright.sync_api import expect, Page


def test_nested_frames(page:Page):
    page.goto('https://ui.vision/demo/webtest/frames/')

    # frame 3
    frame_3 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_3")
    frame_3.locator("input[name='mytext3']").fill("welcome!")

    # all the frames
    child_frames = frame_3.child_frames
    print(f"number of nested frames: {len(child_frames)}")

    # first nested frame
    inner_frame = child_frames[0]
    radio = inner_frame.get_by_label("I am a human")
    radio.check()

    expect(radio).to_be_checked()

    page.wait_for_timeout(3000)