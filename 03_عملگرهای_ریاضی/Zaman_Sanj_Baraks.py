'''
addad hayi ke saat neshun mide az tuye ayne dide mishe va bayad dorost beshe chon bar aks dide mishe
maslan 3:50 --> 9:10
nokte hayi ke hast:
1. SAAT 0:0 NABAYD BESHE 12:60
2. KHURUJI BAYAD HAM HOUR VA HAM MINUTE 2 RAGHAM BASHE(09:10)
'''
Mirror_hour, Mirror_minute = map(int, input().split())
Actual_Hour = (12 - Mirror_hour)%12
Actual_Minute = (60 - Mirror_minute)%60
print(f"{Actual_Hour:02d}:{Actual_Minute:02d}")