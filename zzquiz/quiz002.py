'''
문제 2: 팰린드롬 문자열 확인
주어진 문자열이 팰린드롬인지 확인하는 함수를 작성하세요.
(팰린드롬: 앞뒤가 똑같은 문자열, 예: "level", "radar")
함수 이름: is_palindrome
입력: 문자열 s (예: "radar")
출력: True 또는 False
'''

def is_palindrome(s):
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


user_input = input("문자열을 입력하세요: ")
if is_palindrome(user_input):
    print(f'"{user_input}"은(는) 팰린드롬입니다.')
else:
    print(f'"{user_input}"은(는) 팰린드롬이 아닙니다.')