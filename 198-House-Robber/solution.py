class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        if len(nums) == 3: return max(nums[0] + nums[2], nums[1])
        
        m1, m2, m3 = nums[0], nums[1], nums[0] + nums[2]
        for i in xrange(3, len(nums)):
            if m1 > m2:
                m1, m2, m3 = m2, m3, m1 + nums[i]
            else:
                m1, m2, m3 = m2, m3, m2 + nums[i]
        return max(m2, m3)
            