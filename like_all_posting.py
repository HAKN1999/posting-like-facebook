from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

sleep(3)

while True:

    keyboard.press("j")
    keyboard.release("j")

    sleep(1)
    keyboard.press("l")
    keyboard.release("l")

    sleep(1)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    sleep(3)
