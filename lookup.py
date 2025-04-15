import requests
from bs4 import BeautifulSoup
import argparse
import csv
import time

def lookup_number(phone_number):
    url = f"https://www.numlookup.com/phone/{phone_number}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    response = requests.get(url, headers=headers)
    data = {"phone: phone_number, "info":	"no data"}
    
    if response.status_code == 200:
	soup = BeautifulSoup(response.text, 'html.parser')
	results = soup.find_all("div", class_="card-body")
	if results:
	    info_text = " | " .join(result.get_text(strip=True) for result in results)	
	    data["info"] = info_text

	else:
	    data["info"] = f"Error {response.status_code}"

	return data

    print(f"[+] Looking up {phone_number}...")

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all("div", class_="card-body")

        if results:
            print(f"\n[+] Results for {phone_number}:\n")
            for result in results:
                print(result.get_text(strip=True))
        else:
            print("[-] No public info found.")
    else:
        print(f"[-] Error: Received HTTP {response.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Free Phone Number Lookup CLI")
    parser.add_argument("number", help="Phone number to look up (US only)")
    args = parser.parse_args()

    lookup_number(args.number)
