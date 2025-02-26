import pyautogui
import time
import requests
import os


# download the fucking miku image
url = 'https://is1-ssl.mzstatic.com/image/thumb/Music221/v4/b8/92/ce/b892cead-70a1-8f29-0045-af30080d3a16/4571640501760_cover.png/316x316bb.webp'

response = requests.get(url)

with open("nice_try.webp", "wb") as file:
        file.write(response.content)

# get the username
username = os.getlogin()

while True:
    print(f'Hi, {username}.')
    pyautogui.press('capslock')
    pyautogui.write('hacked by fake virus? imagine!1!1!!')
    pyautogui.press('enter')
    os.startfile("nice_try.webp")
    time.sleep(0.1)