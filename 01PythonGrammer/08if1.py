print(f'{"if문 첫번째 형식":-^30}')
a, b, c, str = 10, 20, 30, "Python"
if a != b:
    print("a와 b는 다르다.")
if a <= c:
    print("a는 c보다 작거나 같다.")
if str:
    print("문자열은 True를 반환한다.")

# if a > str:  # 애러발생
#    print("문자열과 정수는 비교의 대상이 될수없다.")

print(f'{"if문 두번째 형식":-^30}')
if a > b:
    print("a는 b보다 크지 않습니다.")
else:
    print("a는 b보다 큽니다.")

if a == b and b != c:
    print("모든 조건을 만족합니다.")
else:
    print("조건중 False가 있습니다.")

if a > b or b < c:
    print("조건중 True가 있습니다.")
else:
    print("모든 조건에 만족하지 않습니다.")

print(f'{"if문 세번째 형식":-^30}')
age = 33
print("삶은 ", end="")
if age >= 35:
    print("중년입니다.")
elif age >= 30:
    print("중년의 시작입니다.")
else:
    print("청년입니다.")
