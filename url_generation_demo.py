import urllib
from urllib.parse import urlencode
from urllib import request
import requests
from bs4 import BeautifulSoup as bs

key_ = 'AIzaSyCOD3KvY2DDzEfel-NZ_LKIWXr86EF_EUw'

base_endpoint= 'https://maps.googleapis.com/maps/api/geocode/xml'

add = input('Enter your address')

params = {'address': add,'key':key_}

url_add = urlencode(params)
url = f'{base_endpoint}?{url_add}'
print(url)
##api_resp = request.urlopen(url)
resp = requests.get(url)

bs_data = bs(resp.text,'lxml')
lat =  bs_data.find('location').text
long = bs_data.find('lat').text


print(lat,long)
