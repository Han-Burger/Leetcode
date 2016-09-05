class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        for s in strs:
            key = str(sorted(s))
            if key in m: m[key].append(s)
            else: m[key] = [s]
        return [m[key] for key in m]
        