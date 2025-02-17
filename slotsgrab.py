################################################
Age requirement went up, so this is outdated :/
################################################


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

def luckylandslots():

    # Login Details
    email = "[email]"
    password = "[password]"

    open_chrome()

    # Go to Lucky Land Slots
    pyautogui.hotkey('ctrl', 't')
    pyautogui.write("https://luckylandslots.com/loader")
    pyautogui.hotkey('enter')
    time.sleep(10)

    # Log in if necessary
    try:
        login_location = pyautogui.locateCenterOnScreen(image_path("login.png"), grayscale=True, confidence=0.8)

        if login_location:
            pyautogui.click(login_location)
            time.sleep(1)
            pyautogui.write(email, interval=0.05)
            time.sleep(1)

            passfield_location = pyautogui.locateCenterOnScreen(image_path("passfield.png"), grayscale=True, confidence=0.8)
            pyautogui.click(passfield_location)
            pyautogui.write(password, interval=0.05)
            time.sleep(1)

            login2_location = pyautogui.locateCenterOnScreen(image_path("login2.png"), grayscale=True, confidence=0.8)
            pyautogui.click(login2_location)
            time.sleep(1)
    
    except pyautogui.ImageNotFoundException:
        pass

    # Collect Daily Bonus
    time.sleep(5)
    pyautogui.click(615, 595)
    pyautogui.click(853, 588)
    pyautogui.click(1092, 586)
    pyautogui.click(618, 824)
    pyautogui.click(853, 816)
    pyautogui.click(1097, 808)
    pyautogui.click(1323, 670)
    time.sleep(2)
    pyautogui.click(938, 484)
    time.sleep(5)

    # Close tab
    pyautogui.hotkey('ctrl', 'w')

    print("Lucky Land Grab Complete")

def chumbaslots():

    # Redirect to Chumba Casino
    pyautogui.hotkey("ctrl", "t")
    pyautogui.write("https://www.chumbacasino.com/")
    pyautogui.press("enter")
    time.sleep(10)

    # Log in
    pyautogui.click(1363, 153)
    time.sleep(5)
    pyautogui.click(280, 557)
    time.sleep(5)
    pesky_popups(1327, 158)

    # Collect Daily Rewards
    pyautogui.click(1748, 148)
    time.sleep(5)
    pyautogui.click(1186, 234)
    time.sleep(5)
    pyautogui.click(967, 934)
    time.sleep(2)

    # Close tab
    pyautogui.hotkey("ctrl", "w")
    print("Chumba Grab Complete")

def playfameslots():

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
    time.sleep(2)

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
    time.sleep(2)

    # Close tab
    pyautogui.hotkey("ctrl", "w")
    print("McLuck Grab Complete")

luckylandslots()
chumbaslots()
playfameslots()
mcluckslots()
input()
