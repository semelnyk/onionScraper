# Importing modules
import socks
import socket
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket

def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]
socket.getaddrinfo = getaddrinfo
res = requests.get("http://.onion/")
soup = BeautifulSoup(res.content, 'html.parser')
print(soup.prettify())

soup.title
links = [link.get('href') for link in soup.find_all('a')]
links = list(filter(None, links))

onion = []
for l in links:
    if "onion" in l:
        onion.append(l)

onion
