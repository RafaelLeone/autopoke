import pyautogui
import time
import random

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
time.sleep(7)

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
        if key == UP or key == DOWN or key == LEFT or key == RIGHT:
            time.sleep(0.1)
        pyautogui.keyUp(key)
        print(button_dict[key])
        time.sleep(1)  

# Select File
press_button(A, 4)

# Random behavior
i = 0
while True:
    action = random.choice(random_behavior_list)
    press_button(action)
    if i == 50:
        break
