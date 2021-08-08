# w3school html option
# https://www.w3schools.com/tags/tag_option.asp

# https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option
import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver_92.exe")
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

browser.switch_to.frame('iframeResult')

# //*[@id="cars"]/option[1]
# cars 에 해당하는 element 찾고, 드롭다운 내부에 있는 옵션 선택
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[3]')
# elem.click()

# 동일한 텍스트 값을 통해 선택
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')
# elem.click()

# 텍스트 값이 부분 일치하는 항목 선택
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(),"Au")]')
elem.click()

time.sleep(3)

browser.quit()