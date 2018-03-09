import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

defaultURL="https://openapi.naver.com/v1/search/news.xml"
sort='&sort=sim'
start='&start=1'
display='&display=10'
file=open("c:\\python34\\crawl\\window.txt","w",encoding='utf-8')

while 1:
    search=str(input("검색어 : "))
    query='?query='+urllib.parse.quote_plus(search)
    fullURL = defaultURL + query + display + start + sort
    print(fullURL)
    headers={
        'Most':'openapi.naver.com',
        'User-Agent':'curl/7.43.0',
        'Accept':'*/*',
        'Content-Type':'application/xml',
        'X-Naver-Client-Id':'BqGt9k2AGN36MSJWqznB',
        'X-Naver-Client-Secret':'_CJLTTvzol'
        }

    req=urllib.request.Request(fullURL,headers=headers)
    f=urllib.request.urlopen(req)
    resultXML=f.read()
    xmlsoup=BeautifulSoup(resultXML,'html.parser')
    items=xmlsoup.find_all('item')

    for item in items:
        file.write(item.title.get_text(strip=1)+'\n')
        file.write(item.description.get_text(strip=1)+'\n')

file.close()
