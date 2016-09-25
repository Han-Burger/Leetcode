class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums: return -1
        if len(nums) < 3:
            for i in xrange(len(nums)):
                if target == nums[i]: return i
            return -1
        
        # at least 2 values
        i, j = 0, len(nums) - 1
        leftVal, rightVal = nums[i], nums[j]
        if leftVal == target: return i
        if rightVal == target: return j
        """
        while i < j - 1:
            mid = i + (j - i) / 2
            if nums[mid] == target: return mid
            if leftVal < rightVal:
                if nums[mid] < target: i = mid
                else: j = mid
            elif target > leftVal:
                if nums[mid] < rightVal or nums[mid] > target: j = mid
                else: i = mid
            else:
                if nums[mid] > leftVal or nums[mid] < target: i = mid
                else: j = mid
        """
        
        while i <= j:
            mid = i + (j - i) / 2
            if nums[mid] == target: return mid
            if leftVal < rightVal:
                if nums[mid] < target: i = mid + 1
                else: j = mid - 1
            elif target > leftVal:
                if nums[mid] <= rightVal or nums[mid] > target: j = mid - 1
                else: i = mid + 1
            else:
                if nums[mid] >= leftVal or nums[mid] < target: i = mid + 1
                else: j = mid - 1
        
        return -1
        