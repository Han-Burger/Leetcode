class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return 0
        return self.dp(nums, target)
        
    def dp(self, nums, target):
        nums.sort()
        m = [1] * (target + 1)
        for i in xrange(1, target + 1):
            total = 0
            for lastNum in nums:
                remain = i - lastNum
                if remain >= 0: total += m[remain]
                else: break
            m[i] = total
        return m[-1]
    
    def no_unordered_duplicates(self, nums, target):
        if not nums: return 0
        nums.sort()
        return self.dfs(nums, target)
        
    def dfs(self, nums, target):
        if len(nums) == 1: 
            return 1 if target % nums[0] == 0 else 0
        
        total = 0
        num = nums[-1]
        for i in xrange(target / num + 1):
            total += self.dfs(nums[: -1], target - i * num)
        return total