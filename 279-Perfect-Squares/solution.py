class Solution(object):
    hashmap_ = {1: 1}
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return self.dfs(n, self.hashmap_)
        #return self.bfs(n)
        
    def dfs(self, n, hashmap):
        if n in hashmap:
            return hashmap[n]
        
        if int(math.floor(math.sqrt(n))) ** 2 == n:
            hashmap[n] = 1
            return 1
        
        sub_res = [self.dfs(n - i ** 2, hashmap) for i in xrange(int(math.floor(math.sqrt(n))), 0, -1)]
        hashmap[n] = min(sub_res) + 1
        return hashmap[n]
    
    def bfs(self, n):
        depth = 1
        prevDepthStack = [n]
        currDepthStack = []
        while len(prevDepthStack) > 0:
            curNum = prevDepthStack.pop()
            if self.isPerfectSquare(curNum):
                return depth
            else:
                for i in xrange(int(math.floor(math.sqrt(curNum))), 0, -1):
                    currDepthStack.append(curNum - i ** 2)
            if len(prevDepthStack) == 0 and len(currDepthStack) > 0:
                prevDepthStack = currDepthStack
                currDepthStack = []
                depth += 1
        return n
    
    def isPerfectSquare(self, n):
        return int(math.floor(math.sqrt(n))) ** 2 == n
        
        