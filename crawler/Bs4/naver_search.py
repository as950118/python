import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

default_url = "https://openapi.naver.com/v1/search/webkr.xml" #크롤링할 url
query = str(input("Query :")) #검색어
display = 10 #몇개보여줄지
start = 1 #어디부터시작할지

#형식에 맞게 수정
query = "?query=" + urllib.parse.quote_plus(query)
display = "&display=" + str(display)
start = "&start=" + str(start)

#최종 URL
ret_url = default_url + query + display + start

#Header
headers = {
    "Host" : "openapi.naver.com",
    "User-Agent" : "curl/7.49.1",
    "Accept" : "*/*",
    "X-Naver-Client-Id" : "CbFfTj9p53Si_e1133sG",
    "X-Naver-Client-Secret" : "lOTXwx08OL"
}

req = urllib.request.Request(ret_url, headers = headers)
ret = urllib.request.urlopen(req)
ret_XML = ret.read()
xmlsoup = BeautifulSoup(ret_XML, 'html.parser')
items = xmlsoup.find_all('item')
for item in items:
    for elem in item:
        print(elem)
    title = item.title.get_text(strip = 1)
    link = item.link.get_text(strip = 1)
    description = item.description.get_text(strip = 1)
    #출력
    print("TITLE : " + title + "\n")
    print("LNK : " + link + "\n")
    print("DESCRIPTION : " + description + "\n")
    print("--------------------\n") #구분선
