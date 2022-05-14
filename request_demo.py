import requests
from bs4 import BeautifulSoup as bs


url = 'https://www.google.com/search?q=python'

r = requests.get(url)

s = 'iUh30 tjvcx'
s1 = 'TbwUpd NJjxre'

soup = bs(r.text,'html.parser')

h = soup.find_all('div',{'class':s1})
