class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = [[False for j in xrange(len(p) + 1)] for i in xrange(len(s) + 1)]
        m[0][0] = True
        
        for j in xrange(len(p)):
            m[0][j + 1] = j > 0 and p[j] == '*' and m[0][j - 1]
        
        for i in xrange(len(s)):
            for j in xrange(len(p)):
                if p[j] != '*':
                    m[i + 1][j + 1] = m[i][j] and (s[i] == p[j] or p[j] == '.')
                else:
                    m[i + 1][j + 1] = (j > 0 and m[i + 1][j - 1]) or ((j > 0 and (p[j - 1] == '.' or s[i] == p[j -1]) and m[i][j + 1]))
        
        return m[-1][-1]