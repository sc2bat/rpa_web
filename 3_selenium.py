# pip install selenium
# chromedriver
# chrome://version/ 버전 확인해서 버전과 같은 드라이버 설치
# https://chromedriver.chromium.org/downloads

from selenium import webdriver

browser = webdriver.Chrome("./chromedriver_92.exe")
# browser = webdriver.Chrome()

browser.get("http://daum.net")

# C:\Users\Dero\Desktop\p\RPA\chromedriver_92.exe

# https://selenium-python.readthedocs.io/