class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # eliminating bad inputs
        if not nums or len(nums) < 3: return target
        
        nums.sort()
        closest = sum(nums[:3])
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            p, q = i + 1, len(nums) - 1
            while(p < q):
                currSum = sum([nums[i], nums[p], nums[q]])
                if  currSum == target:
                    return target
                else:
                    closest = min(closest, currSum, key = lambda x: abs(target - x))
                    if currSum < target:
                        p += 1
                        while p < q and nums[p] == nums[p - 1]: p += 1
                    else:
                        q -= 1
                        while p < q and nums[q] == nums[p + 1]: q -= 1
        return closest
                    
        