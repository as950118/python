from selenium import webdriver
from selenium.webdriver.common.keys import Keys

wd = webdriver.Chrome() #같은 폴더에 있으므로 생략, 만약 다른 디렉터리에 있다면 명시해줘야함
wd.get("https://www.naver.com/") #네이버에 접속
elem = wd.find_element_by_id('query')
elem.send_keys('헌진정')
elem.submit()
