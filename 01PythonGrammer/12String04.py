# 문자열 바꾸기
print(f"{'replace()':-^30}")
print('Hello, world!'.replace('world', 'Python'))

s = 'Hello, world!'
s = s.replace('Hello', '안녕')
print(s)

# 문자열 바꾸기 (maketrans/translate)
print(f"{'maketrans()/translate()':-^30}")
str1 = "apple"
table = str1.maketrans('aeiou', '12345')
print(str1.translate(table))

str2 = "한글은 아름다운 언어"
table = str2.maketrans('한아언', 'XYZ')
print(str2.translate(table))

# 문자열 연결
print(f"{'join()':-^30}")
print('-'.join(['010', '7986', '3600']))

# 공백 제거 혹은 특정 문자 삭제
# lstrip : 왼쪽 rstrip : 오른쪽 strip : 양쪽
print(f"{'strip()':-^30}")
str = "#%^오늘은 @@ 파이썬 @@ 공부하는날#%^"
print(str.lstrip('#'))
print(str.rstrip('%'))
print(str.rstrip('%').lstrip('#').replace('@', ''))

# 열 위치 찾기
print(f"{'find()':-^30}")
print('apple pineapple'.find('pl'))
print('apple pineapple'.rfind('pl'))

# 문자열 상세 검사
# 문자열에서 숫자, 알파벳, 한글만 있는 경우 True 반대는 False
print(f"{'isalnum()':-^30}")
str = "python312좋아"
print(str.isalnum())
str = "python3.12좋아^^"
print(str.isalnum())

# 시나리오: 입력한 문자열에 영문 대문자, 소문자, 숫자만 포함되어 있다면 True,
# 나머지 문자가 하나라도 포함되면 False를 반환하는 프로그램 작성
print(f"{'시나리오':-^30}")
s = input("문자열을 입력하세요: ")
result = True
for char in s:
    if not (char.isupper() or char.islower() or char.isdigit()):
        result = False

print(f"입력한 문자열: {s}")
print(f"결과: {result}")
