# 시나리오: 1~100사이의 정수 중 3의 배수의 합을 구하시오.
total = 0
for i in range(1, 101):
    if i % 3 == 0:
        total += i
        print(i, end='+')
print('\b', '=', total)

print()
print("="*30)

'''
List Comprehension
대괄호 안에 포 루프로 반복적인 표현식을 실행해서 리스트의 요소들을 초기화하는 방법

'''
list = [n ** 2 for n in range(10) if n % 3 == 0]
print(list)

print()
print("="*30)

# --------------------------------------------
# 메트릭스 출력
n = 4  # 메트릭스의 크기
for i in range(n):
    for j in range(n):
        if i == j:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

# ----------------------------------------------
# 피라미드 출력
n = 5  # 피라미드의 높이
for i in range(1, n + 1):
    print("*" * i)
 