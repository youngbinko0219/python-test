'''
format() 사용
문자열 포매팅은 서식문자보다 더 간단히 문자열을 표현할 수 있다
중괄호 안에 포매팅을 지정하고 format() 메서드로 값을 삽입한다.
'''

str1 = "name : {0}".format("홍길동")
print(str1)

age = 55
str2 = "age : {0}".format(age)
print(str2)

str3 = "name : {name}, age : {age}".format(name="홍길동", age=33)
print(str3)

str4 = "이름 : {}, 나이 : {}".format("이순신", 44)
print(str4)

str5 = "나이 : {1}, 이름 : {0}".format("이성계", 55)
print(str5)

str6 = "항목1 : {0}, 항목2 : {1}, 항목3 : {0}".format("서울", "부산")
print(str6)

str7 = "정수3자리 : {0:03d}, {1:03d}".format(12345, 12)
print(str7)

str8 = "소수점 아래 2자리 : {0:0.2f}, 소수점 아래 5자리 : {1:0.5f}".format(
    123.1234567, 3.14
)
print(str8)
'''
문장이 길어져서 2줄로 표현해야하는 경우 역슬러쉬로 연결하면 된다.
파이껀은 문장의 끝에 ;를 사용하지 않으므로 
줄이 바뀌는 순간 새로운 문장으로 인식하기 때문이다.
'''

str9 = "{{ {0} }}".format("Python 중괄호 표현")
print("str9=", str9)

str10 = 1592000
print(format(str10, ","))
