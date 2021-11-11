import requests
import json
import os
import time
from win10toast import ToastNotifier

toaster = ToastNotifier()
API_endpoint = 'https://wax.pink.gg/v1/chain/get_table_rows'

acc_name = input("Enter yout wallet id: ")

json_data = {
    "json": True,
    "limit": 100,
    "code": "eosio.token",
    "scope": f"{acc_name}",
    "table": "accounts"
}

prev_balance =  float(json.loads(requests.post(url =API_endpoint, json = json_data).content)['rows'][0]['balance'][:-4])

def get_waxp():
    waxp_balance = json.loads(requests.post(url =API_endpoint, json = json_data).content)['rows'][0]['balance']
    return waxp_balance

while True:
    waxp_balance = get_waxp()
    if(prev_balance != float(waxp_balance[:-4])):
        toaster.show_toast(f"Recieved {(float(waxp_balance[:-4])-prev_balance):.8f} WAX",f"Current balance: {waxp_balance}")
        prev_balance = float(waxp_balance[:-4])

    time.sleep(10)