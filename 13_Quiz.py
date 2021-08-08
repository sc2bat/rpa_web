# Selenium 활용 아래 업무를 자동으로 수행하는 프로그램을 작성하시오
# w3schools

# 1. https://www.w3schools.com/ 접속 
# 2. 화면 중간 LEARN HTML 클릭
# 3. 상단 메뉴 중 How To 메뉴 클릭
# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭
# 5. 입력란에 아래 값 입력
# Frist Name : AB
# Last Name : CD
# Country : Seoul
# Subject : Complete Quiz
# ※ 위 값들은 변수로 미리 저장해두세요
# 6. 3초 대기 후 Submit 버튼 클릭
# 7. 3초 대기 후 브라우저 종료

import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver_92.exe")
browser.maximize_window()
browser.get('https://www.w3schools.com/')

# 2. 화면 중간 LEARN HTML 클릭
elem = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/a[1]')
elem.click()
time.sleep(2)

# 3. 상단 메뉴 중 How To 메뉴 클릭
browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click()
time.sleep(2)

# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[116]').click()
# browser.find_element_by_link_text('Contact Form').click()
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click()
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact Form"]').click()
time.sleep(2)

# 5. 입력란에 아래 값 입력

first_name = "AB"
last_name = "CD"
country = "Canada"
subject = "Complete Quiz"

browser.find_element_by_xpath('//*[@id="fname"]').send_keys(first_name)
browser.find_element_by_xpath('//*[@id="lname"]').send_keys(last_name)
# browser.find_element_by_xpath('//*[@id="country"]/option[2]')
browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(country)).click()
browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(subject)

# 6. 3초 대기 후 Submit 버튼 클릭
time.sleep(3)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()


# 7. 3초 대기 후 브라우저 종료
time.sleep(3)

browser.quit()
