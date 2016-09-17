class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        """
        The solution find the start point of the target number first
        If target number exist, then find the end point of the target number
        else return [-1, -1]
        """
        
        if not nums: return [-1, -1]
        
        i, j = -1, len(nums)
        while j - i > 1:
            mid = (i + j) / 2
            if nums[mid] < target: i = mid
            else: j = mid
        
        if j == len(nums) or nums[j] != target: return [-1, -1]
        
        start = j
        
        i, j = start, len(nums)
        while j - i > 1:
            mid = (i + j) / 2
            if nums[mid] <= target: i = mid
            else: j = mid
        
        return [start, i]