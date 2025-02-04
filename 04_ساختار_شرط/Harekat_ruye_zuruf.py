'''
Kmatarin meghdar harekat baraye inke meghdar ba tu 3 zarf a, b, c yeki beshe ro dar biar.
'''


def Minimum_Number_of_Movement(a, b, c, avg):
    if a == b == c:
        return (0)
    elif b == avg:
        return (1)
    elif b == c:
        return (2)
    elif c > b > a:
        return (2)


a, b, c = map(int, input().split())
avg = (a+b+c)/3

# Sort the inputs
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
Output = Minimum_Number_of_Movement(a, b, c, avg)
print(Output)
