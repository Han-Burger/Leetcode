class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = range(len(s))
        for i in xrange(len(s)):
            for j in xrange(i + 1):
                if i + j < len(s) and s[i - j] == s[i + j]:
                    m[i + j] = min(m[i + j], 0 if i - j == 0 else m[i - j - 1] + 1)
                else:
                    break
            for j in xrange(i):
                if i + j < len(s) and s[i - j - 1] == s[i + j]:
                    m[i + j] = min(m[i + j], 0 if i - j - 1 == 0 else m[i - j - 2] + 1)
                else:
                    break
        return m[-1]