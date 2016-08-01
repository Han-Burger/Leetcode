class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = [1] * n
        for i in xrange(1, m):
            for j in xrange(1, n):
                d[j] += d[j - 1]
        return d[-1]
                    
            