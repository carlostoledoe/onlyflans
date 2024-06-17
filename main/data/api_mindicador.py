import requests
import json

url = 'https://www.mindicador.cl/api'

def request_get(url): 
    return json.loads(requests.get(url).text) 

indicators = request_get(url)

valor_dolar = indicators['dolar']['valor']
valor_euro = indicators['euro']['valor']
valor_uf = indicators['uf']['valor']
valor_utm = indicators['utm']['valor']
valor_bitcoin = indicators['bitcoin']['valor']
