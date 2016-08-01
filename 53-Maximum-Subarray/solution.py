class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
            
        max = nums[0]
        sum = nums[0] if nums[0] > 0 else 0
        for i in xrange(1, len(nums)):
            sum += nums[i]
            max = max if max > sum else sum
            sum = 0 if sum < 0 else sum
        return max