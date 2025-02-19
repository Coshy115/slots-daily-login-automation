# Python 3.12.2
import pyautogui
import time
import os

def warning():
    # Warns user of impending script execution
    print("Warning: Automation script will take control of your mouse and keyboard in approximately 10 minutes:\n")
    for i in range(1, 101):
        print(f"\r|{i * '█'}{(100 - i) * ' '}| {i}/100", end="    ")
        time.sleep(6)
    print("\nScript executing now...\n")

def pesky_popups(x, y):
    # Close popups
    pyautogui.click(x, y, clicks=10, interval=0.5)

def PlayFame():
    # Redirect to PlayFame in new tab
    pyautogui.hotkey('ctrl', 't')
    pyautogui.write("https://www.playfame.com/gold-coins")
    pyautogui.press('enter')
    time.sleep(10)

    # Close popups
    pesky_popups(1236, 185)
    time.sleep(2)

    # Claim button
    pyautogui.click(1472, 527)
    time.sleep(5)

    # I am not a robot (lol)
    pyautogui.click(954, 691)
    time.sleep(5)

    # Collect daily bonus
    pyautogui.click(837, 700)
    time.sleep(5)

    # Close tab
    pyautogui.hotkey('ctrl', 'w')
    print("PlayFame Grab Complete")

def McLuck():
    # Redirect to McLuck Slots in new tab
    pyautogui.hotkey('ctrl', 't')
    pyautogui.write("https://www.mcluck.com/gold-coins")
    pyautogui.press('enter')
    time.sleep(10)

    # Close popups
    pesky_popups(1639, 433)
    time.sleep(2)

    # Scroll to daily bonus
    pyautogui.click(1505, 514)
    time.sleep(5)

    # Claim button
    pyautogui.click(1373, 562)
    time.sleep(5)

    # Collect daily bonus
    pyautogui.click(962, 724)
    time.sleep(5)

    # Close tab
    pyautogui.hotkey('ctrl', 'w')
    print("McLuck Grab Complete")

# Warning of impending script execution
warning()

# Open Chrome and maximize window
os.system("start chrome")
time.sleep(3)
pyautogui.hotkey('alt', 'space')
time.sleep(1)
pyautogui.press('x')
time.sleep(2)

# Execute tasks
PlayFame()
McLuck()

# Close Chrome
pyautogui.hotkey('ctrl', 'w')

print("\nAll tasks completed. :)")
input()
