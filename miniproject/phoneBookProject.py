import pandas as pd


def main():
    데이터목록 = []
    while True:
        print("\n1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료")
        메뉴선택 = input("메뉴를 선택하세요: ")
        if 메뉴선택 == "1":
            데이터입력(데이터목록)
        elif 메뉴선택 == "2":
            데이터출력(데이터목록)
        elif 메뉴선택 == "3":
            데이터검색(데이터목록)
        elif 메뉴선택 == "4":
            데이터수정(데이터목록)
        elif 메뉴선택 == "5":
            데이터삭제(데이터목록)
        elif 메뉴선택 == "6":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


def 데이터입력(데이터목록):
    성명 = input("성명: ")
    전화번호 = input("전화번호: ")
    주소 = input("주소: ")
    항목 = {"성명": 성명, "전화번호": 전화번호, "주소": 주소}
    데이터목록.append(항목)
    print("입력이 완료되었습니다.")


def 데이터출력(데이터목록):
    if not 데이터목록:
        print("저장된 데이터가 없습니다.")
    else:
        pd.set_option("display.unicode.east_asian_width", True)
        데이터프레임 = pd.DataFrame(데이터목록)
        print("\n데이터 목록:")
        print(데이터프레임.to_string(index=False))


def 데이터검색(데이터목록):
    검색이름 = input("검색할 성명을 입력하세요: ")
    결과 = [항목 for 항목 in 데이터목록 if 항목["성명"] == 검색이름]
    if 결과:
        데이터프레임 = pd.DataFrame(결과)
        print("\n검색 결과:")
        print(데이터프레임.to_string(index=False))
    else:
        print("해당 성명을 찾을 수 없습니다.")


def 데이터수정(데이터목록):
    수정이름 = input("수정할 성명을 입력하세요: ")
    for 항목 in 데이터목록:
        if 항목["성명"] == 수정이름:
            항목["성명"] = input("새로운 성명: ")
            항목["전화번호"] = input("새로운 전화번호: ")
            항목["주소"] = input("새로운 주소: ")
            print("수정이 완료되었습니다.")
            return
    print("해당 성명을 찾을 수 없습니다.")


def 데이터삭제(데이터목록):
    삭제이름 = input("삭제할 성명을 입력하세요: ")
    for i, 항목 in enumerate(데이터목록):
        if 항목["성명"] == 삭제이름:
            del 데이터목록[i]
            print("삭제가 완료되었습니다.")
            return
    print("해당 성명을 찾을 수 없습니다.")


if __name__ == "__main__":
    main()
