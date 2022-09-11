from pynput import keyboard
import pyautogui
from utils import load_positions, write_position
import random

BOT_DELAY = 0.05
pyautogui.PAUSE = BOT_DELAY

def auto_loot():
    POSITIONS = load_positions()

    random.shuffle(POSITIONS)

    for pos in POSITIONS:
        pyautogui.click(button='right', x=pos['x'], y=pos['y'])

def on_press(key):
    try:
        if key.char == 'r':
            auto_loot()

    except:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False
    elif key == keyboard.Key.f12:
        set_position()

def set_position():
    position = pyautogui.position()
    write_position(position)

def main():
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()