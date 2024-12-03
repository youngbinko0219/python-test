import sqlite3

conn = sqlite3.connect("./saveFiles/biography.db")
curs = conn.cursor()

print(f'{"조회1":-^30}')
curs.execute("select * from people")
print(curs.fetchall())

print(f'{"조회2":-^30}')
curs.execute("select * from people")
for row in curs.fetchall():
    print(row)

print(f'{"조회3":-^30}')
curs.execute("select * from people")
for name, job, pay in curs.fetchall():
    print(name, ":", job, ":", pay)

print("전체 레코드 셀렉트 완료")
