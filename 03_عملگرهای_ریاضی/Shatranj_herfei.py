'''
Standard number of chess pieces:
1 king
1 Queen
2 Rook
2 Bishop
2 Knight
8 Pawn

The input includes 6 digits in order from left to right:
king, queen, rook, bishop, knight, pawn

The Output should tell use the difference of satndard number of chess pieces and the input number
'''
king, queen, rook, bishop, knight, pawn = 1, 1, 2, 2, 2, 8
input_king, input_queen, input_rook, input_bishop, input_knight, input_pawn = map(
    int, input().split())

print((king - input_king), (queen-input_queen), (rook-input_rook), (bishop-input_bishop), (knight-input_knight), (pawn-input_pawn))


#Alternative way
# Standard = [1,1,2,2,2,8]
# input_chess = list(map(int, input().split()))
# for i in range(len(Standard)):
#     print(Standard[i]-input_chess[i], end=" ")
