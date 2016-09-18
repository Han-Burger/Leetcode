class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0: return x
        if x <= 3: return 1
        if x <= 5: return 2
        i, j = 1, x / 2
        while j - i > 1:
            mid = (i + j) / 2
            if mid * mid == x: return mid
            elif mid * mid < x: i = mid
            else: j = mid
        return i