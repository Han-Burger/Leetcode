class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 10: return 0
        if n == 0: return 1
        
        sum = 10
        for digit in xrange(2, n + 1):
            prod = 9
            for i in xrange(2, digit + 1):
                prod *= (11 - i)
            sum += prod
        return sum