import urllib3
import json

URL = 'http://www.nbrb.by/API/ExRates/Rates/?Periodicity=0'

SAVEFILE = 'rates.json'

def get_rates():
    http = urllib3.PoolManager()
    r = http.request('GET', URL)
    rates = json.loads(r.data.decode('utf-8'))
    return rates

def save_rates(file, data):
    with open(file, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

def load_rates(file):
    with open(file, 'r') as infile:
        return json.load(infile)
