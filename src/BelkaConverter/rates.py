import urllib3
import json

URL = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'


def get_rates():
    http = urllib3.PoolManager()
    r = http.request('GET', URL)
    rates = json.loads(r.data.decode('utf-8'))
    return rates

def exchange(base, cur1, cur2, scale):
    if base == 'BYN':
        result = cur1 / cur2 * scale
    else:
        result = cur2 * cur1 / scale
    return result