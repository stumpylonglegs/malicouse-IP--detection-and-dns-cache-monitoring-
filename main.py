import os 
import subprocess
import re


def get_dns_cache_entriess():

    lookup = subprocess.run(['ipconfig', '/displaydns'], capture_output=True, text=True, shell=True)
    reg = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})') 

    found_ip = reg.findall(lookup.stdout)
    removed_dublicate = []

    for ip in found_ip:
        if ip not in removed_dublicate:
            removed_dublicate.append(ip)



    for ip in removed_dublicate:
        print(ip)
    
    




get_dns_cache_entriess()
