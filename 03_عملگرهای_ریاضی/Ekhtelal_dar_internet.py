'''
There is a code on any food or fruits which consist of 2 digit we should extract each digit and add them together.
BECAREFULL: the input number is not splited by space.
for example:
Input --> 23
Output --> 5
'''
n, m = map(int, input().strip())
print(n+m)

# #Alternative
# n = int(input())
# first = n%10
# n //= 10
# print(n+ first)
