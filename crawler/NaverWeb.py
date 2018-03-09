import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import datetime

defaultURL="https://openapi.naver.com/v1/search/webkr.xml"
start='&start=1'
display='&display=10'
search=str(input("검색어 : "))
query='?query='+urllib.parse.quote_plus(search)
fullURL = defaultURL + query + display + start
print(fullURL)

file=open("c:\\python34\\crawl\\web\\%s.txt"%search,"w",encoding='utf-8')
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
    file.write('-------------------------------\n')
    #file.write(' 시간 : '+ item.lastBuildDate.get_text(strip=1)+'\n')
    file.write(' 제목 : '+ item.title.get_text(strip=1)+'\n')
    file.write(' 내용 : '+ item.description.get_text(strip=1)+'\n')
    file.write(' 링크 : '+ item.link.get_text(strip=1)+'\n')#본문의 링크를 가져오기 위해
    file.write('-------------------------------\n')

file.close()
