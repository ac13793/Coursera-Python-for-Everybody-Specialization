import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

sum = 0
url = input('Enter URL: ')
if(1 > len(url)):
    #url = "http://py4e-data.dr-chuck.net/comments_42.xml" # Sample File name
    url = "http://py4e-data.dr-chuck.net/comments_50138.xml" # Actual file name

uh = urllib.request.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)
lst = tree.findall("comments/comment")
for item in lst:
    sum = sum + int(item.find("count").text)
print("Sum:", sum)
    