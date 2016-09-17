class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n == 0: return 1
        if n < 0: return 1.0 / self.myPow(x, -n)
        if x < 0:
            if n % 2 == 0: return self.myPow(-x, n)
            else: return -self.myPow(-x, n)
        
        return self.posPow(x, n)
    
    def posPow(self, x, n):
        if n == 1: return x
        elif n % 2 == 1: return x * self.posPow(x, n - 1)
        else: return self.posPow(x * x, n / 2)