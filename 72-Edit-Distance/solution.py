class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1: return len(word2)
        if not word2: return len(word1)
        
        m = range(len(word2) + 1)
        
        for i in xrange(1, len(word1) + 1):
            prev = i
            for j in xrange(len(word2) + 1):
                curr = prev
                if j == 0:
                    curr == i
                elif word1[i - 1] != word2[j - 1]:
                    curr = min(prev, m[j], m[j - 1]) + 1
                prev = m[j]
                m[j] = curr
        return m[-1]