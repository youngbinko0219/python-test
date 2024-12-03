a = tot = 10

a += 1
tot += a
print(a, tot)

# 알고리즘에서 정렬을 위해 사용하는 스왑 기능을 아래와 같이 간편하게 구현할 수 있다.
v1, v2 = 100, 200
v2, v1 = v1, v2
print(v1, v2)

mylist = [1, 2, 3, 4, 5]
x1, *x2 = mylist
print("패킹연산자1", x1, x2)

*y1, y2 = mylist
print("패킹연산자2", y1, y2)
