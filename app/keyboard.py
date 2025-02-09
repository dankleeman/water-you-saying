import time
import typer
import sys
from pynput.keyboard import Key, KeyCode, Controller, Listener

keyboard = Controller()
ctrl_key = Key.ctrl_l
shift_key = Key.shift_l
esc_key = Key.esc
trigger_key = KeyCode(char='I')
key_combo = [ctrl_key, shift_key, trigger_key]
keys_pressed = set()

def output(msg):
    keyboard.type(msg)

def on_press(key):
    if key in key_combo:
        keys_pressed.add(key)

def on_release(key):
    if all(key in keys_pressed for key in key_combo):
        keys_pressed.clear()
        return False

    if key in key_combo:
        keys_pressed.discard(key)

    if key == esc_key:
        sys.exit()

def wait_until_shortcut():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
