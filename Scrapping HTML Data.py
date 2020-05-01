from urllib import request
from bs4 import BeautifulSoup
html=request.urlopen('http://python-data.dr-chuck.net/comments_458704.html').read()
soup = BeautifulSoup(html)
tags=soup('span')
sum=0
for tag in tags:
    sum=sum+int(tag.contents[0])
print(sum)  #2915