import time
time.sleep(5)
from pynput.keyboard import Key, Controller
keyboard = Controller()

while True:
	i = 0
	while i<50:
		time.sleep(0.1)
		keyboard.press(Key.right)
		keyboard.release(Key.right)
		i = i+1
	i = 0
	while i<49:
		time.sleep(0.1)
		keyboard.press(Key.left)
		keyboard.release(Key.left)
		i = i+1
	
