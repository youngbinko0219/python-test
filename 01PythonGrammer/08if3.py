# 퀴즈 1

scores = [
    int(input("국어 점수를 입력하세요: ")),
    int(input("영어 점수를 입력하세요: ")),
    int(input("수학 점수를 입력하세요: ")),
    int(input("사회 점수를 입력하세요: ")),
    int(input("과학 점수를 입력하세요: ")),
]
sum = sum(scores)

average = sum / len(scores)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"평균 점수: {average:.2f}, 학점: {grade}")

# ------------------------------------------------------------------

# 퀴즈 2

user_info = ["user1", "user2", "user3"]
password = "1234"

user_id = input("아이디를 입력하세요: ")

if user_id in user_info:
    user_password = input("패스워드를 입력하세요: ")
    if user_password == password:
        print("로그인 성공!")
    else:
        print("패스워드가 일치하지 않습니다.")
else:
    print("등록되지 않은 아이디입니다.")
