'''
There is different way of using varibales inside an string
in this section we will discuss about some of them.
'''
#First Using %
#%d = int  %f = float %s = string
Age = 22
decimal_sample = 1.872
print("Parham age is %d" %(Age))
print("the height is %.1f" %(decimal_sample))


# Second using {}
print(f"parham age is {Age}")
print(f"The height is {decimal_sample:.1f}")

'''
What will happen if using number before d in %d??
this approach called padding.
'''
print("parham's age is %02d"%(Age))
print("parham's age is %04d"%(Age))


#Another example
side = 4
shape = "Square"
area = side * side
print(f"Area of {shape} = {area}")


#Final Problem:
#Write a code that take time, region and air tempreature and return this in format o string

Time = input()
Region = input()
Temp = float(input())
print(f"Today is {Time}.\nI live in {Region}, and the tempreture here is {Temp} degree of celcius")
print()
print("Today is %s.\nI live in %s, and the tempreture here is %.2f degree of celcius" %(Time, Region, Temp))
