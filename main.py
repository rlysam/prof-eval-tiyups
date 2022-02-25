# isang run per active tab ng evaluation form
# Read README.md

import pyautogui
import time

pyautogui.alert(text='Press ok and wait 3 sec', title='', button='OK')
time.sleep(3)
hasBack = False
n = 4
outstanding = False

def moveCursor():
	for x in range(1): # pag 0, "Outstanding", pag 4, yung lowest na "Poor" ata yon
		pyautogui.hotkey('left') 

def rate5s():
	for x in range(n):
		pyautogui.hotkey('shift', 'tab') 
	moveCursor() if not outstanding else pyautogui.hotkey('space') 
	for x in range(4):
		pyautogui.hotkey('shift', 'tab') 
		moveCursor() if not outstanding else pyautogui.hotkey('space') 

def next():
	for x in range(3):
		pyautogui.hotkey('shift', 'tab') 
	pyautogui.hotkey('enter') 

def pasteText():
	for x in range(6):
		pyautogui.hotkey('shift', 'tab') 
	pyautogui.write('Palitan mo nalang to ng gusto mo sabihin', interval=0.01)


for x in range(4):
	if hasBack is True:
		n = 5
	rate5s()
	next()
	hasBack = True

pasteText()