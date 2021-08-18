from pynput import keyboard
from pynput.keyboard import Key, Controller
import time
from threading import Thread
from random import randint
from random import uniform

bot_running = False

my_keyboard = Controller()

movement_directions = [keyboard.Key.left, keyboard.Key.right, keyboard.Key.up, keyboard.Key.shift]

def press_key():
    key_probability = randint(0, 100)
    if key_probability < 60:
        my_keyboard.press("c")
        my_keyboard.release("c")
    elif key_probability < 80 and key_probability > 60:
        my_keyboard.press("x")
        my_keyboard.release("x")
        time.sleep(uniform(0, 0.1))
        my_keyboard.press("c")
        my_keyboard.release("c")
    else:
        movement_index = randint(0, 3)

        my_keyboard.press("c")
        my_keyboard.release("c")

        time.sleep(uniform(0, 0.2))

        my_keyboard.press("c")
        my_keyboard.release("c")

        my_keyboard.press(movement_directions[movement_index])
        time.sleep(randint(0, 1))
        my_keyboard.release(movement_directions[movement_index])

def bot_thread():
    my_keyboard.press("c")
    my_keyboard.release("c")
    while bot_running:
        time.sleep(uniform(0, 0.5))
        press_key()

def start_bot():
    global bot_running
    bot_running = True
    thread = Thread(target = bot_thread)
    thread.start()

def stop_bot():
    global bot_running
    bot_running = False
    exit()

def on_press(key):
    try:
        if key == keyboard.Key.home:
            if not bot_running:
                start_bot()
            else:
                stop_bot()
    except AttributeError:
            print('special key {0} pressed'.format(
            key))

def on_release(key):
    return

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
