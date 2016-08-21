class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.dp(nums)
        
    def dp(self, nums):
        nums.sort()
        maxList = []
        m = [[] for n in nums]
        for i in xrange(len(nums)):
            n = nums[i]
            for j in xrange(i):
                if n % m[j][-1] == 0 and len(m[j]) + 1 > len(m[i]):
                    m[i] = list(m[j]) + [n]
                    maxList = maxList if len(maxList) > len(m[i]) else m[i]
            if not m[i]: m[i] = [n]
            if not maxList: maxList = [n]
        return maxList
            
    
    def naive(self, nums):
        nums.sort()
        maxList = []
        lists = []
        for n in nums:
            toAddLists = []
            for l in lists:
                if n % l[-1] == 0:
                    newL = list(l) + [n]
                    toAddLists.append(newL)
                    maxList = newL if len(newL) > len(maxList) else maxList
            lists.extend(toAddLists)
            lists.append([n])
            if not maxList:
                maxList = [n]
        return maxList
        
        