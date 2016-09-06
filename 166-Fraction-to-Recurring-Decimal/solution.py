class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0: return 0
        
        sign = '-' if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0) else ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        intPart = numerator / denominator
        decPart = numerator % denominator
        
        if decPart == 0:
            return sign + str(intPart)
        
        m = {}
        s = ""
        i = 0
        while decPart != 0:
            if decPart in m: break
            m[decPart] = i
            decPart *= 10
            s += str(decPart / denominator)
            decPart = decPart % denominator
            i += 1
        
        if decPart != 0:
            i = m[decPart]
            return sign + str(intPart) + '.' + s[: i] + '(' + s[i: ] + ')'
        else:
            return sign + str(intPart) + '.' + s
        