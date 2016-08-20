from math import log
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        m = [0] * (num + 1)
        for i in xrange(1, len(m)):
            remain = i - 2 ** self.log2(i)
            m[i] = m[remain] + 1
        return m
    
    def log2(self, num):
        return int(log(num)/log(2))