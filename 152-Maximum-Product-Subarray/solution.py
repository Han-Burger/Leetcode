class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        lastZeroIdx = -1
        negIdxList = []
        maxRes = nums[0]
        for i in xrange(len(nums)):
            if nums[i] == 0:
                if lastZeroIdx + 1 <= i - 1:
                    maxRes = max(maxRes, self.noZeroList(nums, lastZeroIdx + 1, i - 1, negIdxList))
                lastZeroIdx = i
                negIdxList = []
                maxRes = max(maxRes, 0)
            elif nums[i] < 0:
                negIdxList.append(i)
        if lastZeroIdx + 1 <= len(nums) - 1:
            maxRes = max(maxRes, self.noZeroList(nums, lastZeroIdx + 1, len(nums) - 1, negIdxList))
        return maxRes
                

    def noZeroList(self, nums, start, end, negIdxList):
        # start and end both included
        if len(negIdxList) % 2 == 0:
            return self.product(nums, start, end)
        else:
            prod1 = self.product(nums, start, negIdxList[-1] - 1)
            prod2 = self.product(nums, negIdxList[0] + 1, end)
            return max(prod1, prod2)
    
    def product(self, nums, start, end):
        # start and end both included
        if start > end: return None
        prod = nums[start]
        for n in nums[start + 1: end + 1]:
            prod *= n
        return prod