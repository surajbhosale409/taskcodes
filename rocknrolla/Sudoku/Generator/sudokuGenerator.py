import os,random,math

def init():
    os.system("clear")
    sudoku=list()
    for i in range(1,10):
        l=list()
        for j in range(1,10):
            l.append(0)
        sudoku.append(l)
    for i in range(0,9):
        print (sudoku[i])

   return sudoku


def transpose():



init()
