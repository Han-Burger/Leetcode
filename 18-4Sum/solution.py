class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        """
        Implement 2 pointers in searching for the expected sum of the last 2 numsbers of the 4
        """
        
        if len(nums) < 4: return []
        nums.sort()
        
        d = set()
        length = len(nums)
        
        print nums
        
        for i in xrange(length):
            # should not skip duplicate numbers when traversing the list for the first number
            # e.g., [1, 1, 1, 1, 2] and is looking for a target of 5.
            # similar problem applies to the second number
            for j in xrange(i + 1, length):
                subTarget = target - nums[i] - nums[j]
                p, q = j + 1, length - 1
                ### NOTE: wipe out some uncessarily recursion by pre-sum check
                if p >= q or subTarget < nums[p] * 2 or subTarget > nums[q] * 2:
                    continue
                else:
                    while p < q:
                        if nums[p] + nums[q] == subTarget:
                            d.add((nums[i], nums[j], nums[p], nums[q]))
                            p += 1
                            q -= 1
                            while p < q and nums[p] == nums[p - 1]: p += 1
                            while p < q and nums[q] == nums[q + 1]: q -= 1
                        elif nums[p] + nums[q] < subTarget:
                            p += 1
                            while p < q and nums[p] == nums[p - 1]: p += 1
                        else:
                            q -= 1
                            while p < q and nums[q] == nums[q + 1]: q -= 1
        return list(d)