import pyautogui
import time

# Move Then Click
def MTC(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

# Open Chrome
MTC(75, 1050, duration=1)
MTC(896, 1054, duration=1)
time.sleep(2)

# Redirect to Chumba Casino
pyautogui.hotkey("ctrl", "t")
time.sleep(0.5)
pyautogui.write("https://www.chumbacasino.com/")
pyautogui.press("enter")
time.sleep(5)

# Log in
MTC(1363, 153, duration=1)
time.sleep(2)
MTC(280, 557, duration=1)
time.sleep(5)
MTC(1327, 158, duration=1)

time.sleep(1)
MTC(970, 149, duration=1)
MTC(1748, 148, duration=1)
MTC(1186, 234, duration=1)
MTC(967, 934, duration=1)

print("Process Complete")
input()