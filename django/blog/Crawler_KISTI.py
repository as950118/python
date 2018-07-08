import os
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def Crawler_KISTI(QUERY):
    
    file = open('./Crawler_KISTI_'+QUERY+'.txt','w', encoding='utf-8')

    Arr_URL = ['Default', 'Key', 'Target', 'Search', 'Count', 'Start', 'Sort', 'Type', 'Res', 'Query']

    Arr_Value = ['http://openapi.ndsl.kr/itemsearch.do', '?keyValue=03323430', '&target=ARTI', '&searchField=BI', '&displayCount=100', '&startPosition=1', '&sortby=', '&returnType=xml', '&responseGroup=advance', '&query='+QUERY]

    URL=''

    for arr in range(len(Arr_URL)):
        URL += Arr_Value[arr]
    print(URL)
    headers = {
    'Host': 'openapi.ndsl.kr',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': '_ga=GA1.2.886947753.1522289626; WMONID=sRG64EHzxAF; JSESSIONID=aeEYqiOaIN5u1jVvsSp3Ru9n0imSEBf7AkwuFBwWXNlzDQrZM1lI2itgzZmg6Nfs.ar228_servlet_engine12'
    }
    req = urllib.request.Request(URL, headers=headers)
    f = urllib.request.urlopen(req)
    resultXML = f.read()
    xmlsoup = BeautifulSoup(resultXML, 'html.parser')
    items = xmlsoup.find_all('dissertation')
    print(items)
    for item in items:
        print(item.dissertationtitle)
        file.write('-------------------------------\n')
        file.write(' TITLE : '+ item.dissertationtitle.get_text(strip=1)+'\n')
        file.write(' CONTENTS : '+ item.abstract.get_text(strip=1)+'\n')
        file.write(' LINK : '+ item.deeplink.get_text(strip=1)+'\n')
        file.write('-------------------------------\n')
    file.close()
