# 브라우저가 뜨면 핸들값을 부여하게 됨

import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver_92.exe")
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
curr_handle = browser.current_window_handle
print(curr_handle)

# Try it Yourself
browser.find_element_by_xpath('//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles # 모든 핸들 정보를 가져옴
for handle in handles:
    print(handle)
    browser.switch_to.window(handle) # 각 핸들로 이동
    print(browser.title) # 현재 핸들 제목 표시
    print()

# 이후 작업 후 종료
print("close window_handle")
browser.close()

print("처음 핸들로 돌아오기")
browser.switch_to.window(curr_handle)

print(browser.title)

time.sleep(3)
browser.get('http://daum.net')

time.sleep(3)

browser.quit()

# https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio

# CDwindow-7AFAE77C7FD27D700254934EAC785B7A