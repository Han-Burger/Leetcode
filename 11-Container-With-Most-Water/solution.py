class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if not height or len(height) < 2: return 0
        
        i, j = 0, len(height) - 1
        maxVol = 0
        while i < j:
            maxVol = max(maxVol, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
                while i < j and height[i] < height[i - 1]: i += 1
            else:
                j -= 1
                while i < j and height[j] < height[j + 1]: j -= 1
        return maxVol
        