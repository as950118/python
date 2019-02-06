from selenium import webdriver

wd = webdriver.Chrome()
wd.get("http://www.historyexam.go.kr/pst/list.do?bbs=dat")
M = 1 #페이지 순서
while 1:
    N = 1 #게시글 순서
    print("next tab")
    while 1:
        temp = 3*(N)-(((M%7)-1)%3)
        print(N,M,3*(N)-(((M%7)-1)%3))
        if 3*(N)-(((M%7)-1)%3)>10:
            print("next page")
            break
        elem = wd.find_elements_by_xpath('//*[@id="sub_content"]/div[2]/div[3]/table/tbody/tr[' + str(temp) + ']/td[2]/a')

        print(elem)
        print(elem[0].text)
        elem[0].click()
        #wd.find_element_by_partial_link_text("문제지").click()
        #wd.find_element_by_partial_link_text("정답표").click()
        wd.execute_script("window.history.go(-1)")
        N+=1
    M+=1
    wd.find_element_by_xpath('//*[@id="sub_content"]/div[2]/div[3]/ul/li['+str(M%5 + 3)+']/a').click()

'''
elem = wd.find_element_by_partial_link_text("고급")
elem.click()
wd.execute_script("window.history.go(-1)")
'''
'''
for i in range(2,6):
    elem = wd.find_element_by_link_text(str(i))
    elem.click()
'''
