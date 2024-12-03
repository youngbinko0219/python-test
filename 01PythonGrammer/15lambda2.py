# 1. map()
# 함수 정의

def multiply_by_two(n):
    return n * 2


# 리스트 정의
numbers = [1, 2, 3, 4, 5]

result = map(multiply_by_two, numbers)
print("결과1-1:", result)  # map 객체 출력
print("결과1-2:", list(result))  # 결과를 리스트로 변환하여 출력


# 2. filter 함수
'''
필터 함수는 주어진 요소 중 조건에 맞는 것만 필터링하여 반환한다.
즉 지정된 함수에서 true가 되는 것만 반환하여 결과를 생성한다.
'''
def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5]
result = filter(is_even, numbers)
print("결과2:", list(result))  # 결과를 리스트로 변환하여 출력

# 3. reduce 함수
'''
반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는
함수이다. 즉 하나의 값을 반환한다. 파이썬 3.x 부터는 내장함수가 아니므로
별도의 모듈을 임포트 해야한다.

리듀스 함수는 리스트의 처음 2개의 요소를 함수로 전달하여 결과를 만들고, 그 결과를
다시 다음 요소와 결합하는 방식으로 전체 리스트를 처리한다.
'''
from functools import reduce


def add(x, y):
    return x + y


numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers)
print(result)
