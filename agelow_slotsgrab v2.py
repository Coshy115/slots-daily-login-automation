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
    pyautogui.write("https://www.playfame.com/lobby")
    pyautogui.press('enter')
    time.sleep(20)

    # Policy Update
    pyautogui.click(842, 628)
    time.sleep(1)
    pyautogui.click(1071, 678)
    time.sleep(3)

    # Close popups
    pesky_popups(1236, 185)
    time.sleep(2)

    # Get Coins
    pyautogui.click(1710, 152)
    time.sleep(5)

    # Close popups
    pesky_popups(1236, 185)
    time.sleep(2)

    # Scroll to daily bonus
    pyautogui.click(1536, 440, clicks=10, interval=0.5)
    time.sleep(1)

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
    pyautogui.write("https://www.mcluck.com/home")
    pyautogui.press('enter')
    time.sleep(20)

    # Policy Update
    pyautogui.click(956, 659)
    time.sleep(3)

    # Close popups
    pesky_popups(1639, 433)
    time.sleep(2)

    # Get Coins
    pyautogui.click(79, 270)
    time.sleep(5)

    # Close popups
    pesky_popups(1639, 433)
    time.sleep(2)

    # Scroll to daily bonus
    pyautogui.click(1505, 536, clicks=10, interval=0.5)
    time.sleep(1)

    # Claim button
    pyautogui.click(1373, 582)
    time.sleep(5)

    # Claim button
    pyautogui.click(965, 778)
    time.sleep(5)

    # Captcha
    pyautogui.click(835, 781)
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
