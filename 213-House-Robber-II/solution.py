class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        return max(self.rob_line(nums, 0, len(nums) - 1), self.rob_line(nums, 1, len(nums)))
    
    def rob_line(self, nums, start, end):
        size = end - start
        if size == 0: return 0
        if size == 1: return nums[start]
        if size == 2: return max(nums[start], nums[start + 1])
        if size == 3: return max(nums[start] + nums[start + 2], nums[start + 1])

        m1, m2, m3 = nums[start], nums[start + 1], nums[start] + nums[start + 2]
        for i in xrange(start + 3, end):
            m1, m2, m3 = m2, m3, max(m1, m2) + nums[i]
        return max(m2, m3)
        