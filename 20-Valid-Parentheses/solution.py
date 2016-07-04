class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            elif c in (')', ']', '}'):
                if len(stack) == 0 or not 0 < ord(c) - ord(stack.pop()) <= 2:
                    return False
            else:
                return False
        return len(stack) == 0