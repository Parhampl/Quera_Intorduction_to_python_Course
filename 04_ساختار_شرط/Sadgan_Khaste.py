'''
2 ta adad 3 raghami darim bayad moghayese konim makusesho bebinim kodum bozorg tare
note: manzur az makus jaye yekan o sadgan esh o avaz konim
akharesh ooni ke makusesh kuchik tar bud ro khodesh ro kuchik tar az oon yeki chap mikonim
'''


a = int(input())
b = int(input())
# a_result = a
# b_result = b

yekan_a = a % 10
dahngan_a = (a % 100 - yekan_a)/10
sadgan_a = a // 100

yekan_b = b % 10
dahngan_b = (b % 100 - yekan_b)/10
sadgan_b = b // 100

if ((yekan_a*100 + dahngan_a * 10 + sadgan_a) < (yekan_b*100 + dahngan_b * 10 + sadgan_b)):
    print(f"{a} < {b}")
elif ((yekan_a*100 + dahngan_a * 10 + sadgan_a) > (yekan_b*100 + dahngan_b * 10 + sadgan_b)):
    print(f"{b} < {a}")
else:
    print(f"{b} = {a}")
