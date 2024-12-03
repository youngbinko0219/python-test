'''
클래스 변수와 정적 메서드
클래스를 통해 생성되는 인스턴스에는 멤버 변수와 멤버 메서드가 포함된다. 하지만
클래스 변수와 정적 메서드는 인스턴스 내부에 존재하지 않고 별도의 공간에 독립적으로
생성된다. 따라서 2개 이상의 인스턴스를 생성하더라도 딱 하나만 생성되어 모든
인스턴스가 공유하게 된다.
자바에서 스태틱과 동일한 개념이다.
'''

class MyCalculator:
    calCount = 0

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def calculate(self, symbol):
        MyCalculator.calCount += 1
        if symbol == "+":
            result = self.first + self.second
        elif symbol == "-":
            result = self.first - self.second
        elif symbol == "*":
            result = self.first * self.second
        elif symbol == "/":
            result = self.first / self.second
        return result

    @staticmethod
    def otherNumMulti(refCls, otherNum):
        '''
        해당 함수는 정적 함수로 정의되었으므로 인스턴스 외부에 독립적으로 생성된다.
        따라서 특정 인스턴스의 멤버 변수에 접근하기 위해 인스턴스의 참조 값을
        매개 변수로 받은 후 사용해야한다.
        '''
        result = (refCls.first + refCls.second) * otherNum
        MyCalculator.calCount += 1
        print("result : ", result)
        print("calcount : ", MyCalculator.calCount)

    def __str__(self):
        str = f"계산기 클래스 입니다." f"first={self.first},second={self.second}"
        return str


cal1 = MyCalculator(5, 9)
cal2 = MyCalculator(3, 4)

print("덧셈 : ", cal1.calculate("+"))
print("뺄셈 : ", cal2.calculate("-"))
print("곱셈 : ", cal1.calculate("*"))
print("나눗셈 : ", cal2.calculate("/"))
print("계산횟수 : ", MyCalculator.calCount)

MyCalculator.otherNumMulti(cal1, 10)
MyCalculator.otherNumMulti(cal2, 10)
