class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        row = len(dungeon)
        col = len(dungeon[0])
        
        m = [0] * col
        for j in xrange(col - 1, -1, -1):
            if j == col - 1:
                m[j] = max(1, 1 - dungeon[row - 1][j])
            else:
                m[j] = max(1, m[j + 1] - dungeon[row - 1][j])
        
        for i in xrange(row - 2, -1, -1):
            for j in xrange(col - 1, -1, -1):
                if j == col - 1:
                    m[j] = max(1, m[j] - dungeon[i][j])
                else:
                    m[j] = max(1, min(m[j], m[j + 1]) - dungeon[i][j])
        
        return m[0]