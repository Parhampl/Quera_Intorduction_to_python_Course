'''
1. kalame aval o dovom havij bud bayad eyes chap shavad
2. kalame aval o sevom ya kalame aval o dovom shalgham bud cold chap kon.
3. dar ghei in surat dead or chap kon.

'''

a, b, c = input().split()

if a == "havij" and b == "havij":
    print("eyes!")
elif a == "shalgham" and (b == "shalgham" or c == "shalgham"):
    print("cold!")
else:
    print("dead")
