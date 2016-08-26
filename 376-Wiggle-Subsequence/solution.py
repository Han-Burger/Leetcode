class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        up, down = 1, 1
        for i in xrange(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            if nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)
        
    
    def method1(self, nums):
        if not nums: return 0
        return max(self.count(nums, -1), self.count(nums, 1))
    
    def count(self, nums, lastChgValue):
        print "count" + str(lastChgValue)
        count = 0
        idx = len(nums) - 1
        while idx >= 0:
            count += 1
            idx = self.prevIdx(nums, idx, lastChgValue)
            lastChgValue *= -1
        return count
    
    def prevIdx(self, nums, idx, lastChgValue):
        """
        return -1 if no prevLow else return first idx in the prevLow series
        e.g. nums = [8, 2, 3, 4, 5, 9, 6, 1], if we're now at 6, then the first lower number is 5
        there's a ascending series before 5, so return the first idx of the series, which is 1 (nums[1] = 2)
        if lastChgValue < 0, (e.g., 6 to 1, lastChgValue = -5) we're looking for prevLow
        if lastChgValue > 0, we're looking for prevHigh
        """
        prevIdx = idx
        sign = 1 if lastChgValue > 0 else -1
        while prevIdx >= 0 and sign * nums[prevIdx] <= sign * nums[idx]:
            prevIdx -= 1
        while prevIdx > 0 and sign * nums[prevIdx - 1] >= sign * nums[prevIdx]:
            prevIdx -= 1
        print prevIdx
        return prevIdx










