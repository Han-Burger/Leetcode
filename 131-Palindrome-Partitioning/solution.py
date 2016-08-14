class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return self.dfs(s, {})
    
    def dfs(self, s, strMap):
        if s in strMap:
            return strMap[s]
        
        res = []
        for j in xrange(len(s)):
            if self.isPalindrome(s[: j + 1]):
                if j == len(s) - 1:
                    res.append([s])
                else:
                    sub_res = self.dfs(s[j + 1:], strMap)
                    for sub in sub_res:
                        res.append([s[: j + 1]] + list(sub))
        strMap[s] = res
        return res
    
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        return True