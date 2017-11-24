import json
import urllib.request, urllib.parse, urllib.error

sum = 0
count = 0
url = input('Enter URL: ')
if(1 > len(url)):
    #url = "http://py4e-data.dr-chuck.net/comments_42.json" # Sample File name
    url = "http://py4e-data.dr-chuck.net/comments_50139.json" # Actual file name

uh = urllib.request.urlopen(url)
data = uh.read()
info = json.loads(data)
print("Info:", info)
for item in info['comments']:
    print('Name', item['name'])
    print('Count', item['count'])
    sum = sum + int(item['count'])
    count = count +1
print("Count:", count)
print("Sum:", sum)