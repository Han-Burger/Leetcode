class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if not nums: return
        # 2 pointers
        p1, p2 = -1, len(nums)
        i = 0
        while i < p2:
            if nums[i] == 0:
                p1 += 1
                nums[i] = nums[p1]
                nums[p1] = 0
            if nums[i] == 2:
                p2 -= 1
                nums[i] = nums[p2]
                nums[p2] = 2
            else:
                i += 1
        return