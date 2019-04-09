import urllib3
import json

URL = f'http://www.nbrb.by/API/ExRates/Rates/?Periodicity=0'


def get_rates():
    http = urllib3.PoolManager()
    r = http.request('GET', URL)
    rates = json.loads(r.data.decode('utf-8'))
    return rates