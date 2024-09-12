# EN. Do Not Modify Any Script Of Code Or Copy It And Say As its Own.
# EN. WARNING! By Opening The App User Agrees To Take Full Responcibility For Every Acrion
#
# PL. Nie Modifikuj nic z skruptu lub nie Kopiuj Tego Kodu I Nie Dawaj Kredytu Na Siebie :)
# PL. OSTRZENIE! Przez  Otwieranie Aplikacji Użytkownik Akceptuje Brania pełnej odpowiedzialnośći
#
# PL. W Tym Skryptie Troche użyłem chatugpt więc nom żeby nie było że jakieś spamy ze chat gpt :)
# PL. To Tak... Jestem Polakiem I Moją Inspiracją Był "RedTiger" tylko że on był francuski a ja nie francus (mówię to bo nudzi mi sie) a no wyślijcie propozycje do updatuw bo nie skończyłem ich robić  
# PL. Będe Pisał Kiedy chat gpt jest użyto od teraz
# PL. Nie Zmieniaj kodu prosze
# PL. Miłego Dnia -VenoDev




import os
import sys
import time
import subprocess
import urllib
import socket
import random
import urllib.request
import colorama
from colorama import Fore, Style
import requests
import webbrowser
import string
import requests
from datetime import datetime



os.system('title PyWine-Multi-Tool 1.0 [Beta]')
colorama.init()

# Definitions :)

def get_roblox_user_info(user_id):
    url = f"https://users.roblox.com/v1/users/{user_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # This will return the user info as a dictionary
    else:
        return {"error": f"Unable to fetch user info. Status code: {response.status_code}"}
def print_user_info(user_info):
    if "error" in user_info:
        slow_print(f"{Fore.MAGENTA}Error:{Style.RESET_ALL} {user_info['error']}")
    else:
        formatted_info = (
            f"{Fore.MAGENTA}User Information:{Style.RESET_ALL}\n"
            f"{Fore.MAGENTA}ID:{Style.RESET_ALL} {user_info.get('id')}\n"
            f"{Fore.MAGENTA}Name:{Style.RESET_ALL} {user_info.get('name')}\n"
            f"{Fore.MAGENTA}Display Name:{Style.RESET_ALL} {user_info.get('displayName')}\n"
            f"{Fore.MAGENTA}Description:{Style.RESET_ALL} {user_info.get('description')}\n"
            f"{Fore.MAGENTA}Created:{Style.RESET_ALL} {user_info.get('created')}\n"
            f"{Fore.MAGENTA}Is Banned:{Style.RESET_ALL} {user_info.get('isBanned')}\n"
            f"{Fore.MAGENTA}Has Verified Badge:{Style.RESET_ALL} {user_info.get('hasVerifiedBadge')}\n"
            f"{Fore.MAGENTA}External App Display Name:{Style.RESET_ALL} {user_info.get('externalAppDisplayName')}\n"
        )
        
        # Printing each line even faster
        for line in formatted_info.split('\n'):
            slow_print(line, delay=0.005)  # Very fast line printing
def scan_ips():
    command = 'ipconfig'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout or result.stderr
    
    return output
def get_public_ip():
    try:
        # Query an external service to get the public IP address
        with urllib.request.urlopen('http://api.ipify.org') as response:
            public_ip = response.read().decode('utf-8')
    except Exception as e:
        return f"Error fetching public IP: {e}"
    
    return public_ip
def get_local_ip():
    try:
        # Create a socket and connect to a remote server
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))  # Google's DNS server
        local_ip = s.getsockname()[0]
    finally:
        s.close()
    
    return local_ip
def generate_code(length=18):
    """Generate a random alphanumeric string of the specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
def check_code(code, webhook_url):
    """Send a GET request to the Discord gift code URL with the generated code."""
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Valid code found: {code}")
            send_to_webhook(code, webhook_url)
        else:
            print(f"Invalid code: {code} - Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
def send_to_webhook(valid_code, DISCORD_WEBHOOK_URL):
    """Send the valid code to the Discord webhook."""
    data = {
        "content": f"Valid code found: {valid_code}",
        "username": "Gift Code Bot"
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        if response.status_code == 204:
            print(f"Successfully sent code {valid_code} to webhook.")
        else:
            print(f"Failed to send code to webhook. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send webhook: {e}")
def Start_Nitro_Gen():
    """Continuously generate and check random codes."""
    webhook = input("Ur Webhook URL")
    while True:
        code = generate_code()
        check_code(code, webhook)
def discord_icon():
    slow_print("""YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYJ?7!~^::.!YYYYYYYYYYYYYYYYYYYY!.::^~!7?JYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYJ?!~^:.         !JJJ????7777????JJJ!         .:^~!?JYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY?^.                 ..              ..                 .^?YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYY!.                                                         !YYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYY~                                                            ~YYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYJ:                                                              :JYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYJ:                                                                :JYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYJ.                                                                  .JYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYJ:                                                                    :JYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYY:                                                                      :YYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYY~                                                                        ~YYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYY7                     .:::.                      .:::.                     7YYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYY:                  .!?JYYYYJ7:                :7JYYYYJ?!.                  :YYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYY!                  ^JYYYYYYYYYY7              7YYYYYYYYYYJ^                  !YYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYY:                 :YYYYYYYYYYYYY!            !YYYYYYYYYYYYY:                 :YYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYY?                  ~YYYYYYYYYYYYY?            ?YYYYYYYYYYYYY~                  ?YYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYY~                  :YYYYYYYYYYYYY~            ~YYYYYYYYYYYYY:                  ~YYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYY^                   ^JYYYYYYYYYY!              !YYYYYYYYYYJ^                   ^YYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYY:                    .~7JJYYJ?!:                :!?JYYJJ7~.                    :YYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYJ.                        ....                      ....                        .JYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYJ.                                                                              .JYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYY.                                                                              .YYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYY:                  ::                                      ::                  :YYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYY?^.               .7JJ7!^:.                          .:^!7JJ7.               .^?YYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYJ7~.              .:~!?YJJ?7!!~^^^::::::::^^^~!!7?JJY?!~:               .~7JYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYY?!^.              7YYYYYYYYYYYYYYYYYYYYYYYYYYYYYY7              .^!?YYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYJ?!^:.       :JYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYJ:       .:^!?JYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYJ?!~^:.~YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY~.:^~!?JYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY""")
def dox_icon():
    slow_print("""                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                       .:^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^:.                      
                                     :?5PGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGPY!.                   
                                    !PBGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGY:                  
                                   :5PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGGGGGGGGGGB?                  
                                   ......................................................:^!YGGGGGGGGJ                  
                                                                                            .~PGGGGGG?                  
                                                                                              !GGGGGG?                  
                        :~?JYJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ7~.        ^GGGGGG?                  
                      .?PGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG5!.      ^GGGGGG?                  
                      JGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG!      ^GGGGGG?                  
                     .GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGY      ^GGGGGG?                  
                     .GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGY      ^GGGGGG?                  
                     .GGGGGGGGGGGGGGGGGGGGGGGGGGP5YJJ????JJY5PGGGGGGGGGGGGGGGGGGGGGGGGGY      ^GGGGGG?                  
                     :GGGGGGGGGGGGGGGGGGGGGPY?!^..          .:^!J5GGGGGGGGGGGGGGGGGGGGGY      ^GGGGGG?                  
                     :GGGGGGGGGGGGGGGGGGPY!:.                    .^75GGGGGGGGGGGGGGGGGGY      ^GGGGGG?                  
                     :GGGGGGGGGGGGGGGGPJ^.        ..::::::.         .~YGGGGGGGGGGGGGGGGY      ^GGGGGG?                  
                     :GGGGGGGGGGGGGGGJ^       .^7J5PPPGGPP5Y?!:        ~5GGGGGGGGGGGGGGY      ^GGGGGG?                  
                     :GGGGGGGGGGGGGG7.      ^?5GGGGGGGGGGGGGGGG57:      .?GGGGGGGGGGGGGY      ^GGGGGG?                  
                     :GGGGGGGGGGGGP!      .?PGGGGGGGGGGGGGGGGGGGGP!.      ?GGGGGGGGGGGGY      ^GGGGGG?                  
                     :GGGGGGGGGGGG7      :5GGGGGGGGGGGGGGGGGGGGGGGGJ.     .JGGGGGGGGGGGY      ^GGGGGG?                  
                     :GGGGGGGGGGG5.     .YGGGGGGGGGGGGGGGGGGGGGGGGGG?      :GGGGGGGGGGGY      ^GGGGGG?                  
                     :GGGGGGGGGGG7      ~GGGGGGGGGGGGGGGGGGGGGGGGGGGP^      YGGGGGGGGGGY      ^GGGGGG?                  
                     :GGGGGGGGGPG!      7GGGGGGGGGGGGGGGGGGGGGGGGGGGG~      ?GGGGGGGGGGY      ^GGGGGG?                  
                     :GGGGGGGGGGG7      !GGGGGGGGGGGGGGGGGGGGGGGGGGGG^      JGGGGGGGGGGY      ^GGGGGG?                  
                     :GGGGGGGGGGGY      :5GGGGGGGGGGGGGGGGGGGGGGGGGGJ.     :PGGGGGGGGGGY      ^GGGGGG?                  
                     :GGGGGGGGGGGG~      ^PGGGGGGGGGGGGGGGGGGGGGGGGY:      ?GGGGGGGGGGGY      ^GGGGGG?                  
                     :GGGGGGGGGGGGP^      ^YGGGGGGGGGGGGGGGGGGGGGG?.      !GGGGGGGGGGGGY      ^GGGGGG?                  
                     :GGGGGGGGGGGGGP~      .~JPGGGGGGGGGGGGGGGGPJ^      .7GGGGGGGGGGGGGY      ~GGGGGG?                  
                     :GGGGGGGGGGGGGGP?.      .:!J5PGGGGGGGPPY?~:        ^PGGGGGGGGGGGGGY      ^GGGGGG?                  
                     :GGGGGGGGGGGGGGGG5!.        .:^~~!~~~:.             :!5GGGGGGGGGGGY      ^GGGGG5^                  
                     :GGGGGGGGGGGGGGGGGGP?^.                               .!YGGGGGGGGGY      ^GGGP?:                   
                     :GGGGGGGGGGGGGGGGGGGGG5J!^.             .:~7?J??~.      .~YGGGGGGGY      :!!^.                     
                     :GGGGGGGGGGGGGGGGGGGGGGGGGP5J?7!!!!!!7?Y5PGGGGGGGY~.      .~JGGGGGY                                
                     .GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG5!.       ^JPGGY                                
                     .GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG57:       :?PY                                
                     .YGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGP?:       :~                                
                      :YGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGP?^                                       
                        ^?Y5555555555555555555555555555555555555555555555555555P57:                                     
                           ........................................................                                     
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        """)
def roblox_icon():
    slow_print("""@@&G5JJ??JJJJJJJJJJJJJJJJJJYYYYYYYYYYYYYYYYYYYY555555555555555555PPPPPPPPPPPPPPPPPPPGGGGGGGGGGGGGGGGGGGBBBBBBBBBBB##&@@@
@GJ????JJJJJJJJJJJJJJJJJJYYYYYYYYYYYYYYYYYYY5555555555555555555PPPPPPPPPPPPPPPPPPPGGGGGGGGGGGGGGGGGGBBBBBBBBBBBBBBBBB#&@
P???JJJJJJJJJJJJJJJJJJYYYYYYYYYYYYYYYYYYY5555555555555555555PPPPPPPPPPPPPPPPPPPGGGGGGGGGGGGGGGGGGBBBBBBBBBBBBBBBBBBB###&
J?JJJJJJJJJJJJJJJJJYYYYYYYYYYYYYYYYYYY5555555555555555555PPPPPPPPPPPPPPPPPPPGGGGGGGGGGGGGGGGGGGBBBBBBBBBBBBBBBBBB#######
JJJJJJJJJJJJJJJJJYYYYYYYYYYYYYYYYYYY5555555555555555555PPPPPPPPPPPPPPPPPPPGGGGGGGGGGGGGGGGGGBBBBBBBBBBBBBBBBBB##########
JJJJJJJJJJJJJJYYYYYYYYYYYYYYYYYYY5555555555555555555PPPPPPPPPPPPPPPPPPPGGGGGGGGGGGGGGGGGGBBBBBBBBBBBBBBBBBB#############
JJJJJJJJJJJYYYYYYYYYYYYYYYYYYY5555555555555555555PPPPPPPPPPPPPPPPPPPGGGGGGGGGGGGGGGGGGBBBBBBBBBBBBBBBBBBB###############
JJJJJJJJJYYYYYYYYYYYYYYYYYYY55555Y?JYY55PPPPPPPPPPPPPPPPPPPPPPPPPPGGGGGGGGGGGGGGGGGGBBBBBBBBBBBBBBBBBB##################
JJJJJJYYYYYYYYYYYYYYYYYYY55555555!...:^~!7?JY55PPPPPPPPPPPPPPPPGGGGGGGGGGGGGGGGGGBBBBBBBBBBBBBBBBBB###################&&
JJJYYYYYYYYYYYYYYYYYYY5555555555J...........::^~!7?JY5PPGGGGGGGGGGGGGGGGGGGGGGGBBBBBBBBBBBBBBBBBB##################&&&&&
YYYYYYYYYYYYYYYYYYYY555555555555~...................::^~!7?JY5PGGGBBGGGGGGGGBBBBBBBBBBBBBBBBBB##################&&&&&&&&
YYYYYYYYYYYYYYYYY5555555555555P?........::::::::::::::::::::::^~!7?J5PGGBBBBBBBBBBBBBBBBBBB###################&&&&&&&&&&
YYYYYYYYYYYYYY55555555555555555^....::::::::::::::::::::::::::::::::::^~!7?J5PGBBB#########################&&&&&&&&&&&&&
YYYYYYYYYYYY55555555555555555P7..::::::::::::::::::::::::::::::::::::::::::::^^~!7?Y5PGB################&&&&&&&&&&&&&&&&
YYYYYYYYY5555555555555555555P5:.:::::::::::::::::::::::::::::::::::::^^^^^^^^^^^:::::^^~!7?Y5PGB##&&&&&&&&&&&&&&&&&&&&&&
YYYYYY5555555555555555555PPPP!.:::::::::::::::::::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~!7?Y5PGB&&&&&&&&&&&&&&&&
YYY5555555555555555555PPPPPPY::::::::::::::::::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!#&&&&&&&&&&&&&&&
Y5555555555555555555PPPPPPPP!.::::::::::::::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^5@&&&&&&&&&&&&&&&
55555555555555555PPPPPPPPPPJ::::::::::::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~^7&@@@&&&&&&&&&&&&&
55555555555555PPPPPPPPPPPPP~:::::::::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~^G@@@@@&&&&&&&&&&&&
555555555555PPPPPPPPPPPPPGJ:::::::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~^?@@@@@@&&&&&&&&&&&&
555555555PPPPPPPPPPPPPPPPP^:::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~B@@@@@@&&&&&&&&&&&&
555555PPPPPPPPPPPPPPPPPPG?:::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~^J@@@@@@&&&&&&&&&&&&&
5555PPPPPPPPPPPPPPPPPPPGP^::::::::::::::^^^^^^^^^^^^^^^:::^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~!#@@@@@@&&&&&&&&&&&&&
5PPPPPPPPPPPPPPPPPPPGGGG7:::::::::::^^^^^^^^^^^^^^^^^^!P5J?!~^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~^5@@@@@@&&&&&&&&&&&&&&
PPPPPPPPPPPPPPPPPGGGGGG5:::::::::^^^^^^^^^^^^^^^^^^^^^P@@@@@&#BP5J?!~^^^^^^~~~~~~~~~~~~~~~~~~~~~~~!&@@@@@@&&&&&&&&&&&&&&
PPPPPPPPPPPPPPGGGGGGGGG!::::::^^^^^^^^^^^^^^^^^^^^^^^7@@@@@@@@@@@@@&!^^^~~~~~~~~~~~~~~~~~~~~~~~~~~P@@@@@@@&&&&&&&&&&&&&&
PPPPPPPPPPPPGGGGGGGGGGY:::^^^^^^^^^^^^^^^^^^^^^^^^^^^G@@@&&&&&&&&&@P^~~~~~~~~~~~~~~~~~~~~~~~~~~~~?@@@@@@@&&&&&&&&&&&&&&&
PPPPPPPPPGGGGGGGGGGGGG!:^^^^^^^^^^^^^^^^^^^^^^^^^^^^?@@@@&&&&&&&&&#!^~~~~~~~~~~~~~~~~~~~~~~~~~~~~G@@@@@@@&&&&&&&&&&&&&&&
PPPPPPGGGGGGGGGGGGGGBY:^^^^^^^^^^^^^^^^^^^^^^^^^^^^^B@@@&&&&&&&&&&Y^~~~~~~~~~~~~~~~~~~~~~~~~~~~~J@@@@@@@@&&&&&&&&&&&&&&@
PPPPGGGGGGGGGGGGGGGGG~:^^^^^^^^^^^^^^^^^^^^^^^^^^^^7B&&@@@@&&&&&&#!~~~~~~~~~~~~~~~~~~~~~~~~~~~~!#@@@@@@@&&&&&&&&&&&&&&&&
PGGGGGGGGGGGGGGGGGGBJ:^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~!7?Y5PGB#&&Y^~~~~~~~~~~~~~~~~~~~~~~~~~~~~Y@@@@@@@@&&&&&&&&&&@&&@@@
GGGGGGGGGGGGGGGGGBBG~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~!7?~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!&@@@@@@@@&&&&&&&&&&&@@@@@
GGGGGGGGGGGGGGBBBBB?:^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!~5@@@@@@@@@&&&&@&&&@@@@@@@@
GGGGGGGGGGGBBBBBBBP^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!~7&@@@@@@@@@&&@&&@@@@@@@@@@@
GGGGGGGGBBBBBBBBBB?^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!~G@@@@@@@@@@&&&@@@@@@@@@@@@@
GGGGGGBBBBBBBBBBBP^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!~?@@@@@@@@@@&@@@@@@@@@@@@@@@@
GGGBBBBBBBBBBBBBB7^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!B@@@@@@@@@@@@@@@@@@@@@@@@@@@
BBBBBBBBBBBBBBB#5^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@
BBBBBBBBBBBBBB#B!^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!#@@@@@@@@@@@@@@@@@@@@@@@@@@@@
BBBBBBBBBBBBB##BYJ7!~~^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
BBBBBBBBBBB##########BGP5J?7!~~^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!7&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
BBBBBBBB###########&&&&@@@@&&#BP5Y?7!~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!P@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
BBBBB###############&&&&&&&&@@@@@@@@&#BGPYJ?7!~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!?@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
BB##################&&&&&&&&&&&&&&@@@@@@@@@@&#BGP5J?7!!~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##################&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@&&#BP5YJ?7!!!~~!!!!!!!!!!!!!!!!!!!!J@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
################&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@&#BGP5J?77!!!!!!!!!!!!!!!7#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#############&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@&&#BP5YJ?77!!!!!!Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##########&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@&#BGPYJJ#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
########&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#####&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")
def create_dox_file():
    import sys
    from colorama import Fore, Style
    from time import sleep

    BOLD = Style.BRIGHT

    # Define a function for slow printing text
    def slow_print(text, delay=0.0001):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(delay)
        print()

    # Prompt for the file name
    name = input("Enter File Name: ")      
    filename = f"{name}.txt"   

    # Open file within the 'with' block to ensure it's not closed prematurely
    with open(filename, "w") as file:
        # Writing the banner to the file
        file.write("""
 ██▓███ ▓██   ██▓ █     █░ ██▓ ███▄    █ ▓█████    ▓█████▄  ▒█████  ▒██   ██▒
▓██░  ██▒▒██  ██▒▓█░ █ ░█░▓██▒ ██ ▀█   █ ▓█   ▀    ▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░
▓██░ ██▓▒ ▒██ ██░▒█░ █ ░█ ▒██▒▓██  ▀█ ██▒▒███      ░██   █▌▒██░  ██▒░░  █   ░
▒██▄█▓▒ ▒ ░ ▐██▓░░█░ █ ░█ ░██░▓██▒  ▐▌██▒▒▓█  ▄    ░▓█▄   ▌▒██   ██░ ░ █ █ ▒ 
▒██▒ ░  ░ ░ ██▒▓░░░██▒██▓ ░██░▒██░   ▓██░░▒████▒   ░▒████▓ ░ ████▓▒░▒██▒ ▒██▒
▒▓▒░ ░  ░  ██▒▒▒ ░ ▓░▒ ▒  ░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░    ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
░▒ ░     ▓██ ░▒░   ▒ ░ ░   ▒ ░░ ░░   ░ ▒░ ░ ░  ░    ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░
░░       ▒ ▒ ░░    ░   ░   ▒ ░   ░   ░ ░    ░       ░ ░  ░ ░ ░ ░ ▒   ░    ░  
         ░ ░         ░     ░           ░    ░  ░      ░        ░ ░   ░    ░  
         ░ ░                                        ░                                                           
        """)

        # Collecting data from the user
        AuthorName = input("[>] | Doxed By      :")   
        Reason = input("[>] | Reason        :") 
        FP = input("[>] | First Pseudo  :")
        SP = input("[>] | Second Pseudo :")

        slow_print(f"{BOLD}{Fore.MAGENTA}[{Fore.RED}!{Fore.MAGENTA}]{Fore.WHITE} Discord Information:")
        DS_T = input("[>] | Token      :")
        DS_USER = input("[>] | Username      :")
        DS_DN = input("[>] | Display Name  :")
        DS_ID = input("[>] | Id            :")
        DS_AV = input("[>] | Avatar        :")
        DS_CA = input("[>] | Created At    :")
        DS_EM = input("[>] | Email         :")
        DS_PH = input("[>] | Phone         :")
        DS_NT = input("[>] | Nitro         :")
        DS_FR = input("[>] | Friends       :")
        DS_GC = input("[>] | Gift Code     :")
        DS_MFA = input("[>] | Mfa           :")

        slow_print(f"{BOLD}{Fore.MAGENTA}[{Fore.RED}!{Fore.MAGENTA}]{Fore.WHITE} IP Information:")
        IP_PB = input("[>] | Ip Publique   :")
        IP_LOC = input("[>] | Ip Local      :")
        IP_IPV6 = input("[>] | Ipv6          :")
        IP_VPN = input("[>] | VPN           :")

        slow_print(f"{BOLD}{Fore.MAGENTA}[{Fore.RED}!{Fore.MAGENTA}]{Fore.WHITE} PC Information:")
        PC_NM = input("[>] | Name          :")
        PC_USRN = input("[>] | Username      :")
        PC_DN = input("[>] | Display Name  :")
        PC_PLA = input("[>] | Plateform     :")
        PC_EX = input("[>] | Exploitation  :")
        PC_KEY = input("[>] | Windows Key   :")
        PC_MADD = input("[>] | MAC Adress    :")
        PC_HWID = input("[>] | HWID Adress   :")
        PC_CPU = input("[>] | CPU           :")
        PC_GPU = input("[>] | GPU           :")
        PC_RAM = input("[>] | RAM           :")
        PC_DSK = input("[>] | Disk          :")
        PC_SM = input("[>] | Screen Main   :")
        PC_SS = input("[>] | Screen Sec    :")

        slow_print(f"{BOLD}{Fore.MAGENTA}[{Fore.RED}!{Fore.MAGENTA}]{Fore.WHITE} Number Information:")
        N_N = input("[>] | Phone Number  :")
        N_B = input("[>] | Brand         :")

        slow_print(f"{BOLD}{Fore.MAGENTA}[{Fore.RED}!{Fore.MAGENTA}]{Fore.WHITE} Personal Information:")
        P_G = input("[>] | Gender        :")
        P_LN = input("[>] | Last Name     :")
        P_FN = input("[>] | First Name    :")
        P_A = input("[>] | Age           :")
        P_MO = input("[>] | Mother        :")
        P_FA = input("[>] | Father        :")
        P_B = input("[>] | Brother       :")
        P_SIS = input("[>] | Sister        :")

        slow_print(f"{BOLD}{Fore.MAGENTA}[{Fore.RED}!{Fore.MAGENTA}]{Fore.WHITE} Loc Information:")
        L_C = input("[>] | Continent     :")
        L_CY = input("[>] | Country       :")
        L_R = input("[>] | Region        :")
        L_PC = input("[>] | Postal Code   :")
        L_CITY = input("[>] | City          :")
        L_ADD = input("[>] | Adress        :")
        L_TZ = input("[>] | Timezone      :")
        L_LG = input("[>] | Longitude     :")
        L_LA = input("[>] | Latitude      :")

        slow_print(f"{BOLD}{Fore.MAGENTA}[{Fore.RED}!{Fore.MAGENTA}]{Fore.WHITE} Social Information:")
        S_PASS = input("[>] | Password      :")
        S_GM = input("[>] | Email         :")

        slow_print(f"{BOLD}{Fore.MAGENTA}[{Fore.RED}!{Fore.MAGENTA}]{Fore.WHITE} Other:")
        O_O = input("[>] | Other         :")
        O_DB = input("[>] | DataBase      :")
        O_L = input("[>] | Logs          :")

        # Write all collected data to the file
        file.write(f"Doxxed By: {AuthorName}\n")
        file.write(f"Reason: {Reason}\n")
        file.write(f"{'='*80}\n")
        file.write("Pseudo Info:\n")
        file.write(f"First Pseudo: {FP}\n")
        file.write(f"Second Pseudo: {SP}\n")
        file.write(f"{'='*80}\n")
        file.write(f"Discord Information:\n")
        file.write(f"Discord Token: {DS_T}\n")
        file.write(f"Discord Username: {DS_USER}\n")
        file.write(f"Discord Display Name: {DS_DN}\n")
        file.write(f"Discord Id: {DS_ID}\n")
        file.write(f"Discord Avatar: {DS_AV}\n")
        file.write(f"Created At: {DS_CA}\n")
        file.write(f"Discord Email: {DS_EM}\n")
        file.write(f"Discord Phone Number: {DS_PH}\n")
        file.write(f"Discord Nitro: {DS_NT}\n")
        file.write(f"Discord Friends: {DS_FR}\n")
        file.write(f"Discord Gift Code: {DS_GC}\n")
        file.write(f"mfa: {DS_MFA}\n")
        file.write(f"{'='*80}\n")
        file.write("IP Information:\n")
        file.write(f"Public Ip: {IP_PB}\n")
        file.write(f"Local Ip: {IP_LOC}\n")
        file.write(f"Ipv6: {IP_IPV6}\n")
        file.write(f"VPN: {IP_VPN}\n")
        file.write(f"{'='*80}\n")
        file.write("PC Information:\n")
        file.write(f"PC Name: {PC_NM}\n")
        file.write(f"Pc User: {PC_USRN}\n")
        file.write(f"PC Display Name: {PC_DN}\n")
        file.write(f"Platform: {PC_PLA}\n")
        file.write(f"PC Exploitation: {PC_EX}\n")
        file.write(f"Windows Key: {PC_KEY}\n")
        file.write(f"MAC Adress: {PC_MADD}\n")
        file.write(f"HWID Adress: {PC_HWID}\n")
        file.write(f"CPU: {PC_CPU}\n")
        file.write(f"GPU: {PC_GPU}\n")
        file.write(f"RAM: {PC_RAM}\n")
        file.write(f"Disk: {PC_DSK}\n")
        file.write(f"Screen Main: {PC_SM}\n")
        file.write(f"Screen Sec: {PC_SS}\n")
        file.write(f"{'='*80}\n")
        file.write("Number Information:\n")
        file.write(f"Phone Number: {N_N}\n")
        file.write(f"Brand: {N_B}\n")
        file.write(f"{'='*80}\n")
        file.write("Personal Information:\n")
        file.write(f"Gender: {P_G}\n")
        file.write(f"Last Name: {P_LN}\n")
        file.write(f"First Name: {P_FN}\n")
        file.write(f"Age: {P_A}\n")
        file.write(f"Mother: {P_MO}\n")
        file.write(f"Father: {P_FA}\n")
        file.write(f"Brother: {P_B}\n")
        file.write(f"Sister: {P_SIS}\n")
        file.write(f"{'='*80}\n")
        file.write("Location Information:\n")
        file.write(f"Continent: {L_C}\n")
        file.write(f"Country: {L_CY}\n")
        file.write(f"Region: {L_R}\n")
        file.write(f"Postal Code: {L_PC}\n")
        file.write(f"City: {L_CITY}\n")
        file.write(f"Address: {L_ADD}\n")
        file.write(f"Timezone: {L_TZ}\n")
        file.write(f"Longitude: {L_LG}\n")
        file.write(f"Latitude: {L_LA}\n")
        file.write(f"{'='*80}\n")
        file.write("Social Information:\n")
        file.write(f"Password: {S_PASS}\n")
        file.write(f"Email: {S_GM}\n")
        file.write(f"{'='*80}\n")
        file.write("Other Information:\n")
        file.write(f"Other: {O_O}\n")
        file.write(f"Database: {O_DB}\n")
        file.write(f"Logs: {O_L}\n")
        file.write(f"{'='*80}\n")
        file.write(f"Free Template By https://github.com/ggvenodev :)")

    # Confirm file creation
    print(f"Dox file '{filename}' has been successfully created.")
def send_repeated_message(webhook_url, message_content, interval=5):
    """
    Sends a message to a Discord channel using a webhook repeatedly.

    :param webhook_url: The Discord webhook URL.
    :param message_content: The content of the message to send.
    :param interval: The time in seconds between messages.
    """
    while True:
        now = datetime.now()
        # Send the message using a POST request
        response = requests.post(webhook_url, json={"content": message_content})

        # Check if the message was sent successfully
        if response.status_code == 204:
            print(f"{Fore.GREEN}[{Fore.WHITE}{now.hour}:{now.minute}:{now.second}{Fore.GREEN}] [{Fore.WHITE}+{Fore.GREEN}] | {Fore.WHITE}Status: {Fore.GREEN}Valid{Fore.WHITE} | Code:{Fore.GREEN}{response.status_code}")
        else:
            print(f"{Fore.RED}[{Fore.WHITE}{now.hour}:{now.minute}:{now.second}2{Fore.RED}] [{Fore.WHITE}x{Fore.RED}] | {Fore.WHITE}Status: {Fore.RED}Invalid{Fore.WHITE} | Code:{Fore.RED}{response.status_code}")

        # Wait before sending the message again
        time.sleep(interval)
def ping_ip(ip):
    while True:
        # Chat Gpt
        try:
            # Ping the IP address
            output = subprocess.check_output(["ping", "-n", "1", ip], universal_newlines=True)
            slow_print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] | {ip} | Status: {Fore.GREEN} Succes")
        except subprocess.CalledProcessError:
            slow_print(f"{Fore.WHITE}[{Fore.RED}x{Fore.WHITE}] | {ip} | Status: {Fore.RED} Fail")
        
        # Wait for 1 second before pinging again
        time.sleep(1)

# ANSI escape codes for purple, white, reset colors, and bold text
PURPLE = '\033[95m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'
USERM = subprocess.run('echo %USERNAME%', shell=True, capture_output=True, text=True)
USER = USERM.stdout.strip() if USERM.stdout else USERM.stderr.strip()
COMPUTERM = subprocess.run('echo %COMPUTERNAME%', shell=True, capture_output=True, text=True)
COMPUTER = COMPUTERM.stdout.strip() if COMPUTERM.stdout else COMPUTERM.stderr.strip()




# Remove spaces and underscores
USER = USER.replace(' ', '').replace('_', '')
COMPUTER = COMPUTER.replace(' ', '').replace('_', '')


def slow_print(text, delay=0.0001):
    """Print text with a slow typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline after the text finishes printing

def print_menu(page):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

    # Title section with slow print
    slow_print(f"{PURPLE}{BOLD}{'='*80}")
    slow_print(f"""{PURPLE}{BOLD}
 ██▓███ ▓██   ██▓ █     █░ ██▓ ███▄    █ ▓█████ 
▓██░  ██▒▒██  ██▒▓█░ █ ░█░▓██▒ ██ ▀█   █ ▓█   ▀ 
▓██░ ██▓▒ ▒██ ██░▒█░ █ ░█ ▒██▒▓██  ▀█ ██▒▒███   
▒██▄█▓▒ ▒ ░ ▐██▓░░█░ █ ░█ ░██░▓██▒  ▐▌██▒▒▓█  ▄ 
▒██▒ ░  ░ ░ ██▒▓░░░██▒██▓ ░██░▒██░   ▓██░░▒████▒
▒▓▒░ ░  ░  ██▒▒▒ ░ ▓░▒ ▒  ░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░
░▒ ░     ▓██ ░▒░   ▒ ░ ░   ▒ ░░ ░░   ░ ▒░ ░ ░  ░
░░       ▒ ▒ ░░    ░   ░   ▒ ░   ░   ░ ░    ░   
         ░ ░         ░     ░           ░    ░  ░
         ░ ░                                    
                                                   
""")
    slow_print(f"{PURPLE}{'='*80}")
    slow_print(f"{WHITE}PyWine Tools - (https://github.com/pywine/pywine-multi-tools){RESET}\n")

    # Pages of options
    if page == 1:
        # Page 1: Main Menu and Virus Builder
        slow_print(f"{PURPLE}{BOLD}{'─'*80}")
        slow_print(f"{WHITE} Scanner")
        slow_print(f"{PURPLE}{BOLD}{'─'*80}{RESET}\n")

        slow_print(f"{WHITE}[I] Info {PURPLE}| {WHITE}[S] Site")

        # Virus Builder Section
        slow_print(f"\n{WHITE}[01] Scan For Ips\n")
        slow_print(f"\n{WHITE}[02] - GeoLocate Public Addres\n")
        slow_print(f"\n{WHITE}[03] - Ping Ip")

        # Navigation options
        slow_print(f"\n{PURPLE}{BOLD}{'─'*80}")
        slow_print(f"{WHITE}[N] Next {PURPLE}| {WHITE}[B] Back")
        slow_print(f"{PURPLE}{'─'*80}{RESET}")

    elif page == 2:
        # Page 2: Roblox Section
        slow_print(f"{PURPLE}{BOLD}{'─'*80}")
        slow_print(f"{WHITE} Roblox")
        slow_print(f"{PURPLE}{BOLD}{'─'*80}{RESET}\n")

        slow_print(f"{WHITE}\n\n[10] - Roblox Id Info")

        # Navigation options
        slow_print(f"\n{PURPLE}{BOLD}{'─'*80}")
        slow_print(f"{WHITE}[N] Next {PURPLE}| {WHITE}[B] Back")
        slow_print(f"{PURPLE}{'─'*80}{RESET}")

    elif page == 3:
        slow_print(f"{PURPLE}{BOLD}{'─'*80}")
        slow_print(f"{WHITE} Discord")
        slow_print(f"{PURPLE}{BOLD}{'─'*80}{RESET}\n") 
        slow_print(f"\n{WHITE}[20] - Discord - Rat - Tool\n")
        slow_print(f"\n{WHITE}[21] - Discord - Stealer\n")
        slow_print(f"\n{WHITE}[22] - Nitro Generator\n")
        slow_print(f"\n{BOLD}{WHITE}[23] - Discord Nuker\n")
        slow_print(f"\n{WHITE}{BOLD}[24] - 🔥 Discord Webhook Raid 🔥")


        slow_print(f"\n{PURPLE}{BOLD}{'─'*80}")
        slow_print(f"{WHITE}[N] Next {PURPLE}| {WHITE}[B] Back")
        slow_print(f"{PURPLE}{'─'*80}{RESET}")   
    elif page == 4:
        slow_print(f"{PURPLE}{BOLD}{'─'*80}")
        slow_print(f"{WHITE} Discord")
        slow_print(f"{PURPLE}{BOLD}{'─'*80}{RESET}\n") 
        slow_print(f"\n{WHITE}[30] Dox Searcher")
        slow_print(f"\n{WHITE}[31] - Dox Creater")


        slow_print(f"\n{PURPLE}{BOLD}{'─'*80}")
        slow_print(f"{WHITE}[N] Next {PURPLE}| {WHITE}[B] Back")
        slow_print(f"{PURPLE}{'─'*80}{RESET}")  
def main():
    current_page = 1
    max_page = 4

    while True:
        print_menu(current_page)
        choice = input(f"\n╔{PURPLE}({WHITE}{USER}{PURPLE}@{WHITE}{COMPUTER}{PURPLE}){WHITE}-{PURPLE}[{WHITE}~/PyWine/menu.py{PURPLE}]{PURPLE}»{WHITE}${PURPLE}").lower()

        if choice == 'i':
            slow_print(f"\n{WHITE}[Info] Selected.")
            input(f"{WHITE}Press Enter to return to the menu...")
        elif choice == 's':
            slow_print(f"{PURPLE}{'─'*80}")
            slow_print(f"{WHITE} [{Fore.GREEN}1{Fore.WHITE}] - Discord")
            slow_print(f"{PURPLE}{'─'*80}")
            site = input(f" {Fore.WHITE}[{Fore.GREEN}>{Fore.WHITE}] Option:")
            if site == '1' or 1:
                webbrowser.open("https://discord.gg/WaT32TmyWE")         
        elif choice == '1':
            dox_icon()
            random_number = random.uniform(0.3, 5)                        
            slow_print(f"\n{PURPLE} Searching For Ips Please Wait...")
            time.sleep(random_number)
            local_ip = f'{PURPLE}{get_local_ip()}'
            public_ip = f'{PURPLE}{get_public_ip()}'
            slow_print(f"{PURPLE}{BOLD} Ips Found:\n1. {local_ip}, type: local.\n2. {public_ip}, type: public\n")
            input("Press Anything To Continue:")
        elif choice == '2':
            slow_print("""                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                    .^~!7?JJJJ?7!~^.                                                    
                                                :!J5GBBBBBBBBBBBBBBG5J!:                                                
                                             :?5BBBBBBBBBBBBBBBBBBBBBBBB57:                                             
                                           ^YBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBY^                                           
                                         :YBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBY:                                         
                                        !GBBBBBBBBBBBBGPY?7777?YPGBBBBBBBBBBBBG!                                        
                                       7BBBBBBBBBBBBY!:          :!YBBBBBBBBBBBB7                                       
                                      !BBBBBBBBBBB5^                ^5BBBBBBBBBBB~                                      
                                     .GBBBBBBBBBB?                    ?BBBBBBBBBBP.                                     
                                     !BBBBBBBBBB5                      5BBBBBBBBBB!                                     
                                     JBBBBBBBBBB!                      !BBBBBBBBBBJ                                     
                                     JBBBBBBBBBB7                      7BBBBBBBBBBJ                                     
                                     7BBBBBBBBBBP.                    .PBBBBBBBBBB!                                     
                                     :GBBBBBBBBBBY.                  .YBBBBBBBBBBG:                                     
                                      JBBBBBBBBBBBP!               .!PBBBBBBBBBBBJ                                      
                                      .GBBBBBBBBBBBBP?~.        .~?PBBBBBBBBBBBBG.                                      
                                       ~BBBBBBBBBBBBBBBGPYJJJJYPGBBBBBBBBBBBBBBB~                                       
                                        !BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB7                                        
                                         7BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB7                                         
                                          !BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB!                                          
                                           ~GBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBG~                                           
                                            :5BBBBBBBBBBBBBBBBBBBBBBBBBBBBP:                                            
                                             .JBBBBBBBBBBBBBBBBBBBBBBBBBBJ.                                             
                                               ~GBBBBBBBBBBBBBBBBBBBBBBG~                                               
                                                .JBBBBBBBBBBBBBBBBBBBBJ.                                                
                                             .    ~PBBBBBBBBBBBBBBBBP~                                                  
                                    .:^!7JY5PG?.   .7GBBBBBBBBBBBBG?.    !PP5YJ7!^:.                                    
                               :~7J5GB###BBGP5Y!     :JBBBBBBBBBBJ:     ~Y5PGBB###BG5J7~:                               
                           .~?5GBB##BPJ7~^:.           ^YBBBBBBY^           .:^~7JPB##BBG5?~.                           
                         :?PBBBBBB5!:                    ~5BB5~                    :!5BBBBBBP?:                         
                        !GBBBBBBBY                         ~~                         5BBBBBBBG!                        
                       .GBBBBBBBBG?^.                                              .^JGBBBBBBBBG.                       
                       .5#BBBBBBBBBBPY?!~:..                                ..:~!?YPBBBBBBBBBB#5.                       
                        .JBBBBBBBBBBBBBBBBGPP5YJ??7!!!~~~~~~~~~~~~!!!7??JY5PPGBBBBBBBBBBBBBBBBJ.                        
                          :?PBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBP?:                          
                             ^7JPGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGPJ!^                             
                                 :^!?YPGGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGGPY?!^:                                 
                                       .:^~!7?JY55PPPGGGGGGGGGGGGGGPPP55YJ?7!~^:.                                       
                                                    .....::::::.....                                                    
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
&&&&&&&@@&&@&@&&&&&@@@&&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@&&&
&&&BGGPGGBPGBGB55YPPPPGJPB#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#BB#####B###B#######BBBBBBBBBBB&&&
&&&&GBGBB#BBBG#GPGGPPPGPP#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#GGGBGGBGGGGGBBBGBGBGBGBGGGGGGB&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
            try:
                PUBLIC_IP = input("Enter:")
                result = subprocess.run(
                 ['curl', f'https://ipinfo.io/{PUBLIC_IP}/json'],
                 capture_output=True,
                 text=True
                ) 
                slow_print(f"[{Fore.GREEN}+{Fore.WHITE}] Sucessfuly Finded Ip")
                slow_print(result.stdout)
                input("Press Anything To Continue")
            except Exception as e:
                slow_print(f"[{Fore.RED}-{Fore.MAGENTA}] Coud Not Find Ip: {e}") 
        elif choice == '3':
            dox_icon()
            ip = input(f" {Fore.WHITE}[{Fore.GREEN}>{Fore.WHITE}] Ip:")
            ping_ip(ip)
        elif choice == '10':
            roblox_icon()
            user_id = input(f"{Fore.MAGENTA}{BOLD} Enter Roblox User Id: ")
            user_info = get_roblox_user_info(user_id)
            print_user_info(user_info)
            input(f"{Fore.MAGENTA} Press Any Key To Continue")
        elif choice == '20':
            discord_icon()
            slow_print(f"\n{WHITE}Opening Rat Discord Builder")
            os.chdir('bat')
            os.system("start RatDiscord.bat")
            os.chdir('../')
            input(f"{WHITE}Press Enter to return to the menu...")
        elif choice == '21':
            discord_icon()
            slow_print(f'\n{WHITE} Opening Discord Stealer Builder')
            os.chdir('bat')
            os.system("start discordstealer.bat")
            os.chdir('../')    
        elif choice == '22':
            discord_icon()
            Start_Nitro_Gen()  
        elif choice == '23':
            discord_icon()
            os.chdir("bat")
            os.system("start Nuker.bat")
            os.chdir("../")      
            input(f"{BOLD} Press Any Key To Continue...")
        elif choice == '24':
            discord_icon() 
            webhook_url = input(f"{Fore.MAGENTA}[{Fore.GREEN}>{Fore.MAGENTA}]{Fore.WHITE} Enter Ur Webhook Url:")
            message_content = input("Enter the message you want to send: ")
            interval = float(input("Enter the interval between messages (in seconds): "))
            
            send_repeated_message(webhook_url, message_content, interval)  
        elif choice == '30':
            dox_icon()
            Search = input(f"{Fore.LIGHTCYAN_EX}UserName:")
            slow_print(f"\n{Fore.LIGHTCYAN_EX}[1] Youtube")
            slow_print(f"\n{Fore.LIGHTCYAN_EX}[2] TikTok")
            slow_print(f"\n{Fore.LIGHTCYAN_EX}[3] Instagram")
            slow_print(f"\n{Fore.LIGHTCYAN_EX}[4] Twiterr [X.com]")
            slow_print(f"\n{Fore.LIGHTCYAN_EX}[5] FaceBook")
            result = input(f"\n{Fore.LIGHTCYAN_EX}Pick:")
            if result == 1 or '1':
                webbrowser.open(f"https://www.youtube.com/results?search_query={Search}")
            elif result == 2 or '2':
                webbrowser.open(f"https://www.tiktok.com/search?q={Search}")  
            elif result == 3 or '3':
                webbrowser.open(f"https://instagram.com/{Search}/")  
            elif result == 4 or '4':
                webbrowser.open(f"https://x.com/search?q={Search}")      
            elif result == 5 or '5':
                webbrowser.open(f"https://www.facebook.com/search/top/?q={Search}")  
            

            input("press any key to continue")   
        elif choice == '31':
         dox_icon()
         create_dox_file()
        elif choice == 'n':
            if current_page < max_page:
                current_page += 1
            else:
                current_page = 1
        elif choice == 'b':
            if current_page > 1:
                current_page -= 1
            else:
                slow_print(f"\n{WHITE}You are already on the first page.")
                input(f"{WHITE}Press Enter to return to the menu...")
        else:
            slow_print(f"\n{WHITE}Invalid option! Try again.")
            input(f"{WHITE}Press Enter to return to the menu...")

if __name__ == "__main__":
    main()
