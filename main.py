import os 
import subprocess
import re
import requests
from time import sleep 





headers = {
    "accept": "application/json",
    "x-apikey": "<apikey>"
}




def get_dns_cache_entriess(headers):

    lookup = subprocess.run(['ipconfig', '/displaydns'], capture_output=True, text=True, shell=True)
    reg = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})') 

    found_ip = reg.findall(lookup.stdout)
    removed_dublicate = []

    for ip in found_ip:
        if ip not in removed_dublicate:
            removed_dublicate.append(ip)

    for ip in removed_dublicate:
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

        print(url)
        
        
        

        response = requests.get(url, headers = headers)
        text = response.text
        regexp = re.compile(r'"malicious":\s*(\d+)')
        match = regexp.search(text)
        if match:
            malicious_count = int(match.group(1))
            print(f"Malicious count: {malicious_count}")
        
        regexp = re.compile(r'"suspicious":\s*(\d+)')
        match = regexp.search(text)
        if match:
            suspicious_count = int(match.group(1))
            print(f"Malicious count: {suspicious_count}")

        if suspicious_count > 0 or malicious_count > 0:
            example = 1
            #code to send to email or msg if ip is found to be maliciouse or suspisciouse
        sleep(20)





    
    
    




get_dns_cache_entriess(headers)
