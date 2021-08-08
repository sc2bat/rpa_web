# https://shopping.naver.com/home/p/index.nhn
# 자동 스크롤
import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver_92.exe")
browser.maximize_window()
browser.get('https://shopping.naver.com/home/p/index.nhn')

# 입력
browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]').send_keys('무선마우스')

time.sleep(1)
# //*[@id="autocompleteWrapper"]/a[2]
# 검색
browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()

time.sleep(1)
# 화면 가장 아래로 스크롤
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# 동적 페이지 마지막까지 수행
interval = 2 # 2초에 한번씩

# 현재 문서 높이 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

while True:
    # 스크롤 가장 아래로 내림
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서높이 가져옴
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height: # 더 이상 높이 변화가 없으면 탈출
        break

    prev_height = curr_height

time.sleep(3)
# 맨위로 올리기
browser.execute_script('window.scrollTo(0, 0)')

time.sleep(3)

browser.quit()