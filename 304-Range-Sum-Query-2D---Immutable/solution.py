class NumMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.dp = self.getDP(matrix)
    
    def sumRegion(self, row1, col1, row2, col2):
        remain = self.dp[row1][col2 + 1] + self.dp[row2 + 1][col1] - self.dp[row1][col1]
        return self.dp[row2 + 1][col2 + 1] - remain
        
    def getDP(self, matrix):
        if len(matrix) == 0:
            return []
        col = len(self.matrix[0])
        row = len(self.matrix)
        dp = [[ 0 for i in range(col + 1)] for j in range(row + 1)]
        for i in range( 1, row + 1):
            for j in range(1, col + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i - 1][j - 1]
        return dp

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)