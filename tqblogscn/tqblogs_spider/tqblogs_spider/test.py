
from selenium import webdriver
import time



browser = webdriver.Chrome("chromedriver")

browser.get('https://passport.lagou.com/login/login.html')

# print(browser.title)

user = browser.find_element_by_xpath('//input[@type="text"]')
user.clear()
user.send_keys('18786040629')


time.sleep(100)











