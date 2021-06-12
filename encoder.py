from gpiozero import RotaryEncoder, Button
import keyboard, threading

rotor = RotaryEncoder(16, 20)
button = Button(12)

def up():
    keyboard.press_and_release('up')
def down():
    keyboard.press_and_release('down')
def enter():
    keyboard.press_and_release('enter')

def rotation():
    while True:
        if rotor.wait_for_rotate():
            rotor.when_rotated_clockwise = up
            rotor.when_rotated_counter_clockwise = down
def press():
    while True:
        button.when_pressed = enter

t1 = threading.Thread(target=rotation)
t2 = threading.Thread(target=press)
t1.start()
t2.start()
