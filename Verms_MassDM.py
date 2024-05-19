import requests
from colorama import Fore, init
import os
from concurrent.futures import ThreadPoolExecutor

init()
os.system("mode con cols=85 lines=15 ")

def title():
    print(Fore.LIGHTMAGENTA_EX+"""
            ╦  ╦┌─┐┬─┐┌┬┐┬┬  ┬  ┬┌─┐┌┐┌┌─┐     ╔╦╗┌─┐┌─┐┌─┐     ╔╦╗╔╦╗
            ╚╗╔╝├┤ ├┬┘│││││  │  ││ ││││└─┐     ║║║├─┤└─┐└─┐      ║║║║║
             ╚╝ └─┘┴└─┴ ┴┴┴─┘┴─┘┴└─┘┘└┘└─┘     ╩ ╩┴ ┴└─┘└─┘     ═╩╝╩ ╩
          """)

title()
token = input("Token: ")
content = input("Message: ")

os.system("cls")
title()

def send_message(channel_id, headers, content):
    try:
        requests.post(f'https://discord.com/api/v6/channels/{channel_id}/messages',
                      headers=headers,
                      json={"content": content})
        print(f"{Fore.LIGHTRED_EX}            |{Fore.LIGHTGREEN_EX} SENT{Fore.LIGHTRED_EX} |{Fore.CYAN} ID:{Fore.WHITE} {channel_id}{Fore.LIGHTRED_EX} |{Fore.CYAN} Message:{Fore.WHITE} {content}{Fore.LIGHTRED_EX} |")
    except Exception as e:
        print(f"{Fore.LIGHTGREEN_EX}            |{Fore.LIGHTRED_EX} FAIL{Fore.LIGHTGREEN_EX} |{Fore.CYAN} ID:{Fore.WHITE} {channel_id}{Fore.LIGHTGREEN_EX} |{Fore.CYAN} ERROR:{Fore.WHITE} {e}{Fore.LIGHTGREEN_EX} |")

def send_mass_dm(token, content):
    headers = {'Authorization': token}
    with ThreadPoolExecutor(max_workers=20) as executor:
        channel_ids = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
        for channel in channel_ids:
            executor.submit(send_message, channel["id"], headers, content)


while True:
    send_mass_dm(token, content)
