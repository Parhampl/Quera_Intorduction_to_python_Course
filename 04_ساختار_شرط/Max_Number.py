#Find the maximum number among the inputs
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a > b:
    b = a 
if c > b:
    b = c 
if d > b:
    b = d 

print(b)