# Should check these rules in the character you are getting in first line
# First = Second -> print max
# First = Third  -> print min
# Else: print None
Char1, Char2, Char3 = input().split()
Num1, Num2, Num3 = map(int, input().split())


MAX = Num1
if MAX < Num2:
    MAX = Num2
if MAX < Num3:
    MAX = Num3

MIN = Num1
if MIN > Num2:
    MIN = Num2
if MIN > Num3:
    MIN = Num3

if Char1 == Char2:
    print(f"Max : {MAX}")
elif Char1 == Char3:
    print(f"Min : {MIN}")
else:
    print("None")
