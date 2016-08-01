class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        if s[j] == ')', then we look for the lowest i that s[i..j] is valid
        valid s[i..j] = s[i1...j1] + '(' + s[i2...j2] + ')'
        where s[i1...j1] and s[i2...j2] can be empty string
        m is used to store the lowest valid i for each j
        it's initialize as m[i] = i but doens't mean s[i..i] is valid.
        """
        
        m = [i for i in range(len(s))]
        max = 0
        
        for j in range(1, len(s)):
            if s[j] == ')':
                i = m[j - 1] if m[j - 1] != j - 1 else j
                if i > 0 and s[i - 1] == '(':
                    m[j] = i - 1
                    if i > 1 and m[i - 2] != i - 2:
                        m[j] = m[i - 2]
                    max = max if max > j - m[j] + 1 else j - m[j] + 1
                    
        return max
                