import base64
from io import BytesIO

import pyautogui
import screeninfo


def take_screenshot(save_filename=None):
    screens = screeninfo.get_monitors()
    monitor = screens[1]
    left, top, width, height = monitor.x, monitor.y, monitor.width, monitor.height

    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    if save_filename:
        screenshot.save(save_filename, format="PNG")

    buffer = BytesIO()
    screenshot.save(buffer, format="PNG")
    return buffer


def encode_image(buffer):
    image_data = buffer.getvalue()
    base64_string = base64.b64encode(image_data).decode("utf-8")
    return base64_string
