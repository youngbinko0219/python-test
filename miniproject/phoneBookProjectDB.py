import pymysql
import pandas as pd


def main():
    conn = pymysql.connect(
        host="localhost",
        user="sample_user",
        password="1234",
        database="sample_db",
    )
    cursor = conn.cursor()

    while True:
        print("\n1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료")
        메뉴선택 = input("메뉴를 선택하세요: ")
        if 메뉴선택 == "1":
            데이터입력(cursor, conn)
        elif 메뉴선택 == "2":
            데이터출력(cursor)
        elif 메뉴선택 == "3":
            데이터검색(cursor)
        elif 메뉴선택 == "4":
            데이터수정(cursor, conn)
        elif 메뉴선택 == "5":
            데이터삭제(cursor, conn)
        elif 메뉴선택 == "6":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

    cursor.close()
    conn.close()


def 데이터입력(cursor, conn):
    성명 = input("성명: ")
    전화번호 = input("전화번호: ")
    주소 = input("주소: ")
    query = "INSERT INTO 데이터목록 (성명, 전화번호, 주소) VALUES (%s, %s, %s)"
    cursor.execute(query, (성명, 전화번호, 주소))
    conn.commit()
    print("입력이 완료되었습니다.")


def 데이터출력(cursor):
    query = "SELECT 성명, 전화번호, 주소 FROM 데이터목록"
    cursor.execute(query)
    결과 = cursor.fetchall()
    if 결과:
        pd.set_option("display.unicode.east_asian_width", True)
        데이터프레임 = pd.DataFrame(결과, columns=["성명", "전화번호", "주소"])
        print("\n데이터 목록:")
        print(데이터프레임.to_string(index=False))
    else:
        print("저장된 데이터가 없습니다.")


def 데이터검색(cursor):
    검색이름 = input("검색할 성명을 입력하세요: ")
    query = "SELECT 성명, 전화번호, 주소 FROM 데이터목록 WHERE 성명 = %s"
    cursor.execute(query, (검색이름,))
    결과 = cursor.fetchall()
    if 결과:
        데이터프레임 = pd.DataFrame(결과, columns=["성명", "전화번호", "주소"])
        print("\n검색 결과:")
        print(데이터프레임.to_string(index=False))
    else:
        print("해당 성명을 찾을 수 없습니다.")


def 데이터수정(cursor, conn):
    수정이름 = input("수정할 성명을 입력하세요: ")
    query = "SELECT * FROM 데이터목록 WHERE 성명 = %s"
    cursor.execute(query, (수정이름,))
    결과 = cursor.fetchone()
    if 결과:
        새로운성명 = input("새로운 성명: ")
        새로운전화번호 = input("새로운 전화번호: ")
        새로운주소 = input("새로운 주소: ")
        update_query = (
            "UPDATE 데이터목록 SET 성명 = %s, 전화번호 = %s, 주소 = %s WHERE 성명 = %s"
        )
        cursor.execute(update_query, (새로운성명, 새로운전화번호, 새로운주소, 수정이름))
        conn.commit()
        print("수정이 완료되었습니다.")
    else:
        print("해당 성명을 찾을 수 없습니다.")


def 데이터삭제(cursor, conn):
    삭제이름 = input("삭제할 성명을 입력하세요: ")
    query = "SELECT * FROM 데이터목록 WHERE 성명 = %s"
    cursor.execute(query, (삭제이름,))
    결과 = cursor.fetchone()
    if 결과:
        delete_query = "DELETE FROM 데이터목록 WHERE 성명 = %s"
        cursor.execute(delete_query, (삭제이름,))
        conn.commit()
        print("삭제가 완료되었습니다.")
    else:
        print("해당 성명을 찾을 수 없습니다.")


if __name__ == "__main__":
    main()
