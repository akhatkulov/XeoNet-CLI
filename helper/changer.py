import time
import os
import subprocess
import requests
import sys
import re

try:
    check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)
    if str('install ok installed') in str(check_pip3):
        pass
except subprocess.CalledProcessError:
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install python3-pip -y', shell=True)

try:
    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)

def has_number(text):
    if re.search(r'\d', text):
        return True
    else:
        return False
    
def ma_ip():
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change():
    os.system("service tor reload")
    return str(ma_ip())



os.system("service tor start")
x = input("[+] time to change Ip in Sec [type=60] >> ")

def main_changer(x):
    os.system("service tor start") 
    while True:
        try:
            time.sleep(int(x))
            if has_number(change()):
                print(f"IP: {change()}")
        except KeyboardInterrupt:
            print('\nauto tor is closed')
            sys.exit()