'''
람다
def 키워드를 사용하지 않고, 식 형식으로 되어있다 해서 람다식이라고 부른다.
이름이 없으므로 익명함수로 부르기도 한다. lambda 키워드를 사용해서 간편하게
작성할 수 있고, 재사용되지 않는 1회성 함수를 만들 때 사용한다.
'''

def two_sum(x, y):
    return x + y


print("함수를 통한 두 수의 합", two_sum(10, 20))

sum = lambda arg1, arg2: arg1 + arg2
print("람다식을 통한 합 = ", sum(10, 20))

power = lambda num: num**2
print("5의 제곱은", power(5))

print("람다의 자체호출 = ", (lambda x, y: x + y)(100, 200))
