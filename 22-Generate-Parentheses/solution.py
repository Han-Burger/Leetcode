class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.propagate("", n, n)
        
    def propagate(self, prev, left_remain, right_remain):
        ret_list = []
        if left_remain == 0 and right_remain == 1:
            ret_list.append(prev + ")")
        elif left_remain == 0:
            ret_list.extend(self.propagate(prev + ")", left_remain, right_remain - 1))
        else:
            ret_list.extend(self.propagate(prev + "(", left_remain - 1, right_remain))
            if left_remain < right_remain:
                ret_list.extend(self.propagate(prev + ")", left_remain, right_remain - 1))
        return ret_list
            