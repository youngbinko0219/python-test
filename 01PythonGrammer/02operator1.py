x = 2
y = 4
z = 8

print("x+y", x + y)
print("x-y", x - y)
print("x*y", x * y)
# 나누기 연산. 결과는 실수형으로 반환
print("x/y", x / y)
# 몫을 구하기 위한 나누기 연산. 결과는 정수형으로 반환
print("x//y", x // y)
# 거듭제곱
print("x**y", x**y)
# pow : 파이썬에서 제공하는 기본함수. 거듭제곱의 결과 반환
print("pow(x,y)", pow(x, y))
# x의 y승의 결과를 z로 나눈 나머지가 반환
print("pow(x,y,z)", pow(x, y, z))
# divmod : 나눈 몫과 나머지를 튜플의 형태로 반환
print("divmod(x,y)", divmod(x, y))

# 수학 관련 여러가지 함수를 가지고 있는 math 모듈을 현재 문서에 임포트 한 후 팩토리얼 함수를 호출
import math

print("math.factorial(5)", math.factorial(5))
