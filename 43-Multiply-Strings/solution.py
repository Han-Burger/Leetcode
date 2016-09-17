class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        d = [0] * (len(num1) + len(num2))
        for p in xrange(len(num1)):
            for q in xrange(len(num2)):
                i, j = len(num1) - p - 1, len(num2) - q - 1
                d[p + q] += int(num1[i]) * int(num2[j])
                d[p + q + 1] += d[p + q] / 10
                d[p + q] %= 10
        
        for i in xrange(len(d) - 1):
            if d[i] > 10:
                d[i + 1] += d[i] / 10
                d[i] %= 10
        
        s = ""
        for i in xrange(len(d) - 1, -1, -1):
            if d[i] == 0 and s == "": continue
            s += str(d[i])
        
        return "0" if s == "" else s