"""
문제 1: 숫자의 합 구하기
사용자로부터 양의 정수를 입력받아 각 자릿수의 합을 계산하는 함수를 작성하세요.
함수 이름: sum_of_digits
입력: 정수 n (예: 1234)
출력: 각 자릿수의 합 (예: 10)
"""


def sum_of_digits(n):
    if n < 0:
        raise ValueError("양의 정수만 입력하세요.")
    total = 0
    for digit in str(n):  # 숫자를 문자열로 변환한 뒤 반복
        total += int(digit)  # 각 자릿수를 정수로 변환하여 더함
    return total


user_input = int(input("양의 정수를 입력하세요: "))
result = sum_of_digits(user_input)
print(f"{user_input}의 각 자릿수의 합은 {result}입니다.")
