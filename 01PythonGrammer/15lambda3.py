# 람다식과 map, filter, reduce 함수 활용
print(f"{'람다식과 map 함수1':-^30}")
multiLambda = lambda x: x * 2
list_data = [1, 2, 3, 4, -1, -2, -5, -10]
result = list(map(multiLambda, list_data))
print("결과1", result)

'''
람다식에서 삼항연산자 사용하기
형식]
식1 if 조건식 else 식2
    조건식이 참일 때 식1, 거짓일 때 식2 사용
    if를 사용했다면 반드시 else를 사용해야함
    elif는 사용할 수 없음
'''

print(f"{'람다식과 map 함수2':-^30}")
list_data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
strNumLambda = lambda x: "3x" if x % 3 == 0 else x
result = list(map(strNumLambda, list_data2))
print("결과2", result)

print(f"{'람다식과 filter 함수':-^30}")
list_data3 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
result = list(filter(lambda z: z > 25 and z < 80, list_data3))
print("결과3", result)

print(f"{'람다식과 reduce 함수':-^30}")
import functools, operator

sum1 = functools.reduce(lambda i, j: i + j, range(1, 11))
print("결과4-1", sum1)

sum2 = functools.reduce(operator.add, range(1, 11))
print("결과4-2", sum2)
