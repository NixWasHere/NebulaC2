from colorama import Fore
import socket, time

def url_to_ip(args, send, client, gray):
    try:
        url = ""
        if len(args) == 2:
            url = args[1]
            host = str(url).replace("https://", "").replace("http://", "").replace("www.", "")
            ip = socket.gethostbyname(host)
            time.sleep(0.2)
            DATA_TEXT = f'URL {url} | IP {ip}'
            send(client, f'{gray} {DATA_TEXT}')
        else:
            send(client, Fore.LIGHTWHITE_EX + '!URL_TO_IP [URL]')
    except socket.gaierror:
        send(client, Fore.RED + 'Invalid website')