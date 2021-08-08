import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver_92.exe")
browser.maximize_window() # 최대화
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult') # frame 전환

elem = browser.find_element_by_xpath('//*[@id="html"]')

# 선택이 되어있지 않으면 선택하기
if elem.is_selected() == False: # 라디오 버튼이 선택되어있지 않으면
    print("선택 안되어 있으므로 선택하기")
    elem.click()
else:
    print("선택 되어 있으므로 아무것도 안함")

time.sleep(5)

if elem.is_selected() == False: # 라디오 버튼이 선택되어있지 않으면
    print("선택 안되어 있으므로 선택하기")
    elem.click()
else:
    print("선택 되어 있으므로 아무것도 안함")

time.sleep(5)

browser.quit()