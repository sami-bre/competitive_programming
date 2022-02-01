class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # get the number of even and odd indice positions
        ev, od = n//2, n//2
        if n%2 != 0:
            ev += 1
            
        evVar = self.helper(5, ev)
        odVar = self.helper(4, od)
        
        return (evVar*odVar) % (10**9 +7)
            
    def helper(self, n, ex):
        if ex%2 != 0:
            return n*self.helper(n, ex-1)
        elif ex == 0:
            return 1
        elif ex == 1:
            return n
        else:
            return self.helper((n**2)%(10**9 + 7), ex/2)
        