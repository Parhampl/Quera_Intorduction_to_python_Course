'''
Check the water is in Steam, Ice or liquid condition by its tempreature.
'''

Temp = int(input())
if Temp > 100:
    print("Steam")
elif Temp < 0:
    print("Ice")
else:
    print("Water")
