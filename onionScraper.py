# Importing modules
import socks
import socket
import requests
from bs4 import BeautifulSoup
# Configuring Socks to use Tor

from urllib.request import urlopen

socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket


# It is necessary to use Tor for DNS resolution of Onion websites
def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]


socket.getaddrinfo = getaddrinfo

# Using requests package to read in the Hidden Wiki Onion Website on the Darknet
res = requests.get("http://quantum445bh3gzuyilxdzs5xdepf3b7lkcupswvkryf3n7hgzpxebid.onion/")

# Using beautifulsoup to get the website content into a nice format
soup = BeautifulSoup(res.content, 'html.parser')

# Having a look at the Website content
print(soup.prettify())

# Checking the Websites title
soup.title

# Getting all links out of the soup and deleting None's
links = [link.get('href') for link in soup.find_all('a')]
links = list(filter(None, links))

# Saving all onion links into a list
onion = []
for l in links:
    if "onion" in l:
        onion.append(l)

# Printing out the onion links
onion
