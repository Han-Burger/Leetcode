class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return 0
        if n < 5: return [0, 0, 1, 2, 4][n]
        scale = (n - 2) / 3
        return 3 ** scale * (n - 3 * scale)