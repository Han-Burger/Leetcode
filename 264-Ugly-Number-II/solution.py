class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1: return 0
        
        nums = [1]
        m2, m3, m5 = 0, 0, 0
        for i in xrange(1, n):
            num = min(2 * nums[m2], 3 * nums[m3], 5 * nums[m5])
            nums.append(num)
            if num % 2 == 0: m2 += 1
            if num % 3 == 0: m3 += 1
            if num % 5 == 0: m5 += 1
        return nums[-1]