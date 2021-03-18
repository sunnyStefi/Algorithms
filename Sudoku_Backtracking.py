#!/usr/bin/python3

row0 = [4,0,0,0,5,0,0,3,2]
row1 = [0,1,0,0,9,0,7,0,5]
row2 = [7,5,3,0,0,4,1,9,6]
row3 = [0,0,1,0,7,0,0,0,0]
row4 = [6,0,9,0,0,1,2,5,0]
row5 = [0,0,0,5,0,0,6,1,3]
row6 = [3,0,4,0,0,8,0,0,1]
row7 = [0,0,0,4,0,0,0,7,8]
row8 = [0,0,0,7,6,3,0,2,9]
sudoku = [row0, row1, row2, row3, row4, row5, row6, row7, row8]
rowNr = 1

def printSudoku(isSolved):
    global rowNr
    if isSolved:
        print("\n   **** SOLVED SUDOKU **** \n")
    else:
        print("\n   **** UNSOLVED SUDOKU **** \n")
   
    print(" O-----------------------------> y")
    for row in sudoku:
        print(" | "+str(row[0:3]) + str(row[3:6]) + str(row[6:9]))
        if (rowNr == len(sudoku)):
             print(" V \n x")
        elif (rowNr%3 == 0):
            print(" |")  
        rowNr = rowNr + 1

def fits(c, r, n):
    global sudoku
#it's possible to add the number in the horizontal line?
    for i in range(9):
        if sudoku[c][i] == n :
            return False
#it's possible to add the number in the vertical line?
    for i in range(9):
        if sudoku[i][r] == n :
            return False
#it's possible to add the number in the square?
    r0 = (r//3)*3
    c0 = (c//3)*3
    for i in range(3):
        for j in range(3):
            if sudoku[c0+i][r0+j] == n :
                return False 
    return True

def findEmptySpace():
    for r in range(9):
        for c in range(9):
          if sudoku[c][r] == 0 :
              return r,c
    return -1, -1


def solve():
    r,c = findEmptySpace()
    #base case
    if r == -1 :
        printSudoku(True)
        return
    else :
        for n in range (1,10):
            if fits(c,r,n):
                sudoku[c][r] = n
                solve()
                sudoku[c][r] = 0 


printSudoku(False)
solve()
