import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = "https://music.bugs.co.kr/chart"
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

song_data = []
rank = 1
songs = soup.select("table.byChart > tbody > tr")
for song in songs:
    title = song.select("p.title > a")[0].text.strip()
    singer = song.select("p.artist > a")[0].text
    song_data.append(["Bugs", rank, title, singer])
    rank += 1
    driver.implicitly_wait(5)

columns = ["서비스", "순위", "타이틀", "가수"]
pd_data = pd.DataFrame(song_data, columns=columns)
print(pd_data.head())
pd_data.to_excel("./saveFiles/bugs_chart.xlsx", index=False)
