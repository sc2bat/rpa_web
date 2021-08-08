# 브라우저 내 파일 다운
# https://www.w3schools.com/tags/att_a_download.asp 

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 경로 지정
chrome_options = Options()
chrome_options.add_experimental_option('perfs', {'download.default_directory':r'C:\Users\Dero\Desktop\p\RPA\3_web'})

browser = webdriver.Chrome("./chromedriver_92.exe",options=chrome_options)
# browser.maximize_window()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to.frame('iframeResult')

time.sleep(1)

# 다운로드 링크 클릭
elem = browser.find_element_by_xpath('/html/body/p[2]/a')
elem.click()

time.sleep(3)

browser.quit()