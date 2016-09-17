class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if not nums or len(nums) < 3: return []
        
        nums.sort()
        result = []
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            p, q = i + 1, len(nums) - 1
            while p < q:
                if nums[p] + nums[q] == -nums[i]:
                    result.append([nums[i], nums[p], nums[q]])
                    p += 1
                    while p < q and nums[p] == nums[p - 1]: p += 1
                    q -= 1
                    while p < q and nums[q] == nums[q + 1]: q -= 1
                elif nums[p] + nums[q] < -nums[i]:
                    p += 1
                    while p < q and nums[p] == nums[p - 1]: p += 1
                else:
                    q -= 1
                    while p < q and nums[q] == nums[q + 1]: q -= 1
        return result