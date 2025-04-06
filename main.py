import pyautogui
from time import sleep

# ===== CONFIG =====
WPM = 60  # Default typing speed (words per minute)
SLEEP_SEC = 4  # Seconds to wait before typing starts
# =================

def txt_to_write():
    return pyautogui.prompt('Enter your text to type', title='Text typer')  # Get user input text

def wrt_more():
    return pyautogui.confirm('Do you want to write more?', buttons=['Yes', 'No'])  # Continue prompt

def wpm_to_interval(wpm):
    return 60 / (wpm * 5)  # Convert WPM to keystroke interval in seconds

INTERVAL = wpm_to_interval(WPM)  # Calculate typing speed once

while True:
    text = txt_to_write()  # Get text from user
    if text is None:  # Exit if user cancels
        break
    
    # Confirm before typing with configurable countdown
    pyautogui.confirm(f"You have {SLEEP_SEC} seconds to point cursor (Typing at {WPM} WPM)", buttons=['OK', 'Cancel'])
    
    sleep(SLEEP_SEC)  # Pause for cursor positioning
    pyautogui.write(text, interval=INTERVAL)  # Type the text
    
    if wrt_more() != 'Yes':  # Break loop if user doesn't want to continue
        break
    
