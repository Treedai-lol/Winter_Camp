class Board():
    def __init__(self,bs: list,o:bool) -> None:
        self.bs = bs
        self.o = o
def PrintBoard(board: Board): #print board function
    for i in range(0,3):
        for j in range(0,3):
            for k in range(3*i,3*i+3):
                for l in range(3*j,3*j+3):
                    print(board.bs[k][l],end=" ")
            print("\n",end="")
        pass
    pass
def BoardFinished(bs:list,index:int):
    bs[index]
temp = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
def main():
    list = []
    for i in range(0,9):
        list.append([])
        for j in range(0,9):
            list[i].append(9*i+j)
    Default: Board = Board(list,True)
    PrintBoard(Default)

if __name__ == '__main__':
    main()