from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = "http://www.daum.net/"
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="loginMy"]/div/div[1]/div/a').click()
time.sleep(2)

driver.find_element(By.NAME, "loginId").send_keys("tjckdwlq@naver.com")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("heimdalr12312!")
time.sleep(2)

driver.find_element(
    By.XPATH, '//*[@id="mainContent"]/div/div[1]/form/div[4]/button[1]'
).click()
time.sleep(40)

driver.find_element(By.NAME, "q").send_keys("파파고")
time.sleep(2)

driver.find_element(By.CLASS_NAME, "btn_ksearch").click()
time.sleep(10)
