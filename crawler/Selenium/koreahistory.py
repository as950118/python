from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

wd = webdriver.Chrome()
wd.get("http://www.historyexam.go.kr/pst/list.do?bbs=dat")
elem = wd.find_elements_by_xpath("//*[@class='page3']")
#print(elem)
#elem = wd.find_element_by_partial_link_text("pageIndex")
print(elem[0].text)
for link in elem:
    try:
        print(link.text)
        link.click()
    except:
        #print("error"+link.text)
        pass
