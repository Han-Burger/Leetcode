class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.hashmap(nums, target)
        
    def hashmap(self, nums, target):
        dic = {}
        for i in xrange(len(nums)):
            x = nums[i]
            y = target - x
            if y in dic: return [dic[y], i]
            else: dic[x] = i
        return [0, 0]
    
    def sortedTwoPointers(self, nums, target):
        # The sorting algo requires O(NlogN) runtime
        sorted_nums = sorted(nums)
        i = 0
        j = len(sorted_nums) - 1
        while i < j:
            sum = sorted_nums[i] + sorted_nums[j]
            if sum == target:
                if sorted_nums[i] != sorted_nums[j]:
                    return [nums.index(sorted_nums[i]), nums.index(sorted_nums[j])]
                else:
                    idx1 = nums.index(sorted_nums[i])
                    idx2 = nums[idx1 + 1:].index(sorted_nums[j]) + idx1 + 1
                    return [idx1, idx2]
            elif sum < target:
                i += 1
            else:
                j -= 1
        return [0, 0]