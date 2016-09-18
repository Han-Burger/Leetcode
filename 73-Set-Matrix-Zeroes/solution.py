class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        """
        Use the first row that has 0 to store colomns that has 0
        """
        row = -1
        for i in xrange(len(matrix)):
            rowHasZero = False
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == 0:
                    if row < 0:
                        row = i
                    rowHasZero = True
                    matrix[row][j] = 0
            if rowHasZero and row != i:
                for j in xrange(len(matrix[0])):
                    matrix[i][j] = 0
        if row >= 0:
            for j in xrange(len(matrix[0])):
                if matrix[row][j] == 0:
                    for i in xrange(len(matrix)):
                        matrix[i][j] = 0
                else:
                    matrix[row][j] = 0
                    
                
                    