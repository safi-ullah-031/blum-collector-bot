from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
from termcolor import colored
import keyboard
import random
from pynput.mouse import Button, Controller
mouse = Controller()
time.sleep(0.5)

white = '\033[1;97m'
red = '\033[1;91m'
green = '\033[1;92m'
yellow = '\033[1m\033[93m'
blue = '\033[1;94m'
reset = '\033[0m'
white_red = '\033[97m\033[41m'
white_green = '\033[97m\033[42m'
red_green = '\033[1;91m\033[42m'



"""The code is free to use, and anyone can edit and share it without needing permission.
If someone has a better idea or improvement, they can update the code and push it to the main repository.
The project creators appreciate support, and users can donate using a specific Ton address.
For any queries or issues, users can contact the project maintainers through GitHub or by emailing su439178@gmail.com."""




print(f" {white_red}Github: @safi-ullah-031 {reset}")
print(f" {yellow}Donate (TON) to support us:{white} UQDZcf_U8zGrOJgjNt9zSnsJjJmAgYgrWp6usxzvhgGyYger{reset}")
print(f"{green}If you dont know how this bot works or any other issues just reach me through github")

window_input = f"\n{white} [?] | Press 0 to continue {green}(TelegramDesktop){white}: {reset}"
window_not_found = f"{white} [>] | Your Window - {{}} {yellow}not found!{reset}"
window_found = f"{green} [>] | Window found - {{}}\n{green} Now bot start working... {white}Press {yellow}'Space button'{white} on the keyboard to pause the bot.{reset}"
pause_message = f"{blue} Bot paused...\n{white} Press {yellow}'Space button'{white} again on the keyboard to start again the bot{reset}"
continue_message = f"{blue} Bot start working again...{reset}"

def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)

window_name = input(window_input)

if window_name == '0':
    window_name = "TelegramDesktop"


check = gw.getWindowsWithTitle(window_name)
if not check:
    print(window_not_found.format(window_name))
    print(f" {white_red}Error (404):{reset}\n   {white_red}Make sure you use the TelegramDesktop application (not Telegram Web).{reset}\n   {white_red}And have opened the Blum bot on your Telegram Desktop.{reset}\n   {white_red}Until the Blum window is available{reset}")
else:
    print(window_found.format(window_name))
    telegram_window = check[0]
    paused = False

    while True:
        if keyboard.is_pressed(' '):
            paused = not paused
            if paused:
                print(pause_message)
            else:
                print(continue_message)
            time.sleep(0.2)

        if paused:
            continue

        window_rect = (
            telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
        )

        if telegram_window != []:
            try:
                telegram_window.activate()
            except:
                telegram_window.minimize()
                telegram_window.restore()

        scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))

        width, height = scrn.size
        pixel_found = False
        if pixel_found:
            break

        for x in range(0, width, 20):
            for y in range(0, height, 20):
                r, g, b = scrn.getpixel((x, y))
                if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                    screen_x = window_rect[0] + x
                    screen_y = window_rect[1] + y
                    click(screen_x + 4, screen_y)
                    time.sleep(0.001)
                    pixel_found = True
                    break

                
