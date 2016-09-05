class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in xrange(9):
            s = set()
            for j in xrange(9):
                c = board[i][j]
                if c >= '1' and c <= '9':
                    if c in s: return False
                    else: s.add(c)
                elif c != '.':
                    return False
        
        for j in xrange(9):
            s = set()
            for i in xrange(9):
                c = board[i][j]
                if c >= '1' and c <= '9':
                    if c in s: return False
                    else: s.add(c)
                elif c != '.':
                    return False
        
        for p in xrange(3):
            for q in xrange(3):
                s = set()
                for i in xrange(3):
                    for j in xrange(3):
                        c = board[p * 3 + i][q * 3 + j]
                        if c >= '1' and c <= '9':
                            if c in s: return False
                            else: s.add(c)
                        elif c != '.':
                            return False
    
        return True
                                