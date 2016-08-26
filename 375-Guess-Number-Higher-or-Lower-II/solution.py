class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return self.dfs(1, n, [[-1 for j in xrange(n + 1)] for i in xrange(n + 1)])
        return self.dp(n)
        
    def dfs(self, start, end, m):
        if start > end: return 0
        if m[start][end] >= 0:
            return m[start][end]
        
        if start == end:
            m[start][end] = 0
        else:
            minPrice = 2 ** 31 - 1
            for pick in xrange(start, end + 1):
                currPrice = pick + max(self.dfs(start, pick - 1, m), self.dfs(pick + 1, end, m))
                minPrice = min(minPrice, currPrice)
            m[start][end] = minPrice
        return m[start][end]
        
    def dp(self, n):
        m = [[0 for j in xrange(n + 1)] for i in xrange(n + 1)]
        for j in xrange(1, n + 1):
            for i in xrange(j - 1, 0, -1):
                minPrice = 2 ** 31 - 1
                for pick in xrange(i, j + 1):
                    if pick == j: minPrice = min(minPrice, pick + m[i][pick - 1])
                    else: minPrice = min(minPrice, pick + max(m[i][pick - 1], m[pick + 1][j]))
                m[i][j] = minPrice
        return m[1][n]



















