class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        if not matrix or len(matrix) < 2: return
        n = len(matrix)
        
        i, j = 0, n - 1
        while(i < j):
            for shift in xrange(0, j - i):
                p, q = i + shift, j - shift
                tmp = matrix[i][p]
                matrix[i][p] = matrix[q][i]
                matrix[q][i] = matrix[j][q]
                matrix[j][q] = matrix[p][j]
                matrix[p][j] = tmp
            i += 1
            j -= 1
        return
                