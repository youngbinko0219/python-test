'''
내장함수
내장함수는 외부 모듈과 달리 임포트가 필요하지 않기 때문에
아루먼 설정없이 바로 사용할 수 있다.
int, print, input 과 같은 함수가 있다.
'''

# 기본 내장 함수
print(f"{'기본 내장 함수':-^30}")

data1 = list(range(1, 11))
print(data1)
print("len=", len(data1))
print("sum=", sum(data1))
print("max=", max(data1))
print("min=", min(data1))

'''
순서가 있는 자료형을 입력받아 인덱스 값을 포함하는 객체로 반환한다.
'''
# enumerate()
print(f"{'enumerate()':-^30}")
for i, v in enumerate(data1):
    print(i, v, end=", ")
print()

data2 = dict(birth=1970, name="홍길동", size="100cm")
for i, v in enumerate(data2):
    print(i, v, data2[v], end=", ")
print()

# eval()
print(f"{'eval()':-^30}")
# 실행 가능한 문자열을 입력받아 결과값을 반환한다.
print(eval("1+2"))
print(eval("'hi' + 'a'"))

# sorted()
print(f"{'sorted()':-^30}")
numbers = (8, 7, 6, 8, 4, 9, 7, 5, 3, 2, 7, 4, 9, 8, 2, 6, 5)
print(sorted(numbers))

# 이터레이터(iterator)
print(f"{'이터레이터(iterator)':-^30}")
# 값을 차례대로 꺼낼 수 있는 객체
# iter() : 반복을 끈탤 값을 지정하면 특정 값이 나올 때 반복을 종료하는 함수
it = iter([1, 2, 3, 4, 5, 99])
while it:
    row = next(it)
    if row == 99:
        break
    print(row, end=", ")
print()
'''
위 문장은 더 이상 출력할 항목이 없을경우 next()에서 예외가 발생되면서
실행이 중지된다. 이 부분은 예외처리에서 학습할 예정
'''

# 반복문과 난수 생성
import random

count = 0
for i in iter(lambda: random.randint(0, 10), 2):
    print(i, end=", ")
    count += 1
else:
    print("\n난수 2가 생성되어 종료")
print(f"반복 횟수: {count}")
