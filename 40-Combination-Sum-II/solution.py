class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if not candidates: return []
        candidates.sort()
        return self.backtracking(candidates, 0, target)
        
    def backtracking(self, cand, start, target):
        if target < 0: return []
        
        result = []
        for i in xrange(start, len(cand)):
            if cand[i] > target: break
            if i > start and cand[i] == cand[i - 1]: continue
            if cand[i] == target:
                result.append([cand[i]])
            else:
                subs = self.backtracking(cand, i + 1, target - cand[i])
                result.extend([cand[i]] + sub for sub in subs)
        return result
            
                