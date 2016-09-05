class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        #self.backtracking(board)
        self.preElimination(board)
    
    def preElimination(self, b):
        hasChange = False
        for i in xrange(9):
            for j in xrange(9):
                if b[i][j] == '.':
                    validInput = '0'
                    overOneInput = False
                    for c in map(str, xrange(1, 10)):
                        if self.valid(b, i, j, c):
                            if validInput != '0':
                                overOneInput = True
                                break
                            else:
                                validInput = c
                    if overOneInput: 
                        continue
                    else:
                        b[i][j] = validInput
                        hasChange = True
                        break
            if hasChange: break
        if hasChange: self.preElimination(b)
        else: return self.backtracking(b)
    
    def backtracking(self, b):
        self.solve(b)
    
    def solve(self, b):
        for i in xrange(9):
            for j in xrange(9):
                if b[i][j] == '.':
                    for c in map(str, xrange(1, 10)):
                        if self.valid(b, i, j, c):
                            b[i][j] = c
                            if self.solve(b): return True
                            else: b[i][j] = '.'
                    # has no solution for this cell
                    return False
        return True
                            
    
    def valid(self, b, p, q, c):
        # b for board, p for row, q for column, c for input
        for j in xrange(9):
            if j != q and b[p][j] == c: return False
        for i in xrange(9):
            if i != p and b[i][q] == c: return False
        for i in xrange(3):
            for j in xrange(3):
                row, col = (p / 3) * 3 + i, (q / 3) * 3 + j
                if row != p and col != q and b[row][col] == c: return False
        return True
                    