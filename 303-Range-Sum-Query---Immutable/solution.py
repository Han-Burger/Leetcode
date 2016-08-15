class NumArray(object):
    m = []
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.m = []
        for i in xrange(len(nums)):
            if i == 0: self.m.append(nums[i])
            else: self.m.append(self.m[-1] + nums[i])
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0: return self.m[j]
        else: return self.m[j] - self.m[i - 1]
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)