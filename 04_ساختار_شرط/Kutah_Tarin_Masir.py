'''
Problem URL: https://quera.org/problemset/170059?tab=description




1 ----------------- 2 
'                   '
'                   '
'                   '
'                   '
3 ----------------- 4

bayad bebinim az harnoghte shuru konim chand harekat bayad bznim beresim be ye noghte dg 
masln az 1 be 2 mishe 1 harekat

1 ---> 2   1 
1 ---> 3   1 
1 ---> 4   2

2 ---> 4   1 
2 ---. 3   2

3 ----> 4  1
'''


start_point = int(input())
end_point = int(input())

if start_point > end_point:
    start_point, end_point = end_point, start_point

if start_point == end_point:
    print(0)
elif (start_point == 1 and end_point == 4) or (start_point == 2 and end_point == 3):
    print(2)
else:
    print(1)
