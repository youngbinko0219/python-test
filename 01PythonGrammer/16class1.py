class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print(f"이름 : {self.name}")
        print(f"나이 : {self.age}")

    def justDoit(self, act):
        print(f"{self.name} 님이 {act}를 합니다.")

    def __str__(self):
        return f"제 이름은 {self.name}({self.age})입니다."


person1 = Person("박찬호", 30)
person2 = Person("손흥민", 28)

person1.showInfo()
person1.justDoit("야구")

print(person2)
person2.justDoit("축구")
