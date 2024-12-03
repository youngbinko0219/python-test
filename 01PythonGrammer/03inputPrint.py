i, j, k = 7, 8, 9
print(i, j, k)
print(i, j, k, sep="-")
print(i, end=" ")
print(j, end=" ")
print(k)

print("원주율 =", format(3.14159, "8.3f"))
print("맥주 =", format(5000, "10d"))
print("노트북 =", format(1580000, "3,d"))

# 서식문자 : 문자열 %s, 정수 %d, 실수 %f
name = "성유겸"
age = 13
price = 123.456
print("이름 : %s, 나이 : %d, 용돈 : %.2f" % (name, age, price))

menu1 = "치킨"
menu2 = "맥주"
print("오늘은 {str}로 {0}과 {1}로 정했다.".format(menu1, menu2, str="저녁"))
print("오늘은 {}과 {}로 {str}을 시작하겠다.".format(menu1, menu2, str="아침"))

# 인풋을 통해 입력받는 값은 항상 문자가 되기 때문에 따로 처리를 해야한다.
num = input("숫자를 입력하세요 : ")
print("입력한 숫자는", num, "이고, 타입은", type(num))

result1 = int(num) + 10
print("덧셈결과", result1)

result2 = int(input("숫자1 : ")) * int(input("숫자2 : "))
print("곱셈결과", result2)

result3 = float(input("원주율 : ")) * (float(input("원의반지름 : ")) ** 2)
print("원의넓이", result3)
