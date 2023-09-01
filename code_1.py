import pyautogui
import time
import random
from PIL import ImageGrab
import numpy as np

import text_box_check


# Use the keyboard shortcut to open the terminal
pyautogui.hotkey('ctrl', 'alt', 't')

# Wait for the terminal to open
time.sleep(1)

# Type the command and press Enter
command = "visualboyadvance-m"
pyautogui.typewrite(command, interval=0.01)
pyautogui.press('enter')

# Wait for the Emu to open
time.sleep(2)

# Press Ctrl+F1 to open Recent ROM 1
pyautogui.hotkey('ctrl', 'f1')

# Wait for the game Opening
time.sleep(5)

# Buttons
UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'
A = 'l'
B = 'k'
L = 'i'
R = 'o'
START = 'enter'
SELECT = 'backspace'

button_dict = {'w': 'UP', 's': 'DOWN', 'a': 'LEFT', 'd': 'RIGHT',
               'l': 'A', 'k': 'B', 'i': 'L', 'o': 'R',
               'enter': 'START', 'backspace': 'SELECT'}

random_behavior_list = [UP, DOWN, LEFT, RIGHT, A, B]

def press_button(key, n_times = 1):
    for _ in range(n_times):
        pyautogui.keyDown(key)
        time.sleep(0.1)
        pyautogui.keyUp(key)
        print(button_dict[key])

# Select File
press_button(A, 10)

# Fullscreen
pyautogui.press('f11')

# Get the screen resolution
screen_width, screen_height = ImageGrab.grab().size

# Define the region to capture (e.g., the bottom half of the screen)
top = screen_height // 2  # Halfway down the screen
left = 0                 # Left edge of the screen
bottom = screen_height    # Full height (bottom of the screen)
right = screen_width     # Full width (right edge of the screen)

# Random behavior
i = 0 # testing (remove later)
while True:
    # Capture the specified region
    screenshot = np.array(ImageGrab.grab(bbox=(left, top, right, bottom)))
    if text_box_check.is_text_box(screenshot):
        print("In a text box.")
        press_button(A)
        time.sleep(0.5)
        continue
    else:
        print("Not in a text box.")
        time.sleep(0.5)
    action = random.choice(random_behavior_list)
    press_button(action)
    i += 1 # testing (remove later)
    if i == 200: # testing (remove later)
        break # testing (remove later)
