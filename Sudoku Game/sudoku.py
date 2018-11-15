# Sudoku generator Algorithm

import copy
import random

# sample = []
def construct_solution():
    while True:
        try:
            sudoku = [[0]*9 for i in range(9)]
            rows = [set(range(1,10)) for i in range(9)]
            columns = [set(range(1,10)) for i in range(9)]
            squares = [set(range(1,10)) for i in range(9)]
            for i in range(9):
                for j in range(9):
                    choices = rows[i].intersection(columns[j]).intersection(squares[int(i/3)*3+int(j/3)])
                    choice = random.choice(list(choices))
                    
                    sudoku[i][j] = choice
                    
                    rows[i].discard(choice)
                    columns[j].discard(choice)
                    squares[int(i/3)*3 + int(j/3)].discard(choice)
            return sudoku
        except IndexError:
            pass

def pluck(sudoku, n=0):
    
    def canBeA(puz, i, j, c):
        v = puz[int(c/9)][c%9]
        if puz[i][j] == v: return True
        if puz[i][j] in range(1,10): return False
        
        for m in range(9):
            if not (m==int(c/9) and j==c%9) and puz[m][j] == v: return False
            if not (i==int(c/9) and m==c%9) and puz[i][m] == v: return False
            if not (int(i/3)*3 + int(m/3)==int(c/9) and int(j/3)*3 + m%3==c%9) and puz[int(i/3)*3 + int(m/3)][int(j/3)*3 + m%3] == v:
                return False
        return True
    
    cells = set(range(81))
    cellleft = cells.copy()
    while len(cells) > n and len(cellleft):
        cell = random.choice(list(cellleft))
        cellleft.discard(cell)
        
        row = col = square = False
        
        for i in range(9):
            if i != int(cell/9):
                if canBeA(sudoku, i, cell%9, cell): row = True
            if i != cell%9:
                if canBeA(sudoku, int(cell/9), i, cell): col = True
            if not ((int(cell/9)/3)*3 + int(i/3) == int(cell/9)) and (int(cell/9)%3 + i%3 == cell%9):
                if canBeA(sudoku, int((cell/9)/3)*3 + int(i/3), (int(cell/9)%3)*3 + i%3, cell): square = True
        if row and col and square:
            continue
        else:
            sudoku[int(cell/9)][cell%9] = 0
            cells.discard(cell)
    return(sudoku, len(cells))

def run(n = 28, iter = 100):
    all_results = {}
    a_sudoku_solution = construct_solution()
    
    for i in range(iter):
        sudoku = copy.deepcopy(a_sudoku_solution)
        (result, number_of_cells) = pluck(sudoku,n)
        all_results.setdefault(number_of_cells, []).append(result)
        if number_of_cells <= n: break
    return all_results

def best(set_of_puzzels):
    return set_of_puzzels[min(set_of_puzzels.keys())][0]

#def display(sudoku):
 #   print(sudoku)
        
#results = run()
#sudoku = best(results)
#display(sudoku)
