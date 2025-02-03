c = input()
n = int(input())
for i in range(n):
    if i == n-1 or i == 0:
        print(n*c)
    else:
        print(c+" "*(n-2)+c)
