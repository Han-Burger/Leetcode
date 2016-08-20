
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        m = [0] * (num + 1)
        scale = 0
        for i in xrange(1, len(m)):
            scale = self.log2(i, scale)
            m[i] = m[i - 2 ** scale] + 1
        return m
    
    def log2(self, num, prev):
        return prev + 1 if (num >> prev) > 1 else prev