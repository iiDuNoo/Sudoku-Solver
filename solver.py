#sudoku solver project
#project uses backtracking algorithm and returns complete solution
def solvemode(bo):
    find = find_empty(bo) #finds empty cell
    if find:
        row, column = find #collects row and column dimensions, stores in bo 2D array of integers
    else:
        return True

    for i in range (1, 10):
        if correct(bo, (row,column),i):
            bow[row][column] = i

            if solve(bo):
                return True

            bo[row][column] = 0

    return False

def correct(bo,pos,num):
#if the move is correct, uses 2D array of stored integers and row/column coordinates
#returns bool val

#first check rows
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

#then check column
    for i in range(0, len(bo)):
        if bo[i][pos[1]]== num and pos[1] !=i:
            return False

    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

    def find_empty(bo):
        #finds empty space on sudoku board using bo
        #should return row and columns

        for i in range(len(bo)):
            for x in range(len(bo)):
                if bo[i][x]==0:
                    return (i,x)
        return None

    def print_board(bo):
        #outputs board using bo
        for i in range(len(bo)):
            if i % 3 ==0 and i !=0:
                print("- - - - - - - - - - - - - -")

            for x in range(len(bo[0])):
                if x % 3 ==0:
                    print(" | ",end="")

                if x == 8:
                    print(bo[i][j], end="\n")

                else:
                    print(str(bo[i][j])+ " ", end = "")
