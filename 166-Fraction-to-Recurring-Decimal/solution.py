class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0: return 0
        
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        
        # avoid MAX_INT, MIN_INT
        intPart = numerator / denominator
        decPart = numerator % denominator
        
        # avoid -1 to 0
        sign = '-' if intPart < 0 else ''
        if intPart < 0:
            if decPart != 0:
                intPart = abs(intPart + 1)
                decPart = abs(decPart - denominator)
            else:
                intPart = abs(intPart)
        
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
        elif s == "":
            return sign + str(intPart)
        else:
            return sign + str(intPart) + '.' + s
        