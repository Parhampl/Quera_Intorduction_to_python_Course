'''
d*e*f ---> abaad mokaab mostatil yakh.
a*b*c ---> abaad jaabe dar baz(az samt a*b baz ast)

ajbe ro nemishe tekun dad vali yakh ro mishe charkhund ta be andaze i berese ke betune az samt a*b
vared e jabe beshe
'''
a, b, c, d, e, f = map(int, input().split())

if a < b:
    a, b = b, a


if ((d <= a and e <= b) or (d <= b and e <= a)) or (d <= a and f <= b) or (d <= b and f <= a) or (f <= a and e <= b) or (f <= b and e <= a):
    print("zende mimuni")
else:
    print("dari mimiri")
