str = """아래와같이
여러줄에 걸쳐 문자열을 작성하고 싶으면
이와같이 더블쿼테이션을 3개 작성한다.
"""
print(str)

head = "나는 헤더 "
bottom = " 나는 보텀"
print(head + bottom)
print(head * 3)

# 인덱스 번호를 통해 문자열에 접근할 수 있다.
engStr = "Hello Python Good"
print(engStr[0]) # H
print(engStr[:3]) # H-l
print(engStr[1:3]) # e-l
print(engStr[1:]) # e-d

korStr = "안녕하세요? 파이썬입니다."
print(korStr[0])
print(korStr[:2])
print(korStr[0:6])

print(engStr + 100)
