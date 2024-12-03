'''
멤버 변수의 정보 은닉을 위해 private 대신 __를 사용한다. 정보은닉이란
멤버 변수의 외부 접근을 차단하고, 클래스 내부에서만 접근하도록 처리하는 것을
말한다.
'''

class Computer:
    def __init__(self, name, passwd):
        self.name = name
        self.__passwd = passwd

    def hitKeyboard(self):
        return f"{self.name}로 키보드 작업을 합니다."

    def clickMouse(self):
        return self.__passwd

    def getPasswd(self):
        return self.__passwd

    def setPasswd(self, passwd):
        self.__passwd = passwd


mycom = Computer("lg gram", "qwer1234")

print(mycom.hitKeyboard())
mycom.clickMouse()

print("computer name", mycom.name)

print("password", mycom.getPasswd)

mycom.setPasswd("asdf1234")
print("changed password", mycom.getPasswd())

mycom.__passwd = "xxxxXXXX"
print("changed password2", mycom.getPasswd())
