import requests
import random
from colorama import Fore
import os
import sys
import string
g = Fore.GREEN
r = Fore.RED
b = Fore.BLUE
y = Fore.YELLOW
re = Fore.RESET
l = Fore.LIGHTBLACK_EX
blue = Fore.BLUE
letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]





def drawshit():
    print(f'''
    
{g}    
  /$$$$$$                        /$$     /$$  /$$$$$$          
 /$$__  $$                      | $$    |__/ /$$__  $$         
| $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$   /$$| $$  \__//$$   /$$
|  $$$$$$  /$$__  $$ /$$__  $$|_  $$_/  | $$| $$$$   | $$  | $$
 \____  $$| $$  \ $$| $$  \ $$  | $$    | $$| $$_/   | $$  | $$
 /$$  \ $$| $$  | $$| $$  | $$  | $$ /$$| $$| $$     | $$  | $$
|  $$$$$$/| $$$$$$$/|  $$$$$$/  |  $$$$/| $$| $$     |  $$$$$$$
 \______/ | $$____/  \______/    \___/  |__/|__/      \____  $$
          | $$                                        /$$  | $$
          | $$                                       |  $$$$$$/
          |__/                                        \______/ 
 {y}LMAO
 Github.com/twirdie{re}   
    ''')






def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


url = "https://spclient.wg.spotify.com/signup/public/v1/account"


headers = {
            "Host": "spclient.wg.spotify.com",
            "Content-Type": "application /x-www-form-urlencoded",
            "Connection": "keep-alive",
            "Accept": "*/*",
            "User-Agent": "Spotify/8.5.7iOS/13.5.1(iPhone12, 8)",
            "Accept-Language": "fr, en;q = 0.01",
            "Content-Length": "283",
            "Accept-Encoding": "gzip,deflate,br",
}






def mainfunction():
    os.system("cls")
    drawshit()
    x = input("Ready? Y/N > ")
    if x == "y":
        while True:
            number = 0
            Email = random_char(17)+"@outlook.com.tr"
            password = random_char(5)+"twirdie1337"
            payload=f'birth_day=2&birth_month=02&birth_year=1989&collect_personal_info=undefined&creation_flow=&creation_point=https%3A%2F%2Fwww.spotify.com%2Fus%2F&displayname=twirdie1337&gender=male&iagree=1&key=bff58e9698f40080ec4f9ad97a2f21e0&platform=iOS-ARM&creation_flow=mobile_email&send-email=0&thirdpartyemail=1&email={Email}&password={password}&password_repeat={password}'
            response = requests.request("POST", url, headers=headers, data=payload)
            print(f"[{g}WORKING{y} twirdie1337{re}] " + Email + ":" + password + " (SAVED)")
            hits = open("hits.txt","a")
            hits.write(Email + ":" + password + " | Github.com/twirdie" + "\n")
            hits.close








if __name__ == "__main__":
    mainfunction()
