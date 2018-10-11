import os
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

QUERY = str(input("SEARCH : "))

file = open('./Crawler_DBpia_'+QUERY+'.txt','w', encoding='utf-8')

Arr_URL = ['Default', 'Key', 'Target','Search']

Arr_Value = ['http://api.dbpia.co.kr/v1/search/search.xml', '?key=90dc645234b3ce76408e390f1b7f7ffc', '&target=se', '&searchall='+QUERY]

URL=''

for arr in range(len(Arr_URL)):
    URL += Arr_Value[arr]
print(URL)
req = urllib.request.Request(URL)
f = urllib.request.urlopen(req)
resultXML = f.read()
xmlsoup = BeautifulSoup(resultXML, 'html.parser')
items = xmlsoup.find_all('item')
for item in items:
    file.write('-------------------------------\n')
    file.write(' TITLE : '+ item.title.get_text(strip=1)+'\n')
    file.write(' LINK : '+ item.link_url.get_text(strip=1)+'\n')
    file.write('-------------------------------\n')
file.close()
