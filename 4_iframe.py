# <html>
#     <body>
#         <iframe id="1">
#             <html>
#                 <body>
#                     <div...>
#                 </body>
#             </html>
#         <iframe id="2">
#             <html>
#                 <body>
#                     <div...>
#                 </body>
#             </html>
#     </body>
# </html>

# https://www.w3schools.com/tags/att_input_type_radio.asp
import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver_92.exe")

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult') # frame 전환

elem = browser.find_element_by_xpath('//*[@id="html"]')

elem.click()

browser.switch_to.default.content()

time.sleep(5)

browser.quit()
# //*[@id="html"]