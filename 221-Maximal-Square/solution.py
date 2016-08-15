class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        
        m = [1 if c == '1' else 0 for c in matrix[0]]
        maxR = 1 if 1 in m else 0
        for i in xrange(1, len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == '0':
                    m[j] = 0
                elif j == 0:
                    m[j] = 1
                elif m[j] == m[j - 1]:
                    m[j] += 1 if matrix[i - m[j]][j - m[j]] == '1' else 0
                else:
                    m[j] = 1 + min(m[j], m[j - 1])
                maxR = max(maxR, m[j])
        return maxR ** 2
        
                    