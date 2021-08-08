# https://www.w3schools.com/html/
# 좌측 목록 다수 별도의 스크롤

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome("./chromedriver_92.exe")
browser.maximize_window()
browser.get('https://www.w3schools.com/html/')

time.sleep(3)

# //*[@id="leftmenuinnerinner"]/a[61]
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[61]')

# # ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 방법2: 좌표 정보 이용 [ 함수가 아니라 변수이므로 () 불필요 ]
# xy = elem.location_once_scrolled_into_view 
# print('type : ', type(xy))
# print('value : ', xy)

elem.click()

time.sleep(3)

browser.quit()