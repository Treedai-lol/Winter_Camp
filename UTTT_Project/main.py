board = []
for i in range(0,9):
    board.append([])
    for j in range(0,9):
        board[i].append(9*i+j)
def printb(bs: list):
    for i in range(0,3):
        for j in range(0,3):
            for k in range(3*i,3*i+3):
                for l in range(3*j,3*j+3):
                    print(bs[k][l],end=" ")
            print("\n",end="")
        pass
    pass

printb(board)
