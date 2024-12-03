# 모듈 사용 예제
'''
모듈
다른 파이썬 프로그램에서 불러와 사용할 수 있도록 만든 파이썬 파일로 변수
혹은 함수 등을 모아놓은 것이다.
'''

import mod1

print("모듈의 함수 호출1:", mod1.add(3, 4))
print("모듈의 함수 호출2:", mod1.sub(4, 2))

from mod1 import add

result = add(3, 4)
print("결과:", result)

from mod1 import *

result1 = add(3, 4)
print("결과:", result1)
result2 = sub(3, 4)
print("결과:", result2)

import mod2

result = mod2.mul(3, 4)
print(result)

# 모듈을 나누어 관리할 때는 패키지를 사용한다.
import mod3

mod3.sum1To10()

from mod3 import sum1To10

sum1To10()
