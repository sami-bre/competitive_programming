class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n = -n
        if n==1:    # base cases
            return x
        elif n==0:
            return 1
        elif not n%2:   # general cases
            return self.myPow(x, n/2)**2
        else:
            return x*self.myPow(x, n-1)
        