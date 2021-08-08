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

# time.sleep(1)
# # 지정한 위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, 1000)')

# time.sleep(1)
# browser.execute_script('window.scrollTo(0, 2000)')

time.sleep(1)
# 화면 가장 아래로 스크롤
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

time.sleep(3)

browser.quit()