'''
Write down a code that takes seconds as input and turn it to standard time(Hour:Minute:Second)

Ex.
Input --> 7560
Output --> 2 : 6 : 0

'''
n = int(input())
Hour = n // (60*60)
Minute = (n % (60*60))//60
Second = (n % (60*60)) % 60
print(f"{Hour} : {Minute} : {Second}")
