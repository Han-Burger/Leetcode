class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1: return "1"
        
        splits = [1]
        for i in xrange(2, n):
            splits.append(splits[-1] * i)
        
        k -= 1 # let index starts from 0
        res = ""
        nums = range(1, n + 1)
        for i in xrange(len(splits) - 1, -1, -1):
            split = splits[i]
            pos = k / split
            res += str(nums[pos])
            nums.pop(pos)
            k -= pos * split
        res += str(nums[0])
        
        return res
            