import os
from selenium import webdriver

uid=""				# your ID card number
password=''			# your CMS password

browser = webdriver.Firefox()
browser.get('http://cms.svce.ac.in')
email = browser.find_element_by_id('userName')
email.send_keys('ST'+uid+'.SVCE')
pwd = browser.find_element_by_id('hashedpassword')
pwd.send_keys(password)
submit=browser.find_element_by_xpath('//input[@type="submit"]')
submit.click()

os.system("taskkill /f /im geckodriver.exe")
