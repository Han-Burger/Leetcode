class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1 if obstacleGrid[i][j] == 0 else 0
                elif obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = (0 if i == 0 else obstacleGrid[i - 1][j]) + (0 if j == 0 else obstacleGrid[i][j - 1])
        return obstacleGrid[-1][-1]
                    