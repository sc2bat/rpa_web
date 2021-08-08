import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver_92.exe")
# browser.maximize_window()
browser.get('https://beta-flight.naver.com/')

# # 제주도 선택
# browser.find_element_link_text('도착').click()
# time.sleep(1)
# browser.find_element_link_text('국내').click()
# time.sleep(1)
# browser.find_element_link_text('제주').click()
# time.sleep(1)

# 가는 날
browser.find_elements_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
browser.find_elements_by_link_text('17')[0].click()
# 오는날
browser.find_elements_by_link_text('25')[1].click()

# 항공권 검색 클릭
browser.find_elements_by_link_text('항공권 검색').click()

time.sleep(3)

browser.quit()

# 오류 다수 포기