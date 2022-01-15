class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n<3):
            if(n==1):
                return True
            else:
                return False
        else:
            return self.isPowerOfThree(n/3)

        