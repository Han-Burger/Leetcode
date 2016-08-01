class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        sPtr = 0
        pPtr = 0
        star = -1
        toMatch = 0
        
        while sPtr < len(s):
            if pPtr < len(p) and (s[sPtr] == p[pPtr] or p[pPtr] == '?'):
                sPtr += 1
                pPtr += 1
            elif pPtr < len(p) and p[pPtr] == '*':
                star = pPtr
                toMatch = sPtr
                pPtr += 1
            # doesn't match
            elif star >= 0:
                pPtr = star + 1
                sPtr = toMatch + 1
                toMatch = sPtr
            else:
                return False
        
        while pPtr < len(p):
            if p[pPtr] == '*':
                pPtr += 1
            else:
                return False
        
        return True
            