# In this Problem we are trying to detect the degree which we will get from
# input command are for Right triangle or NotImplemented.
a, b, c = map(int, input().split())
if a+b+c == 180 and (a != 0 and b != 0 and c != 0):
    if a == 90 or b == 90 or c == 90:
        print("Bale")
    else:
        print("Na")
else:
    print("Na")
