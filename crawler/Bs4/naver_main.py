import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

url = "https://blog.naver.com/na_qa" #크롤링할 url
req = urllib.request.Request(url) #request
html = urllib.request.urlopen(req) #html 추출
ret = html.read() #문자열로 변환

htmlsoup = BeautifulSoup(ret, 'html.parser') #bs4의 html parser를 활용해 data를 parsing

#elems = htmlsoup.find_all('link') #해당 태그를 포함한 모든 elem들을 추출
#for elem in elems:
#    print(elem)

elems = htmlsoup.find_all('link', {'rel':'alternate'}) #g해당 태그와 속성값을 가지는 모든 elem을 추출
for elem in elems:
    print(elem)
