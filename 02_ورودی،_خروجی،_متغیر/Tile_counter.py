# n = Length    m = Width
n, m = map(int, input().split())
Length_kashi = 5
Width_kashi = 4
area_kashi = Length_kashi * Width_kashi
area_pool = n*100*m*100
print(int(area_pool/area_kashi))
