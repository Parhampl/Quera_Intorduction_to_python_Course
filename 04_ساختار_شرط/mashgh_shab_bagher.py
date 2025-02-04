a, b, c = map(int, input().split())
a, b, c = sorted([a, b, c])
if a != 0 and a+b+c == 180 and c != 180:
    print("Yes")
else:
    print("No")
