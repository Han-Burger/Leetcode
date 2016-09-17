class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        """
        Similar to permuataion I.
        The only different is not to insert a number after any of it's duplicates
        Not need to sort
        """
        if not nums: return []
        return self.backtracking(nums, 0)
    
    def backtracking(self, nums, start):
        if start == len(nums) - 1: return [[nums[start]]]
        
        res = []
        for l in self.backtracking(nums, start + 1):
            n = nums[start]
            for i in xrange(len(l) + 1):
                res.append(l[: i] + [n] + l[i: ])
                if i < len(l) and n == l[i]: break
        return res