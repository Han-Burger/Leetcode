class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.dfs(s, wordDict, {})
        
    def dfs(self, s, wordDict, strMap):
        if s in strMap:
            return strMap[s]
        
        res = []
        for w in wordDict:
            if s.startswith(w):
                if s == w:
                    res.append(w)
                else:
                    sub_res = self.dfs(s[len(w):], wordDict, strMap)
                    for sub in sub_res:
                        res.append(w + ' ' + sub)
        strMap[s] = res
        return res