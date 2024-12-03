'''
반복문
파이썬에서 반복문은 와일문과 포문만 있다.
형식]
초기값
while 조건문:
    수행할문장
    증감식
else:
    정상 종료되었을 때 진입
    
단 와일문이 완료되지 않은 상태로 탈출하게 되면 else구문으로 진입할 수 없다.
'''

# 시나리오 1: 열 번 찍어 안 넘어가는 나무 없다는 속담을 while문으로 구현하세요.
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")

print()
print("="*30)

# 파이썬에서는 문자열도 조건식으로 사용할 수 있다.
str = 'python'
while str:
    print(str, end=' ')
    str = str[1:]

print()
print("="*30)

# 시나리오 2: 1~10까지의 합을 구하시오.
sum = 0
i = 1
while i <= 10:
    sum += i
    if i < 10:
        print(i, end=" + ")
    else:
        print(i, end=" = ")
    i += 1
print(sum)

print()
print("="*30)

# 시나리오 3: 하루에 판매할 수 있는 커피는 모두 10잔이다.
# while문으로 무한루프를 만든 후 10잔의 커피가 모두 판매되었을 때
# 반복문을 탈출하는 프로그램을 작성하시오. 단, break를 사용하시오.
coffee = 10
while True:
    print("커피 한잔을 판매합니다.")
    coffee -= 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

print()
print("="*30)

# 시나리오 4: 로또 번호를 생성하는 프로그램을 작성하시오.
# 1~45 사이에서 중복되지 않은 숫자 6개를 추출하면 된다.
import random
lotto = set()
while True:
    rndNum = random.randint(1, 45)
    lotto.add(rndNum)
    if len(lotto) == 6:
        break
print("로또번호:", sorted(lotto))
