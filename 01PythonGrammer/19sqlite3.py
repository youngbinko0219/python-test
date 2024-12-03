import sqlite3

conn = sqlite3.connect("./saveFiles/biography.db")
curs = conn.cursor()

curs.execute("update people set pay=? where name=?", (9999, "곽재우83"))

curs.execute("delete from people where pay=?", (1200,))

conn.commit()
print("레코드 업데이트/딜리트 및 커밋 완료")
