'''
튜플
소괄호 안에 콤마로 구분된 항목들이 나열되어 표현되는 시퀀스 자료형
서로 다른 자료형으로 구성할 수 있지만 항목을 변경할 수 없는 데이터 타입이다.
'''

tu1 = tuple()
tu2 = (1, 2, 3, 4, 5)
# 1개의 항목을 가진 튜플 생성.
tu3 = (1,)
tu4 = (98, 99, 100)
print(tu1, tu2, tu3)

# 인덱싱, 슬라이싱
print(f'{"인덱싱/슬라이싱":-^30}')
print("tu2[0]", tu2[0])
# 음수 인덱싱번호는 마지막 항목
print("tu2[-1]", tu2[-1])
print("tu2[1:3]", tu2[1:3])

print(f'{"포함여부확인":-^30}')
print("4 in tu2", 4 in tu2)
print("99 not in tu2", 99 not in tu2)

print(f'{"반복출력":-^30}')
print("tu2 * 3", tu2 * 3)

print(f'{"병합":-^30}')
new_tu = tu2 + tu4
print("new_tu", new_tu)

print(f'{"튜플과 리스트 변환":-^30}')
my_list = [1, 2, 3]
my_tuple = ("x", "y", "z")
print(tuple(my_list))
print(list(my_tuple))
