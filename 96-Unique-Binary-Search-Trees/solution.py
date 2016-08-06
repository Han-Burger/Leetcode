class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1: return 0
        
        m = [1] * 2 + [0] * (n - 1)
        for i in xrange(2, n + 1):
            for x in xrange(i):
                m[i] += m[x] * m[i - 1 - x]
        
        return m[-1]