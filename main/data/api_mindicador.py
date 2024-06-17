import requests
import json

url = 'https://www.mindicador.cl/api'

def request_get(url): 
    return json.loads(requests.get(url).text) 

indicators = request_get(url)