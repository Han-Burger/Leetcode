class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        m = {'1': ['*'],
             '2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z'],
             '0': [' ']}
            
        result = []
        for d in digits:
            if d not in m: return []
            if len(result) == 0:
                result = list(m[d])
            else:
                newResult = []
                for c in m[d]:
                    newResult.extend([s + c for s in result])
                result = newResult
        return result