import lib

def main():
    list = []
    for i in range(0,9):
        list.append([])
        for j in range(0,9):
            list[i].append(0)
    Default: lib.Board = lib.Board(list,True)
    lib.PrintBoard(Default)
if __name__ == '__main__':
    main()