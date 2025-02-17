import pyautogui
import time
from pathlib import Path


def image_path(image_name):

    return str(Path(__file__).parent / "Images" / image_name)

def open_chrome():

    time.sleep(2)
    chrome_location = pyautogui.locateCenterOnScreen(image_path("chrome.png"), grayscale=True, confidence=0.8)
    pyautogui.click(chrome_location)
    time.sleep(2)

def pesky_popups(x, y):

    time.sleep(3)
    pyautogui.click(x, y, duration=0.25, clicks = 10, interval=0.25)
    time.sleep(3)

def playfameslots():

    open_chrome()

    # Redirect to PlayFame
    pyautogui.hotkey("ctrl", "t")
    pyautogui.write("https://www.playfame.com/lobby")
    pyautogui.press("enter")
    time.sleep(10)

    pesky_popups(1236, 185)
    pyautogui.click(1715, 148)
    pesky_popups(1236, 185)
    pesky_popups(1236, 185)

    # Collect Daily Rewards
    pyautogui.click(1472, 527)
    time.sleep(5)
    pyautogui.click(954, 691)
    time.sleep(5)
    pyautogui.click(837, 700)
    time.sleep(5)

    # Close tab
    pyautogui.hotkey("ctrl", "w")
    print("PlayFame Grab Complete")

def mcluckslots():

    # Redirect to McLuck Slots
    pyautogui.hotkey("ctrl", "t")
    pyautogui.write("https://www.mcluck.com/gold-coins")
    pyautogui.press("enter")
    time.sleep(10)

    # Collect Daily Rewards
    pesky_popups(1639, 433)
    time.sleep(1)
    pyautogui.click(1505, 514)
    time.sleep(1)
    pyautogui.click(1373, 562)
    time.sleep(1)
    pyautogui.click(962, 724)
    time.sleep(5)

    # Close tab
    pyautogui.hotkey("ctrl", "w")
    print("McLuck Grab Complete")

playfameslots()
mcluckslots()
input()