import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

 
position = 17 #18-1(Position-1)
count = 7
html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Braydyn.html', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
Sequence = []
tags = soup('a')
for i in range(count):
    link = tags[position].get('href', None)
    print("Retrieving:",link)
    Sequence.append(tags[position].contents[0])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[position].get('href', None)
print(Sequence[-1])  #Ismaeel
