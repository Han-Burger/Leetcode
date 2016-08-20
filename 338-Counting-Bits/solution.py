class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        return self.noBitManipulation(num)
    
    def noBitManipulation(self, num):
        if num == 0: return [0]
        
        m = [0, 1] + [0] * (num - 1)
        prev2Exp = 1
        for i in xrange(2, len(m)):
            if i == prev2Exp * 2:
                m[i] = 1
                prev2Exp *= 2
            else:
                m[i] = 1 + m[i - prev2Exp]
        return m
        
    def bitManipulation(self, num):
        m = [0] * (num + 1)
        scale = 0
        for i in xrange(1, len(m)):
            scale = self.log2(i, scale)
            m[i] = m[i - 2 ** scale] + 1
        return m
    
    def log2(self, num, prev):
        return prev + 1 if (num >> prev) > 1 else prev