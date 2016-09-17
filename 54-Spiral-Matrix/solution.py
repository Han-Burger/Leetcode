class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if not matrix or len(matrix) == 0 or not matrix[0] or len(matrix[0]) == 0: return []
        x, y, p, q = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        
        res = []
        while x <= y and p <= q:
            if x == y and p == q:
                res.append(matrix[x][q])
            elif x == y:
                for j in xrange(p, q + 1):
                    res.append(matrix[x][j])
            elif p == q:
                for i in xrange(x, y + 1):
                    res.append(matrix[i][p])
            else:
                for j in xrange(p, q):
                    res.append(matrix[x][j])
                for i in xrange(x, y):
                    res.append(matrix[i][q])
                for j in xrange(q, p, -1):
                    res.append(matrix[y][j])
                for i in xrange(y, x, -1):
                    res.append(matrix[i][p])
            x += 1
            y -= 1
            p += 1
            q -= 1
        return res