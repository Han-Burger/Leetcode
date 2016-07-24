class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.subCombination([], candidates, target)
        
        
    def subCombination(self, prev, candidates, target):
        if len(candidates) == 0:
            return []
            
        candidate = candidates[-1]
        
        if len(candidates) == 1:
            if target % candidate == 0:
                return [prev + ([candidate] * (target / candidate))]
            else:
                return []
        
        ret = []
        for i in range(target/candidate + 1):
            new_prev = copy.deepcopy(prev) + ([candidate] * i)
            new_target = target - candidate * i
            if new_target == 0:
                ret.append(new_prev)
            else:
                ret.extend(self.subCombination(new_prev, candidates[: -1], new_target))
        return ret