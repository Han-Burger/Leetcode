class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        return self.recursive(nums, 0)
        
    def recursive(self, nums, start):
        if start == len(nums) - 1: return [[nums[start]]]
        
        result = []
        for l in self.recursive(nums, start + 1):
            c = nums[start]
            for i in xrange(len(l)):
                result.append(l[: i] + [c] + l[i:])
            result.append(l + [c])
        return result