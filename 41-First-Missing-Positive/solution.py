class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        using the position in the array as the index
        if nums[i] <= 0 or nums[i] > len(nums)
        """
        
        for i in xrange(len(nums)):
            p = nums[i]
            while(p > 0 and p <= len(nums)):
                q = nums[p - 1]
                # print i, p, q, nums
                if nums[p - 1] != p:
                    nums[p - 1] = p
                else:
                    break
                p = q
        
        print nums
        
        for i in xrange(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        
        return len(nums) + 1
        
        