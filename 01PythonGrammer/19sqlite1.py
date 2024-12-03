import sqlite3
import random

conn = sqlite3.connect("./saveFiles/biography.db")
curs = conn.cursor()
rnd = random.randint(0, 100)

try:
    tblcmd = "create table people(name char, job char, pay int)"
    curs.execute(tblcmd)
except Exception as e:
    print("예외 발생 테이블이 이미 생성됨", e)

curs.execute("insert into people values (?,?,?)", (f"이순신{rnd}", "장군", 500))
curs.executemany(
    "insert into people values (?,?,?)",
    [(f"강감찬{rnd}", "장군", 700), (f"홍길동{rnd}", "의적", 800)],
)

rows = [
    [f"곽재우{rnd}", "의병", 1100],
    [f"류성룡{rnd}", "재상", 1200],
    [f"임꺽정{rnd}", "의적", 1500],
]

for row in rows:
    curs.execute("insert into people values (?,?,?)", row)

conn.commit()
print("레코드 인서트 및 커밋 완료")
