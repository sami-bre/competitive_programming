class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        nums.sort()
        result = []
        start = True
        for i in range(len(nums)):
            if(start):
                result.append(nums.pop(0))
                start = False
            else:
                result.append(nums.pop(-1))
                start = True
        
        return result
                
        