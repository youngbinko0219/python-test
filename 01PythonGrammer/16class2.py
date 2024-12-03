import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calArea(self):
        return math.pi * (self.radius**2)

    def calRound(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"원의 반지름은 {self.radius}입니다."


circle1 = Circle(5)
print(circle1)
print("원의 넓이 : ", circle1.calArea())
print("원의 둘레 : ", circle1.calRound())
