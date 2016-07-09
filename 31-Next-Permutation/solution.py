class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        changed = False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(i + 1, len(nums)):
                    if j == len(nums) - 1 or nums[j + 1] <= nums[i] and nums[j] > nums[i]:
                        if j == len(nums) - 1 and nums[j] == nums[i]:
                            nums[i], nums[i + 1] = nums[i + 1], nums[i]
                        else:
                            nums[i], nums[j] = nums[j], nums[i]
                            self.partialReverse(nums, i + 1, len(nums) - 1)
                        break
                changed = True
                break
        if not changed:
            self.partialReverse(nums, 0, len(nums) - 1)
        
    def partialReverse(self, nums, start, end):
        i, j = start, end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1