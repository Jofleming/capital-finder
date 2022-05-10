from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    
    api_url = 'https://restcountries.com/v3.1'
    path = self.path
    url_components = parse.urlsplit(path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)

    is_capital = dic.get('capital')
    is_country = dic.get('country')

    if is_capital:
        url = f'{api_url}/capital/{is_capital}'
        res = requests.get(url)
        data = res.json()
        country = data[0]['name']['common']

        message = f'{is_capital} is the capital of {country}.'
    elif is_country:
        url = f'{api_url}/name/{is_country}'
        res = requests.get(url)
        data = res.json()
        capital = data[0]['capital'][0]

    
        message = f'The capital of {is_country} is {capital}.'




    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    return
