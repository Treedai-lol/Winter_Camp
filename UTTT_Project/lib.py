class Board():
    def __init__(self,bs: list,o:bool) -> None:
        self.bs = bs
        self.o = o
def PrintBoard(board:Board) ->None: #print board function
    for i in range(0,3):
        for j in range(0,3):
            for k in range(3*i,3*i+3):
                for l in range(3*j,3*j+3):
                    print(board.bs[k][l],end=" ")
            print("\n",end="")
        pass
    pass
def GetOwnerShip(board:Board,index:int,o:bool) ->list: #returns the indices of pieces owned
    output = []
    if o:
        for i in range(0,9):
            if  board.bs[index][i] == 1:
                output.append(i)
    else:
        for i in range(0,9):
            if  board.bs[index][i] == 2:
                output.append(i)
    return output
def BoardFinished(board:Board,index:int,o:bool) ->bool:
    output = False
    piecelist = GetOwnerShip(board,index,o)
    a = b = c = False
    winning = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in winning:
        for j in piecelist:
            if j == i[0]:
                a = True
            if j == i[1]:
                b = True
            if j == i[2]:
                c = True
        if a & b & c:
            output = True
    return output


        
def BoardInit() ->Board:
    list = []
    for i in range(0,9):
        list.append([])
        for j in range(0,9):
            list[i].append(0)
    list[0][0] = 0
    list[0][1] = 0
    list[0][2] = 0
    list[0][3] = 0
    list[0][4] = 0
    list[0][5] = 0
    list[0][6] = 2
    list[0][7] = 2
    list[0][8] = 2
    board = Board(list,True)
    return board
def main():
    board = BoardInit()
    PrintBoard(board)
    print(GetOwnerShip(board,0,False))
    print(BoardFinished(board,0,False))
if __name__ == '__main__':
    main()