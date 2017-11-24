# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if(1 > len(url)):
    #url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html" # Sample File name
    url = "http://py4e-data.dr-chuck.net/known_by_Gemma.html" # Actual file name
count = input("Enter count:")
count = int(count)
position = input("Enter position:")
position = int(position)

i = 1
while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')

    for tag in tags:
        if(i == position):
            print(tag.get('href', None))
            url = str(tag.get('href', None))
            break
        i = i + 1
    count = count - 1
    i = 1

