'''
Mikhaim dozdi konimva midunim maghaze 4 ta durbin dare ka har kodum tuye yeki az azlae mostatile
maghaze hastan va mogheiat 3 tasho midunim o bayad 4 romi peida konim masln shabih zir
Inputs:
        6 7
        4 7
        6 5
Outputs:
        4 5(chon fghd in mogheiat az mosalas nist)
'''


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x4 = x3 ^ x2 ^ x1
y4 = y3 ^ y2 ^ y1

print(x4, y4)


# x4, y4 = 0, 0

# if x1 == x2:
#     x4 = x3
# elif x1 == x3:
#     x4 = x2
# elif x2 == x3:
#     x4 = x1

# if y1 == y2:
#     y4 = y3
# elif y1 == y3:
#     y4 = y2
# elif y2 == y3:
#     y4 = y1

# print(x4, y4)
