class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        N =  n
        n = 2
        num = "0"
        
        
        
        def getNumber(N, num, n, k):
            if N == 1:
                return 0
            
            if n == N+1: #base case
                return int(num)
            else:
                if num=="0":
                    num =  "01"
                elif num=="1":
                    num = "10"
                
                if k > (2**(N-1))/(2**(n-1)):
                    k -= (2**(N-1))/(2**(n-1))
                    num = num[1]
                else:
                    num = num[0]
                    
                n += 1
                
            return getNumber(N, num, n, k)
        
        return getNumber(N, num, n, k)
                
