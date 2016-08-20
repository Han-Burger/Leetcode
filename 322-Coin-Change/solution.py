class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or amount < 0: return -1
        #return self.dp(sorted(coins), amount)
        #return self.dfs(sorted(coins, reverse = True), amount, {0: 0})
        return self.bfs(sorted(coins), amount)
        
    def dp(self, coins, amount):
        m = [0] + [-1] * amount
        for i in xrange(1, len(m)):
            for c in coins:
                if c > i: break
                if m[i - c] >= 0:
                    m[i] = m[i - c] + 1 if m[i] < 0 else min(m[i], m[i - c] + 1)
        return m[-1]
    
    def dfs(self, coins, amount, dic):
        if amount in dic: return dic[amount]
        if amount in coins:
            dic[amount] = 1
            return 1
        
        minAmount = -1
        for c in coins:
            if c <= amount:
                sub = self.dfs(coins, amount - c, dic)
                if sub >= 0:
                    minAmount = sub + 1 if minAmount < 0 else min(minAmount, sub + 1)
        dic[amount] = minAmount
        return minAmount
    
    def bfs(self, coins, amount):
        if amount < 0: return -1
        if amount == 0: return 0
        
        visited = [True] + [False] * amount
        count = 0
        oldList = [0]
        while oldList:
            count += 1
            newList = []
            for v in oldList:
                for c in coins:
                    if v + c > amount: break
                    elif v + c == amount: return count
                    elif not visited[v + c]:
                        visited[v + c] = True
                        newList.append(v + c)
            oldList = newList
        return -1
        