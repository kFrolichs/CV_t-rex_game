import keyboard # Take control of the keyboard
import mss # Mutliple Screenshots
import cv2
import numpy as np
from time import time, sleep
# import pyautogui # To control mouse and keyboard

print("Press 's' to start playing.")
print("Once started press 'q' to quit")
keyboard.wait('s')

# Settings
cacti = []
cacSz = np.zeros((2,2))
# Small Cactus
cacSmall = cv2.imread('images\cactus_small1.png')
cacti.append(cacSmall)
cacSz[0,0] = int(cacSmall.shape[1]) # Width
cacSz[0,1] = int(cacSmall.shape[0]) # Height
# Big Cactus
cacBig   = cv2.imread('images\cactus_big.png')
cacti.append(cacBig)
cacSz[1,0] = int(cacBig.shape[1]) # Width
cacSz[1,1] = int(cacBig.shape[0]) # Height

game_dim = {
    'left'  : 651,
    'top'   : 200,
    'width' : 250,
    'height': 150
    }
sct = mss.mss()

while True:
    # Get a screenshot of the game window
    scr = np.array(sct.grab(game_dim))

    scr_rem = scr[:,:,:3] # Remove alpha
    for idx, cac in enumerate(cacti):
        result = cv2.matchTemplate(scr_rem, cac, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        # print(f"Max Val: {max_val} Max Loc: {max_loc}")

        if max_val > .85:
            cv2.rectangle(scr, max_loc, (max_loc[0] + int(cacSz[idx,0]), max_loc[1] + int(cacSz[idx,1])), (0,255,0), 2)
            keyboard.press_and_release('space')

    # Stream the game
    cv2.imshow('Screen Shot', scr)
    cv2.waitKey(1)
    sleep(.1)

    if keyboard.is_pressed('q'):
        break
