# Three digit can be sides of a triangle when the sum of each two pair is greater than the other sidea, b, c = map(int, input().split())

if a+b > c and a+c > b and b+c > a:
    print("Bale")
else:
    print("Na")
