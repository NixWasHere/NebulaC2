from colorama import Fore
import requests

def get_location(ip_addr):
    ip_address = ip_addr
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    version = response.get("version")
    city = response.get("city")
    region_city = response.get("region")
    country_name = response.get("country_name")
    latitude = response.get("latitude")
    longitude = response.get("longitude")
    timezone = response.get("timezone")
    network = response.get("network")

    location_data = f'''IP            : {ip_address}
NETWORK       : {network}
VERSION       : {version}

# LOCATION
CITY          : {city}
REGION        : {region_city}
COUNTRY       : {country_name}
LATITUDE      : {latitude}
LONGITUDE     : {longitude}

# TIME
TIMEZONE      : {timezone}'''

    return location_data

def ip_to_loc(args, send, client, gray):
    try:
        ip = ''
        if len(args) == 3:
            ip = str(args[1])
            ip_location = get_location(ip)
            DATA_TEXT = f'{ip_location}'
            send(client, f'{gray}' + DATA_TEXT)
        else:
            send(client, Fore.LIGHTWHITE_EX + '!IP_TO_GEO [IP]')
    except:
        send(client, Fore.RED + 'Invalid data')