import random
import time
import keyboard
import pyautogui
import autopy


possible_moves = ['move_right', 'move_left', 'jump', 'double_jump', 'nail_up', 'nail_right', 'nail_left', 'nail_down',
                  'shade_soul', 'descending_dark', 'abyss_shriek', 'dash', 'cyclone_slash', 'dash_slash', 'great_slash']

possible_moves_mmc = ['double_jump', 'shade_soul', 'descending_dark', 'nail', 'nail', 'nail', 'nail', 'dash']
while True:
    if keyboard.is_pressed('tab'):
        while True:
            #time.sleep(0.2)

            random_move = random.choice(possible_moves_mmc)

            if random_move == 'double_jump':
                keyboard.press('space')
                time.sleep(0.3)
                keyboard.release('space')
                time.sleep(0.1)
                keyboard.press('space')
                time.sleep(0.3)
                keyboard.release('space')
            elif random_move == 'shade_soul':
                keyboard.press_and_release('e')
            elif random_move == 'descending_dark':
                keyboard.press_and_release('space')
                time.sleep(0.4)
                keyboard.press('s')
                keyboard.press_and_release('e')
                keyboard.release('s')
            elif random_move == 'nail':
                pyautogui.click()
            elif random_move == 'dash':
                keyboard.press_and_release('shift')

            if keyboard.is_pressed('backspace'):
                exit()
