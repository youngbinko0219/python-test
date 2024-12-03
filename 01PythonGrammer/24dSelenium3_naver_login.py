from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = 'http://www.naver.com/'
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="account"]/div/a/i').click()
time.sleep(2)

driver.find_element(By.NAME,'id').send_keys('heimdalr')
time.sleep(2)
driver.find_element(By.NAME,'pw').send_keys('tjckdwlq12!')
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="log.login"]').click()
time.sleep(30)

driver.find_element(By.NAME,'query').send_keys('파파고')
time.sleep(2)

driver.find_element(By.CLASS_NAME,'btn_search').click()
time.sleep(10)
