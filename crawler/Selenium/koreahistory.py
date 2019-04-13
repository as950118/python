from selenium import webdriver

wd = webdriver.Chrome()
wd.get("http://www.historyexam.go.kr/pst/list.do?bbs=dat")

def movetoboard():
    global index
    elems = wd.find_elements_by_xpath("//a[@href]")
    for x in elems[index+1:]:
        if '고급' in x.text or '1급' in x.text or '2급' in x.text:
            print(x.text) #게시글 제목 출력
            index = elems.index(x) #인덱스 수정
            x.click()
            '''
            try: #문제지와 정답표가 따로있는 경우도 있으므로
                wd.find_element_by_partial_link_text("문제지").click()
            except:
                continue
            try:
                wd.find_element_by_partial_link_text("정답표").click()
            except:
                continue
            '''
            wd.find_elements_by_xpath('//*[@id="sub_content"]/div[2]/div[3]/div/div/a')[0].click()
            return 1
    return 0


try:
    M = 1 #페이지
    while 1:
        index = -1 #초기값
        while movetoboard():
            continue

        M+=1
        if ((M-1)%5)==0:
            wd.find_element_by_xpath('//*[@id="sub_content"]/div[2]/div[3]/ul/li[9]/a').click()
        else:
            wd.find_element_by_xpath('//*[@id="sub_content"]/div[2]/div[3]/ul/li['+str((M-1)%5 + 4)+']/a').click()
except Exception as e:
    print("Error :", e)
'''
def back(PageNum):
    wd.get("http://www.historyexam.go.kr/pst/list.do?bbs=dat")
    while PageNum>5:
        wd.find_element_by_xpath('//*[@id="sub_content"]/div[2]/div[3]/ul/li[9]/a').click()
        PageNum -= 5
    return PageNum

def movepage(PageNum):
    while PageNum>5:
        wd.find_element_by_xpath('//*[@id="sub_content"]/div[2]/div[3]/ul/li[9]/a').click()
        PageNum -= 5
    if PageNum == 1:
        return PageNum
    wd.find_element_by_xpath('//*[@id="sub_content"]/div[2]/div[3]/ul/li['+str(PageNum+3) +']/a').click()
    return PageNum
'''
