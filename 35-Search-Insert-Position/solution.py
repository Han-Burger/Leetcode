class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums or len(nums) < 1: return 0
        
        i, j = -1, len(nums)
        while j - i > 1:
            mid = (i + j) / 2
            if nums[mid] == target: return mid
            elif nums[mid] < target:
                i = mid
            else:
                j = mid
        return j
        