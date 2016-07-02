class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        max = 0
        length = 0
        for i in range(len(s)):
            c = s[i]
            length += 1
            if c in d:
                length = length if length < i - d[c] else i - d[c]
            max = max if max > length else length
            d[c] = i
        return max
            