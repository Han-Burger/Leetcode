class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #return self.dp(nums)
        #return self.greedy(nums, set([]), 0)
        return self.reverse(nums)
    
    def reverse(self, nums):
        res = True
        lastZero = -1
        for i in xrange(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                if lastZero < 0:
                    lastZero = i
                    res = False
            elif nums[i] + i > lastZero:
                lastZero = -1
                res = True
        return res
                
    
    def greedy(self, nums, m, idx):
        if not nums or len(nums) < 1: return True
        if nums[idx] + idx >= len(nums) - 1: return True
        if idx in m: return False
        
        for j in xrange(nums[idx], 0, -1):
            if self.greedy(nums, m, idx + j): return True
        
        m.add(idx)
        return False
    
    def dp(self, nums):
        if not nums or len(nums) < 1: return True
        m = [False] * (len(nums) - 1) + [True]
        for i in xrange(len(nums) - 2, -1, -1):
            for j in xrange(1, nums[i] + 1):
                if i + j >= len(nums): break
                if m[i + j]:
                    m[i] = True
                    break
        return m[0]