board = []
temp = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
for i in range(0,9): #board initialization
    board.append([])
    for j in range(0,9):
        board[i].append(9*i+j)
def printb(bs: list): #print board function
    for i in range(0,3):
        for j in range(0,3):
            for k in range(3*i,3*i+3):
                for l in range(3*j,3*j+3):
                    print(bs[k][l],end=" ")
            print("\n",end="")
        pass
    pass
def BoardFinished(bs:list,index:int):
    bs[index]
printb(board)
