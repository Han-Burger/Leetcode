class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ""
        if len(s) < 2: return s
        
        longest = ""
        mid = len(s) / 2
        for r in xrange((len(s) + 1) / 2):
            if len(s) % 2 == 0:
                if len(longest) >= len(s) - r * 2:
                    break
                centers = [mid - 1 - r, mid + r]
            else: 
                if len(longest) >= len(s) - r * 2 + 1:
                    break
                if r == 0:
                    centers = [mid]
                else:
                    centers = [mid - r, mid + r]
            
            for c in centers:
                i, j = c, c
                while i >= 0 and j < len(s) and s[i] == s[j]:
                    i -= 1
                    j += 1
                longest = max(longest, s[i + 1: j], key = len)
                i, j = c, c + 1
                while i >= 0 and j < len(s) and s[i] == s[j]:
                    i -= 1
                    j += 1
                longest = max(longest, s[i + 1: j], key = len)
        return longest
            